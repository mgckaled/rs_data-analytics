# Bloco D - Aula 4: Arranjo Simples

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Definição

Um **arranjo simples** é uma forma de **contagem de combinações ordenadas** em que selecionamos **k elementos distintos de um conjunto de n elementos**, considerando a **ordem dos elementos**.
Ou seja, mudar a posição dos elementos gera um arranjo diferente.

A fórmula para calcular o número de arranjos simples é:

$$
A_n^k = \frac{n!}{(n-k)!}
$$

Onde:

* `n` é o número total de elementos disponíveis.
* `k` é o número de elementos escolhidos para formar o arranjo.
* `!` representa o fatorial.

## Exemplo

Suponha que temos 5 livros diferentes e queremos escolher 3 para colocar em uma prateleira. Como a **ordem importa**, cada sequência diferente é um arranjo.

* Conjunto: {A, B, C, D, E}
* Escolhendo 3: possíveis arranjos incluem:

  * (A, B, C)
  * (A, C, B)
  * (B, A, C)
  * (C, A, B)

Número total de arranjos:

$$
A_5^3 = \frac{5!}{(5-3)!} = \frac{120}{2} = 60
$$

Portanto, existem **60 arranjos diferentes**.

---

## Exemplo em código Python com NumPy e Pandas

Aqui, vamos gerar **arranjos de 3 elementos a partir de um conjunto de 5 elementos**.

```python
import pandas as pd
from itertools import permutations

# Conjunto de elementos
elementos = ['A', 'B', 'C', 'D', 'E']

# Gerando arranjos de 3 elementos
arranjos = list(permutations(elementos, 3))

# Convertendo para DataFrame para visualização
df_arranjos = pd.DataFrame(arranjos, columns=['Pos1', 'Pos2', 'Pos3'])

# Mostrando número de arranjos e os primeiros
print(f"Total de arranjos: {len(arranjos)}")
print(df_arranjos.head(10))
```

### Saída esperada (resumida)

* Total de arranjos: 60
* Primeiros 10 arranjos:

| Pos1 | Pos2 | Pos3 |
| ---- | ---- | ---- |
| A    | B    | C    |
| A    | B    | D    |
| A    | B    | E    |
| A    | C    | B    |
| A    | C    | D    |
| A    | C    | E    |
| A    | D    | B    |
| A    | D    | C    |
| A    | D    | E    |
| A    | E    | B    |

---

## Exemplo com conjunto maior

Suponha um time de 10 jogadores e queremos formar **trios de ataque** considerando a posição na formação.

```python
jogadores = [f'Jogador{i}' for i in range(1, 11)]

# Arranjos de 3 jogadores
arranjos_trio = list(permutations(jogadores, 3))

# Convertendo em DataFrame
df_trio = pd.DataFrame(arranjos_trio, columns=['Ataque1', 'Ataque2', 'Ataque3'])

print(f"Total de arranjos de ataque: {len(arranjos_trio)}")
print(df_trio.head(5))
```

* Total de arranjos: 720
* Cada arranjo considera **a ordem dos jogadores na formação**, então (Jogador1, Jogador2, Jogador3) é diferente de (Jogador3, Jogador2, Jogador1).

Esse exemplo mostra como arranjos simples são úteis para situações **onde a ordem importa**, tanto em pequenos conjuntos quanto em grandes.
