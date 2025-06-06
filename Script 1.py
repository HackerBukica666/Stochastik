import math
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def print_as_fraction(decimal):
    """Zeigt eine Dezimalzahl als Bruch an"""
    fraction = Fraction(decimal).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}"


def calculate_probability(favorable, possible):
    """Berechnet Wahrscheinlichkeit nach Grundformel P = günstige Fälle / mögliche Fälle"""
    print(f"\n🔢 LÖSUNGSWEG - Grundformel der Wahrscheinlichkeit:")
    print(f"Formel: P = günstige Fälle / mögliche Fälle")
    print(f"Gegeben: günstige Fälle = {favorable}, mögliche Fälle = {possible}")
    print(f"Einsetzen: P = {favorable} / {possible}")

    probability = favorable / possible
    print(f"Ergebnis: P = {probability}")
    return probability


def print_probability(p, as_percent=True, as_fraction=True):
    """Druckt eine Wahrscheinlichkeit in verschiedenen Formaten aus"""
    print(f"\n📊 ENDERGEBNIS:")
    if as_percent:
        print(f"P = {p:.6f} = {p * 100:.2f}%")
    if as_fraction:
        print(f"P = {print_as_fraction(p)}")
    return p


def sum_rule(p_list):
    """Additionsregel: Berechnet P(A oder B) = P(A) + P(B) für unvereinbare Ereignisse"""
    print(f"\n🔢 LÖSUNGSWEG - Summenregel (ODER-Verknüpfung):")
    print(f"Formel: P(A ∪ B) = P(A) + P(B) + ... (für unvereinbare Ereignisse)")
    print(f"Gegeben: Wahrscheinlichkeiten = {p_list}")
    print(f"Berechnung: P = {' + '.join(map(str, p_list))}")

    result = sum(p_list)
    print(f"Ergebnis: P = {result}")
    return result


def product_rule(p_list):
    """Multiplikationsregel: Berechnet P(A und B) = P(A) * P(B) für unabhängige Ereignisse"""
    print(f"\n🔢 LÖSUNGSWEG - Produktregel (UND-Verknüpfung):")
    print(f"Formel: P(A ∩ B) = P(A) × P(B) × ... (für unabhängige Ereignisse)")
    print(f"Gegeben: Wahrscheinlichkeiten = {p_list}")
    print(f"Berechnung: P = {' × '.join(map(str, p_list))}")

    result = 1
    for p in p_list:
        result *= p
    print(f"Ergebnis: P = {result}")
    return result


def factorial(n):
    """Berechnet die Fakultät n!"""
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)


def binomial_coefficient(n, k):
    """Berechnet den Binomialkoeffizienten (n über k)"""
    return math.comb(n, k)


def print_binomial_coefficient(n, k):
    """Druckt einen Binomialkoeffizienten aus"""
    print(f"\n🔢 LÖSUNGSWEG - Binomialkoeffizient:")
    print(f"Formel: (n über k) = n! / (k! × (n-k)!)")
    print(f"Gegeben: n = {n}, k = {k}")
    print(f"Berechnung: ({n} über {k}) = {n}! / ({k}! × {n - k}!)")
    print(f"= {factorial(n)} / ({factorial(k)} × {factorial(n - k)})")
    print(f"= {factorial(n)} / {factorial(k) * factorial(n - k)}")

    result = binomial_coefficient(n, k)
    print(f"Ergebnis: ({n} über {k}) = {result}")
    return result


def pascal_triangle(n):
    """Erzeugt das Pascal'sche Dreieck bis zur Zeile n (0-basiert)"""
    triangle = []
    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            row.append(binomial_coefficient(i, j))
        triangle.append(row)
    return triangle


def print_pascal_triangle(n):
    """Druckt das Pascal'sche Dreieck bis zur Zeile n (0-basiert)"""
    print(f"\n🔢 LÖSUNGSWEG - Pascal'sches Dreieck:")
    print(f"Das Pascal'sche Dreieck wird durch Binomialkoeffizienten gebildet.")
    print(f"Jede Zahl ist die Summe der beiden Zahlen darüber.")
    print(f"Zeile i, Position j: (i über j)")
    print(f"\nPascal'sches Dreieck bis Zeile {n}:")

    triangle = pascal_triangle(n)
    for i, row in enumerate(triangle):
        spaces = " " * (n - i) * 2
        formatted_row = spaces + "   ".join(str(val) for val in row)
        print(formatted_row)
    return triangle


def plot_pascal_triangle(n):
    """Zeichnet das Pascal'sche Dreieck bis zur Zeile n"""
    triangle = pascal_triangle(n)
    fig, ax = plt.subplots(figsize=(12, 8))

    for i, row in enumerate(triangle):
        x_positions = [j - i / 2 for j in range(len(row))]
        ax.scatter(x_positions, [-i] * len(row), s=100)

        for j, val in enumerate(row):
            ax.text(x_positions[j], -i, str(val), ha='center', va='center')

    ax.axis('equal')
    ax.axis('off')
    plt.title("Pascal's Triangle")
    plt.tight_layout()
    plt.show()


def bernoulli_probability(n, k, p):
    """Berechnet die Wahrscheinlichkeit nach der Bernoulli-Formel"""
    print(f"\n🔢 LÖSUNGSWEG - Bernoulli-Wahrscheinlichkeit:")
    print(f"Formel: P(X=k) = (n über k) × p^k × (1-p)^(n-k)")
    print(f"Gegeben: n = {n} (Versuche), k = {k} (Erfolge), p = {p} (Erfolgswahrscheinlichkeit)")

    q = 1 - p
    coefficient = binomial_coefficient(n, k)

    print(f"Schritt 1: Binomialkoeffizient berechnen")
    print(f"({n} über {k}) = {coefficient}")
    print(f"Schritt 2: Wahrscheinlichkeiten berechnen")
    print(f"p^k = {p}^{k} = {p ** k}")
    print(f"(1-p)^(n-k) = {q}^{n - k} = {q ** (n - k)}")
    print(f"Schritt 3: Alles multiplizieren")
    print(f"P(X={k}) = {coefficient} × {p ** k} × {q ** (n - k)}")

    result = coefficient * (p ** k) * (q ** (n - k))
    print(f"Ergebnis: P(X={k}) = {result}")
    return result


def cumulative_binomial_probability(n, k, p, greater_than=False):
    """Berechnet die kumulative Binomialwahrscheinlichkeit"""
    print(f"\n🔢 LÖSUNGSWEG - Kumulative Binomialwahrscheinlichkeit:")

    if greater_than:
        print(f"Formel: P(X ≥ {k}) = Σ(i={k} bis {n}) P(X=i)")
        print(f"Berechnung: P(X ≥ {k}) = P(X={k}) + P(X={k + 1}) + ... + P(X={n})")
        result = sum(bernoulli_probability(n, i, p) for i in range(k, n + 1))
        print(f"Ergebnis: P(X ≥ {k}) = {result}")
    else:
        print(f"Formel: P(X ≤ {k}) = Σ(i=0 bis {k}) P(X=i)")
        print(f"Berechnung: P(X ≤ {k}) = P(X=0) + P(X=1) + ... + P(X={k})")
        result = sum(bernoulli_probability(n, i, p) for i in range(0, k + 1))
        print(f"Ergebnis: P(X ≤ {k}) = {result}")

    return result


def plot_binomial_distribution(n, p):
    """Zeichnet die Binomialverteilung für n Versuche mit Erfolgswahrscheinlichkeit p"""
    print(f"\n📊 Erstelle Grafik für Binomialverteilung B({n},{p})")

    x = list(range(n + 1))
    y = [bernoulli_probability(n, k, p) for k in x]

    plt.figure(figsize=(12, 6))
    plt.bar(x, y, width=0.8)
    plt.xlabel('Anzahl der Erfolge (k)')
    plt.ylabel('Wahrscheinlichkeit P(X=k)')
    plt.title(f'Binomialverteilung B({n},{p})')
    plt.grid(True, alpha=0.3)
    plt.xticks(x)
    plt.show()


def combination_without_repetition(n, k):
    """Berechnet die Anzahl der Kombinationen ohne Wiederholung (n über k)"""
    print(f"\n🔢 LÖSUNGSWEG - Kombination ohne Wiederholung:")
    print(f"Formel: C(n,k) = (n über k) = n! / (k! × (n-k)!)")
    print(f"Anwendung: Auswahl von k Objekten aus n Objekten, Reihenfolge unwichtig")
    return binomial_coefficient(n, k)


def combination_with_repetition(n, k):
    """Berechnet die Anzahl der Kombinationen mit Wiederholung (n+k-1 über k)"""
    print(f"\n🔢 LÖSUNGSWEG - Kombination mit Wiederholung:")
    print(f"Formel: C(n+k-1,k) = ((n+k-1) über k)")
    print(f"Anwendung: Auswahl von k Objekten aus n Objekten mit Wiederholung")
    print(f"Berechnung: C({n}+{k}-1,{k}) = C({n + k - 1},{k})")
    return binomial_coefficient(n + k - 1, k)


def variation_without_repetition(n, k):
    """Berechnet die Anzahl der Variationen ohne Wiederholung: n! / (n-k)!"""
    print(f"\n🔢 LÖSUNGSWEG - Variation ohne Wiederholung:")
    print(f"Formel: V(n,k) = n! / (n-k)!")
    print(f"Anwendung: Anordnung von k Objekten aus n Objekten, Reihenfolge wichtig")
    print(f"Berechnung: V({n},{k}) = {n}! / {n - k}! = {factorial(n)} / {factorial(n - k)}")

    result = factorial(n) // factorial(n - k)
    print(f"Ergebnis: {result}")
    return result


def variation_with_repetition(n, k):
    """Berechnet die Anzahl der Variationen mit Wiederholung: n^k"""
    print(f"\n🔢 LÖSUNGSWEG - Variation mit Wiederholung:")
    print(f"Formel: V(n,k) = n^k")
    print(f"Anwendung: Anordnung von k Objekten aus n Objekten mit Wiederholung")
    print(f"Berechnung: V({n},{k}) = {n}^{k}")

    result = n ** k
    print(f"Ergebnis: {result}")
    return result


def permutation_without_repetition(n):
    """Berechnet die Anzahl der Permutationen ohne Wiederholung: n!"""
    print(f"\n🔢 LÖSUNGSWEG - Permutation ohne Wiederholung:")
    print(f"Formel: P(n) = n!")
    print(f"Anwendung: Anordnung aller n Objekte")
    print(f"Berechnung: P({n}) = {n}!")

    result = factorial(n)
    print(f"Ergebnis: {result}")
    return result


def permutation_with_repetition(n, repetitions):
    """Berechnet die Anzahl der Permutationen mit Wiederholung"""
    print(f"\n🔢 LÖSUNGSWEG - Permutation mit Wiederholung:")
    print(f"Formel: P(n; n₁,n₂,...) = n! / (n₁! × n₂! × ... × nₖ!)")
    print(f"Anwendung: Anordnung von n Objekten mit Wiederholungen")
    print(f"Gegeben: n = {n}, Wiederholungen = {repetitions}")

    denominator = 1
    denom_str = []
    for rep in repetitions:
        denominator *= factorial(rep)
        denom_str.append(f"{rep}!")

    print(f"Berechnung: P = {n}! / ({' × '.join(denom_str)})")
    print(f"= {factorial(n)} / {denominator}")

    result = factorial(n) // denominator
    print(f"Ergebnis: {result}")
    return result


def tree_diagram_path_probability(path_probabilities):
    """Berechnet die Wahrscheinlichkeit eines Pfades im Baumdiagramm"""
    print(f"\n🔢 LÖSUNGSWEG - Pfadwahrscheinlichkeit im Baumdiagramm:")
    print(f"Regel: Wahrscheinlichkeiten entlang eines Pfades werden multipliziert")
    print(f"Gegeben: Pfadwahrscheinlichkeiten = {path_probabilities}")
    print(f"Berechnung: P(Pfad) = {' × '.join(map(str, path_probabilities))}")

    result = product_rule(path_probabilities)
    return result


def tree_diagram_total_probability(paths):
    """Berechnet die Gesamtwahrscheinlichkeit mehrerer Pfade im Baumdiagramm"""
    print(f"\n🔢 LÖSUNGSWEG - Gesamtwahrscheinlichkeit mehrerer Pfade:")
    print(f"Regel: Wahrscheinlichkeiten verschiedener Pfade werden addiert")

    path_probabilities = [tree_diagram_path_probability(path) for path in paths]
    return sum_rule(path_probabilities)


def solve_urne_with_replacement(total_balls, colors, num_draws, target_counts):
    """Löst Urnen-Problem mit Zurücklegen"""
    print(f"\n🔢 LÖSUNGSWEG - Urnen-Problem MIT Zurücklegen:")
    print(f"Bei jedem Zug bleibt die Wahrscheinlichkeit gleich")
    print(f"Gegeben:")
    print(f"  - Gesamtanzahl Kugeln: {total_balls}")
    print(f"  - Farben und Anzahlen: {colors}")
    print(f"  - Anzahl Ziehungen: {num_draws}")
    print(f"  - Gewünschte Ziehungen: {target_counts}")

    probability = 1
    calculation_steps = []

    for color, count in target_counts.items():
        p_single = colors[color] / total_balls
        p_multiple = p_single ** count
        probability *= p_multiple
        calculation_steps.append(f"P({color}) = ({colors[color]}/{total_balls})^{count} = {p_multiple}")

    print(f"Berechnung:")
    for step in calculation_steps:
        print(f"  {step}")
    print(
        f"Gesamtwahrscheinlichkeit = {' × '.join([f'({colors[color]}/{total_balls})^{count}' for color, count in target_counts.items()])}")
    print(f"Ergebnis: P = {probability:.6f}")
    return probability


def solve_urne_without_replacement(total_balls, colors, num_draws, target_counts):
    """Löst Urnen-Problem ohne Zurücklegen"""
    print(f"\n🔢 LÖSUNGSWEG - Urnen-Problem OHNE Zurücklegen:")
    print(f"Hypergeometrische Verteilung")
    print(f"Formel: P = (Π(Kᵢ über kᵢ)) / (N über n)")
    print(f"Gegeben:")
    print(f"  - Gesamtanzahl Kugeln (N): {total_balls}")
    print(f"  - Farben und Anzahlen: {colors}")
    print(f"  - Anzahl Ziehungen (n): {num_draws}")
    print(f"  - Gewünschte Ziehungen: {target_counts}")

    numerator = 1
    numerator_parts = []
    for color, count in target_counts.items():
        part = math.comb(colors[color], count)
        numerator *= part
        numerator_parts.append(f"({colors[color]} über {count}) = {part}")

    denominator = math.comb(total_balls, num_draws)

    print(f"Berechnung:")
    print(f"Zähler = {' × '.join(numerator_parts)} = {numerator}")
    print(f"Nenner = ({total_balls} über {num_draws}) = {denominator}")
    print(f"P = {numerator} / {denominator}")

    probability = numerator / denominator
    print(f"Ergebnis: P = {probability:.6f}")
    return probability


def binomische_formel(a, b, formel_nummer):
    """Berechnet eine der binomischen Formeln mit Lösungsweg"""
    print(f"\n🔢 LÖSUNGSWEG - Binomische Formel:")

    if formel_nummer == 1:
        print(f"1. Binomische Formel: (a + b)² = a² + 2ab + b²")
        print(f"Gegeben: a = {a}, b = {b}")
        print(f"Einsetzen: ({a} + {b})² = {a}² + 2×{a}×{b} + {b}²")
        print(f"Berechnung: = {a ** 2} + {2 * a * b} + {b ** 2}")
        result = (a + b) ** 2
        print(f"Ergebnis: {result}")
    elif formel_nummer == 2:
        print(f"2. Binomische Formel: (a - b)² = a² - 2ab + b²")
        print(f"Gegeben: a = {a}, b = {b}")
        print(f"Einsetzen: ({a} - {b})² = {a}² - 2×{a}×{b} + {b}²")
        print(f"Berechnung: = {a ** 2} - {2 * a * b} + {b ** 2}")
        result = (a - b) ** 2
        print(f"Ergebnis: {result}")
    elif formel_nummer == 3:
        print(f"3. Binomische Formel: (a + b)(a - b) = a² - b²")
        print(f"Gegeben: a = {a}, b = {b}")
        print(f"Einsetzen: ({a} + {b})×({a} - {b}) = {a}² - {b}²")
        print(f"Berechnung: = {a ** 2} - {b ** 2}")
        result = (a + b) * (a - b)
        print(f"Ergebnis: {result}")
    else:
        print("Ungültige Formelnummer (1, 2 oder 3).")
        return None
    return result


# Menüfunktionen für interaktive Nutzung
def menu_probability():
    print("\n--- Grundformel der Wahrscheinlichkeit ---")
    favorable = int(input("Anzahl günstiger Fälle: "))
    possible = int(input("Anzahl möglicher Fälle: "))
    p = calculate_probability(favorable, possible)
    print_probability(p)


def menu_sum_rule():
    print("\n--- Summenregel (ODER-Verknüpfung) ---")
    num = int(input("Anzahl der Wahrscheinlichkeiten: "))
    probabilities = []
    for i in range(num):
        p = float(input(f"Wahrscheinlichkeit {i + 1}: "))
        probabilities.append(p)
    result = sum_rule(probabilities)
    print_probability(result)


def menu_product_rule():
    print("\n--- Produktregel (UND-Verknüpfung) ---")
    num = int(input("Anzahl der Wahrscheinlichkeiten: "))
    probabilities = []
    for i in range(num):
        p = float(input(f"Wahrscheinlichkeit {i + 1}: "))
        probabilities.append(p)
    result = product_rule(probabilities)
    print_probability(result)


def menu_binomial_coefficient():
    print("\n--- Binomialkoeffizient ---")
    n = int(input("n: "))
    k = int(input("k: "))
    result = print_binomial_coefficient(n, k)
    return result


def menu_pascal_triangle():
    print("\n--- Pascal'sches Dreieck ---")
    n = int(input("Anzahl der Zeilen (0-basiert): "))
    print_pascal_triangle(n)


def menu_bernoulli():
    print("\n--- Bernoulli-Wahrscheinlichkeit ---")
    n = int(input("Anzahl der Versuche (n): "))
    k = int(input("Anzahl der Erfolge (k): "))
    p = float(input("Wahrscheinlichkeit für Erfolg (p): "))
    result = bernoulli_probability(n, k, p)
    print_probability(result)


def menu_cumulative_binomial():
    print("\n--- Kumulative Binomialwahrscheinlichkeit ---")
    n = int(input("Anzahl der Versuche (n): "))
    k = int(input("Anzahl der Erfolge (k): "))
    p = float(input("Wahrscheinlichkeit für Erfolg (p): "))
    choice = input("Berechnen für: (1) P(X <= k)  (2) P(X >= k): ")
    greater_than = (choice == "2")
    result = cumulative_binomial_probability(n, k, p, greater_than)
    print_probability(result)


def menu_plot_binomial():
    print("\n--- Binomialverteilung grafisch darstellen ---")
    n = int(input("Anzahl der Versuche (n): "))
    p = float(input("Wahrscheinlichkeit für Erfolg (p): "))
    plot_binomial_distribution(n, p)


def menu_urne_problem():
    print("\n--- Urnen-Problem (Ziehen von Kugeln) ---")
    colors = {}
    num_colors = int(input("Anzahl der Kugelfarben: "))
    for i in range(num_colors):
        color_name = input(f"Name der Farbe {i + 1}: ")
        color_count = int(input(f"Anzahl der {color_name}-farbigen Kugeln: "))
        colors[color_name] = color_count
    total_balls = sum(colors.values())
    num_draws = int(input("Anzahl der Ziehungen: "))
    target_counts = {}
    for color in colors:
        target_counts[color] = int(input(f"Gewünschte Anzahl an {color}-Kugeln: "))
    replacement = input("Mit Zurücklegen? (j/n): ").lower() in ['j', 'ja', 'yes', 'y']

    if replacement:
        solve_urne_with_replacement(total_balls, colors, num_draws, target_counts)
    else:
        solve_urne_without_replacement(total_balls, colors, num_draws, target_counts)


def menu_combinatorics():
    print("\n--- Kombinatorik ---")
    print("1: Kombination ohne Wiederholung (n über k)")
    print("2: Kombination mit Wiederholung (n+k-1 über k)")
    print("3: Variation ohne Wiederholung (n! / (n-k)!)")
    print("4: Variation mit Wiederholung (n^k)")
    print("5: Permutation ohne Wiederholung (n!)")
    print("6: Permutation mit Wiederholung (n! / (a!b!c!...))")

    choice = int(input("Wähle eine Option: "))

    if choice in [1, 2, 3, 4]:
        n = int(input("n: "))
        k = int(input("k: "))

        if choice == 1:
            result = combination_without_repetition(n, k)
            print(f"Ergebnis: {result}")
        elif choice == 2:
            result = combination_with_repetition(n, k)
            print(f"Ergebnis: {result}")
        elif choice == 3:
            result = variation_without_repetition(n, k)
        elif choice == 4:
            result = variation_with_repetition(n, k)

    elif choice == 5:
        n = int(input("n: "))
        result = permutation_without_repetition(n)

    elif choice == 6:
        n = int(input("Gesamtanzahl der Elemente (n): "))
        num_groups = int(input("Anzahl der Gruppen mit Wiederholungen: "))
        repetitions = []
        for i in range(num_groups):
            rep = int(input(f"Anzahl der Wiederholungen in Gruppe {i + 1}: "))
            repetitions.append(rep)

        if sum(repetitions) != n:
            print(f"Fehler: Die Summe der Wiederholungen ({sum(repetitions)}) muss gleich n ({n}) sein.")
        else:
            result = permutation_with_repetition(n, repetitions)


def menu_binomische_formeln():
    print("\n--- Binomische Formeln ---")
    print("1: (a + b)² = a² + 2ab + b²")
    print("2: (a - b)² = a² - 2ab + b²")
    print("3: (a + b)(a - b) = a² - b²")
    formel = int(input("Wähle eine Formel (1–3): "))
    a = float(input("a: "))
    b = float(input("b: "))
    binomische_formel(a, b, formel)


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("🎯 STOCHASTIK-RECHNER MIT LÖSUNGSWEG")
        print("=" * 50)
        print("1: Grundformel der Wahrscheinlichkeit")
        print("2: Summenregel (ODER-Verknüpfung)")
        print("3: Produktregel (UND-Verknüpfung)")
        print("4: Binomialkoeffizient")
        print("5: Pascal'sches Dreieck")
        print("6: Bernoulli-Wahrscheinlichkeit")
        print("7: Kumulative Binomialwahrscheinlichkeit")
        print("8: Binomialverteilung grafisch darstellen")
        print("9: Urnen-Problem (Ziehen von Kugeln)")
        print("10: Kombinatorik")
        print("11: Binomische Formeln")
        print("0: Beenden")
        print("=" * 50)

        choice = input("Wähle eine Option: ")

        if choice == "1":
            menu_probability()
        elif choice == "2":
            menu_sum_rule()
        elif choice == "3":
            menu_product_rule()
        elif choice == "4":
            menu_binomial_coefficient()
        elif choice == "5":
            menu_pascal_triangle()
        elif choice == "6":
            menu_bernoulli()
        elif choice == "7":
            menu_cumulative_binomial()
        elif choice == "8":
            menu_plot_binomial()
        elif choice == "9":
            menu_urne_problem()
        elif choice == "10":
            menu_combinatorics()
        elif choice == "11":
            menu_binomische_formeln()
        elif choice == "0":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")


# Beispiele für direkte Verwendung (ohne Menü)
def examples():
    print("\n" + "=" * 60)
    print("📚 BEISPIELE MIT LÖSUNGSWEG")
    print("=" * 60)

    # Beispiel für Grundformel der Wahrscheinlichkeit
    print("\n🎲 Beispiel: Wahrscheinlichkeit für gerade Zahl beim Würfeln")
    p = calculate_probability(3, 6)  # 3 gerade Zahlen (2,4,6) von 6 möglichen
    print_probability(p)

    # Beispiel für Binomialkoeffizient
    print("\n🔢 Beispiel: Binomialkoeffizient")
    result = print_binomial_coefficient(7, 3)

    # Beispiel für Pascal'sches Dreieck
    print("\n🔺 Beispiel: Pascal'sches Dreieck")
    print_pascal_triangle(5)

    # Beispiel für Bernoulli-Wahrscheinlichkeit
    print("\n🎯 Beispiel: 10 Würfe, genau 4 Sechsen")
    p = bernoulli_probability(10, 4, 1 / 6)
    print_probability(p)

    # Beispiel für Urnen-Problem mit Zurücklegen
    print("\n🏺 Beispiel: Urnen-Problem mit Zurücklegen")
    solve_urne_with_replacement(10, {"rot": 4, "blau": 3, "grün": 3}, 2, {"rot": 1, "blau": 1})

    # Beispiel für Urnen-Problem ohne Zurücklegen
    print("\n🏺 Beispiel: Urnen-Problem ohne Zurücklegen")
    solve_urne_without_replacement(10, {"rot": 4, "blau": 3, "grün": 3}, 2, {"rot": 1, "blau": 1})


# Weitere Hilfsfunktionen
def generate_tree_diagram_probabilities(n, p_success, with_replacement=True):
    """Generiert alle Pfad-Wahrscheinlichkeiten für ein Baumdiagramm"""

    def generate_paths(depth, current_path, current_prob, paths_dict):
        if depth == n:
            paths_dict[tuple(current_path)] = current_prob
            return

        if not with_replacement and depth > 0:
            success_count = current_path.count(True)
            fail_count = current_path.count(False)

            total = n - 1
            remaining_success = n - success_count
            remaining_fail = n - fail_count

            if remaining_success > 0:
                p_success_next = remaining_success / (n - depth)
            else:
                p_success_next = 0
        else:
            p_success_next = p_success

        p_fail_next = 1 - p_success_next

        generate_paths(depth + 1, current_path + [True], current_prob * p_success_next, paths_dict)
        generate_paths(depth + 1, current_path + [False], current_prob * p_fail_next, paths_dict)

    all_paths = {}
    generate_paths(0, [], 1, all_paths)
    return all_paths


# Starte das Menü
if __name__ == "__main__":
    print("🎓 Willkommen beim erweiterten Stochastik-Rechner!")
    print("Dieses Programm zeigt dir nicht nur die Ergebnisse, sondern auch den kompletten Lösungsweg.")

    choice = input("\nMöchtest du einige Beispiele mit Lösungsweg sehen? (j/n): ")
    if choice.lower() in ['j', 'ja', 'yes', 'y']:
        examples()

    main_menu()