# Bloco C - Aula 3: Amplitude Interquartil  (Medidas de Posição)

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-c---medidas-de-posição)
>
> retornar ao [README.md](../../../../README.md)

A **Amplitude Interquartil** é uma **medida de dispersão** que representa a variação dos **50% centrais** de um conjunto de dados.
Ela é calculada como a **diferença entre o terceiro quartil (Q3)** e o **primeiro quartil (Q1)**:

$$
\text{AIQ} = Q3 - Q1
$$

## Interpretação

* Indica o **intervalo em que se encontra a metade central dos dados**, ignorando os 25% mais baixos e os 25% mais altos.
* É **menos sensível a outliers** do que a amplitude total, pois desconsidera valores extremos.

## Exemplo em texto

Considere o conjunto de dados:

$$
\{2,\ 4,\ 5,\ 7,\ 8,\ 10,\ 12,\ 15\}
$$

Já sabemos que:

* $Q1 = 4,5$
* $Q3 = 11$

Então:

$$
\text{AIQ} = 11 - 4,5 = 6,5
$$

Interpretação:

* Os 50% centrais dos dados variam em um intervalo de **6,5 unidades**.

## Exemplo em código

### Usando **NumPy**

```python
import numpy as np

dados = np.array([2, 4, 5, 7, 8, 10, 12, 15])

q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
aiq = q3 - q1

print(f"Q1: {q1}, Q3: {q3}, AIQ: {aiq}")
```

### Usando **Pandas**

```python
import pandas as pd

dados = pd.Series([2, 4, 5, 7, 8, 10, 12, 15])

q1 = dados.quantile(0.25)
q3 = dados.quantile(0.75)
aiq = q3 - q1

print(f"Q1: {q1}, Q3: {q3}, AIQ: {aiq}")
```

Saída aproximada:

```plaintext
Q1: 4.5, Q3: 11.0, AIQ: 6.5
```

## Resumo

* **Amplitude Interquartil (AIQ)** mede a dispersão da **metade central** dos dados.
* Fórmula: **Q3 – Q1**
* Vantagem: **robusta** contra outliers, ideal para dados assimétricos.
