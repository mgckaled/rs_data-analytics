# Bloco E - Aula 3: Tensores

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-e---algebra-linear)
>
> retornar ao [README.md](../../../../README.md)

## Definição

Um **tensor** é uma generalização de escalares (ordem 0), vetores (ordem 1) e matrizes (ordem 2) para ordens superiores. Formalmente, um tensor de ordem `N` é um array multidimensional com `N` índices que identificam suas componentes. Tensores modelam campos, imagens multicanal, dados espaciais-temporais, transformações multilineares e muito mais.

## Conceitos e notação (resumo)

* Ordem (rank do tensor): número de índices necessários para acessar uma componente.
* Forma (shape): tupla com o tamanho em cada modo/ dimensão, por exemplo `shape = (I, J, K)` para um tensor 3-D.
* Componentes: para um tensor de ordem 3 escrevemos `T[i, j, k]` (índices em notação de programação) ou `T_{i j k}` (notação matemática).
* Modo-n (fatia/matricização): operação que “desdobra” (unfold) o tensor ao longo de um modo, produzindo uma matriz.
* Contração (contraction): soma sobre índices iguais entre tensores, geral do produto escalar/multiplicação de matrizes.
* Produto externo (outer product): combinação de tensores que aumenta a ordem (concatena índices).
* Broadcasting: regras que permitem operações elemento a elemento entre tensores de formas compatíveis.
* Norma de Frobenius: norma natural para tensores obtida pela raiz da soma dos quadrados das componentes.

Fórmula isolada (norma de Frobenius)

$$
\|T\|_F = \sqrt{\sum_{i_1}\sum_{i_2}\dots\sum_{i_N} T_{i_1 i_2 \dots i_N}^2}
$$

## Operações fundamentais (descrição e significado)

* Indexação e fatiamento: acessar sub-tensores por índices ou slices.
* Transposição/permutação de eixos: reorganizar a ordem dos modos (por exemplo trocar canais e altura).
* Matricização (unfold / mode-n unfolding): converter um tensor em uma matriz para aplicar operações matriciais.
* Contração (tensordot / einsum): generaliza produto escalar e multiplicação de matrizes, reduzindo a ordem do resultado ao somar sobre índices comuns.
* Produto externo: gera um tensor de ordem somada (por exemplo outer(u, v) para vetores u e v produz um tensor de ordem 2 equivalente à matriz u ⊗ v).
* Reduções: soma, média, max ao longo de modos.
* Decomposições (SVD, CP, Tucker): formas de fatorar tensores para compressão, análise de componentes e redução de dimensionalidade.

Fórmula isolada (contração genérica em notação einsum-like)

$$
(R)_{i_1,\dots,i_a, j_1,\dots,j_b} = \sum_{k_1,\dots,k_c} A_{i_1,\dots,i_a, k_1,\dots,k_c}\; B_{k_1,\dots,k_c, j_1,\dots,j_b}
$$

## Exemplos

### Exemplo 1 — imagem RGB como tensor 3-D

* Representação comum: uma imagem colorida com `H` linhas, `W` colunas e 3 canais (RGB) é um tensor `I` de forma `(H, W, 3)`.
* Acessos: `I[h, w, 0]` é o valor do canal vermelho no pixel `(h, w)`.
* Operações típicas: permutar eixos para passar a `(3, H, W)` (por exemplo para frameworks que exigem canais primeiro); calcular média por canal; normalizar por norma ou desvio padrão por canal.
* Matricização: a unfold mode-0 (altura) produzirá uma matriz `(H) × (W*3)`, útil para certos filtros ou modelos lineares por pixel.

### Exemplo 2 — tensor de ordem 3 em modelos físicos / séries temporais multivariadas

* Considere um tensor `T` com forma `(N, M, K)` representando `N` instantes de tempo, `M` sensores e `K` variáveis por sensor.
* Contração sobre o modo de sensores (somar sobre `M`) produz um tensor `(N, K)` agregando todos os sensores; contração sobre variáveis específicas combina as informações conforme um operador de peso.
* Produto externo entre um vetor de tempos `t (N,)` e um vetor de características `f (K,)` gera um tensor `(N, K)` que pode ser somado/contratado com `T` para projeções.

## Exemplos em código (NumPy e Pandas)

* Exemplo A: criar tensores 3-D, permutar eixos, calcular norma, média por modo.
* Exemplo B: matricizar (unfold) um tensor modo-1 e exibir a matriz resultante com `pandas.DataFrame`.
* Exemplo C: contrair dois tensores com `np.tensordot` e `np.einsum`.

```python
import numpy as np
import pandas as pd

# Exemplo A: criar e inspecionar um tensor 3-D
H, W, C = 4, 5, 3  # altura, largura, canais
I = np.arange(H * W * C, dtype=float).reshape(H, W, C)  # tensor de exemplo (pode representar uma imagem)

print("shape I:", I.shape)     # (4, 5, 3)
print("I[0,0,:] (pixel 0,0, todos os canais):", I[0, 0, :])

# Permutar eixos (por exemplo canais first)
I_c_first = np.transpose(I, (2, 0, 1))  # shape (3, 4, 5)
print("shape I_c_first:", I_c_first.shape)

# Estatísticas por modo
mean_per_channel = I.mean(axis=(0,1))   # média sobre H e W -> vetor de tamanho C
norm_F = np.linalg.norm(I)              # norma de Frobenius
print("mean per channel:", mean_per_channel)
print("Frobenius norm:", norm_F)

# Exemplo B: matricização (mode-1 unfolding)
# Unfold mode-1 (por exemplo 'rows' = eixo 0) -> ficar com shape (H) x (W*C)
unfold_mode0 = I.reshape(H, W * C)  # equivalente a mode-0 unfolding se forma (H, W*C)
df_unfold = pd.DataFrame(unfold_mode0)
print("\nMode-0 unfolding (DataFrame):")
print(df_unfold)

# Exemplo C: contração com tensordot e einsum
# Construir dois tensores de exemplo
A = np.random.rand(3, 4, 5)  # shape (3,4,5)
B = np.random.rand(5, 6, 2)  # shape (5,6,2)

# Queremos contrair sobre o índice de tamanho 5 (terceiro do A e primeiro do B)
# Resultado terá shape (3,4,6,2)
C_tensordot = np.tensordot(A, B, axes=([2], [0]))
print("\nC_tensordot.shape:", C_tensordot.shape)  # (3,4,6,2)

# Mesma operação com einsum (notação explícita de índices)
# A_{i j k} B_{k l m} -> C_{i j l m}
C_einsum = np.einsum('ijk,klm->ijlm', A, B)
print("C_einsum.shape:", C_einsum.shape)

# Produto externo entre vetores (aumenta ordem)
u = np.array([1.0, 2.0, 3.0])   # shape (3,)
v = np.array([10.0, 20.0])      # shape (2,)
outer_uv = np.multiply.outer(u, v)  # shape (3,2) equivalente a np.outer mas generalizável
print("\nouter_uv.shape:", outer_uv.shape)
print("outer_uv:")
print(pd.DataFrame(outer_uv))

# Redução exemplo: somar sobre um modo para agregar
# soma sobre o eixo de sensores no exemplo T (N, M, K)
T = np.random.rand(100, 5, 8)  # N=100, M=5, K=8
agg_over_sensors = T.sum(axis=1)  # shape (100, 8)
print("\nT.shape:", T.shape)
print("agg_over_sensors.shape:", agg_over_sensors.shape)
```

Saídas/inspeções esperadas (resumidas):

* `I.shape` = `(4, 5, 3)` e `I_c_first.shape` = `(3, 4, 5)`.
* `mean_per_channel` é um vetor de comprimento `C` com a média de cada canal.
* `unfold_mode0` é uma matriz `(H, W*C)` exibida como `DataFrame`.
* `C_tensordot.shape` e `C_einsum.shape` ambos devem ser `(3, 4, 6, 2)` quando a contração é feita sobre o índice comum.
* `outer_uv.shape` = `(3, 2)`.
* Agregação sobre sensores em `T` leva a `(100, 8)`.

## Observações práticas

* Para operações complexas prefira `np.einsum` pela clareza de índice e potencial otimização; `np.tensordot` é simples para contrações sobre eixos correspondentes.
* Use `np.transpose` (ou `.transpose(axes)`) para reorganizar eixos antes de matricizações ou operações que esperam determinado layout de memória.
* Para matricizações consistentes, documente a ordem dos índices e o modo escolhido (mode-n) e aplique `reshape`/`transpose` conforme necessário.
* Em muitos problemas de aprendizado e visão computacional, manter o layout de memória (C-contiguous vs Fortran-contiguous) pode impactar performance; use `np.ascontiguousarray` quando necessário.
* Para decomposições e compressão de tensores considere algoritmos CP, Tucker ou SVD aplicados a unfoldings; bibliotecas especializadas (por exemplo `tensorly`) facilitam essas operações.
