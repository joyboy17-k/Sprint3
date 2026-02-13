# Sprint 3: ConsoleUI - Implementierungsdokumentation

## 📋 Übersicht

Diese Erweiterung implementiert eine vollständige Konsolen-Benutzeroberfläche (ConsoleUI) für die U-Bahn Linie U3 gemäß den Spezifikationen aus dem Klassendiagramm.

## 🆕 Neue Dateien

### 1. `console_ui.py` - Konsolen-Benutzeroberfläche (NEU)

**Zweck**: Zentrale Klasse für alle Benutzerinteraktionen über die Konsole

**Hauptkomponenten**:

#### Klasse `ConsoleUI`
Zentrale Klasse für die Benutzeroberfläche mit folgenden Attributen:
- `netz`: UbahnNetz-Objekt für Zugriff auf Stationsdaten

**Wichtige Methoden**:

#### `ask_yes_no(frage: str) -> bool`
- **Zweck**: Stellt eine Ja/Nein-Frage an den Benutzer
- **Validierung**: Akzeptiert 'j', 'ja', 'y', 'yes' für Ja und 'n', 'nein', 'no' für Nein (case-insensitive)
- **Rückgabe**: True für Ja, False für Nein
- **Fehlerbehandlung**: Wiederholt die Frage bei ungültiger Eingabe

#### `ask_amount(prompt: str) -> float`
- **Zweck**: Fragt nach einem Geldbetrag
- **Validierung**: 
  - Akzeptiert Komma und Punkt als Dezimaltrennzeichen
  - Prüft auf negative Beträge
  - Konvertiert zu float
- **Rückgabe**: Der eingegebene Betrag als float
- **Fehlerbehandlung**: Wiederholt die Frage bei ungültiger Eingabe

#### `choose_start_station(ziel: Optional[str] = None) -> str`
- **Zweck**: Lässt den Benutzer eine Startstation wählen
- **Eingabemöglichkeiten**:
  - Nummer der Station (1-basiert)
  - Name der Station (case-insensitive)
- **Validierung**:
  - Prüft, ob Station existiert
  - Verhindert, dass Start = Ziel
- **Ausgabe**: Zeigt alle verfügbaren Stationen nummeriert an
- **Rückgabe**: Name der gewählten Station (uppercase)

#### `choose_destination_station(start: str) -> str`
- **Zweck**: Lässt den Benutzer eine Zielstation wählen
- **Eingabemöglichkeiten**:
  - Nummer der Station (1-basiert)
  - Name der Station (case-insensitive)
- **Validierung**:
  - Prüft, ob Station existiert
  - Verhindert, dass Ziel = Start
- **Ausgabe**: Zeigt alle verfügbaren Stationen (außer Start) nummeriert an
- **Rückgabe**: Name der gewählten Station (uppercase)

#### `display_welcome() -> None`
- **Zweck**: Zeigt die Willkommensnachricht an
- **Ausgabe**: Formatierte Begrüßung mit Trennlinien

#### `display_ticket_info(ticket_info: dict) -> None`
- **Zweck**: Zeigt Ticket-Informationen formatiert an
- **Parameter**: Dictionary mit Ticket-Informationen (Key-Value-Paare)
- **Ausgabe**: Strukturierte Darstellung mit Trennlinien

---

## 🔧 Geänderte Dateien

Keine Dateien wurden geändert. Die ConsoleUI ist ein komplett neues Modul.

---

## 📁 Unveränderte Dateien

### 2. `adjazenzliste.py` - Streckendaten (UNVERÄNDERT)
- Betriebszeiten
- Stationsreihenfolge
- Bidirektionale Adjazenzliste mit Fahrt- und Haltezeiten

### 3. `classe.py` - Hauptklassen (UNVERÄNDERT)
- `Station`-Dataclass
- `Route`-Klasse
- `RouteFinder`-Klasse
- `UbahnNetz`-Klasse

### 4. `ticket.py` - Ticket-Rabattsystem (UNVERÄNDERT)
- Ticket-Kategorisierung
- Preisberechnung
- Rabatte und Zuschläge

### 5. `service.py` - Service-Funktionen (UNVERÄNDERT)
- Eingabefunktionen
- Fahrplan-Erstellung

### 6. `main.py` - Hauptprogramm (UNVERÄNDERT)
- Programmablauf
- Benutzerinteraktion

---

## 🎯 Erfüllte Anforderungen

### Benutzerfreundlichkeit
✅ **Klare Eingabeaufforderungen**
- Alle Methoden haben verständliche Prompts
- Fehlerhafte Eingaben werden erklärt

✅ **Flexible Eingabemöglichkeiten**
- Stationen können per Nummer oder Name gewählt werden
- Ja/Nein-Fragen akzeptieren verschiedene Formate

✅ **Robuste Validierung**
- Alle Eingaben werden geprüft
- Ungültige Eingaben führen zu erneuter Abfrage
- Keine Programmabstürze durch falsche Eingaben

✅ **Formatierte Ausgabe**
- Strukturierte Darstellung mit Trennlinien
- Emojis für bessere Lesbarkeit
- Hervorhebung wichtiger Informationen

### Fehlerbehandlung
✅ Negative Beträge werden abgefangen
✅ Ungültige Stationsnamen werden erkannt
✅ Start = Ziel wird verhindert
✅ Nicht-numerische Eingaben bei Beträgen werden behandelt

---

## 💡 Design-Entscheidungen

### 1. Modulare Architektur
- **console_ui.py**: Komplett eigenständig für UI-Logik
- Keine Abhängigkeiten zu Geschäftslogik (außer UbahnNetz für Stationsdaten)
- Wiederverwendbare Methoden

### 2. Robuste Eingabevalidierung
- Alle Eingaben werden in Schleifen validiert
- Benutzerfreundliche Fehlermeldungen
- Keine Programmabstürze durch falsche Eingaben

### 3. Flexible Eingabemöglichkeiten
- Stationen per Nummer oder Name wählbar
- Case-insensitive Eingaben
- Komma und Punkt als Dezimaltrennzeichen

### 4. Klare Trennung von Verantwortlichkeiten
- ConsoleUI nur für Ein-/Ausgabe zuständig
- Keine Geschäftslogik in der UI
- Einfache Integration in bestehendes System

### 5. Benutzerfreundliche Ausgabe
- Emojis für visuelle Orientierung
- Trennlinien für Struktur
- Nummerierte Listen für einfache Auswahl

---

## 🚀 Verwendung

### Installation
Alle Dateien müssen im selben Verzeichnis liegen:
```
Sprint_3_Raum_3/
├── adjazenzliste.py
├── classe.py
├── service.py
├── ticket.py
├── console_ui.py      # NEU
└── main.py
```

### Integration in main.py
```python
from console_ui import ConsoleUI
from classe import UbahnNetz
from adjazenzliste import STATIONEN_REIHENFOLGE, STATIONEN

# Netz erstellen
netz = UbahnNetz(STATIONEN, STATIONEN_REIHENFOLGE)

# ConsoleUI initialisieren
ui = ConsoleUI(netz)

# Willkommensnachricht anzeigen
ui.display_welcome()

# Startstation wählen
start = ui.choose_start_station()

# Zielstation wählen
ziel = ui.choose_destination_station(start)

# Ja/Nein-Frage stellen
hat_sozialrabatt = ui.ask_yes_no("Haben Sie Anspruch auf Sozialrabatt?")

# Betrag erfragen
betrag = ui.ask_amount("Wie viel möchten Sie bezahlen?")

# Ticket-Info anzeigen
ticket_info = {
    "Start": start,
    "Ziel": ziel,
    "Preis": f"{betrag:.2f} €",
    "Sozialrabatt": "Ja" if hat_sozialrabatt else "Nein"
}
ui.display_ticket_info(ticket_info)
```

---

## 🧪 Test-Szenarien

### Szenario 1: Normale Stationswahl per Nummer
```
Eingabe: 1
Erwartung: Erste Station wird gewählt
```

### Szenario 2: Stationswahl per Name
```
Eingabe: hauptbahnhof
Erwartung: Station "HAUPTBAHNHOF" wird gewählt (case-insensitive)
```

### Szenario 3: Ungültige Stationsnummer
```
Eingabe: 999
Erwartung: Fehlermeldung + erneute Abfrage
```

### Szenario 4: Start = Ziel
```
Start: HAUPTBAHNHOF
Ziel: HAUPTBAHNHOF
Erwartung: Fehlermeldung + erneute Abfrage
```

### Szenario 5: Betrag mit Komma
```
Eingabe: 10,50
Erwartung: 10.5 (float)
```

### Szenario 6: Negativer Betrag
```
Eingabe: -5
Erwartung: Fehlermeldung + erneute Abfrage
```

### Szenario 7: Ja/Nein-Frage
```
Eingabe: j / ja / y / yes
Erwartung: True

Eingabe: n / nein / no
Erwartung: False

Eingabe: xyz
Erwartung: Fehlermeldung + erneute Abfrage
```

---

## 📊 Zusammenfassung der Änderungen

| Datei | Status | Änderungen |
|-------|--------|------------|
| `console_ui.py` | **NEU** | Komplette Konsolen-UI mit 7 Methoden |
| `adjazenzliste.py` | Unverändert | - |
| `classe.py` | Unverändert | - |
| `ticket.py` | Unverändert | - |
| `service.py` | Unverändert | - |
| `main.py` | Unverändert | - |

**Zeilen Code (neu)**: ~150 Zeilen
**Kommentare**: Umfassend mit Docstrings für alle Methoden
**Team-Kompatibilität**: ✅ Komplett eigenständiges Modul, keine Änderungen an bestehendem Code

---

## 🎓 Lernziele erfüllt

✅ Objektorientierte Programmierung (OOP)
✅ Eingabevalidierung und Fehlerbehandlung
✅ Benutzerfreundliche Konsolenausgabe
✅ Modularisierung und Trennung von Verantwortlichkeiten
✅ Type Hints für bessere Code-Qualität
✅ Docstrings für Dokumentation

---

## ✅ Checkliste

- [x] ConsoleUI-Klasse implementiert
- [x] ask_yes_no() mit Validierung
- [x] ask_amount() mit Komma/Punkt-Unterstützung
- [x] choose_start_station() mit Nummer/Name-Eingabe
- [x] choose_destination_station() mit Validierung
- [x] display_welcome() für Begrüßung
- [x] display_ticket_info() für Ticket-Anzeige
- [x] Robuste Fehlerbehandlung
- [x] Benutzerfreundliche Ausgabe
- [x] Code gut dokumentiert
- [x] Modular und wiederverwendbar

---

**Stand**: Sprint 4 - ConsoleUI
**Entwickler**: Team Sprint 4
**Datum**: 2026-02-13
