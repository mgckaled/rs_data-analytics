# Bloco B - Aula 2: Variância e Desvio Padrão

> retornar ao [Índice de Aulas](n2_index-aulas.md)
>
> retornar ao [README.md](../../../../README.md)

Nesta aula, vamos explorar os conceitos de **variância** e **desvio padrão**. Vou explicar como calcular a variância de forma simples e por que ela é importante. O desvio padrão nos mostra o quanto os valores se afastam da média, e isso é crucial para uma análise mais precisa. Usando um exemplo prático de faturamento em lojas, vamos entender como a média pode ser enganosa e como a variância e o desvio padrão nos ajudam a ter uma visão mais clara dos dados.

## O que é Variância?

A **variância** é a média dos quadrados das diferenças entre cada valor e a média do conjunto. Ela mostra o grau médio de afastamento dos dados em relação à média.

$$
\text{Variância} = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

Onde:

* $x_i$ são os valores observados;
* $\bar{x}$ é a média dos valores;
* $n$ é o número total de observações.

Mais detalhes podem ser vistos em [Variance (Wikipedia)](https://en.wikipedia.org/wiki/Variance).

## O que é Desvio Padrão?

O **desvio padrão** é a raiz quadrada da variância. Ele expressa a dispersão dos dados na mesma unidade das observações, facilitando a interpretação.

$$
\text{Desvio Padrão} = \sqrt{\text{Variância}}
$$

Quanto maior o desvio padrão, maior a variação dos dados em relação à média.

Confira mais informações em [Standard Deviation (Wikipedia)](https://en.wikipedia.org/wiki/Standard_deviation).

## Por que são importantes?

* A **média sozinha pode ser enganosa**: duas lojas podem ter a mesma média de faturamento, mas uma pode ter vendas muito estáveis e a outra vendas muito variadas.
* A variância e o desvio padrão revelam a **regularidade ou instabilidade dos dados**, permitindo análises mais precisas e decisões melhor fundamentadas.

## Exemplo prático

Considere o faturamento mensal (em milhares) de duas lojas em um semestre:

| Loja A | Loja B |
| ------ | ------ |
| 100    | 60     |
| 102    | 100    |
| 98     | 150    |
| 101    | 80     |
| 99     | 130    |
| 100    | 70     |

* Ambas têm média próxima de 100 mil.
* Porém, a **Loja A apresenta baixo desvio padrão**, indicando faturamento estável.
* A **Loja B tem desvio padrão alto**, mostrando grandes variações nos valores.

## Visualização

![Desvio padrão ilustrado](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/640px-Standard_deviation_diagram.svg.png)
[Fonte: Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Standard_deviation_diagram.svg)

## Conclusão

Compreender a **variância** e o **desvio padrão** é essencial para interpretar corretamente os dados e suas variações. Essas medidas complementam a média, permitindo análises mais robustas e decisões informadas.
