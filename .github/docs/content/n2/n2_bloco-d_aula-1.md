# Bloco D - Aula 1: Princípio Fundamental da Contagem (PFC)

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

O **Princípio Fundamental da Contagem** é a base da **Análise Combinatória**.
Ele estabelece que, quando um processo pode ser decomposto em **etapas independentes**, o **número total de resultados possíveis** é o **produto** do número de maneiras de realizar cada etapa.

## Definição formal

Se uma tarefa é composta por **k etapas independentes** e:

* a primeira pode ser realizada de **n₁** maneiras,
* a segunda de **n₂** maneiras,
* …,
* a k-ésima de **nₖ** maneiras,

então o **número total de possibilidades** é:

$$
N = n₁ \times n₂ \times \cdots \times nₖ
$$

## Exemplo em texto 1 – Refeição completa

Um restaurante oferece:

* 5 tipos de **entradas**,
* 7 tipos de **pratos principais**,
* 4 tipos de **sobremesas**,
* 3 tipos de **bebidas**.

Cada cliente escolhe **1 item de cada categoria**.
Como as escolhas são independentes, o total de combinações é:

$$
N = 5 \times 7 \times 4 \times 3 = 420
$$

Portanto, existem **420 refeições completas diferentes** possíveis.

## Exemplo em texto 2 – Senhas alfanuméricas

Considere senhas de **6 caracteres**, onde cada caractere pode ser:

* uma **letra maiúscula** (26 possibilidades), ou
* um **dígito** (10 possibilidades).

Total de opções para cada posição:

$$
26 + 10 = 36
$$

Total de senhas possíveis:

$$
36^6 = 2.176.782.336
$$

Existem **2.176.782.336** senhas diferentes.

## Exemplo em código – NumPy

Podemos usar o **NumPy** para calcular rapidamente essas possibilidades.

```python
import numpy as np

# Exemplo 1: refeições
entradas = 5
pratos = 7
sobremesas = 4
bebidas = 3

total_refeicoes = np.prod([entradas, pratos, sobremesas, bebidas])
print("Total de refeições possíveis:", total_refeicoes)

# Exemplo 2: senhas alfanuméricas
opcoes = 36  # 26 letras + 10 dígitos
tamanho_senha = 6

total_senhas = np.power(opcoes, tamanho_senha)
print("Total de senhas possíveis:", total_senhas)
```

Saída aproximada:

```plaintext
Total de refeições possíveis: 420
Total de senhas possíveis: 2176782336
```

---

## Exemplo em código – Pandas

Podemos usar o **Pandas** para estruturar os dados em um DataFrame, facilitando cálculos em cenários mais complexos.

```python
import pandas as pd
import numpy as np

# Criação de um DataFrame com as etapas e as opções
dados = pd.DataFrame({
    "Etapa": ["Entrada", "Prato Principal", "Sobremesa", "Bebida"],
    "Opcoes": [5, 7, 4, 3]
})

# Cálculo do total usando o produto das opções
total = np.prod(dados["Opcoes"])
print(dados)
print("\nTotal de combinações:", total)
```

Saída:

```plaintext
             Etapa  Opcoes
0          Entrada       5
1  Prato Principal       7
2         Sobremesa      4
3           Bebida       3

Total de combinações: 420
```

## Conclusão

O **Princípio Fundamental da Contagem** permite calcular, de maneira direta, o número de possibilidades em processos **sequenciais e independentes**, evitando a necessidade de listar cada combinação individualmente.
Ele é a **ferramenta inicial** para problemas de **Análise Combinatória** e **Probabilidade**.
