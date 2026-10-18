"""
EINSTELLUNGEN - hier änderst du Texte, Farben, Zeiten und Namen.
Nach jeder Änderung den Bot neu starten. Kein Discord-Wissen nötig.
"""

# ---------- Aussehen ----------
FOOTER = "Landespolizei Berlin"  # steht unter JEDEM Embed
BLAU, GRUEN, ORANGE, ROT = 0x2B5BFF, 0x5BFF3A, 0xF5A623, 0xE5301F

# ---------- Zeiten & Limits ----------
ANWALT_COOLDOWN_MIN = 15            # Minuten zwischen zwei Anwalt-Rufen pro Person
ANWALT_WORT = "anwalt"              # Wort im Anwalt-Kanal (klein geschrieben)
AUSWEIS_COOLDOWN_SEK = 20           # Sperre gegen Spam beim "Ausweis vorzeigen"
DIENST_MAX_STUNDEN = 12             # danach wird ein vergessener Dienst automatisch beendet
TEAMLISTE_INTERVALL_MIN = 5         # so oft aktualisiert sich die Teamliste
LAUFZEIT_TAGE_STANDARD = 7          # Disziplinarmaßnahme läuft nach X Tagen ab
BEWERBUNGSSPERRE_TAGE_STANDARD = 7
PLATZVERWEIS_DAUER_STANDARD = "24 Stunden"
AKTENZEICHEN_LAENGE = 6

# ---------- Fahndung: Gefahrenstufen ----------
STUFEN = {
    "niedrig": ("🟡 Niedrig", ORANGE),
    "mittel": ("🟠 Mittel", ORANGE),
    "hoch": ("🔴 Hoch (gefährlich/bewaffnet)", ROT),
}

# ---------- Was man mit /setup einstellen kann ----------
KANAELE = {
    "personal": "Personal-Log (Einstellung, Uprank, Entlassung)",
    "disziplin": "Disziplin-Log",
    "bewerbung": "Bewerbungssperren-Log",
    "ausweis_pruefung": "Ausweis-Prüfung (Anträge)",
    "fahndung": "Fahndungen",
    "dienst": "Dienst-Log (Dienstzeiten)",
}
ROLLEN = {
    "direktion": "Direktion (darf alle Personal-Befehle)",
    "polizei": "Polizei (Aktivitätscheck, Dienst)",
    "pflichtverteidiger": "Pflichtverteidiger (Anwalt-Ping)",
    "ausweis_team": "Ausweis-Team (Anträge prüfen)",
    "imdienst": "Im-Dienst-Rolle (wird automatisch vergeben)",
}
AUTO_EREIGNISSE = {
    "personal": "Personal-Aktionen (Einstellung, Uprank, Entlassung …)",
    "disziplin": "Disziplinarmaßnahmen",
    "bewerbung": "Bewerbungssperren",
    "fahndung": "Fahndungen",
    "dienst": "Dienstzeiten",
}

# ---------- Texte der Panels: (Titel, Text) ----------
# {platzhalter} nicht löschen, sie werden vom Bot ersetzt.
TEXTE = {
    "anwalt": ("👔 Anwalt benötigt?",
               "Drücke den Button **Anwalt rufen** oder schreibe das Wort **\"Anwalt\"** in diesen Kanal, "
               "um die Rolle {rolle} zu alarmieren und einen Anwalt anzufordern.\n\n"
               "*Pro Nutzer ist dies nur alle {minuten} Minuten möglich.*"),
    "platzverweis": ("🚧 Platzverweis ausstellen",
                     "Betätige den Button, um einen Platzverweis für eine Person zu erfassen. "
                     "Die Angaben werden anschließend automatisch in diesem Kanal veröffentlicht."),
    "ausweis": ("🪪 Ausweis-Center",
                "**Ausweis beantragen** – dein Antrag wird vom Team geprüft.\n"
                "**Ausweis vorzeigen** – zeigt deinen Ausweis hier im Kanal."),
    "dienst": ("🚓 Dienstpanel",
               "Nutze die Buttons, um deinen Dienst zu **beginnen**, zu **pausieren** oder zu **beenden**."),
    "aktivitaet": ("📢 Aktivitätscheck",
                   "Bitte bestätigt mit dem Button **Aktivität bestätigen** eure Aktivität.\n\n"
                   "⏳ **Frist:** {frist}\n\n"
                   "⚠️ Wer bis dahin nicht bestätigt hat, erhält automatisch eine DAB-Warnung."),
    "fahndung_panel": ("🚨 Fahndungszentrale",
                       "Hier kannst du eine Fahndung **ausschreiben** oder alle **aktiven Fahndungen** ansehen."),
}
