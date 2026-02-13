# Sprint_2/service.py

from datetime import datetime, date
from classe import Fahrplan
from adjazenzliste import (
    UHRZEITEN_BETRIEB_LINIE_U1,
    STATIONEN_U1,
    STATIONEN_REIHENFOLGE,
    MAX_VERSUCHE
)
from ticket import erstelle_ticket, Ticketpreis


def eingabe_station(alle_stationen: list[str]) -> str | None:
    """Fordert Benutzereingabe für eine Station und validiert sie"""
    for _ in range(MAX_VERSUCHE):
        s = input(f"Haltestelle eingeben aus {alle_stationen}: ").strip().upper()
        if s in alle_stationen:
            return s
        print("Ungültige Haltestelle. Bitte eine gültige Station eingeben.")
    return None


def eingabe_zeit() -> str | None:
    """Fordert Benutzereingabe für eine Uhrzeit und validiert das Format"""
    for _ in range(MAX_VERSUCHE):
        t = input("Gewünschte Zeit eingeben (HH:MM), z.B. 05:08: ").strip()
        try:
            datetime.strptime(t, "%H:%M")
            return t
        except ValueError:
            print("Ungültiges Format. Bitte so eingeben: HH:MM (z.B. 08:07).")
    return None


def eingabe_ja_nein(frage: str) -> bool:
    """
    Stellt eine Ja/Nein-Frage und gibt True für Ja, False für Nein zurück
    
    Args:
        frage: Die zu stellende Frage
        
    Returns:
        True wenn Ja, False wenn Nein
    """
    while True:
        antwort = input(f"{frage} (j/n): ").strip().lower()
        if antwort in ['j', 'ja']:
            return True
        elif antwort in ['n', 'nein']:
            return False
        else:
            print("Bitte mit 'j' für Ja oder 'n' für Nein antworten.")


def erfasse_ticketdaten(anzahl_stationen: int) -> Ticketpreis:
    """
    Erfasst alle notwendigen Daten für die Ticketberechnung
    
    Args:
        anzahl_stationen: Anzahl der zu fahrenden Stationen
        
    Returns:
        Ticketpreis-Objekt mit allen erfassten Daten
    """
    print("\n" + "─" * 60)
    print("TICKET-OPTIONEN")
    print("─" * 60)
    
    # Ticketart erfragen
    print("\nTicketart:")
    print("  [1] Einzelticket (eine Fahrt)")
    print("  [2] Mehrfahrtenticket (4 Fahrten)")
    
    while True:
        wahl = input("\nIhre Wahl (1 oder 2): ").strip()
        if wahl == "1":
            ist_mehrfahrt = False
            break
        elif wahl == "2":
            ist_mehrfahrt = True
            break
        else:
            print("Ungültige Eingabe. Bitte 1 oder 2 wählen.")
    
    # Sozialrabatt erfragen
    print("\n" + "─" * 60)
    hat_sozialrabatt = eingabe_ja_nein(
        "Haben Sie Anspruch auf Sozialrabatt?\n"
        "(Schüler, Studenten, Rentner, Schwerbehinderte)"
    )
    
    # Zahlart erfragen
    print("\n" + "─" * 60)
    print("Zahlart:")
    print("  [1] Bargeldlos (EC-Karte, Kreditkarte, App)")
    print("  [2] Bar (Bargeld)")
    
    while True:
        wahl = input("\nIhre Wahl (1 oder 2): ").strip()
        if wahl == "1":
            ist_barzahlung = False
            break
        elif wahl == "2":
            ist_barzahlung = True
            break
        else:
            print("Ungültige Eingabe. Bitte 1 oder 2 wählen.")
    
    # Ticket erstellen
    return erstelle_ticket(
        anzahl_stationen=anzahl_stationen,
        ist_mehrfahrt=ist_mehrfahrt,
        ist_barzahlung=ist_barzahlung,
        hat_sozialrabatt=hat_sozialrabatt
    )


def zeige_preisaufschluesselung(ticket: Ticketpreis) -> None:
    """
    Zeigt eine detaillierte Aufschlüsselung des Ticketpreises an
    
    Args:
        ticket: Das Ticketpreis-Objekt
    """
    aufschluesselung = ticket.erstelle_preisaufschluesselung()
    
    print("\n" + "─" * 60)
    print("PREISBERECHNUNG")
    print("─" * 60)
    print(f"Ticket-Kategorie: {ticket.kategorie.value} ({ticket.anzahl_stationen} Stationen)")
    print(f"Basispreis: {aufschluesselung['basispreis']:.2f} €")
    
    # Zuschläge anzeigen
    if aufschluesselung['zuschlaege']:
        print("\nZuschläge:")
        for zuschlag in aufschluesselung['zuschlaege']:
            print(f"  + {zuschlag['beschreibung']}: {zuschlag['betrag']:.2f} €")
    
    # Rabatte anzeigen
    if aufschluesselung['rabatte']:
        print("\nRabatte:")
        for rabatt in aufschluesselung['rabatte']:
            print(f"  - {rabatt['beschreibung']}: {rabatt['betrag']:.2f} €")
    
    print("\n" + "=" * 60)
    print(f"ENDPREIS: {aufschluesselung['endpreis']:.2f} €")
    print("=" * 60)


def erstelle_fahrplan() -> Fahrplan:
    """Erstellt ein Fahrplan-Objekt mit den Daten der Linie U1"""
    heute = date.today()

    start = datetime.combine(
        heute,
        datetime.strptime(UHRZEITEN_BETRIEB_LINIE_U1["start"], "%H:%M").time()
    )

    ende = datetime.combine(
        heute,
        datetime.strptime(UHRZEITEN_BETRIEB_LINIE_U1["ende"], "%H:%M").time()
    )

    return Fahrplan(
        startzeit=start,
        endzeit=ende,
        intervall=int(UHRZEITEN_BETRIEB_LINIE_U1["intervall_minuten"]),
        stationen=STATIONEN_U1,
        stationen_reihenfolge=STATIONEN_REIHENFOLGE
    )
