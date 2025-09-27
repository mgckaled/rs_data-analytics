# Bloco C - Aula 4: Gráfico Bloxplot (Medidas de Posição)

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-c---medidas-de-posição)
>
> retornar ao [README.md](../../../../README.md)

O **boxplot** (ou **diagrama de caixa**) é um tipo de gráfico estatístico usado para **resumir e visualizar a distribuição de um conjunto de dados**.
Ele destaca **tendência central**, **dispersão** e **possíveis outliers** de forma compacta.

## Elementos principais

Um boxplot é construído a partir de **cinco números-chave** (também chamados de *five-number summary*):

* **Mínimo**: menor valor dentro do limite permitido (excluindo outliers).
* **Q1 (1º quartil)**: 25% dos dados estão abaixo desse valor.
* **Mediana (Q2)**: 50% dos dados estão abaixo desse valor.
* **Q3 (3º quartil)**: 75% dos dados estão abaixo desse valor.
* **Máximo**: maior valor dentro do limite permitido (excluindo outliers).

**Outliers** (valores atípicos) são geralmente marcados como pontos individuais, fora dos "bigodes" (*whiskers*), que se estendem normalmente até:

$$
[Q1 - 1,5 \times AIQ,\ Q3 + 1,5 \times AIQ]
$$

onde $AIQ = Q3 - Q1$.

## Interpretação

* A **caixa** mostra onde está a metade central dos dados (entre Q1 e Q3).
* A **linha dentro da caixa** é a mediana (Q2).
* Os **bigodes** indicam a variação dos dados, sem considerar outliers.
* **Pontos fora dos bigodes** indicam valores anormais (outliers).

## Exemplo em texto

Suponha o conjunto:

$$
\{2, 4, 5, 7, 8, 10, 12, 15\}
$$

* Q1 = 4,5
* Mediana = 7,5
* Q3 = 11
* AIQ = 6,5
* Limites dos bigodes:

  * Inferior = $4,5 - 1,5 \times 6,5 \approx -5,25$
  * Superior = $11 + 1,5 \times 6,5 \approx 20,75$

Como todos os dados estão dentro desses limites, **não há outliers**.

## Exemplo em código

### Usando **Matplotlib**

```python
import matplotlib.pyplot as plt

dados = [2, 4, 5, 7, 8, 10, 12, 15]

plt.boxplot(dados, vert=True, patch_artist=True)
plt.title("Boxplot dos Dados")
plt.ylabel("Valores")
plt.show()
```

### Usando **Pandas** (com DataFrame)

```python
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.Series([2, 4, 5, 7, 8, 10, 12, 15])

dados.plot(kind="box", title="Boxplot dos Dados")
plt.ylabel("Valores")
plt.show()
```

## Resumo

* O **boxplot** exibe, em um único gráfico, **mediana, quartis, dispersão e outliers**.
* É ideal para **comparar distribuições** entre diferentes grupos ou amostras.
