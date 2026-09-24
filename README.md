# Lernmaterial – Arbeitsblatt-Tool

Ein kleines Tool, um einheitlich gestaltete Mathematik-Arbeitsblätter zu erstellen.

## Features

- Einheitlicher Kopf mit Universität, Kurs, Semester, Blattnummer und Abgabedatum
- Aufgaben als Rohtext eingeben
- Automatische leichte Redaktion (Stil, Abkürzungen, Satzende, einfache Notations-Normalisierung)
- Konsistenter Markdown-Export für Weiterverarbeitung (z. B. PDF via Pandoc)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Nutzung

### 1) Neues Blatt anlegen

```bash
worksheet-tool new \
  --file data/analysis1_blatt01.json \
  --course "Analysis 1" \
  --semester "WS 2026/27" \
  --sheet 1 \
  --due "2026-10-15" \
  --lecturer "Dr. Beispiel"
```

### 2) Aufgabe hinzufügen (Rohtext wird redigiert)

```bash
worksheet-tool add-task \
  --file data/analysis1_blatt01.json \
  --title "Folgen in ℝ" \
  --text "zeige z.b. dass fuer alle n in N die folge a_n = 1/n gegen 0 konvergiert" \
  --points 8 \
  --topic "Folgen" \
  --difficulty "leicht"
```

### 3) Blatt rendern

```bash
worksheet-tool render \
  --file data/analysis1_blatt01.json \
  --out build/analysis1_blatt01.md
```

## Projektstruktur

- `src/worksheet_tool/models.py`: Datenmodell + Laden/Speichern
- `src/worksheet_tool/editing.py`: Redaktion + kleine mathematische Lints
- `src/worksheet_tool/renderer.py`: Einheitliches Layout als Markdown
- `src/worksheet_tool/cli.py`: CLI-Befehle (`new`, `add-task`, `render`)


## Interaktive HTML-Lernumgebung

Für eine schrittweise Visualisierung der Zahlenfolge `4, 9, 16, …` gibt es die Datei `lernumgebung.html`.
Sie kann direkt im Browser geöffnet werden.
Für eine interaktive Visualisierung von Forward Pass, quadratischem Fehler, Kettenregel-Backpropagation und Gewichtsupdate in einem linearen neuronalen Netz gibt es die Datei `backpropagation-linear.html`.
Sie kann ebenfalls direkt im Browser geöffnet werden.


## Geraden-Billard für lineare Funktionen

Mit `billard-lineare-funktionen.html` steht eine interaktive Lernumgebung für die 8. Klasse zur Verfügung. Die Schüler*innen steuern den y-Achsenabschnitt `b` und die Steigung `m`, um eine rote Kugel entlang einer linearen Funktion direkt einzulochen. Vier aufeinander aufbauende Aufgaben führen von ganzzahligen Werten zu Brüchen und Dezimalzahlen. Die animierten Stöße berücksichtigen Kugelkollisionen, Reibung und den Einzugsbereich der Löcher; die Geradenvorschau kann bei Bedarf eingeblendet werden. Die Datei kann direkt im Browser geöffnet werden.
