# Bloco D - Aula 6: Espaço Amostral e Eventos

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Definição

O **espaço amostral** Ω é o conjunto de todos os resultados possíveis de um experimento aleatório.
Um **evento** é qualquer subconjunto de Ω (pode conter um, vários ou nenhum resultado).
Em espaços discretos equiprováveis, a probabilidade de um evento E é a razão entre o número de resultados favoráveis e o número total de resultados.

$$
P(E) = \frac{|E|}{|\Omega|}
$$

## Operações básicas entre eventos

* União: `A ∪ B` contém os resultados que pertencem a `A` ou `B` (ou ambos).
* Interseção: `A ∩ B` contém os resultados que pertencem simultaneamente a `A` e `B`.
* Complemento: `A^c` contém os resultados de Ω que não pertencem a `A`.
* Disjunção (mutuamente exclusivos): `A ∩ B = ∅` significa que `A` e `B` não têm resultados em comum.

Fórmulas úteis (em blocos, fora de listas)

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

$$
P(A^{c}) = 1 - P(A)
$$

Se `A` e `B` são disjuntos então

$$
P(A \cup B) = P(A) + P(B)
$$

## Exemplos

### Experimento 1 — moeda lançada duas vezes

Ω = `{HH, HT, TH, TT}`

Evento A: obter pelo menos uma cara
A = `{HH, HT, TH}`

|Ω| = 4
|A| = 3

$$
P(A) = \frac{|A|}{|\Omega|} = \frac{3}{4} = 0{,}75
$$

---

## Experimento 2 — dois dados justos (cada dado com faces 1–6)

Ω é o conjunto dos pares ordenados `(d1, d2)` com `d1, d2 ∈ {1,2,3,4,5,6}`

$$
|\Omega| = 6 \times 6 = 36
$$

Evento B: soma igual a 7
B = `{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}`
|B| = 6

$$
P(B) = \frac{|B|}{|\Omega|} = \frac{6}{36} = \frac{1}{6} \approx 0{,}1667
$$

---

## Experimento 3 — sortear 3 bolas de uma urna com 5 distintas, sem ordem

Os resultados são as combinações de 3 elementos dentre 5.

$$
|\Omega| = \binom{5}{3} = 10
$$

Se todos os resultados em Ω forem equiprováveis, para qualquer evento $E \subseteq \Omega$:

$$
P(E) = \frac{|E|}{10}
$$

### Exemplos em código (NumPy e Pandas)

* exemplo 1: moeda lançada duas vezes — enumerar Ω, definir eventos e calcular probabilidades.
* exemplo 2: dois dados — enumerar pares, construir DataFrame, calcular interseção/união.
* exemplo 3: exemplo com conjunto maior (urna com 5 bolas, combinações) — usar itertools para combinações e mostrar contagens.

```python
import numpy as np
import pandas as pd
from itertools import product, combinations

# Exemplo 1: moeda lançada duas vezes
faces_moeda = ['H', 'T']
omega_moeda = [''.join(p) for p in product(faces_moeda, repeat=2)]  # ['HH','HT','TH','TT']
df_moeda = pd.DataFrame({'outcome': omega_moeda})
df_moeda['at_least_one_H'] = df_moeda['outcome'].str.contains('H')

total_m = len(df_moeda)
count_A = df_moeda['at_least_one_H'].sum()
prob_A = count_A / total_m

print("Moeda (2 lançamentos)")
print(df_moeda)
print(f"Total outcomes: {total_m}")
print(f"Eventos com pelo menos uma cara: {count_A}")
print(f"P(A) = {prob_A:.4f}\n")

# Exemplo 2: dois dados
faces = np.arange(1, 7)
omega_dados = list(product(faces, faces))  # 36 resultados ordenados
df_dados = pd.DataFrame(omega_dados, columns=['d1', 'd2'])
df_dados['sum'] = df_dados['d1'] + df_dados['d2']

# Evento B: soma igual a 7
df_dados['is_sum_7'] = df_dados['sum'] == 7

# Evento C: primeiro dado é par
df_dados['first_is_even'] = (df_dados['d1'] % 2 == 0)

total_d = len(df_dados)
count_B = df_dados['is_sum_7'].sum()
count_C = df_dados['first_is_even'].sum()
count_B_and_C = df_dados['is_sum_7' ].mul(df_dados['first_is_even']).sum()  # interseção

prob_B = count_B / total_d
prob_C = count_C / total_d
prob_B_and_C = count_B_and_C / total_d
prob_B_or_C = prob_B + prob_C - prob_B_and_C

print("Dois dados")
print(df_dados.head(10))
print(f"Total outcomes: {total_d}")
print(f"|B| (soma 7): {count_B} -> P(B) = {prob_B:.4f}")
print(f"|C| (primeiro é par): {count_C} -> P(C) = {prob_C:.4f}")
print(f"|B ∩ C|: {count_B_and_C} -> P(B ∩ C) = {prob_B_and_C:.4f}")
print(f"P(B ∪ C) = {prob_B_or_C:.4f}\n")

# Exemplo 3: combinação (urna com 5 bolas, sortear 3, sem ordem)
bolas = [f'B{i}' for i in range(1, 6)]  # B1..B5
omega_urna = list(combinations(bolas, 3))  # 10 combinações
df_urna = pd.DataFrame(omega_urna, columns=['x1', 'x2', 'x3'])

total_u = len(df_urna)
# Exemplo de evento E: combinacoes que incluem 'B1'
df_urna['contains_B1'] = df_urna.apply(lambda r: 'B1' in r.values, axis=1)
count_E = df_urna['contains_B1'].sum()
prob_E = count_E / total_u

print("Urna (5 bolas, escolher 3 sem ordem)")
print(df_urna)
print(f"Total outcomes: {total_u}")
print(f"|E| (contém B1): {count_E} -> P(E) = {prob_E:.4f}")
```

* saídas esperadas (resumidas)

  * moeda: `Total outcomes: 4`, `Eventos com pelo menos uma cara: 3`, `P(A) = 0.75`.
  * dados: `Total outcomes: 36`, `|B| = 6`, `P(B) ≈ 0.1667`, `P(B ∪ C) ≈ 0.5833`.
  * urna: `Total outcomes: 10`, `|E| = 4` (combinações contendo B1), `P(E) = 0.4`.

## Observações práticas finais

* Determine sempre Ω antes de definir eventos; sem Ω não há contagem consistente.
* Em espaços equiprováveis calcule contagens e divida; em espaços não equiprováveis some as probabilidades individuais dos resultados que compõem o evento.
* Use enumeração explícita (product/combinations) para pequenos e médios espaços; para espaços muito grandes recorra a técnicas analíticas ou simulação Monte Carlo.
