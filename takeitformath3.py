import math
import random
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def grundformel_wahrscheinlichkeit(günstige_fälle, mögliche_fälle):
    if mögliche_fälle == 0:
        return "Fehler: Mögliche Fälle dürfen nicht 0 sein."
    wahrscheinlichkeit = günstige_fälle / mögliche_fälle
    return f"P = {günstige_fälle} / {mögliche_fälle} = {wahrscheinlichkeit:.4f}"

def gesetz_grosse_zahlen(wahrscheinlichkeit, versuche):
    ergebnisse = sum(random.random() < wahrscheinlichkeit for _ in range(versuche))
    return f"Relative Häufigkeit nach {versuche} Versuchen: {ergebnisse / versuche:.4f}"

def einfache_wahrscheinlichkeit(karten_deck, gewünschte_karten):
    return grundformel_wahrscheinlichkeit(gewünschte_karten, karten_deck)

def binomialverteilung(n, p, k):
    result = binom.pmf(k, n, p)
    return f"P(X = {k}) = {result:.4f}"

def galton_apparat(n, p=0.5):
    ergebnisse = [sum(random.choices([0, 1], weights=[1-p, p], k=n)) for _ in range(1000)]
    plt.hist(ergebnisse, bins=range(n+2), align='left', edgecolor='black')
    plt.xlabel("Anzahl Erfolge")
    plt.ylabel("Häufigkeit")
    plt.title("Galton’scher Zufallsapparat")
    plt.show()

def bernoulli_experiment(p, n):
    ergebnisse = [1 if random.random() < p else 0 for _ in range(n)]
    return f"Ergebnisse: {ergebnisse}, Anteil Erfolge: {sum(ergebnisse)/n:.4f}"

def kombinationen(n, k):
    return math.comb(n, k)

def permutation(n):
    return math.factorial(n)

def variation(n, k):
    return math.perm(n, k)

def baumdiagramm(prob_liste):
    fig, ax = plt.subplots()
    ax.set_title("Baumdiagramm")
    ax.plot([0, 1], [1, 2], 'ko-')
    for i, p in enumerate(prob_liste):
        ax.text(0.5, 1.5 + i*0.2, f"P = {p}")
    plt.show()

def main():
    print("Stochastik-Tool - Wähle eine Berechnung:")
    print("1. Grundformel Wahrscheinlichkeit")
    print("2. Gesetz der großen Zahlen")
    print("3. Einfache Wahrscheinlichkeit")
    print("4. Binomialverteilung")
    print("5. Galton’scher Zufallsapparat")
    print("6. Bernoulli-Experiment")
    print("7. Kombinationen")
    print("8. Permutationen")
    print("9. Variationen")
    print("10. Baumdiagramm")
    
    auswahl = int(input("Gib die Nummer ein: "))
    
    if auswahl == 1:
        g = int(input("Günstige Fälle: "))
        m = int(input("Mögliche Fälle: "))
        print(grundformel_wahrscheinlichkeit(g, m))
    elif auswahl == 2:
        p = float(input("Wahrscheinlichkeit p: "))
        n = int(input("Anzahl Versuche: "))
        print(gesetz_grosse_zahlen(p, n))
    elif auswahl == 3:
        deck = int(input("Anzahl Karten im Deck: "))
        wunsch = int(input("Anzahl gewünschter Karten: "))
        print(einfache_wahrscheinlichkeit(deck, wunsch))
    elif auswahl == 4:
        n = int(input("Anzahl Versuche: "))
        p = float(input("Erfolgswahrscheinlichkeit p: "))
        k = int(input("Erwartete Erfolge: "))
        print(binomialverteilung(n, p, k))
    elif auswahl == 5:
        n = int(input("Anzahl Stufen im Galton-Apparat: "))
        galton_apparat(n)
    elif auswahl == 6:
        p = float(input("Erfolgswahrscheinlichkeit p: "))
        n = int(input("Anzahl Versuche: "))
        print(bernoulli_experiment(p, n))
    elif auswahl == 7:
        n = int(input("n: "))
        k = int(input("k: "))
        print(f"Kombination: {kombinationen(n, k)}")
    elif auswahl == 8:
        n = int(input("n: "))
        print(f"Permutation: {permutation(n)}")
    elif auswahl == 9:
        n = int(input("n: "))
        k = int(input("k: "))
        print(f"Variation: {variation(n, k)}")
    elif auswahl == 10:
        p_liste = list(map(float, input("Wahrscheinlichkeiten (mit Komma getrennt): ").split(',')))
        baumdiagramm(p_liste)
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
