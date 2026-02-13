# Sprint_2/main.py

from datetime import datetime
from service import (
    erstelle_fahrplan, 
    eingabe_zeit, 
    erfasse_ticketdaten,
    zeige_preisaufschluesselung
)

if __name__ == "__main__":
    # Fahrplan initialisieren
    fahrplan = erstelle_fahrplan()

    # Begrüßung
    print("=" * 60)
    print("Willkommen zum Fahrplan der U-Bahn Linie U1!")
    print("Langwasser Süd ↔ Fürth Hbf")
    print("=" * 60)

    # =========================================================================
    # SCHRITT 1: STARTSTATION ERFASSEN
    # =========================================================================
    start = None
    while not start:
        start = input("\nGeben Sie die Starthaltestelle ein: ").strip().upper()
        if start not in fahrplan.stationen_reihenfolge:
            print("❌ Ungültige Haltestelle. Bitte versuchen Sie es erneut.")
            start = None

    # =========================================================================
    # SCHRITT 2: ZIELSTATION ERFASSEN
    # =========================================================================
    ziel = None
    while not ziel:
        ziel = input("Geben Sie die Zielhaltestelle ein: ").strip().upper()
        if ziel not in fahrplan.stationen_reihenfolge:
            print("❌ Ungültige Haltestelle. Bitte versuchen Sie es erneut.")
            ziel = None
        elif start == ziel:
            print("❌ Start und Ziel sind identisch. Bitte wählen Sie unterschiedliche Stationen.")
            ziel = None

    # =========================================================================
    # SCHRITT 3: GEWÜNSCHTE ABFAHRTSZEIT ERFASSEN
    # =========================================================================
    gewuenscht = eingabe_zeit()
    if not gewuenscht:
        print("\n❌ Ungültige Zeiteingabe. Programm wird beendet.")
        exit()

    # =========================================================================
    # SCHRITT 4: NÄCHSTE ABFAHRT BERECHNEN
    # Berechnet die nächstmögliche Abfahrt nach der gewünschten Zeit
    # =========================================================================
    abfahrt = fahrplan.naechste_abfahrt(start, ziel, gewuenscht)

    if not abfahrt:
        print("\n❌ Keine Verbindung gefunden (außerhalb der Betriebszeiten).")
        print("=" * 60)
        exit()

    # =========================================================================
    # SCHRITT 5: REISEDATEN BERECHNEN
    # - Weg zwischen Start und Ziel ermitteln
    # - Anzahl der Stationen zählen
    # - Reisedauer berechnen
    # - Ankunftszeit ermitteln
    # =========================================================================
    weg = fahrplan.finde_linear_weg(start, ziel)
    anzahl_stationen = len(weg) - 1  # Anzahl Stationen = Anzahl Verbindungen
    reisedauer = fahrplan.berechne_reisezeit(weg)
    ankunft = abfahrt + reisedauer

    # =========================================================================
    # SCHRITT 6: TICKETDATEN ERFASSEN
    # Fragt den Benutzer nach:
    # - Ticketart (Einzel oder Mehrfahrt)
    # - Sozialrabatt-Berechtigung
    # - Zahlart (Bar oder bargeldlos)
    # =========================================================================
    ticket = erfasse_ticketdaten(anzahl_stationen)

    # =========================================================================
    # SCHRITT 7: PREISBERECHNUNG ANZEIGEN
    # Zeigt detaillierte Aufschlüsselung des Ticketpreises
    # =========================================================================
    zeige_preisaufschluesselung(ticket)

    # =========================================================================
    # SCHRITT 8: REISEZUSAMMENFASSUNG AUSGEBEN
    # Vollständige Übersicht über die Reise mit allen relevanten Daten
    # =========================================================================
    print("\n" + "=" * 60)
    print("REISEZUSAMMENFASSUNG")
    print("=" * 60)
    print(f"Von:              {start}")
    print(f"Nach:             {ziel}")
    print(f"Stationen:        {anzahl_stationen}")
    print(f"─" * 60)
    print(f"Abfahrt:          {abfahrt.strftime('%H:%M')} Uhr")
    print(f"Ankunft:          {ankunft.strftime('%H:%M')} Uhr")
    print(f"Reisedauer:       {int(reisedauer.total_seconds() // 60)} Minuten")
    print(f"─" * 60)
    print(f"Ticket:           {ticket.kategorie.value}")
    print(f"Art:              {ticket.art.value}")
    print(f"Zahlart:          {ticket.zahlart.value}")
    print(f"Sozialrabatt:     {'Ja' if ticket.hat_sozialrabatt else 'Nein'}")
    print(f"─" * 60)
    print(f"GESAMTPREIS:      {ticket.berechne_endpreis():.2f} €")
    print("=" * 60)
    
    # =========================================================================
    # SCHRITT 9: ZEITSTEMPEL DER BERATUNG
    # Dokumentiert, wann diese Fahrplanauskunft erstellt wurde
    # =========================================================================
    zeitstempel = datetime.now()
    print(f"\nBeratung durchgeführt am: {zeitstempel.strftime('%d.%m.%Y um %H:%M:%S Uhr')}")
    print("=" * 60)
    print("\nGute Fahrt! 🚇")
