# Bloco C - Aula 2: Percentis (Medidas de Posição)

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-c---medidas-de-posição)
>
> retornar ao [README.md](../../../../README.md)

Os **percentis** são medidas estatísticas que **dividem um conjunto de dados ordenados em 100 partes iguais**, cada uma representando **1% da distribuição**.
Eles indicam a posição relativa de um valor dentro da amostra ou população, permitindo avaliar a **dispersão**, **concentração** e **comparação** entre indivíduos ou grupos.

## Tipos e interpretação

* **P25**: ponto abaixo do qual estão **25% dos dados** (equivale ao **Q1**).
* **P50**: ponto abaixo do qual estão **50% dos dados** (equivale à **mediana** ou **Q2**).
* **P75**: ponto abaixo do qual estão **75% dos dados** (equivale ao **Q3**).
* **P90**: ponto abaixo do qual estão **90% dos dados** (muito usado em provas, notas de corte e análises de desempenho).

## Exemplo em texto

Considere o conjunto de dados (ordenado):

$$
\{2,\ 4,\ 5,\ 7,\ 8,\ 10,\ 12,\ 15\}
$$

* **P25**: marca 25% dos dados → entre 4 e 5
  $\Rightarrow P25 \approx 4,5$
* **P50**: marca 50% dos dados → entre 7 e 8
  $\Rightarrow P50 \approx 7,5$
* **P75**: marca 75% dos dados → entre 10 e 12
  $\Rightarrow P75 \approx 11$
* **P90**: marca 90% dos dados → entre 12 e 15
  $\Rightarrow P90 \approx 14,1$ (aproximado)

Interpretação:
Por exemplo, uma nota no **P90** significa que o aluno obteve desempenho **igual ou superior a 90%** dos demais.

## Exemplo em código

### Usando **NumPy**

```python
import numpy as np

dados = np.array([2, 4, 5, 7, 8, 10, 12, 15])

p25 = np.percentile(dados, 25)
p50 = np.percentile(dados, 50)  # Mediana
p75 = np.percentile(dados, 75)
p90 = np.percentile(dados, 90)

print(f"P25: {p25}, P50: {p50}, P75: {p75}, P90: {p90}")
```

### Usando **Pandas**

```python
import pandas as pd

dados = pd.Series([2, 4, 5, 7, 8, 10, 12, 15])

percentis = dados.quantile([0.25, 0.50, 0.75, 0.90])
print(percentis)
```

Saída esperada (aproximada):

```plaintext
0.25     4.5
0.50     7.5
0.75    11.0
0.90    14.1
dtype: float64
```

## Resumo

* **Percentis** dividem os dados em **100 partes iguais**.
* São úteis para avaliar **posicionamento relativo**, como notas em provas, tempos em corridas ou rendimentos em testes.
* **Quartis** são casos especiais de percentis: **Q1 = P25**, **Q2 = P50**, **Q3 = P75**.
