# Bloco E - Aula 2: Matrizes

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-e---algebra-linear)
>
> retornar ao [README.md](../../../../README.md)

## Definição

Uma **matriz** é uma tabela retangular de números organizada em linhas e colunas. Matrizes representam transformações lineares, sistemas lineares, tabelas de dados e coeficientes em problemas de álgebra linear. Uma matriz com `m` linhas e `n` colunas é dita de dimensão `m × n`.

## Conceitos e notação (resumo)

* Uma matriz `A` de dimensão `m × n` tem entradas `a_{ij}`, com `i = 1..m` (linha) e `j = 1..n` (coluna).
* Matrizes quadradas têm `m = n`.
* Matriz identidade `I_n` é a matriz quadrada com 1 na diagonal e 0 fora dela.
* Matriz transposta `A^T` (ou `Aᵀ`) é obtida trocando linhas por colunas.
* Matriz invertível (não singular): `A` é invertível se existir `A^{-1}` tal que `A A^{-1} = A^{-1} A = I`.
* Rank: posto (rank) de `A` é o número máximo de colunas (ou linhas) linearmente independentes.
* Determinante: valor escalar associado a matrizes quadradas que, entre outras interpretações, indica se a matriz é invertível (`det(A) ≠ 0`).
* Traço (trace): soma dos elementos da diagonal principal, `tr(A)`.

## Operações fundamentais (fórmulas isoladas)

Adição e subtração (mesma dimensão):

$$
A + B = (a_{ij} + b_{ij})
$$

Multiplicação por escalar:

$$
\alpha A = (\alpha a_{ij})
$$

Multiplicação de matrizes (compatibilidade: A é m×p e B é p×n):

$$
(AB)_{i j} = \sum_{k=1}^{p} a_{i k}\, b_{k j}
$$

Transposta:

$$
(A^{T})_{i j} = a_{j i}
$$

Inversa (quando existe):

$$
A A^{-1} = A^{-1} A = I
$$

Determinante (para matriz quadrada):

$$
\det(A)
$$

Rank e trace (valores escalares associados a A):

$$
\operatorname{rank}(A),\quad \operatorname{tr}(A) = \sum_{i} a_{ii}
$$

## Exemplos

### Exemplo 1 — operações elementares (matrizes 2×2)

* Seja

  * `A = [[1, 2], [3, 4]]`
  * `B = [[0, 1], [1, 0]]`
* Adição: `A + B = [[1, 3], [4, 4]]`.
* Escalar: `2·A = [[2, 4], [6, 8]]`.
* Multiplicação: `A @ B = [[2, 1], [4, 3]]` (usar produto de linhas por colunas).
* Transposta: `A^T = [[1, 3], [2, 4]]`.
* Determinante: `det(A) = 1*4 - 2*3 = -2` → `A` é invertível.
* Inversa: `A^{-1} = (1/det(A)) * [[4, -2], [-3, 1]] = [[-2, 1], [1.5, -0.5]]`.

### Exemplo 2 — sistemas lineares e rank (matriz 3×3)

* Considere matriz de coeficientes `A` e vetor `b`. Resolver `A x = b` significa encontrar `x` tal que a combinação linear das colunas de `A` gere `b`.
* Se `rank(A) = n` (número de colunas) e `A` é quadrada, existe solução única `x = A^{-1} b`.
* Se `rank(A) < n`, o sistema pode ter infinitas soluções ou ser indeterminado; se `rank(A) < rank([A|b])` então é inconsistente (sem solução).

## Exemplos em código (NumPy e Pandas)

* criar matrizes com `np.array`, visualizar com `pd.DataFrame`;
* operações: `+`, `-`, `*` (elementwise), `@` (matriz), `np.dot`, `A.T`, `np.linalg.inv`, `np.linalg.det`, `np.linalg.matrix_rank`, `np.trace`, `np.linalg.solve`, `np.linalg.eig`.

```python
import numpy as np
import pandas as pd

# Matrizes exemplo
A = np.array([[1.0, 2.0],
              [3.0, 4.0]])
B = np.array([[0.0, 1.0],
              [1.0, 0.0]])

# Visualização
df_A = pd.DataFrame(A, columns=['c1', 'c2'], index=['r1', 'r2'])
df_B = pd.DataFrame(B, columns=['c1', 'c2'], index=['r1', 'r2'])

print("A:")
print(df_A)
print("\nB:")
print(df_B)

# Operações básicas
A_plus_B = A + B
scalar_times_A = 2.0 * A
A_dot_B = A @ B          # ou np.matmul(A, B)
A_T = A.T

print("\nA + B =")
print(pd.DataFrame(A_plus_B))
print("\n2 * A =")
print(pd.DataFrame(scalar_times_A))
print("\nA @ B =")
print(pd.DataFrame(A_dot_B))
print("\nA^T =")
print(pd.DataFrame(A_T))

# Determinante, inversa, rank, trace
det_A = float(np.linalg.det(A))
rank_A = int(np.linalg.matrix_rank(A))
trace_A = float(np.trace(A))
inv_A = np.linalg.inv(A) if det_A != 0 else None

print(f"\ndet(A) = {det_A:.6f}")
print(f"rank(A) = {rank_A}")
print(f"trace(A) = {trace_A}")
if inv_A is not None:
    print("A^{-1} =")
    print(pd.DataFrame(inv_A))

# Resolver sistema linear A x = b
b = np.array([5.0, 11.0])  # exemplo
if det_A != 0:
    x = np.linalg.solve(A, b)
    print("\nSolução de A x = b:")
    print(pd.DataFrame(x, index=['x1', 'x2']))
    # verificação
    print("A @ x = ", A @ x)
else:
    # caso singular: usar lstsq para solução em mínimos quadrados
    x, residuals, rank_solve, s = np.linalg.lstsq(A, b, rcond=None)
    print("\nSolução (mínimos quadrados) A x ≈ b:")
    print(pd.DataFrame(x, index=['x1', 'x2']))
    print("residuals:", residuals)

# Exemplo com matriz 3x3: autovalores/autovetores
C = np.array([[2.0, 0.0, 0.0],
              [0.0, 3.0, 4.0],
              [0.0, 4.0, 9.0]])
eigvals, eigvecs = np.linalg.eig(C)
print("\nMatriz C:")
print(pd.DataFrame(C))
print("\nAutovalores de C:", eigvals)
print("Autovetores (colunas):")
print(pd.DataFrame(eigvecs))
```

* saídas esperadas (resumidas)

  * `A + B`, `2·A`, `A @ B`, `A^T` mostrados como DataFrames.
  * `det(A) = -2.0`, `rank(A) = 2`, `trace(A) = 5.0`.
  * `A^{-1}` exibida quando `det(A) ≠ 0`.
  * solução do sistema `A x = b` retorna `x` com verificação `A @ x == b`.
  * para `C`, autovalores e autovetores numéricos calculados por `np.linalg.eig`.

## Observações práticas

* Para multiplicação, verifique compatibilidade de dimensões: `A (m×p)` pode multiplicar `B (p×n)` resultando em `m×n`.
* Evite usar o operador `*` para produto matricial em NumPy (use `@` ou `np.matmul`); `*` faz multiplicação elemento a elemento.
* Para sistemas lineares quadrados bem condicionados, use `np.linalg.solve` em vez de calcular explicitamente `A^{-1}`.
* Para matrizes grandes ou próximas da singularidade, prefira decomposições numéricas estáveis (LU, QR, SVD) em vez de inversão direta.
* Cuidado com condicionamento numérico: `np.linalg.cond(A)` dá uma noção da sensibilidade da solução a perturbações.
