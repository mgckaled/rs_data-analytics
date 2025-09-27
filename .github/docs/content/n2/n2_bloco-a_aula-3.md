# Bloco A - Aula 3: Média Aritmética

> retornar ao [Índice de Aulas](n2_index-aulas.md)
>
> retornar ao [README.md](../../../../README.md)

Nesta aula, aprofundamos nosso estudo das **medidas de tendência central**, com foco especial na **média aritmética** — uma das formas mais comuns de representar um valor típico em um conjunto de dados.

A média aritmética é útil para **resumir grandes volumes de dados** em um único número representativo, facilitando a interpretação de fenômenos como desempenho acadêmico, fluxo de acessos, vendas ou produtividade.

## O que é a Média Aritmética?

A **[média aritmética](https://en.wikipedia.org/wiki/Arithmetic_mean)** é calculada somando todos os valores de um conjunto de dados e dividindo o total pela quantidade de observações.

$$
\text{Média} = \frac{x_1 + x_2 + \ldots + x_n}{n}
$$

Onde:

* $x_1, x_2, \ldots, x_n$ são os valores observados;
* $n$ é o número de observações.

## Exemplo prático

Suponha que estamos analisando os **acessos diários a um site durante uma semana**:

| Dia     | Acessos |
| ------- | ------- |
| Segunda | 180     |
| Terça   | 195     |
| Quarta  | 210     |
| Quinta  | 185     |
| Sexta   | 202     |
| Sábado  | 190     |
| Domingo | 228     |

**Cálculo:**

$$
\text{Média} = \frac{180 + 195 + 210 + 185 + 202 + 190 + 228}{7} = \frac{1390}{7} \approx 198{,}57
$$

Portanto, a **média de acessos diários é aproximadamente 198,57**.

## Quando usar a média?

* Quando os dados **não possuem valores extremos (outliers)** que distorcem o resultado;
* Para **representar um comportamento geral** de fenômenos quantitativos;
* Em contextos de **avaliações, finanças, economia, estatísticas esportivas**, entre outros.

## Limitações da média

* **Sensível a valores extremos**: um único valor muito alto ou muito baixo pode distorcer significativamente a média.
* **Não reflete a distribuição dos dados**: duas amostras com a mesma média podem ter variações muito diferentes.

## Comparação com outras medidas de tendência central

| Medida                                                      | Definição                                 | Quando usar                         |
| ----------------------------------------------------------- | ----------------------------------------- | ----------------------------------- |
| [Média](https://en.wikipedia.org/wiki/Mean)                 | Soma dos valores dividida pela quantidade | Dados simétricos, sem outliers      |
| [Mediana](https://en.wikipedia.org/wiki/Median)             | Valor central de um conjunto ordenado     | Dados assimétricos ou com outliers  |
| [Moda](https://en.wikipedia.org/wiki/Mode_%28statistics%29) | Valor mais frequente                      | Dados categóricos ou com repetições |

## Visualização

Abaixo, um gráfico ilustrativo mostrando a média em uma distribuição normal:

![Distribuição com média](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/640px-Standard_deviation_diagram.svg.png)
[Fonte: Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Standard_deviation_diagram.svg)

## Conclusão

A **média aritmética** é uma ferramenta simples, porém poderosa, para **resumir e comparar conjuntos de dados**. É uma das primeiras estatísticas que aprendemos, mas seu uso correto exige atenção às características do conjunto analisado.

Saber **quando usar a média e quando optar por mediana ou moda** faz toda a diferença na qualidade da análise estatística.
