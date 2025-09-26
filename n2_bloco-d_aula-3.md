# Bloco D - Aula 3: Permutação Simples

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Conceito

A **permutação simples** corresponde ao **número de maneiras diferentes de ordenar** todos os elementos distintos de um conjunto, **sem repetição** e **considerando a ordem**.
Quando temos $n$ elementos distintos, a quantidade de permutações é dada por:

$$
P(n) = n!
$$

Onde $n!$ é o **fatorial** de $n$.

---

## Exemplos

* **Exemplo 1 (Palavra):**
  Quantas maneiras diferentes podemos organizar as letras da palavra **LUA** (3 letras distintas)?

  $$
  P(3) = 3! = 3 \times 2 \times 1 = 6
  $$

  Possíveis ordens: LUA, LAU, ULA, UAL, ALU, AUL.

* **Exemplo 2 (Grupo maior):**
  Uma empresa deseja organizar **7 funcionários distintos** em uma fila para uma foto oficial.
  Quantas permutações são possíveis?

  $$
  P(7) = 7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5040
  $$

  Existem **5040 maneiras** de ordenar os 7 funcionários.

## Exemplo em Código (NumPy e Pandas)

A seguir, um cálculo de permutações simples para diferentes valores de $n$:

```python
import numpy as np
import pandas as pd
import math

# Conjunto de tamanhos (ex.: número de elementos de 1 a 10)
elementos = np.arange(1, 11)

# Cálculo das permutações simples (n!)
permutacoes = np.array([math.factorial(n) for n in elementos])

# Criação de DataFrame
df = pd.DataFrame({
    "n (elementos distintos)": elementos,
    "Permutações Simples (n!)": permutacoes
})

print(df)
```

### Saída esperada (resumida)

| n (elementos distintos) | Permutações Simples (n!) |
| ----------------------: | -----------------------: |
|                       1 |                        1 |
|                       2 |                        2 |
|                       3 |                        6 |
|                       4 |                       24 |
|                       5 |                      120 |
|                       6 |                      720 |
|                       7 |                     5040 |
|                       8 |                    40320 |
|                       9 |                   362880 |
|                      10 |                  3628800 |

## Observação

* A **ordem importa** em permutações simples.
* É um caso específico em que usamos **todos os elementos disponíveis** do conjunto, sem repetição.
