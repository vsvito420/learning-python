# Eigenschaften von Algorithmen 🧮

## Inhaltsverzeichnis
- [Eindeutigkeit](#eindeutigkeit)
  - [Definition](#definition)
  - [Beispiele](#beispiele)
- [Finitheit](#finitheit)
  - [Begrenzte Schritte](#begrenzte-schritte)
  - [Endliche Beschreibung](#endliche-beschreibung)
- [Terminierung](#terminierung)
  - [Endliche Laufzeit](#endliche-laufzeit)
  - [Ergebnislieferung](#ergebnislieferung)
- [Determinismus](#determinismus)
  - [Vorhersehbarkeit](#vorhersehbarkeit)
  - [Ausnahmen](#ausnahmen)
- [Determiniertheit](#determiniertheit)
  - [Festgelegte Schritte](#festgelegte-schritte)
  - [Klarer Ablauf](#klarer-ablauf)
- [Ausführbarkeit](#ausführbarkeit)
  - [Praktische Umsetzbarkeit](#praktische-umsetzbarkeit)
  - [Ressourcenbedarf](#ressourcenbedarf)
- [Beispiele für Algorithmen](#beispiele-für-algorithmen)
  - [Summe berechnen](#summe-berechnen)
  - [Größte Zahl finden](#größte-zahl-finden)
  - [Sortieralgorithmen](#sortieralgorithmen)

---

Vorheriges Thema: [Python Kommentare](/Anleitungen/01_Kommentare.md) | Nächstes Thema: [Python Interpreter](/Anleitungen/03_python_interpreter.md)

---

Ein Algorithmus ist eine eindeutige Handlungsvorschrift zur Lösung eines Problems oder einer Klasse von Problemen. Algorithmen bestehen aus endlich vielen, wohldefinierten Einzelschritten. Damit können sie zur Ausführung in ein Computerprogramm implementiert werden.

## Eindeutigkeit

- Ein Algorithmus muss klare und eindeutige Anweisungen haben, damit jeder genau weiß, was zu tun ist. 🔍
- Es darf keine Verwirrung oder Mehrdeutigkeit geben.
- Beispiel: "Addiere 5 zu x" ist eindeutig, "Mache x größer" ist nicht eindeutig.

## Finitheit

- Ein Algorithmus muss in einer begrenzten Anzahl von Schritten fertig sein. ⏱️
- Er darf nicht unendlich viele Schritte benötigen.
- Die Beschreibung des Algorithmus muss endlich sein.

## Terminierung

- Ein Algorithmus muss immer zu einem Ende kommen und ein Ergebnis liefern. 🏁
- Er darf nicht für immer weiterlaufen.
- Für jede gültige Eingabe muss der Algorithmus nach endlich vielen Schritten anhalten.

## Determinismus

- Wenn man einen Algorithmus mit den gleichen Eingaben ausführt, sollte immer das gleiche Ergebnis herauskommen. 🔄
- Der Algorithmus muss vorhersehbar sein.
- Zufallsalgorithmen sind eine Ausnahme, aber auch sie folgen bestimmten Wahrscheinlichkeitsverteilungen.

## Determiniertheit

- Jeder Schritt im Algorithmus muss genau festgelegt sein. 📋
- Es darf keine Unsicherheiten geben, was als Nächstes passiert.
- Nach jedem Schritt muss klar sein, welcher Schritt als nächstes folgt oder ob der Algorithmus beendet ist.

## Ausführbarkeit

- Ein Algorithmus muss so geschrieben sein, dass ein Computer oder Mensch ihn tatsächlich ausführen kann. 💻
- Jeder einzelne Schritt muss ausführbar sein.
- Die benötigten Ressourcen (Zeit, Speicher) müssen realistisch sein.

## Beispiele für Algorithmen

Hier sind einige Beispiele für einfache Algorithmen:

1. **Summe berechnen**:
   ```
   1. Setze Summe = 0
   2. Für jede Zahl in der Liste:
      a. Addiere die Zahl zur Summe
   3. Gib die Summe zurück
   ```

2. **Größte Zahl finden**:
   ```
   1. Setze max = erste Zahl in der Liste
   2. Für jede weitere Zahl in der Liste:
      a. Wenn die Zahl größer als max ist, setze max = diese Zahl
   3. Gib max zurück
   ```

3. **Sortieralgorithmus (Bubble Sort)**:
   ```
   1. Für i von 0 bis Länge der Liste - 1:
      a. Für j von 0 bis Länge der Liste - i - 1:
         i. Wenn Liste[j] > Liste[j+1], tausche die Elemente
   2. Die Liste ist nun sortiert
   ```

---

Algorithmen sind die Grundlage der Informatik und des Programmierens. Sie helfen uns, Probleme systematisch zu lösen und effiziente Lösungen zu finden. 🚀
