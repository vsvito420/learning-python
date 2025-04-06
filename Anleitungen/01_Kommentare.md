# Python Kommentare 💬

## Inhaltsverzeichnis
- [Einzeilige Kommentare](#einzeilige-kommentare)
- [Mehrzeilige Kommentare](#mehrzeilige-kommentare)
- [Best Practices](#best-practices)
- [Beispiele](#beispiele)

---

Nächstes Thema: [Algorithmen](/Anleitungen/02_Algorithmen.md)

---

Python bietet verschiedene Möglichkeiten, Code zu kommentieren. Kommentare sind wichtig, um deinen Code zu dokumentieren und anderen (oder dir selbst in der Zukunft) zu erklären, was dein Code tut.

## Einzeilige Kommentare

Einzeilige Kommentare beginnen mit dem `#` Symbol:

```python
# Dies ist ein einzeiliger Kommentar
x = 5  # Kommentar am Ende einer Code-Zeile
```

Alles nach dem `#` wird vom Python-Interpreter ignoriert und dient nur zur Information für Menschen, die den Code lesen.

## Mehrzeilige Kommentare

Mehrzeilige Kommentare werden mit dreifachen Anführungszeichen erstellt:

```python
"""
Dies ist ein mehrzeiliger
Kommentar über
mehrere Zeilen
"""
```

Diese Art von Kommentaren wird auch für Docstrings verwendet, um Funktionen und Module zu dokumentieren.

## Best Practices

Hier sind einige bewährte Praktiken für das Schreiben von Kommentaren: 📝

- Kommentare sollten kurz und präzise sein
- Kommentare erklären das "Warum", nicht das "Was"
- Verwende aussagekräftige Variablen- und Funktionsnamen statt unnötiger Kommentare
- Halte Kommentare aktuell, wenn du deinen Code änderst
- Nutze Kommentare, um komplexe Algorithmen oder Entscheidungen zu erklären
- Verwende Docstrings für Funktionen und Module

## Beispiele

Hier sind einige Beispiele für gute Kommentare:

```python
def calculate_sum(a, b):
    # Addiere zwei Zahlen und gib das Ergebnis zurück
    return a + b

"""
Diese Funktion berechnet
die Summe zweier Zahlen
und gibt das Ergebnis zurück
"""

# Konstanten für die Berechnung der Mehrwertsteuer
TAX_RATE = 0.19  # 19% Mehrwertsteuer in Deutschland

# Schlechtes Beispiel - unnötiger Kommentar
x = x + 1  # Erhöhe x um 1

# Gutes Beispiel - erklärt das Warum
retry_count = retry_count + 1  # Erhöhe Wiederholungszähler nach fehlgeschlagenem Netzwerkversuch
```

---

Kommentare sind ein wichtiger Teil des Programmierens und helfen dir, deinen Code verständlicher und wartbarer zu machen. Nutze sie weise! 🧠
