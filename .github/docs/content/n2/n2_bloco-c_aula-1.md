# Bloco C - Aula 1: Quartis (Medidas de Posição)

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-c---medidas-de-posição)
>
> retornar ao [README.md](../../../../README.md)

Os **quartis** são medidas estatísticas que **dividem um conjunto de dados ordenados em quatro partes iguais**, cada uma contendo **25%** das observações.
Eles indicam **posições específicas** dentro da distribuição, ajudando a entender a **dispersão** e a **tendência central**.

## Tipos de quartis

* **Q1 (1º quartil)**: valor que separa os **25% menores** dados do restante (também chamado de **quartil inferior**).
* **Q2 (2º quartil)**: corresponde à **mediana**, dividindo os **50% inferiores** dos **50% superiores**.
* **Q3 (3º quartil)**: valor que separa os **75% menores** dos **25% maiores** (também chamado de **quartil superior**).

## Exemplo

Considere o conjunto de dados (já ordenado):

$$
\{2,\ 4,\ 5,\ 7,\ 8,\ 10,\ 12,\ 15\}
$$

* **Q1**: Posição que marca 25% dos dados → entre 4 e 5
  $\Rightarrow Q1 \approx 4,5$
* **Q2**: Mediana (50%) → entre 7 e 8
  $\Rightarrow Q2 \approx 7,5$
* **Q3**: Posição que marca 75% dos dados → entre 10 e 12
  $\Rightarrow Q3 \approx 11$

Interpretação:

* 25% dos valores são **≤ 4,5**
* 50% dos valores são **≤ 7,5**
* 75% dos valores são **≤ 11**

## Exemplo em código

### Usando **NumPy**

```python
import numpy as np

dados = np.array([2, 4, 5, 7, 8, 10, 12, 15])

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)  # Mediana
q3 = np.percentile(dados, 75)

print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")
```

### Usando **Pandas**

```python
import pandas as pd

dados = pd.Series([2, 4, 5, 7, 8, 10, 12, 15])

quartis = dados.quantile([0.25, 0.50, 0.75])
print(quartis)
```

Saída esperada (aproximada):

```text
0.25     4.5
0.50     7.5
0.75    11.0
dtype: float64
```

## Resumo

* **Quartis** dividem os dados em quatro partes com 25% das observações cada.
* **Q1, Q2 e Q3** são fundamentais para identificar **tendência central** e **dispersão**, sendo usados em análises como **boxplot** e **identificação de outliers**.
