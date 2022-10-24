class Sang:
		def __init__ (self, artist, tittel):
				self.artist = artist
				self.tittel = tittel
		
		def spill(self):
			# "spiller av" musikken i sangen den kalles for – 
			# i dette programmet betyr det at den skriver meldingen 
			# "Spiller <info om tittel og artist>" ut på terminalen
			print(f"Spiller {self.tittel} av {self.artist}")
	
		def sjekk_tittel(self, tittel):
			return tittel.lower() in self.tittel.lower()

		def sjekk_artist(self, artist):
		  	# metoden returnerer True dersom ett eller flere av navnene i strengen 
			# navn finnes i _artist, ellers False.
			return artist.lower() in self.artist.lower() 
	
		def sjekk_artist_og_tittel(self, artist, tittel):
		  # metoden returnerer True dersom både tittelen og artisten 
			# (samme regler som i sjekk-metodene) stemmer med sangens instansvariabler, 
			# ellers False.
			return self.tittet == tittel and self.artist == artist