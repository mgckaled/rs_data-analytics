# Bloco A - Aula 4: Moda e Mediana

> retornar ao [Índice de Aulas](n2_index-aulas.md)
>
> retornar ao [README.md](../../../../README.md)

Nesta aula, aprofundamos duas medidas fundamentais de tendência central: **[moda](https://en.wikipedia.org/wiki/Mode_%28statistics%29)** e **[mediana](https://en.wikipedia.org/wiki/Median)**. Ambas são complementares à média e oferecem uma **visão mais precisa em certos contextos**, especialmente quando os dados são assimétricos ou contêm valores extremos.

## Moda – O valor mais frequente

A **moda** é a medida que **representa o valor que ocorre com maior frequência** em um conjunto de dados.

### Características da Moda

* Pode haver **mais de uma moda** (bimodal ou multimodal);
* Pode **não existir moda** se nenhum valor se repete;
* É muito útil em dados **categóricos ou discretos**.

### Exemplo 1 – Compras em uma loja

Suponha que uma loja vende os seguintes números de um mesmo tênis durante uma semana:

```plaintext
Tamanhos vendidos: 38, 39, 39, 38, 40, 39, 41
```

O tamanho **39** aparece 3 vezes, mais do que os outros. Moda = 39

---

## Mediana – O valor central

A **mediana** representa o **valor central** de um conjunto de dados **ordenado**. É particularmente útil quando os dados contêm **valores extremos (outliers)** que distorcem a média.

### Como calcular

1. Ordene os dados do menor para o maior;
2. Se a quantidade for **ímpar**, a mediana é o valor do meio;
3. Se for **par**, a mediana é a média dos dois valores centrais.

### Exemplo 2 – Tempo de uso de um app (em minutos)

```plaintext
Dados: 8, 10, 12, 13, 16, 18, 20
```

Há 7 valores → posição central é o 4º: Mediana = 13

### Exemplo 3 – Número par de dados

```plaintext
Dados: 5, 6, 8, 12, 14, 18
```

Há 6 valores → média dos dois centrais (8 e 12):

$$
\text{Mediana} = \frac{8 + 12}{2} = 10
$$

## Comparação: Moda × Mediana × Média

| Medida                                                      | Define               | Quando usar                                       |
| ----------------------------------------------------------- | -------------------- | ------------------------------------------------- |
| [Moda](https://en.wikipedia.org/wiki/Mode_%28statistics%29) | Valor mais frequente | Dados categóricos, preferências, vendas repetidas |
| [Mediana](https://en.wikipedia.org/wiki/Median)             | Valor central        | Dados assimétricos, presença de outliers          |
| [Média](https://en.wikipedia.org/wiki/Arithmetic_mean)      | Valor médio          | Dados simétricos, sem distorções relevantes       |

## Visualização gráfica da mediana e moda em uma distribuição

![Distribuição com média, moda e mediana](https://upload.wikimedia.org/wikipedia/commons/d/de/Comparison_mean_median_mode.svg)

## Conclusão

A **moda** e a **mediana** são ferramentas poderosas para entender o comportamento dos dados, especialmente quando a **média não representa bem a realidade**. Saber qual medida aplicar é fundamental para **evitar interpretações erradas e tomar decisões mais acertadas**.

> [!NOTE]
> Em situações com muitos valores extremos, **prefira a mediana**. Se a frequência for mais relevante que o valor médio, **use a moda**.
