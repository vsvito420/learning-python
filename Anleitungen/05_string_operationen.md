# String-Operationen in Python 🧵

## Inhaltsverzeichnis
- [Grundlagen von Strings](#grundlagen-von-strings)
  - [String-Definition und Eigenschaften](#grundlagen-von-strings)
  - [Grundlegende Operationen](#grundlagen-von-strings)
- [String-Methoden](#string-methoden)
  - [Groß- und Kleinschreibung](#string-methoden)
  - [Leerzeichen entfernen](#string-methoden)
  - [Suchen und Ersetzen](#string-methoden)
  - [Eigenschaften überprüfen](#string-methoden)
- [String-Formatierung](#string-formatierung)
  - [Formatierungsmethoden](#string-formatierung)
  - [f-Strings](#string-formatierung)
- [String-Slicing und Indexierung](#string-slicing-und-indexierung)
  - [Zeichen zugreifen und Teilstrings](#string-slicing-und-indexierung)
  - [Fortgeschrittenes Slicing](#string-slicing-und-indexierung)
- [Praktische Anwendungen](#praktische-anwendungen)
  - [Beispiele aus dem Alltag](#praktische-anwendungen)
- [Übungsaufgaben](#übungsaufgaben)
  - [Einfache Übung: Namenformatierer](#übungsaufgaben)
  - [Mittelschwere Übung: Buchstabenzähler](#übungsaufgaben)
  - [Herausforderung: Palindrom-Checker](#übungsaufgaben)
- [Zusammenfassung](#zusammenfassung)
  - [Wichtigste Konzepte](#zusammenfassung)

---

Vorheriges Thema: [Variablen und Datentypen](/Anleitungen/04_variablen_und_Datentypen.md) | Nächstes Thema: [Nächstes Thema](/Anleitungen/XX_nächstes_thema.md)

---

Stell dir vor, du möchtest mit Text arbeiten - Namen speichern, Nachrichten anzeigen oder Benutzereingaben verarbeiten. Dafür brauchst du Strings! Strings sind in Python die Datentypen für Text und gehören zu den wichtigsten Werkzeugen beim Programmieren. In dieser Anleitung lernst du, wie du mit Strings arbeiten, sie verändern und formatieren kannst.

## Grundlagen von Strings

Stell dir einen String wie eine Perlenkette vor, bei der jede Perle ein Buchstabe oder Zeichen ist. In Python schreibst du Strings in einfachen (`'`) oder doppelten (`"`) Anführungszeichen. Beide Varianten funktionieren gleich. 📌

- Ein String kann alles enthalten: Buchstaben, Zahlen, Sonderzeichen, Leerzeichen
- Strings sind unveränderlich (immutable) - wie eine versiegelte Nachricht
- Mit dem `+` Operator kannst du Strings verbinden (wie zwei Perlenketten zusammenfügen)

```python
# Strings erstellen
name = "Python"
beschreibung = 'ist eine Programmiersprache'

# Strings verbinden (Konkatenation)
satz = name + " " + beschreibung
print(satz)  # Ausgabe: Python ist eine Programmiersprache

# Länge eines Strings ermitteln (Anzahl der Zeichen)
länge = len(name)
print(länge)  # Ausgabe: 6

# Strings wiederholen
wiederholung = "Hip " * 3
print(wiederholung)  # Ausgabe: Hip Hip Hip 
```

## String-Methoden

Strings in Python haben viele eingebaute "Superkräfte" (Methoden), mit denen du sie bearbeiten kannst. Diese Methoden erstellen immer einen neuen String, da Strings unveränderlich sind. 🔎

1. Groß- und Kleinschreibung ändern - wie ein Textformatierungswerkzeug
2. Leerzeichen entfernen - wie ein digitaler Radiergummi
3. Suchen und Ersetzen - wie die Suchen-Funktion in einem Texteditor
4. Überprüfen von Eigenschaften - wie ein Textdetektiv

Hier sind einige wichtige String-Methoden:

```python
text = "  Hallo Welt  "

# Groß- und Kleinschreibung
print(text.upper())      # Ausgabe: "  HALLO WELT  "
print(text.lower())      # Ausgabe: "  hallo welt  "
print(text.capitalize()) # Ausgabe: "  hallo welt  "
print(text.title())      # Ausgabe: "  Hallo Welt  " (Jedes Wort groß)

# Leerzeichen entfernen
print(text.strip())      # Ausgabe: "Hallo Welt"
print(text.lstrip())     # Ausgabe: "Hallo Welt  "
print(text.rstrip())     # Ausgabe: "  Hallo Welt"

# Suchen und Ersetzen
print(text.replace("Welt", "Python"))  # Ausgabe: "  Hallo Python  "
print(text.find("Welt"))               # Ausgabe: 8 (Position)
print(text.count("l"))                 # Ausgabe: 3 (Anzahl der "l")
print("Welt" in text)                  # Ausgabe: True

# Eigenschaften überprüfen
print("123".isdigit())   # Ausgabe: True (nur Ziffern?)
print("abc".isalpha())   # Ausgabe: True (nur Buchstaben?)
print("Hallo123".isalnum())  # Ausgabe: True (Buchstaben oder Ziffern?)
print("Hallo".startswith("Ha"))  # Ausgabe: True
print("Welt".endswith("lt"))     # Ausgabe: True
```

## String-Formatierung

Stell dir vor, du hast eine Vorlage für eine Nachricht und willst persönliche Daten einfügen. Dafür gibt es in Python verschiedene Möglichkeiten. Die modernste und coolste Methode sind f-Strings (ab Python 3.6). 💡

```python
# Alte Methode mit %
name = "Max"
alter = 15
print("Hallo, ich bin %s und %d Jahre alt." % (name, alter))

# Methode mit .format()
print("Hallo, ich bin {} und {} Jahre alt.".format(name, alter))

# f-Strings (empfohlen, ab Python 3.6) - am einfachsten zu lesen!
print(f"Hallo, ich bin {name} und {alter} Jahre alt.")

# Mit f-Strings kannst du auch direkt rechnen
print(f"In 5 Jahren werde ich {alter + 5} Jahre alt sein.")

# Zahlenformatierung für schöne Ausgaben
pi = 3.14159
print(f"Pi gerundet: {pi:.2f}")  # Ausgabe: Pi gerundet: 3.14

# Ausrichtung von Text
print(f"{'Links':<10}|{'Mitte':^10}|{'Rechts':>10}")
# Ausgabe: Links     |  Mitte   |    Rechts
```

## String-Slicing und Indexierung

Stell dir einen String wie ein Wort aus Scrabble-Steinen vor. Du kannst einzelne Steine (Zeichen) nehmen oder mehrere auf einmal (Teilstrings). Python-Indizes beginnen bei 0 für das erste Zeichen - das ist wichtig zu merken! ⚠️

```python
text = "Python ist cool"

# Einzelne Zeichen über Index zugreifen (wie auf einen bestimmten Scrabble-Stein)
print(text[0])    # Ausgabe: P (erstes Zeichen)
print(text[7])    # Ausgabe: i
print(text[-1])   # Ausgabe: l (letztes Zeichen)

# Slicing: text[start:ende:schritt] (wie mehrere Scrabble-Steine auf einmal nehmen)
print(text[0:6])     # Ausgabe: Python (Zeichen 0 bis 5)
print(text[7:10])    # Ausgabe: ist
print(text[11:])     # Ausgabe: cool (von 11 bis Ende)
print(text[:6])      # Ausgabe: Python (vom Anfang bis 5)
print(text[::2])     # Ausgabe: Pto s ol (jedes zweite Zeichen)
print(text[::-1])    # Ausgabe: looc tsi nohtyP (rückwärts)
```

Tipps:
- Der Startindex ist inklusive (wird mitgenommen), der Endindex exklusive (wird nicht mitgenommen)
- Negative Indizes zählen vom Ende des Strings (-1 ist das letzte Zeichen)
- Wenn du einen Index außerhalb des gültigen Bereichs verwendest, erhältst du einen Fehler
- Slicing ist sehr mächtig und wird oft in Python-Programmen verwendet

## Praktische Anwendungen

Hier sind einige Beispiele, wie du String-Operationen im Alltag nutzen kannst: 🚀

### Beispiel 1: Benutzernamen formatieren
```python
# Benutzernamen standardisieren
eingabe = "   Max Mustermann  "
username = eingabe.strip().lower().replace(" ", "_")
print(username)  # Ausgabe: max_mustermann
```

### Beispiel 2: E-Mail-Adresse prüfen
```python
email = "benutzer@example.com"
if "@" in email and "." in email and email.count("@") == 1:
    print("Gültige E-Mail-Form")
else:
    print("Ungültige E-Mail-Form")
```

### Beispiel 3: Passwort-Stärke prüfen
```python
passwort = "Sicher123!"
if len(passwort) >= 8 and any(c.isupper() for c in passwort) and any(c.isdigit() for c in passwort):
    print("Starkes Passwort")
else:
    print("Schwaches Passwort")
```

## Übungsaufgaben

Hier sind einige Aufgaben, mit denen du das Gelernte üben kannst: 🏋️‍♂️

1. **Einfache Übung: Namenformatierer** 
   Schreibe ein Programm, das einen Vor- und Nachnamen einliest und dann in verschiedenen Formaten ausgibt.
   ```python
   # Beispielcode für die Aufgabe
   vorname = input("Gib deinen Vornamen ein: ")
   nachname = input("Gib deinen Nachnamen ein: ")
   # Hier deine Lösung einfügen
   # Ausgabe 1: "NACHNAME, Vorname" (Nachname in Großbuchstaben)
   # Ausgabe 2: "V. Nachname" (Vorname als Initial)
   # Ausgabe 3: "vorname.nachname" (alles kleingeschrieben)
   ```

2. **Mittelschwere Übung: Buchstabenzähler**
   Schreibe ein Programm, das einen Satz einliest und für jeden Buchstaben zählt, wie oft er vorkommt.
   ```python
   satz = input("Gib einen Satz ein: ")
   # Hier deine Lösung einfügen
   # Beispielausgabe für "Hallo Welt":
   # H: 1
   # a: 1
   # l: 3
   # o: 1
   # W: 1
   # e: 1
   # t: 1
   ```

3. **Herausforderung: Palindrom-Checker**
   Schreibe ein Programm, das prüft, ob ein eingegebener Text ein Palindrom ist (vorwärts und rückwärts gelesen gleich). Beachte: Ignoriere Leerzeichen und Groß-/Kleinschreibung.
   ```python
   text = input("Gib einen Text ein: ")
   # Hier deine Lösung einfügen
   # Beispiele für Palindrome:
   # "Anna"
   # "Otto"
   # "Reliefpfeiler"
   # "Ein Neger mit Gazelle zagt im Regen nie"
   ```

**Tipp**: Versuche die Aufgaben selbständig zu lösen. Falls du nicht weiterkommst, experimentiere mit den String-Methoden und Slicing-Techniken, die du in dieser Anleitung gelernt hast. Denk daran, dass du Strings mit Methoden wie `.lower()` und `.replace()` bearbeiten kannst, bevor du weitere Operationen durchführst.

## Zusammenfassung

In dieser Anleitung haben wir die Welt der String-Operationen in Python erkundet:

- Wir haben gelernt, was Strings sind und wie man sie erstellt 📝
- Wir haben die mächtigen String-Methoden kennengelernt, um Texte zu bearbeiten ✂️
- Wir haben verschiedene Möglichkeiten der String-Formatierung entdeckt, besonders f-Strings 🎨
- Wir haben gesehen, wie String-Slicing und Indexierung funktionieren 🔍
- Wir haben praktische Anwendungen für String-Operationen im Alltag kennengelernt 🛠️

Strings sind überall in der Programmierung - von Benutzereingaben über Dateiverarbeitung bis hin zu Webentwicklung. Mit den Techniken aus dieser Anleitung kannst du jetzt Text in deinen Python-Programmen effektiv verarbeiten!

---

Probiere das Gelernte aus und experimentiere mit Strings in deinen eigenen Programmen! 🚀

---
