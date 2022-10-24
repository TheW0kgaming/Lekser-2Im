from sang import Sang
import time
import random 

class Spilleliste:
	def __init__(self, listenavn):
		self._sanger = []
		self._navn = listenavn

	def  les_fra_fil(self, filnavn):
		# metoden åpner den oppgitte filen, og leser inn data om sanger – 
		# en linje per sang, på formatet tittel;artist 
		# en linje kan for eksempel leses slik:
		# alleData = linje.strip().split(';')

		artist_og_sang = open(filnavn, "r")

		Liste_av_sanger = artist_og_sang.readlines()

		for sang in Liste_av_sanger:
			sangRad = sang.rstrip("\n")

			splittedRad = sangRad.split(";")
			sang = Sang(splittedRad[1], splittedRad[0])

			self._sanger.append(sang)
		
		artist_og_sang.close()

	def legg_til_sang(self, nySang):

		self._sanger.append(nySang)

	def fjern_sang(self, sangnummer):

		if (sangnummer > 0 and sangnummer <= len(self._sanger)):
			self._sanger.pop(sangnummer-1)

	def se_alle_sanger(self):
		teller = 0
		for sang in self._sanger:
			teller += 1
			print(f"{teller}.{sang.tittel} - {sang.artist}")

	def spill_alle(self):
		# spiller hver enkelt sang i listen.
		
		for sang in self._sanger:
			sang.spill()
			time.sleep(1)
	
	def tilfeldig_sang(self):
		#gir tilfeldig sang

		tilfeldig = random.choice(self._sanger)
		tilfeldig.spill()

	def finn_sang(self, tittel): 
			# metoden sjekker om oppgitt tittel er den samme som i instansvariabelen 
			# og returnerer True ved likhet, ellers False. 
			# Titlene skal defineres som like uavhengig av små/ store bokstaver

		for sang in self._sanger:
			if sang.sjekk_tittel(tittel):
				sang.spill()

	def hent_artist_utvalg(self, artistnavn):
		#går gjennom alle sanger i spillelisten og returnerer en liste med 
		#sanger der artisten har et eller flere navn fra parameteren artistnavn.
		
		artist_liste = []

		for sang in self._sanger:
			if sang.sjekk_artist(artistnavn):
				artist_liste.append(sang.tittel)

		return artist_liste