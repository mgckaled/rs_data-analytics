# Bloco D - Aula 2: Fatorial

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Conceito

O **fatorial** de um número natural $n$, representado por $n!$, é o **produto de todos os números inteiros positivos de 1 até $n$**.
É uma das operações mais importantes em **Análise Combinatória e Probabilidade**, pois é usada para calcular **permutação**, **combinação**, e outros arranjos.

A definição formal é:

$$
n! = n \times (n - 1) \times (n - 2) \times \cdots \times 2 \times 1
$$

Por convenção,

$$
0! = 1
$$

## Exemplos

* **Exemplo 1:**
  Calcular $5!$:

  $$
  5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
  $$

* **Exemplo 2 (Aplicação):**
  Quantas maneiras diferentes podemos organizar 6 pessoas em uma fila?
  Cada posição é única, logo:

  $$
  6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720
  $$

  Existem **720 permutações** possíveis.

## Exemplo em Código (NumPy e Pandas)

A seguir, um exemplo prático com cálculo de fatoriais de um conjunto maior de números.

```python
import numpy as np
import pandas as pd
import math

# Conjunto de números de 0 a 10
numeros = np.arange(0, 11)

# Cálculo do fatorial usando numpy e math.factorial
fatoriais = np.array([math.factorial(n) for n in numeros])

# Criação de um DataFrame para visualização
df = pd.DataFrame({
    "Número": numeros,
    "Fatorial": fatoriais
})

print(df)
```

### Saída esperada (resumida)

| Número | Fatorial |
| -----: | -------: |
|      0 |        1 |
|      1 |        1 |
|      2 |        2 |
|      3 |        6 |
|      4 |       24 |
|      5 |      120 |
|      6 |      720 |
|      7 |     5040 |
|      8 |    40320 |
|      9 |   362880 |
|     10 |  3628800 |

## Observação

* O fatorial cresce **muito rapidamente**.
* Para valores grandes (por exemplo, $20!$), os números tornam-se extremamente grandes, exigindo cuidado com desempenho e tipo de dado.
