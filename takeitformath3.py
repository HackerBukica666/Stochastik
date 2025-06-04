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
    probability = favorable / possible
    return probability

def print_probability(p, as_percent=True, as_fraction=True):
    """Druckt eine Wahrscheinlichkeit in verschiedenen Formaten aus"""
    if as_percent:
        print(f"P = {p:.6f} = {p*100:.2f}%")
    if as_fraction:
        print(f"P = {print_as_fraction(p)}")
    return p

def sum_rule(p_list):
    """Additionsregel: Berechnet P(A oder B) = P(A) + P(B) für unvereinbare Ereignisse
    - Akzeptiert eine Liste von Wahrscheinlichkeiten"""
    return sum(p_list)

def product_rule(p_list):
    """Multiplikationsregel: Berechnet P(A und B) = P(A) * P(B) für unabhängige Ereignisse
    - Akzeptiert eine Liste von Wahrscheinlichkeiten"""
    result = 1
    for p in p_list:
        result *= p
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
    result = binomial_coefficient(n, k)
    print(f"({n} über {k}) = {result}")
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
        x_positions = [j - i/2 for j in range(len(row))]
        ax.scatter(x_positions, [-i] * len(row), s=100)
        
        for j, val in enumerate(row):
            ax.text(x_positions[j], -i, str(val), ha='center', va='center')
    
    ax.axis('equal')
    ax.axis('off')
    plt.title("Pascal's Triangle")
    plt.tight_layout()
    plt.show()

def bernoulli_probability(n, k, p):
    """Berechnet die Wahrscheinlichkeit nach der Bernoulli-Formel:
    P(X=k) = (n über k) * p^k * (1-p)^(n-k)
    
    Parameter:
    n - Anzahl der Versuche
    k - Anzahl der Erfolge
    p - Wahrscheinlichkeit für Erfolg in einem einzelnen Versuch
    """
    q = 1 - p
    coefficient = binomial_coefficient(n, k)
    return coefficient * (p ** k) * (q ** (n - k))

def cumulative_binomial_probability(n, k, p, greater_than=False):
    """Berechnet die kumulative Binomialwahrscheinlichkeit
    P(X <= k) oder P(X >= k)
    
    Parameter:
    n - Anzahl der Versuche
    k - Anzahl der Erfolge
    p - Wahrscheinlichkeit für Erfolg in einem einzelnen Versuch
    greater_than - wenn True, berechnet P(X >= k), sonst P(X <= k)
    """
    if greater_than:
        return sum(bernoulli_probability(n, i, p) for i in range(k, n + 1))
    else:
        return sum(bernoulli_probability(n, i, p) for i in range(0, k + 1))

def plot_binomial_distribution(n, p):
    """Zeichnet die Binomialverteilung für n Versuche mit Erfolgswahrscheinlichkeit p"""
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
    return binomial_coefficient(n, k)

def combination_with_repetition(n, k):
    """Berechnet die Anzahl der Kombinationen mit Wiederholung (n+k-1 über k)"""
    return binomial_coefficient(n + k - 1, k)

def variation_without_repetition(n, k):
    """Berechnet die Anzahl der Variationen ohne Wiederholung: n! / (n-k)!"""
    return factorial(n) // factorial(n - k)

def variation_with_repetition(n, k):
    """Berechnet die Anzahl der Variationen mit Wiederholung: n^k"""
    return n ** k

def permutation_without_repetition(n):
    """Berechnet die Anzahl der Permutationen ohne Wiederholung: n!"""
    return factorial(n)

def permutation_with_repetition(n, repetitions):
    """Berechnet die Anzahl der Permutationen mit Wiederholung:
    n! / (a! * b! * c! * ...)
    
    Parameter:
    n - Gesamtanzahl der Elemente
    repetitions - Liste mit der Anzahl der Wiederholungen jedes Elements
    """
    denominator = 1
    for rep in repetitions:
        denominator *= factorial(rep)
    return factorial(n) // denominator

def tree_diagram_path_probability(path_probabilities):
    """Berechnet die Wahrscheinlichkeit eines Pfades im Baumdiagramm
    durch Multiplikation der einzelnen Wahrscheinlichkeiten"""
    return product_rule(path_probabilities)

def tree_diagram_total_probability(paths):
    """Berechnet die Gesamtwahrscheinlichkeit mehrerer Pfade im Baumdiagramm
    durch Addition der einzelnen Pfadwahrscheinlichkeiten
    
    Parameter:
    paths - Liste von Listen mit Pfadwahrscheinlichkeiten
    """
    path_probabilities = [tree_diagram_path_probability(path) for path in paths]
    return sum_rule(path_probabilities)

def generate_tree_diagram_probabilities(n, p_success, with_replacement=True):
    """Generiert alle Pfad-Wahrscheinlichkeiten für ein Baumdiagramm
    mit n Ebenen und konstanter Erfolgswahrscheinlichkeit p
    
    Parameter:
    n - Anzahl der Ebenen/Versuche
    p_success - Wahrscheinlichkeit für Erfolg in einem einzelnen Versuch
    with_replacement - Bei True wird die Wahrscheinlichkeit bei jedem Versuch zurückgesetzt
    
    Rückgabe:
    Dictionary mit Pfaden als Schlüssel und Wahrscheinlichkeiten als Werte
    """
    def generate_paths(depth, current_path, current_prob, paths_dict):
        if depth == n:
            paths_dict[tuple(current_path)] = current_prob
            return
        
        # Anpassung der Wahrscheinlichkeiten für das nächste Level
        if not with_replacement and depth > 0:
            # Beispielimplementierung für eine einfache Anpassung
            # In realen Anwendungen muss dies entsprechend dem Problem angepasst werden
            success_count = current_path.count(True)
            fail_count = current_path.count(False)
            
            total = n - 1  # Anzahl bereits gezogener
            remaining_success = n - success_count
            remaining_fail = n - fail_count
            
            if remaining_success > 0:
                p_success_next = remaining_success / (n - depth)
            else:
                p_success_next = 0
        else:
            p_success_next = p_success
        
        p_fail_next = 1 - p_success_next
        
        # Rekursiver Aufruf für Erfolg und Misserfolg
        generate_paths(depth + 1, current_path + [True], current_prob * p_success_next, paths_dict)
        generate_paths(depth + 1, current_path + [False], current_prob * p_fail_next, paths_dict)
    
    all_paths = {}
    generate_paths(0, [], 1, all_paths)
    return all_paths

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
        p = float(input(f"Wahrscheinlichkeit {i+1}: "))
        probabilities.append(p)
    result = sum_rule(probabilities)
    print_probability(result)

def menu_product_rule():
    print("\n--- Produktregel (UND-Verknüpfung) ---")
    num = int(input("Anzahl der Wahrscheinlichkeiten: "))
    probabilities = []
    for i in range(num):
        p = float(input(f"Wahrscheinlichkeit {i+1}: "))
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


def solve_urne_with_replacement(total_balls, colors, num_draws, target_counts):
    probability = 1
    for color, count in target_counts.items():
        p = (colors[color] / total_balls) ** count
        probability *= p
    print(f"Wahrscheinlichkeit mit Zurücklegen: {probability:.6f}")


def solve_urne_without_replacement(total_balls, colors, num_draws, target_counts):
    numerator = 1
    for color, count in target_counts.items():
        numerator *= math.comb(colors[color], count)
    denominator = math.comb(total_balls, num_draws)
    probability = numerator / denominator
    print(f"Wahrscheinlichkeit ohne Zurücklegen: {probability:.6f}")

def binomische_formel(a, b, formel_nummer):
    """Berechnet eine der binomischen Formeln:
    1: (a + b)^2
    2: (a - b)^2
    3: (a + b)(a - b)
    """
    if formel_nummer == 1:
        result = (a + b) ** 2
        print(f"({a} + {b})² = {a}² + 2*{a}*{b} + {b}² = {a**2} + {2*a*b} + {b**2} = {result}")
    elif formel_nummer == 2:
        result = (a - b) ** 2
        print(f"({a} - {b})² = {a}² - 2*{a}*{b} + {b}² = {a**2} - {2*a*b} + {b**2} = {result}")
    elif formel_nummer == 3:
        result = (a + b) * (a - b)
        print(f"({a} + {b})*({a} - {b}) = {a}² - {b}² = {a**2} - {b**2} = {result}")
    else:
        print("Ungültige Formelnummer (1, 2 oder 3).")
        return None
    return result


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
            print(f"Kombination ohne Wiederholung: {result}")
        elif choice == 2:
            result = combination_with_repetition(n, k)
            print(f"Kombination mit Wiederholung: {result}")
        elif choice == 3:
            result = variation_without_repetition(n, k)
            print(f"Variation ohne Wiederholung: {result}")
        elif choice == 4:
            result = variation_with_repetition(n, k)
            print(f"Variation mit Wiederholung: {result}")
            
    elif choice == 5:
        n = int(input("n: "))
        result = permutation_without_repetition(n)
        print(f"Permutation ohne Wiederholung: {result}")
        
    elif choice == 6:
        n = int(input("Gesamtanzahl der Elemente (n): "))
        num_groups = int(input("Anzahl der Gruppen mit Wiederholungen: "))
        repetitions = []
        for i in range(num_groups):
            rep = int(input(f"Anzahl der Wiederholungen in Gruppe {i+1}: "))
            repetitions.append(rep)
        
        if sum(repetitions) != n:
            print(f"Fehler: Die Summe der Wiederholungen ({sum(repetitions)}) muss gleich n ({n}) sein.")
        else:
            result = permutation_with_repetition(n, repetitions)
            print(f"Permutation mit Wiederholung: {result}")


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
        print("\n===== Stochastik-Rechner =====")
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
    # Beispiel für Grundformel der Wahrscheinlichkeit
    print("\n--- Beispiel für Grundformel der Wahrscheinlichkeit ---")
    # Wahrscheinlichkeit, mit einem Würfel eine gerade Zahl zu werfen
    p = calculate_probability(3, 6)  # 3 gerade Zahlen (2,4,6) von 6 möglichen
    print_probability(p)
    
    # Beispiel für Binomialkoeffizient
    print("\n--- Beispiel für Binomialkoeffizient ---")
    result = print_binomial_coefficient(7, 3)
    
    # Beispiel für Pascal'sches Dreieck
    print("\n--- Beispiel für Pascal'sches Dreieck ---")
    print_pascal_triangle(5)
    
    # Beispiel für Bernoulli-Wahrscheinlichkeit
    print("\n--- Beispiel für Bernoulli-Wahrscheinlichkeit ---")
    # Wahrscheinlichkeit, bei 10 Würfen genau 4 Sechsen zu werfen
    p = bernoulli_probability(10, 4, 1/6)
    print_probability(p)
    
    # Beispiel für Urnen-Problem mit Zurücklegen
    print("\n--- Beispiel für Urnen-Problem mit Zurücklegen ---")
    solve_urne_with_replacement(10, {"rot": 4, "blau": 3, "grün": 3}, 2, {"rot": 1, "blau": 1})
    
    # Beispiel für Urnen-Problem ohne Zurücklegen
    print("\n--- Beispiel für Urnen-Problem ohne Zurücklegen ---")
    solve_urne_without_replacement(10, {"rot": 4, "blau": 3, "grün": 3}, 2, {"rot": 1, "blau": 1})

# Starte das Menü
if __name__ == "__main__":
    print("Willkommen beim Stochastik-Rechner!")
    print("Dieses Programm hilft dir, verschiedene Aufgaben aus der Stochastik zu lösen.")
    
    choice = input("Möchtest du einige Beispiele sehen? (j/n): ")
    if choice.lower() in ['j', 'ja', 'yes', 'y']:
        examples()
    
    main_menu()