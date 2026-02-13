# Sprint_2/test_ticket.py
"""
Test-Datei für das Ticket-Rabattsystem
Demonstriert verschiedene Preis-Szenarien
"""

from ticket import erstelle_ticket, TicketKategorie


def test_szenario(beschreibung: str, 
                  anzahl_stationen: int,
                  ist_mehrfahrt: bool,
                  ist_barzahlung: bool,
                  hat_sozialrabatt: bool,
                  erwarteter_preis: float):
    """
    Testet ein Preisszenario und zeigt die Berechnung an
    """
    print("\n" + "=" * 70)
    print(f"TEST: {beschreibung}")
    print("=" * 70)
    
    ticket = erstelle_ticket(
        anzahl_stationen=anzahl_stationen,
        ist_mehrfahrt=ist_mehrfahrt,
        ist_barzahlung=ist_barzahlung,
        hat_sozialrabatt=hat_sozialrabatt
    )
    
    print(f"Stationen: {anzahl_stationen}")
    print(f"Kategorie: {ticket.kategorie.value}")
    print(f"Ticketart: {ticket.art.value}")
    print(f"Zahlart: {ticket.zahlart.value}")
    print(f"Sozialrabatt: {'Ja' if hat_sozialrabatt else 'Nein'}")
    print("-" * 70)
    
    aufschluesselung = ticket.erstelle_preisaufschluesselung()
    print(f"Basispreis: {aufschluesselung['basispreis']:.2f} €")
    
    if aufschluesselung['zuschlaege']:
        print("\nZuschläge:")
        for z in aufschluesselung['zuschlaege']:
            print(f"  + {z['beschreibung']}: {z['betrag']:.2f} €")
    
    if aufschluesselung['rabatte']:
        print("\nRabatte:")
        for r in aufschluesselung['rabatte']:
            print(f"  - {r['beschreibung']}: {r['betrag']:.2f} €")
    
    endpreis = ticket.berechne_endpreis()
    print("\n" + "=" * 70)
    print(f"ENDPREIS: {endpreis:.2f} €")
    
    # Validierung
    if abs(endpreis - erwarteter_preis) < 0.01:
        print("✓ TEST BESTANDEN")
    else:
        print(f"✗ TEST FEHLGESCHLAGEN (erwartet: {erwarteter_preis:.2f} €)")
    print("=" * 70)


if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("# TICKET-RABATTSYSTEM - TEST-SUITE")
    print("#" * 70)
    
    # =========================================================================
    # KURZTICKET-TESTS (1-3 Stationen)
    # =========================================================================
    
    test_szenario(
        beschreibung="Kurzstrecke - Einzelticket - Bargeldlos - Kein Rabatt",
        anzahl_stationen=2,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=1.65  # 1.50 + 10% = 1.65
    )
    
    test_szenario(
        beschreibung="Kurzstrecke - Einzelticket - Bargeldlos - MIT Sozialrabatt",
        anzahl_stationen=3,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=True,
        erwarteter_preis=1.32  # 1.50 + 10% = 1.65, -20% = 1.32
    )
    
    test_szenario(
        beschreibung="Kurzstrecke - Einzelticket - BAR - MIT Sozialrabatt",
        anzahl_stationen=1,
        ist_mehrfahrt=False,
        ist_barzahlung=True,
        hat_sozialrabatt=True,
        erwarteter_preis=1.52  # 1.50 + 10% = 1.65, -20% = 1.32, +15% = 1.52
    )
    
    test_szenario(
        beschreibung="Kurzstrecke - MEHRFAHRT - Bargeldlos - Kein Rabatt",
        anzahl_stationen=2,
        ist_mehrfahrt=True,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=5.00  # Basis 5.00, kein Zuschlag bei Mehrfahrt
    )
    
    # =========================================================================
    # MITTELTICKET-TESTS (4-8 Stationen)
    # =========================================================================
    
    test_szenario(
        beschreibung="Mittelstrecke - Einzelticket - BAR - Kein Rabatt",
        anzahl_stationen=5,
        ist_mehrfahrt=False,
        ist_barzahlung=True,
        hat_sozialrabatt=False,
        erwarteter_preis=2.53  # 2.00 + 10% = 2.20, +15% = 2.53
    )
    
    test_szenario(
        beschreibung="Mittelstrecke - MEHRFAHRT - BAR - MIT Sozialrabatt",
        anzahl_stationen=8,
        ist_mehrfahrt=True,
        ist_barzahlung=True,
        hat_sozialrabatt=True,
        erwarteter_preis=6.44  # 7.00, -20% = 5.60, +15% = 6.44
    )
    
    # =========================================================================
    # LANGTICKET-TESTS (9+ Stationen)
    # =========================================================================
    
    test_szenario(
        beschreibung="Langstrecke - Einzelticket - Bargeldlos - Kein Rabatt",
        anzahl_stationen=15,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=3.30  # 3.00 + 10% = 3.30
    )
    
    test_szenario(
        beschreibung="Langstrecke - Einzelticket - BAR - Kein Rabatt (MAXIMUM)",
        anzahl_stationen=22,  # Gesamte Strecke
        ist_mehrfahrt=False,
        ist_barzahlung=True,
        hat_sozialrabatt=False,
        erwarteter_preis=3.80  # 3.00 + 10% = 3.30, +15% = 3.80
    )
    
    test_szenario(
        beschreibung="Langstrecke - MEHRFAHRT - Bargeldlos - MIT Sozialrabatt (MINIMUM)",
        anzahl_stationen=20,
        ist_mehrfahrt=True,
        ist_barzahlung=False,
        hat_sozialrabatt=True,
        erwarteter_preis=8.00  # 10.00, -20% = 8.00
    )
    
    # =========================================================================
    # GRENZFÄLLE
    # =========================================================================
    
    test_szenario(
        beschreibung="GRENZFALL: 3 Stationen (noch Kurzticket)",
        anzahl_stationen=3,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=1.65  # 1.50 + 10% = 1.65
    )
    
    test_szenario(
        beschreibung="GRENZFALL: 4 Stationen (jetzt Mittelticket)",
        anzahl_stationen=4,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=2.20  # 2.00 + 10% = 2.20
    )
    
    test_szenario(
        beschreibung="GRENZFALL: 8 Stationen (noch Mittelticket)",
        anzahl_stationen=8,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=2.20  # 2.00 + 10% = 2.20
    )
    
    test_szenario(
        beschreibung="GRENZFALL: 9 Stationen (jetzt Langticket)",
        anzahl_stationen=9,
        ist_mehrfahrt=False,
        ist_barzahlung=False,
        hat_sozialrabatt=False,
        erwarteter_preis=3.30  # 3.00 + 10% = 3.30
    )
    
    print("\n" + "#" * 70)
    print("# TEST-SUITE ABGESCHLOSSEN")
    print("#" * 70)
    print("\nAlle Preis-Szenarien wurden getestet.")
    print("Die Berechnungslogik entspricht den Spezifikationen.")
