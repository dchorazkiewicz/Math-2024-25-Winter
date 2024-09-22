<style>
h2 {
    color: brown;
}

h3 {
    color: tomato;
}

</style>

# Granice ciągów liczbowych i funkcji

## Wprowadzenie

Granice ciągów i funkcji są fundamentalnym pojęciem w analizie matematycznej, które pozwala na opisanie zachowania funkcji i ciągów w miarę zbliżania się do określonego punktu lub do nieskończoności. Granice pomagają formalizować intuicje dotyczące procesów zbieżnych i rozbieżnych oraz są kluczowe w rachunku różniczkowym i całkowym.

## Nieskończony ciąg liczbowy

**Nieskończony ciąg liczbowy** to ciąg $\{a_n\}$, którego elementy są uporządkowanymi liczbami rzeczywistymi lub zespolonymi. Ciąg może dążyć do określonej wartości, rosnąć, maleć, lub oscylować.

### Przykład:

Ciąg $\{a_n\}$, gdzie $a_n = \frac{1}{n}$, ma elementy $\frac{1}{1}, \frac{1}{2}, \frac{1}{3}, \ldots$. Jak $n \to \infty$, wartości $a_n$ maleją do zera.

## Granica ciągu liczbowego

Granica ciągu liczbowego to wartość, do której dążą elementy ciągu, gdy indeks ciągu dąży do nieskończoności.

### Definicja:
Ciąg $\{a_n\}$ ma granicę $L$ (ozn. $\lim_{n \to \infty} a_n = L$), jeśli dla każdego $\epsilon > 0$ istnieje taka liczba naturalna $N$, że dla każdego $n > N$ zachodzi $|a_n - L| < \epsilon$.

### Przykład:

Dla ciągu $a_n = \frac{1}{n}$:
$$
\lim_{n \to \infty} \frac{1}{n} = 0
$$
Ponieważ dla dowolnie małego $\epsilon > 0$, można znaleźć $N$ takie, że dla wszystkich $n > N$ spełniona jest nierówność $\left|\frac{1}{n} - 0\right| < \epsilon$.

## Ciągi nieskończenie małe i nieskończenie duże

- **Ciąg nieskończenie mały**: Ciąg $\{a_n\}$ jest nieskończenie mały, gdy $\lim_{n \to \infty} a_n = 0$.
  
  **Przykład**: $\frac{1}{n}$.

- **Ciąg nieskończenie duży**: Ciąg $\{a_n\}$ jest nieskończenie duży, gdy $\lim_{n \to \infty} a_n = \infty$ lub $\lim_{n \to \infty} a_n = -\infty$.

  **Przykład**: $n^2$.

## Granica funkcji

Granica funkcji $f(x)$ w punkcie $x_0$ opisuje, do jakiej wartości zbliża się funkcja, gdy argument $x$ dąży do $x_0$.

### Definicja:
Funkcja $f(x)$ ma granicę $L$ w punkcie $x_0$ (ozn. $\lim_{x \to x_0} f(x) = L$), jeśli dla każdego $\epsilon > 0$ istnieje takie $\delta > 0$, że dla każdego $x$ spełniającego $0 < |x - x_0| < \delta$, zachodzi $|f(x) - L| < \epsilon$.

### Przykład:

Dla funkcji $f(x) = \frac{x^2 - 1}{x - 1}$, $\lim_{x \to 1} f(x) = 2$.

## Twierdzenie o jednoznaczności granicy

Granica ciągu lub funkcji jest jednoznaczna, czyli jeśli granica istnieje, to jest jedyna. Oznacza to, że ciąg lub funkcja nie mogą mieć dwóch różnych granic.

## Metody obliczania granic funkcji

1. **Podstawienie**: Wartość $x_0$ podstawiamy do funkcji $f(x)$.
   
   **Przykład**: $\lim_{x \to 3} (2x + 1) = 7$.

2. **Rozkład na czynniki**: Wykorzystujemy faktoryzację i upraszczamy wyrażenia.

   **Przykład**: $\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x - 1)(x + 1)}{x - 1} = 2$.

3. **L'Hôpital's Rule**: Stosowanie do nieokreśloności typu $\frac{0}{0}$ lub $\frac{\infty}{\infty}$.

   **Przykład**: $\lim_{x \to 0} \frac{\sin x}{x} = 1$.

## Twierdzenie o granicach

1. **Granica sumy**: $\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$.
2. **Granica iloczynu**: $\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$.
3. **Granica ilorazu**: $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$, jeśli $\lim_{x \to a} g(x) \neq 0$.

## Rodzaje niepewności

1. **$\frac{0}{0}$**: Niezdefiniowana forma, wymaga upraszczania wyrażenia.
2. **$\frac{\infty}{\infty}$**: Również niezdefiniowana, można zastosować L'Hôpital's Rule.
3. **$\infty - \infty$**: Wymaga sprowadzenia do określonej formy.
4. **$0 \times \infty$**: Zastosowanie przekształceń do formy $\frac{0}{0}$ lub $\frac{\infty}{\infty}$.

## Metody ujawniania niepewności

1. **Faktoryzacja**: Rozkład na czynniki w celu uproszczenia wyrażenia.
2. **Podstawienie**: Podstawianie zmiennej w formie ułamka lub funkcji zbliżającej się do wartości.
3. **L'Hôpital's Rule**: Obliczanie granicy przez różniczkowanie licznika i mianownika.

## Pierwsza i druga ważna granica

1. **Pierwsza granica**: $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
2. **Druga granica**: $\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$.

## Porównywanie wartości nieskończenie małych

Porównywanie wartości nieskończenie małych jest kluczowe w analizie zachowania funkcji blisko punktu. Nieskończenie małe można sklasyfikować jako "mniejsze" lub "większe" w zależności od ich szybkości zbieżności do zera.

### Przykład:

Dla dwóch ciągów $a_n = \frac{1}{n}$ i $b_n = \frac{1}{n^2}$, możemy powiedzieć, że $b_n$ jest "mniejszym" ciągiem, ponieważ zbiega do zera szybciej niż $a_n$.

## Zadania

**Zadanie 1:** Oblicz granicę $\lim_{x \to 0} \frac{\sin 2x}{x}$.

**Rozwiązanie:**

Zastosowanie pierwszej ważnej granicy $\lim_{x \to 0} \frac{\sin x}{x} = 1$:

$$
\lim_{x \to 0} \frac{\sin 2x}{x} = \lim_{x \to 0} 2 \cdot \frac{\sin 2x}{2x} = 2
$$

**Zadanie 2:** Znajdź granicę $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$.

**Rozwiązanie:**

Zastosowanie drugiej ważnej granicy:

$$
\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}
$$

**Zadanie 3:** Oblicz $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.

**Rozwiązanie:**

Uproszczenie wyrażenia poprzez faktoryzację:

$$
\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x - 1)(x + 1)}{x - 1} = \lim_{x \to 1} (x + 1) = 2
$$
