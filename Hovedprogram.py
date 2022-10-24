from spilleliste import Spilleliste
from sang import Sang
import os
import time

def bruker_valg():
    os.system("clear")
    print("1. Legg til ny sang?")
    print("2. vil du slette en sang?")
    print("3. Spill alle sanger?")
    print("4. Vil du spille en tilfeldig sang?")
    print("5. Vil du søke etter tittel?")
    print("6. Vil du søke etter Artist")
    try: 
        valg = int(input("Velg: "))
        return valg
    except:
        input("Skriv for å fortsette: ")
        return bruker_valg()

spillListe = Spilleliste("min-musikk-liste")
spillListe.les_fra_fil("musikk.txt")

valg = bruker_valg()


while valg < 99:
    os.system("clear")

    if valg == 1:
        artist = input("legg til artist?: ")
        sang_tittel = input("legg til tittel?: ")

        nySang = Sang(artist, sang_tittel)
        spillListe.legg_til_sang(nySang)

    elif valg == 2:
        try:
            spillListe.se_alle_sanger()
            sangnummer = int(input("Skriv Nummeret på sangen som skal slettes: ")) 
            
            if sangnummer > len(spillListe._sanger):
                print("Du skrev feil 🤓")
                input("skriv noe for å fortsette: ")
                bruker_valg()

            else:
                spillListe.fjern_sang(sangnummer)
                input("Sangen er slettet! skriv noe for å fortsette: ")
        except:
            print("Dette er ikke et nummer")
            input("Skriv noe: ")
        

    elif valg == 3:
        spillListe.spill_alle()
        input("skriv noe for å fortsette: ")
    
    elif valg == 4:
        spillListe.tilfeldig_sang()
        input("skriv noe for å fortsette: ")

    elif valg == 5:
        spillListe.se_alle_sanger()
        tittel = input("Hvilken sang leter du etter?: ")
        spillListe.finn_sang(tittel)
        
        input("skriv noe for å fortsette: ")
    
    elif valg == 6:
        spillListe.se_alle_sanger()
        artistnavn = input("Hvilken artist vil du søke etter?: ")
        
        tittler = spillListe.hent_artist_utvalg(artistnavn)
        if (len(tittler) == 0):
            print("Ingen sanger funnet")
        else:
            for t in tittler:
                print(t)
        input("skriv noe for å fortsette: ")
        
    elif valg < 99:
        bruker_valg()
    
    valg = bruker_valg()