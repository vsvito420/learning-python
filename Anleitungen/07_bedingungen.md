# Bedingungen und Entscheidungen in Python 🔀

## Inhaltsverzeichnis
- [Was sind Bedingungen?](#was-sind-bedingungen)
  - [Vergleichsoperatoren](#vergleichsoperatoren)
  - [Logische Operatoren](#logische-operatoren)
- [Die if-Anweisung](#die-if-anweisung)
  - [Syntax und Grundstruktur](#syntax-und-grundstruktur)
  - [Einfache Beispiele](#einfache-beispiele)
- [if-else-Anweisungen](#if-else-anweisungen)
  - [Syntax und Verwendung](#syntax-und-verwendung)
  - [Beispiele](#beispiele)
- [if-elif-else-Anweisungen](#if-elif-else-anweisungen)
  - [Mehrfache Bedingungen](#mehrfache-bedingungen)
  - [Komplexe Beispiele](#komplexe-beispiele)
- [Verschachtelte Bedingungen](#verschachtelte-bedingungen)
  - [Struktur und Lesbarkeit](#struktur-und-lesbarkeit)
  - [Praxisbeispiele](#praxisbeispiele)
- [Der Ternäre Operator](#der-ternäre-operator)
  - [Kurzschreibweise](#kurzschreibweise)
- [Übungsaufgaben](#übungsaufgaben)
  - [Einfache Übung: Alterscheck](#übungsaufgaben)
  - [Mittelschwere Übung: Notenrechner](#übungsaufgaben)
  - [Herausforderung: Passwortprüfer](#übungsaufgaben)
- [Zusammenfassung](#zusammenfassung)
  - [Wichtigste Konzepte](#zusammenfassung)

---

Vorheriges Thema: [Lernweg](/Anleitungen/06_lernweg.md) | Nächstes Thema: [Schleifen](/Anleitungen/08_schleifen.md)

---

Stell dir vor, du stehst an einer Weggabelung – je nachdem, welchen Weg du wählst, kommst du zu unterschiedlichen Zielen. Genauso arbeiten Bedingungen in Python! Sie ermöglichen deinem Programm, Entscheidungen zu treffen und unterschiedliche Aktionen auszuführen, je nachdem ob bestimmte Bedingungen erfüllt sind oder nicht.

## Was sind Bedingungen?

Bedingungen sind Ausdrücke, die entweder `True` (wahr) oder `False` (falsch) ergeben. Sie werden verwendet, um die Programmausführung zu steuern und basierend auf bestimmten Kriterien unterschiedliche Aktionen auszuführen. 🧠

### Vergleichsoperatoren

Mit Vergleichsoperatoren kannst du Werte miteinander vergleichen:

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `==` | gleich | `5 == 5` (True) |
| `!=` | ungleich | `5 != 3` (True) |
| `>` | größer als | `5 > 3` (True) |
| `<` | kleiner als | `5 < 3` (False) |
| `>=` | größer oder gleich | `5 >= 5` (True) |
| `<=` | kleiner oder gleich | `5 <= 3` (False) |

```python
# Beispiele für Vergleiche
x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

### Logische Operatoren

Mit logischen Operatoren kannst du mehrere Bedingungen verknüpfen:

- `and` - Beide Bedingungen müssen wahr sein
- `or` - Mindestens eine Bedingung muss wahr sein
- `not` - Kehrt den Wahrheitswert um

```python
# Beispiele für logische Operatoren
x = 10
y = 5
z = 20

print(x > y and x < z)   # True (beide Bedingungen sind wahr)
print(x < y or x < z)    # True (eine Bedingung ist wahr)
print(not x > y)         # False (kehrt True in False um)
```

## Die if-Anweisung

Die `if`-Anweisung ist die grundlegendste Entscheidungsstruktur. Sie führt einen Codeblock aus, wenn eine bestimmte Bedingung wahr ist. 🔍

### Syntax und Grundstruktur

```python
if bedingung:
    # Dieser Code wird ausgeführt, wenn die Bedingung wahr ist
    anweisung1
    anweisung2
# Dieser Code wird immer ausgeführt, unabhängig von der Bedingung
weitere_anweisung
```

**Wichtig**: In Python wird die Einrückung (meistens 4 Leerzeichen) verwendet, um Codeblöcke zu definieren. Alle eingerückten Zeilen unter einer `if`-Anweisung gehören zum selben Block und werden nur ausgeführt, wenn die Bedingung wahr ist.

### Einfache Beispiele

```python
# Prüfen, ob eine Zahl positiv ist
zahl = 10

if zahl > 0:
    print("Die Zahl ist positiv!")

# Prüfen, ob eine Zahl gerade ist
if zahl % 2 == 0:
    print("Die Zahl ist gerade!")
```

## if-else-Anweisungen

Mit `if-else` kannst du zwei alternative Wege definieren: einen für den Fall, dass die Bedingung wahr ist, und einen für den Fall, dass sie falsch ist. 🔄

### Syntax und Verwendung

```python
if bedingung:
    # Wird ausgeführt, wenn die Bedingung wahr ist
    anweisung1
else:
    # Wird ausgeführt, wenn die Bedingung falsch ist
    anweisung2
```

### Beispiele

```python
# Prüfen, ob eine Zahl positiv oder nicht positiv ist
zahl = -5

if zahl > 0:
    print("Die Zahl ist positiv!")
else:
    print("Die Zahl ist nicht positiv!")

# Prüfen, ob eine Zahl gerade oder ungerade ist
if zahl % 2 == 0:
    print("Die Zahl ist gerade!")
else:
    print("Die Zahl ist ungerade!")
```

## if-elif-else-Anweisungen

Wenn du mehr als zwei Alternativen hast, kannst du `elif` (kurz für "else if") verwenden. 🧩

### Mehrfache Bedingungen

```python
if bedingung1:
    # Wird ausgeführt, wenn bedingung1 wahr ist
    anweisung1
elif bedingung2:
    # Wird ausgeführt, wenn bedingung1 falsch und bedingung2 wahr ist
    anweisung2
elif bedingung3:
    # Wird ausgeführt, wenn bedingung1 und bedingung2 falsch und bedingung3 wahr ist
    anweisung3
else:
    # Wird ausgeführt, wenn alle Bedingungen falsch sind
    anweisung4
```

### Komplexe Beispiele

```python
# Notenausgabe basierend auf Punktzahl
punkte = 85

if punkte >= 90:
    note = "sehr gut"
elif punkte >= 80:
    note = "gut"
elif punkte >= 70:
    note = "befriedigend"
elif punkte >= 60:
    note = "ausreichend"
else:
    note = "mangelhaft"

print(f"Deine Note ist: {note}")  # Ausgabe: Deine Note ist: gut

# Tageszeit-Gruß
stunde = 14  # 14 Uhr

if stunde < 12:
    print("Guten Morgen!")
elif stunde < 18:
    print("Guten Tag!")
else:
    print("Guten Abend!")
```

## Verschachtelte Bedingungen

Du kannst auch Bedingungen ineinander verschachteln, um komplexere Entscheidungsstrukturen zu erstellen. 🎯

### Struktur und Lesbarkeit

```python
if hauptbedingung:
    # Dieser Code wird ausgeführt, wenn hauptbedingung wahr ist
    if unterbedingung1:
        # Dieser Code wird ausgeführt, wenn hauptbedingung und unterbedingung1 wahr sind
        anweisung1
    else:
        # Dieser Code wird ausgeführt, wenn hauptbedingung wahr und unterbedingung1 falsch ist
        anweisung2
else:
    # Dieser Code wird ausgeführt, wenn hauptbedingung falsch ist
    anweisung3
```

### Praxisbeispiele

```python
# Beispiel: Zugangskontrolle
benutzername = "max"
passwort = "sicher123"

if benutzername == "max":
    if passwort == "sicher123":
        print("Zugang gewährt!")
    else:
        print("Falsches Passwort!")
else:
    print("Unbekannter Benutzer!")

# Alternative mit logischen Operatoren (übersichtlicher)
if benutzername == "max" and passwort == "sicher123":
    print("Zugang gewährt!")
else:
    print("Zugang verweigert!")
```

## Der Ternäre Operator

Python bietet auch eine Kurzschreibweise für einfache if-else-Entscheidungen: den ternären Operator. ⚡

### Kurzschreibweise

```python
# Normale if-else-Anweisung
if bedingung:
    ergebnis = wert1
else:
    ergebnis = wert2

# Äquivalente Kurzschreibweise mit ternärem Operator
ergebnis = wert1 if bedingung else wert2
```

Beispiel:
```python
alter = 20
status = "volljährig" if alter >= 18 else "minderjährig"
print(status)  # Ausgabe: volljährig

# Berechnung des absoluten Werts
x = -10
absolutwert = x if x >= 0 else -x
print(absolutwert)  # Ausgabe: 10
```

## Übungsaufgaben

Hier sind einige Aufgaben, mit denen du das Gelernte üben kannst: 🏋️‍♂️

1. **Einfache Übung: Alterscheck**
   Schreibe ein Programm, das den Benutzer nach seinem Alter fragt und basierend darauf verschiedene Nachrichten ausgibt.
   ```python
   # Beispielcode für die Aufgabe
   alter = int(input("Wie alt bist du? "))
   
   # Hier deine Lösung einfügen
   # Unter 13: "Du darfst noch nicht alle Filme sehen."
   # 13-17: "Du darfst Filme ab 12 Jahren sehen."
   # Ab 18: "Du darfst alle Filme sehen."
   ```

2. **Mittelschwere Übung: Notenrechner**
   Schreibe ein Programm, das die Punktzahl einer Klassenarbeit (0-100) einliest und die entsprechende Note ausgibt.
   ```python
   punkte = int(input("Gib deine Punktzahl ein (0-100): "))
   
   # Hier deine Lösung einfügen
   # 90-100: "sehr gut"
   # 80-89: "gut"
   # 70-79: "befriedigend"
   # 60-69: "ausreichend"
   # 50-59: "mangelhaft"
   # 0-49: "ungenügend"
   ```

3. **Herausforderung: Passwortprüfer**
   Schreibe ein Programm, das prüft, ob ein Passwort sicher ist. Ein sicheres Passwort sollte:
   - Mindestens 8 Zeichen lang sein
   - Mindestens einen Großbuchstaben enthalten
   - Mindestens eine Zahl enthalten
   ```python
   passwort = input("Gib ein Passwort ein: ")
   
   # Hier deine Lösung einfügen
   # Ausgabe: "Dein Passwort ist sicher" oder "Dein Passwort ist unsicher" mit Begründung
   ```

**Tipp**: Versuche die Aufgaben selbständig zu lösen. Falls du nicht weiterkommst, experimentiere mit den Bedingungsstrukturen, die du in dieser Anleitung gelernt hast. Denk daran, dass du mehrere Bedingungen mit `and` und `or` verknüpfen kannst.

## Zusammenfassung

In dieser Anleitung haben wir gelernt:

- Was Bedingungen sind und wie sie in Python verwendet werden 📝
- Wie Vergleichsoperatoren (`==`, `!=`, `>`, `<`, `>=`, `<=`) funktionieren ⚖️
- Wie logische Operatoren (`and`, `or`, `not`) Bedingungen verknüpfen 🔗
- Wie die `if`-Anweisung für einfache Entscheidungen verwendet wird 🚦
- Wie `if-else` für Entscheidungen mit zwei Alternativen genutzt wird 🔀
- Wie `if-elif-else` für Entscheidungen mit mehreren Alternativen eingesetzt wird 🌲
- Wie verschachtelte Bedingungen komplexe Entscheidungsstrukturen erstellen 🧩
- Wie der ternäre Operator als Kurzschreibweise für einfache if-else-Anweisungen dient ⚡

Bedingungen sind ein fundamentales Konzept in der Programmierung und ermöglichen es deinen Programmen, intelligent zu agieren und auf verschiedene Situationen zu reagieren.

---

Probiere das Gelernte aus und experimentiere mit Bedingungen in deinen eigenen Programmen! 🚀

---
