# Sprint 3: Ticket-Bauerservice - Implementierungsdokumentation

## 📖 Übersicht

Dieses Erweitering implementiert ein vollständiges Basissystem für die U-Bahn Linie U3 gemäß dem SPRINTS_BACKLOG.md (Über Story 3.3).

## 🎯 Neue Dateien

### 📝 Key: `ticket.py` (Ticket Bauerservice (NEW))

**Ziel**: Zentrale Klasse für alle Ticket-bezogenen Berechnungen

**Hauptkomponente**:

- **Ticketkategorie**: KURZ (1-3 Stationen), MITTEL (4-8 Stationen), LANG (9+ Stationen)
- **Ticketart**: EINZEL, MEHRFART (6 Fahrten)
- **Rabatt**: BAR, ERMÄSSIGUNG
- **hat_sozialrabatt**: Boolean für Sozialrabatt-Berechtigung
- **anzahl_stationen**: Anzahl der zu fahrenden Stationen

**Beispielwert (gemäß Spezifikation)**:

- **Einzelticket**: kurz 1,50 € | Mittel 2,00 € | Lang 3,00 €
- **Mehrfahrtticket**: kurz 5,00 € | Mittel 7,00 € | Lang 10,00 €

---

## 📂 Projektstruktur

```
Sprint_3_Raum_3/
├── README.md                 # Diese Datei
├── adjazenzliste.py         # U-Bahn Netz Datenstruktur
├── classe.py                # Hauptklassen (Station, Route, RouteFinder, UbahnNetz)
├── ticket.py                # Ticket-Berechnungslogik
├── service.py               # Service-Klassen
├── console_ui.py            # Konsolen-Benutzeroberfläche
├── main.py                  # Hauptprogramm
├── test_ticket.py           # Unit-Tests
└── .gitignore              # Git-Ignore-Datei
```

---

## 🚀 Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/IhrUsername/Sprint_3_Raum_3.git
   cd Sprint_3_Raum_3
   ```

2. **Python-Version:** Python 3.8 oder höher erforderlich

3. **Keine externen Abhängigkeiten** - verwendet nur Python Standard-Bibliothek

---

## 💻 Verwendung

### Programm starten:

```bash
python main.py
```

### Beispiel-Ablauf:

1. Wählen Sie die Startstation
2. Wählen Sie die Zielstation
3. Wählen Sie die Ticketart (Einzel/Mehrfart)
4. Geben Sie an, ob Sie Sozialrabatt haben
5. Wählen Sie die Zahlungsart (Bar/Karte)
6. Erhalten Sie Ihr Ticket mit Preis

---

## 🧪 Tests ausführen

```bash
python test_ticket.py
```

---

## 📋 Features

✅ Automatische Routenberechnung zwischen Stationen  
✅ Dynamische Preisberechnung basierend auf:
  - Anzahl der Stationen
  - Ticketart (Einzel/Mehrfart)
  - Sozialrabatt (20%)
  - Zahlungsart (Bar: +15% Zuschlag)  
✅ Benutzerfreundliche Konsolen-UI  
✅ Robuste Eingabevalidierung  
✅ Unit-Tests für Kernfunktionalität

---

## 🛠️ Technische Details

### Ticketkategorien:
- **KURZ**: 1-3 Stationen
- **MITTEL**: 4-8 Stationen  
- **LANG**: 9+ Stationen

### Preisberechnung:
```
Endpreis = Basispreis 
         + Zuschlag Ticketart (10% für Einzelticket)
         - Sozialrabatt (20%)
         + Barzahlungszuschlag (15%)
```

---

## 👥 Mitwirkende

- **Sven-Luka** - Entwicklung und Implementierung

---

## 📄 Lizenz

Dieses Projekt ist für Bildungszwecke erstellt.

---

## 📞 Kontakt

Bei Fragen oder Problemen öffnen Sie bitte ein Issue auf GitHub.
