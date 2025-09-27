# Bloco D - Aula 5: Combinações Simples

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Definição

Uma **combinação simples** é uma forma de **contagem de subconjuntos de k elementos de um conjunto de n elementos**, **onde a ordem não importa**.
Diferente dos arranjos, trocar a posição dos elementos **não gera uma nova combinação**.

A fórmula para calcular o número de combinações simples é:

$$
C_n^k = \frac{n!}{k! \cdot (n-k)!}
$$

Onde:

* `n` é o número total de elementos disponíveis.
* `k` é o número de elementos escolhidos para formar a combinação.
* `!` representa o fatorial.

## Exemplo

Suponha que temos 5 livros diferentes e queremos escolher 3 para levar em uma viagem. Como a **ordem não importa**, apenas o conjunto de livros conta, não a sequência.

* Conjunto: {A, B, C, D, E}
* Escolhendo 3: possíveis combinações incluem:

  * {A, B, C}
  * {A, B, D}
  * {A, C, D}
  * {B, C, E}

Número total de combinações:

$$
C_5^3 = \frac{5!}{3! \cdot (5-3)!} = \frac{120}{6 \cdot 2} = 10
$$

Portanto, existem **10 combinações diferentes**.

## Exemplo em código Python com NumPy e Pandas

Aqui, vamos gerar **combinações de 3 elementos a partir de um conjunto de 5 elementos**.

```python
import pandas as pd
from itertools import combinations

# Conjunto de elementos
elementos = ['A', 'B', 'C', 'D', 'E']

# Gerando combinações de 3 elementos
comb = list(combinations(elementos, 3))

# Convertendo para DataFrame para visualização
df_comb = pd.DataFrame(comb, columns=['Item1', 'Item2', 'Item3'])

# Mostrando número de combinações e os primeiros
print(f"Total de combinações: {len(comb)}")
print(df_comb.head(10))
```

### Saída esperada (resumida)

* Total de combinações: 10
* Combinações:

| Item1 | Item2 | Item3 |
| ----- | ----- | ----- |
| A     | B     | C     |
| A     | B     | D     |
| A     | B     | E     |
| A     | C     | D     |
| A     | C     | E     |
| A     | D     | E     |
| B     | C     | D     |
| B     | C     | E     |
| B     | D     | E     |
| C     | D     | E     |

## Exemplo com conjunto maior

Suponha que temos um time de 10 jogadores e queremos escolher **trios para treino**, sem considerar a posição:

```python
jogadores = [f'Jogador{i}' for i in range(1, 11)]

# Combinações de 3 jogadores
comb_trio = list(combinations(jogadores, 3))

# Convertendo em DataFrame
df_trio = pd.DataFrame(comb_trio, columns=['Jogador1', 'Jogador2', 'Jogador3'])

print(f"Total de combinações de treino: {len(comb_trio)}")
print(df_trio.head(5))
```

* Total de combinações: 120
* Aqui, **a ordem dos jogadores não importa**, então (Jogador1, Jogador2, Jogador3) é o mesmo que (Jogador3, Jogador2, Jogador1).

Este exemplo mostra como combinações simples são úteis para situações **onde apenas o grupo importa, não a ordem**.
