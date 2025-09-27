# Bloco D - Aula 7: Probabilidade

> retornar ao [Índice de Aulas](n2_index-aulas.md#bloco-d---análise-combinatória-e-probabilidade)
>
> retornar ao [README.md](../../../../README.md)

## Definição

A **probabilidade** é a medida numérica da chance de ocorrência de um evento dentro de um experimento aleatório. Dados um espaço amostral Ω e um evento `E ⊆ Ω`, quando todos os resultados de Ω são equiprováveis:

$$
P(E) = \frac{|E|}{|\Omega|}
$$

* Valores possíveis: `0 ≤ P(E) ≤ 1`.
* Evento certo: `P(Ω) = 1`.
* Evento impossível: `P(∅) = 0`.

## Conceitos fundamentais

Probabilidade condicional: probabilidade de `A` ocorrer dado que `B` ocorreu:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \text{se } P(B) > 0
$$

Independência: `A` e `B` são independentes se `P(A ∩ B) = P(A) P(B)`.

Lei da probabilidade total: se `B1, ..., Bn` formam uma partição de Ω com `P(Bi) > 0` então:

$$
P(A) = \sum_{i=1}^{n} P(A \mid B_i)\,P(B_i)
$$

Teorema de Bayes: para `P(A)>0` e `P(B)>0`:

$$
P(B \mid A) = \frac{P(A \mid B)\,P(B)}{P(A)}
$$

Esperança e variância (variáveis discretas):

$$
\mathbb{E}[X] = \sum_x x\,P(X=x)
$$

$$
\mathrm{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

## Propriedades úteis

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

$$
P(A^{c}) = 1 - P(A)
$$

Se `A` e `B` são disjuntos (`A ∩ B = ∅`) então

$$
P(A \cup B) = P(A) + P(B)
$$

## Exemplos

### Experimento 1 — moeda lançada duas vezes

Ω = `{HH, HT, TH, TT}`

Evento `A`: obter pelo menos uma cara
A = `{HH, HT, TH}`

|Ω| = 4
|A| = 3

$$
P(A) = \frac{|A|}{|\Omega|} = \frac{3}{4} = 0{,}75
$$

### Experimento 2 — dois dados justos (cada dado com faces 1–6)

Ω é o conjunto dos pares ordenados `(d1, d2)` com `d1, d2 ∈ {1,2,3,4,5,6}`

$$
|\Omega| = 6 \times 6 = 36
$$

Evento `B`: soma igual a 7
B = `{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}`

|B| = 6

$$
P(B) = \frac{|B|}{|\Omega|} = \frac{6}{36} = \frac{1}{6} \approx 0{,}1667
$$

### Experimento 3 — retirar 2 cartas de um baralho padrão sem reposição

Ω são as combinações unordered de 2 cartas entre 52: `|Ω| = C(52,2) = 1326`

Evento `C`: ambas as cartas são copas
Número de pares de copas = `C(13,2) = 78`

$$
P(C) = \frac{78}{1326} \approx 0{,}0588
$$

## Exemplos em código (NumPy e Pandas)

* exemplo 1: moeda (2 lançamentos) — enumerar Ω, definir evento e calcular `P`.
* exemplo 2: dois dados — enumerar pares, calcular `P(soma=7)`, `P(primeiro par)`, `P(soma=7 | primeiro par)`.
* exemplo 3: baralho (2 cartas sem reposição) — contagem exata e simulação Monte Carlo para validação.

```python
import numpy as np
import pandas as pd
from itertools import product, combinations
import random

# Exemplo 1: moeda duas vezes
faces = ['H', 'T']
omega_moeda = [''.join(p) for p in product(faces, repeat=2)]
df_moeda = pd.DataFrame({'outcome': omega_moeda})
df_moeda['at_least_one_H'] = df_moeda['outcome'].str.contains('H')

total_m = len(df_moeda)
count_A = df_moeda['at_least_one_H'].sum()
prob_A = count_A / total_m

print("Moeda (2 lançamentos)")
print(df_moeda)
print(f"Total outcomes: {total_m}")
print(f"|A| (>=1 H): {count_A} -> P(A) = {prob_A:.4f}\n")


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
count_B_and_C = df_dados[df_dados['is_sum_7'] & df_dados['first_is_even']].shape[0]

prob_B = count_B / total_d
prob_C = count_C / total_d
prob_B_and_C = count_B_and_C / total_d
prob_B_given_C = prob_B_and_C / prob_C if prob_C > 0 else np.nan

print("Dois dados")
print(df_dados.head(10))
print(f"Total outcomes: {total_d}")
print(f"|B| (sum=7): {count_B} -> P(B) = {prob_B:.4f}")
print(f"|C| (first even): {count_C} -> P(C) = {prob_C:.4f}")
print(f"|B ∩ C|: {count_B_and_C} -> P(B ∩ C) = {prob_B_and_C:.4f}")
print(f"P(B | C) = {prob_B_given_C:.4f}\n")


# Exemplo 3: baralho - combinações de 2 cartas (sem reposição)
suits = ['S', 'H', 'D', 'C']  # usando letras para representar naipes
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{r}{s}" for s in suits for r in ranks]  # 52 cartas

omega_cards = list(combinations(deck, 2))  # 1326 pares unordered
df_cards = pd.DataFrame(omega_cards, columns=['c1', 'c2'])

def suit(card):
    return card[-1]  # último caractere representa o naipe aqui

df_cards['both_hearts'] = df_cards.apply(lambda r: (suit(r['c1']) == 'H') and (suit(r['c2']) == 'H'), axis=1)
count_both_hearts = df_cards['both_hearts'].sum()
prob_both_hearts = count_both_hearts / len(df_cards)

print("Baralho (2 cartas sem reposição)")
print(f"|Ω| = {len(df_cards)}")
print(f"|both_hearts| = {count_both_hearts} -> P = {prob_both_hearts:.4f}")

# Simulação Monte Carlo (validação)
def simulate_two_card_draws(n_sim=50000, seed=42):
    rng = random.Random(seed)
    cnt = 0
    for _ in range(n_sim):
        a, b = rng.sample(deck, 2)
        if suit(a) == 'H' and suit(b) == 'H':
            cnt += 1
    return cnt / n_sim

sim_prob = simulate_two_card_draws(50000)
print(f"Simulação Monte Carlo (50k) P(both hearts) ≈ {sim_prob:.4f}")
```

* saídas esperadas (resumidas)

  * moeda: `P(at least one H) = 0.75`.
  * dados: `P(soma = 7) ≈ 0.1667`, `P(primeiro par) = 0.5`, `P(soma=7 | primeiro par) ≈ 0.3333`.
  * baralho: `P(duas copas) = C(13,2)/C(52,2) ≈ 0.0588`; simulação deve convergir para valor similar.

## Observações práticas

* Identifique sempre Ω antes de definir eventos; em espaços equiprováveis calcule contagens e divida.
* Para espaços não equiprováveis atribua probabilidades individuais aos resultados e some sobre o evento.
* Para espaços muito grandes prefira argumentos analíticos ou simulação Monte Carlo.
* Verifique independência com `P(A ∩ B) ?= P(A) P(B)` antes de simplificar condicionais.
