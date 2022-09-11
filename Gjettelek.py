# Denne filen starter programmet, og kommuniserer med brukeren
import time
import os

start_nytt_spill = True
highscore = 0

while start_nytt_spill == True:
    start_spill = input(f"Vil du spille en gjettelek? Din highscore = {highscore} j/n: ")
    if start_spill == "n":
        print("Hadet :)")

        time.sleep(3)
        os.system('clear')
        break

    else:

        time.sleep(1)
        print("Loading.")

        time.sleep(1)
        print("Loading..")
            
        time.sleep(1)
        print("Loading...")

        time.sleep(3)

        tid = str(time.time())

        bakerste_tall = int(tid[len(tid)-1])

        bruker_tall = int(input("Hvilket tall tror du datamaskinene har valgt?: "))
            
        while bruker_tall != bakerste_tall:

            if bruker_tall > bakerste_tall:
                print("Det er lavere enn du skrev! Du skrev ", bruker_tall,"!")

                bruker_tall = int(input("Hvilket tall tror du datamaskinene har valgt?: "))
            else:
                print("Det er større enn du skrev! du skrev ", bruker_tall,"!")
                
                bruker_tall = int(input("Hvilket tall tror du datamaskinene har valgt?: "))
                
        if bruker_tall == bakerste_tall:
            riktig = print("Du gjettet riktig tall! :) tallet er ",bakerste_tall,"!" )
            prov_igjen = str(input("Vil du prøve igjen?: j/n "))
            
            if prov_igjen == "j":
                start_nytt_spill == True
                os.system('clear')
                highscore = highscore + 1

            elif prov_igjen == "n":
                print("Hadet :)!")
                time.sleep(3)
                os.system('clear')
                break
            