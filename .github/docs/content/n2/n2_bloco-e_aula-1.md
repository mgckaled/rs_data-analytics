# Bloco E - Aula 1: Vetores

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-e---algebra-linear)
>
> retornar ao [README.md](../../../../README.md)

## Definição

Um **vetor** é um elemento de um espaço vetorial; em termos concretos costuma-se representá-lo como uma sequência ordenada de números. Vetores modelam posições, deslocamentos, características, sinais, entre outros. Em notação compacta escrevemos vetores como `(v1, v2, ..., vn)`.

## Conceitos e notação (resumo)

* Dimensão: um vetor em `R^n` tem `n` componentes.
* Vetor nulo: `0 = (0, 0, ..., 0)`.
* Igualdade: dois vetores são iguais se todas as componentes forem iguais.
* Combinação linear: `a1*v1 + a2*v2 + ... + ak*vk` com escalares `a1,...,ak`.
* Independência linear: `a1*v1 + ... + ak*vk = 0` implica `a1 = ... = ak = 0`.
* Base e dimensão do espaço: uma base é um conjunto de vetores linearmente independentes que geram o espaço; a dimensão é o número de vetores em qualquer base.
* Span (geração): conjunto de todas as combinações lineares de um conjunto de vetores.

## Operações fundamentais (fórmulas isoladas)

Adição de vetores:

$$
u + v = (u_1 + v_1,\; u_2 + v_2,\; \dots,\; u_n + v_n)
$$

Multiplicação por escalar:

$$
\alpha v = (\alpha v_1,\; \alpha v_2,\; \dots,\; \alpha v_n)
$$

Produto escalar (dot product):

$$
u \cdot v = \sum_{i=1}^{n} u_i\,v_i
$$

Norma (comprimento) e distância:

$$
\|v\| = \sqrt{v \cdot v}
$$

Projeção de `u` sobre `v` (quando `v ≠ 0`):

$$
\mathrm{proj}_v(u) = \frac{u \cdot v}{v \cdot v}\; v
$$

Ortogonalidade: `u` e `v` são ortogonais se `u · v = 0`.

## Exemplos

### Exemplo 1 — operações em R²

* Seja `u = (2, 1)` e `v = (−1, 3)`.
* Soma: `u + v = (1, 4)`.
* Escalar: `2·u = (4, 2)`.
* Produto escalar: `u · v = 2*(−1) + 1*3 = 1`.
* Norma de `u`: `||u|| = sqrt(5) ≈ 2.236`.
* Conclusão: `u` e `v` não são ortogonais porque `u · v ≠ 0`.

### Exemplo 2 — independência e base em R⁴

* Considere os vetores

  * `v1 = (1, 0, 0, 0)`
  * `v2 = (0, 1, 0, 0)`
  * `v3 = (1, 1, 1, 0)`
  * `v4 = (0, 0, 0, 1)`
* A matriz formada por essas colunas tem posto (rank) que indica o número máximo de vetores linearmente independentes do conjunto.
* Se o posto for `4`, os vetores formam uma base de `R^4`. Se for menor, não geram todo `R^4`.
* Para representar um vetor `w = (2,3,1,1)` como combinação linear desses vetores, resolvemos `A x = w` onde `A = [v1 v2 v3 v4]`.

## Exemplos em código (NumPy e Pandas)

* exemplo A: operações básicas (adição, escalar, dot, norma, projeção) em R²;
* exemplo B: conjunto em R⁴ — rank, independência e resolução `A x = w`;
* os DataFrames são usados apenas para visualização.

```python
import numpy as np
import pandas as pd

# Exemplo A: operações básicas em R^2
u = np.array([2.0, 1.0])
v = np.array([-1.0, 3.0])

soma = u + v                      # [1. 4.]
escalar = 2.0 * u                 # [4. 2.]
dot = float(u.dot(v))             # 1.0
norm_u = float(np.linalg.norm(u)) # sqrt(5)
proj_u_on_v = (u.dot(v) / v.dot(v)) * v if v.dot(v) != 0 else np.zeros_like(v)

df_basic = pd.DataFrame(
    [u, v, soma, escalar, proj_u_on_v],
    index=['u', 'v', 'u+v', '2*u', 'proj_u_on_v'],
    columns=['x1', 'x2']
)

print("Operações básicas (R^2):")
print(df_basic)
print(f"u · v = {dot}")
print(f"||u|| = {norm_u:.6f}\n")

# Exemplo B: vetores em R^4 — rank, independência, solução A x = w
v1 = np.array([1.0, 0.0, 0.0, 0.0])
v2 = np.array([0.0, 1.0, 0.0, 0.0])
v3 = np.array([1.0, 1.0, 1.0, 0.0])
v4 = np.array([0.0, 0.0, 0.0, 1.0])

A = np.column_stack([v1, v2, v3, v4])  # shape (4,4)
rank_A = np.linalg.matrix_rank(A)
independent = (rank_A == A.shape[1])

print("Matriz A (colunas v1..v4):")
print(A)
print(f"Rank(A) = {rank_A}")
print(f"Vetores v1..v4 linearmente independentes? {independent}\n")

# Representação de w = (2,3,1,1)
w = np.array([2.0, 3.0, 1.0, 1.0])
# Se A for quadrada e invertível, usar solve; caso contrário, lstsq
if rank_A == A.shape[0] == A.shape[1]:
    x = np.linalg.solve(A, w)
else:
    x, residuals, rank_solve, s = np.linalg.lstsq(A, w, rcond=None)

print("Coeficientes x tais que A @ x ≈ w:")
print(x)
# Verificação aproximada
reconstructed = A @ x
print("A @ x = ", reconstructed)
print("w      = ", w)
print("Residual (w - A@x) = ", w - reconstructed, "\n")

# Visualização em DataFrame (colunas representando vetores)
df_r4 = pd.DataFrame(np.column_stack([v1, v2, v3, v4, w]),
                     columns=['v1', 'v2', 'v3', 'v4', 'w'])
print("v1..v4 e w (colunas):")
print(df_r4)
```

* saídas e interpretações relevantes

  * no Exemplo A: veja `u + v`, `2·u`, `u · v`, `||u||` e projeção de `u` sobre `v`.
  * no Exemplo B: `rank(A)` mostra independência; `x` dá os coeficientes para representar `w` como combinação linear (se possível). O produto `A @ x` deve aproximar `w` (residual pequeno se sistema compatível).

## Observações práticas

* Para checar independência use `np.linalg.matrix_rank` sobre a matriz que tem os vetores como colunas (ou linhas).
* Para resolver representações exatas use `np.linalg.solve` quando a matriz for quadrada e inversível; caso contrário use `np.linalg.lstsq`.
* Para projeções, ângulos e ortogonalidade use produto escalar e norma; o cosseno do ângulo entre `u` e `v` pode ser calculado como `(u·v) / (||u|| ||v||)`.
* Em problemas numéricos e de dimensão alta prefira decomposições numéricas estáveis (SVD, QR) para obter robustez.
