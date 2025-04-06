# Variablen und Datentypen in Python 🐍

## Inhaltsverzeichnis
- [Was sind Variablen?](#was-sind-variablen)
  - [Variablen als Behälter](#variablen-als-behälter)
  - [Speicherung im Arbeitsspeicher](#speicherung-im-arbeitsspeicher)
- [Wie definiere ich eine Variable?](#wie-definiere-ich-eine-variable)
  - [Syntax der Variablendefinition](#syntax-der-variablendefinition)
  - [Namenskonventionen](#namenskonventionen)
  - [Ausgabe von Variablen](#ausgabe-von-variablen)
- [Wie kopiere ich eine Variable?](#wie-kopiere-ich-eine-variable)
  - [Wertzuweisung zwischen Variablen](#wertzuweisung-zwischen-variablen)
  - [Referenzen vs. Kopien](#referenzen-vs-kopien)
- [Variablenzuweisung mit Zahlen](#variablenzuweisung-mit-zahlen)
  - [Grundrechenarten](#grundrechenarten)
  - [Kurzschreibweisen](#kurzschreibweisen)
- [Datentypen in Python](#datentypen-in-python)
  - [Zahlentypen (int, float)](#zahlentypen-int-float)
  - [Texttypen (str)](#texttypen-str)
  - [Wahrheitswerte (bool)](#wahrheitswerte-bool)
  - [Sammlungstypen (list, tuple, dict)](#sammlungstypen-list-tuple-dict)
  - [Typbestimmung](#typbestimmung)
- [Umwandlung von Datentypen](#umwandlung-von-datentypen)
  - [Typkonvertierung](#typkonvertierung)
  - [Häufige Konvertierungen](#häufige-konvertierungen)
- [Arbeiten mit Strings](#arbeiten-mit-strings)
  - [String-Erstellung](#string-erstellung)
  - [Konkatenation](#konkatenation)
  - [String-Operationen](#string-operationen)

## Was sind Variablen?

Stell dir eine Variable wie eine beschriftete Kiste vor. In diese Kiste kannst du Dinge reinlegen und später wieder rausholen! 📦

In der Computertechnik dienen Variablen dazu, Daten im Arbeitsspeicher zu speichern und ihnen einen Namen zu geben. So können wir auf diese Daten später wieder zugreifen und sie verwenden.

## Wie definiere ich eine Variable?

Es ist ganz einfach! Du gibst deiner Kiste einen Namen und legst etwas hinein:

```python
# Eine Variable mit dem Namen "alter" erstellen und den Wert 10 zuweisen
alter = 10

# Eine Variable mit dem Namen "name" erstellen und den Text "Anna" zuweisen
name = "Anna"

# Den Inhalt der Variablen anzeigen
print(alter)  # Gibt 10 aus
print(name)   # Gibt Anna aus
```

## Wie kopiere ich eine Variable?

Eine Variable kopieren ist wie eine zweite Kiste mit dem gleichen Inhalt:

```python
# Erste Variable erstellen
punkte = 100

# Zweite Variable mit dem Wert der ersten Variable erstellen
neue_punkte = punkte

# Beide Variablen ausgeben
print(punkte)      # Gibt 100 aus
print(neue_punkte) # Gibt ebenfalls 100 aus
```

## Variablenzuweisung mit Zahlen

Mit Python kannst du rechnen und die Ergebnisse in Variablen speichern! 🔢

```python
# Einfache Berechnungen
a = 5
b = 3
summe = a + b      # Addition: 8
differenz = a - b  # Subtraktion: 2
produkt = a * b    # Multiplikation: 15
quotient = a / b   # Division: 1.6666...

# Variablen können auch aktualisiert werden
punkte = 10
punkte = punkte + 5  # punkte ist jetzt 15
# oder kürzer:
punkte += 5          # punkte ist jetzt 20
```

## Datentypen in Python

Python kennt verschiedene Arten von Daten:

1. **Zahlen**:
   - `int` (Ganzzahlen): `42`, `-7`, `0`
   - `float` (Dezimalzahlen): `3.14`, `-2.5`, `1.0`

2. **Text**:
   - `str` (Strings): `"Hallo"`, `'Python'`, `"123"`

3. **Wahrheitswerte**:
   - `bool` (Boolean): `True`, `False`

4. **Sammlungen**:
   - `list` (Listen): `[1, 2, 3]`, `["a", "b", "c"]`
   - `tuple` (Tupel): `(1, 2, 3)`
   - `dict` (Wörterbücher): `{"name": "Anna", "alter": 10}`

```python
# Den Datentyp einer Variable herausfinden
name = "Max"
alter = 12
print(type(name))  # <class 'str'>
print(type(alter)) # <class 'int'>
```

## Umwandlung von Datentypen

Manchmal musst du Zahlen in Text verwandeln oder andersherum:

```python
# Von Zahl zu String
alter = 10
alter_als_text = str(alter)
print("Ich bin " + alter_als_text + " Jahre alt.")  # Ich bin 10 Jahre alt.

# Von String zu Zahl
text_zahl = "42"
zahl = int(text_zahl)
ergebnis = zahl + 8
print(ergebnis)  # 50

# Von String zu Dezimalzahl
text_dezimal = "3.14"
dezimal = float(text_dezimal)
ergebnis = dezimal * 2
print(ergebnis)  # 6.28
```

## Arbeiten mit Strings

Text (auch "Strings" genannt) schreibst du in Anführungszeichen:

```python
# Strings erstellen
name = "Emma"
gruß = 'Hallo'

# Strings verbinden (Konkatenation)
nachricht = gruß + " " + name + "!"
print(nachricht)  # Hallo Emma!

# Mehrfache Wiederholung
echo = "Hallo! " * 3
print(echo)  # Hallo! Hallo! Hallo!

# Länge eines Strings
wort = "Programmieren"
länge = len(wort)
print(länge)  # 13

# Auf einzelne Zeichen zugreifen
erster_buchstabe = wort[0]  # P
letzter_buchstabe = wort[-1]  # n
```

---

Das sind die Grundlagen! Mit Variablen kannst du:

- Informationen speichern 💾
- Werte wiederverwenden 🔄
- Berechnungen durchführen ➕
- Text und Zahlen verarbeiten 📝

Probier es einfach aus und experimentiere damit! 🚀
