#databases, sose 2017
#agnes voisard
#tutorium nina kubiessa
#assignment 6, aufgabe 4
#eike sommer thomas sieron

"""
4 a)


Ergebnis des Webscrapers: ein leeres File "greyhound-data.csv" und eine Fehlermeldungen zu fehlgeschlagenen Webverbindungen.

Der Scraper versucht, die Tabellen mit den Statistiken und Eltern der 100 besten Greyhounds (Windhunde?, Rennhunde?) für die Jahre von 2000 bis 2016 für die vier Länder USA; Australien, Irland und Großbritannien zu speichern.
Zeilenweise als csv, Trennung mit ';', Voranstehend (am Beginn der csv-Zeile) der Text mit Landesnamen und Jahr



4 b)
Quelltext siehe unten, die laut scraper drei häufigsten Wörter lauten:

HTTPS (kommt 23 Mal vor)

und (kommt 15 Mal vor)

für (kommt 13 Mal vor)

(siehe xterm-Ausgabetext als Kommentar ganz unten)

"""

# imports
from bs4 import BeautifulSoup
import requests
import csv

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: https://www.heise.de/thema/https
def scrape():

	fobj = open("heise-https.csv", "w")      # open file
	csvw = csv.writer(fobj, delimiter = ";")      # create csv writer, set delimiter to ;
	heise_url="https://www.heise.de/thema/https"
	soup = getPage(heise_url)
	a_tags= soup.find_all("a")
	i=1
	for tag in a_tags:
		try:		
			txt = a_tags[i].find("header")
			csvw.writerow(txt)
		except:
			print("scrape...")
		i=i+1
	
	j=1	
	while j<4:
		heise_url = "https://www.heise.de/thema/https?seite="+str(j)		
		soup = getPage(heise_url)
		a_tags= soup.find_all("a")
		i=1
		for tag in a_tags:
			try:		
				txt = a_tags[i].find("header")
				csvw.writerow(txt)
			except:
				print("scrape...")
			i=i+1
		j=j+1

	
	fobj.close()                                # close file
	print("\nHeisedaten scraped.\n")


def eintragen (wortliste3, wortliste):
	i=len(wortliste)
	wortliste2=[]
	wortindex=[1]
	gef=False
	k=0
	while k<i:
		hilfswort=wortliste[k]
		if (len(hilfswort) > 1):
			wortliste2.append(hilfswort)
		k=k+1
	wortliste3[0]=wortliste2[0]
	i=len(wortliste2)
	k=1
	l=1
	while k<i:
		k2=0
		while k2<len(wortliste3):
			if wortliste2[k]==wortliste3[k2]:
				wortindex[k2]=wortindex[k2]+1
				gef=True
			k2=k2+1
		if gef==False:
			wortliste3.append(wortliste2[k])
			wortindex.append(1)
		gef=False
		k=k+1
	#print(wortliste2)
	#print(len(wortliste))
	#print(len(wortliste2))
	wortbuch=[]
	eintrag=[]
	i=0
	while i<(len(wortindex)):
		eintrag.append(wortliste3[i])
		eintrag.append(wortindex[i])
		wortbuch.append(eintrag)
		eintrag=[]
		i=i+1
	#print(len(wortbuch))
	#print(wortindex)	
	return(wortbuch,wortliste3,wortindex)


def parsen(inhalt, wortliste):
	i=0
	while (i<(len(inhalt))):
		wort=""
		x=0
		zeile=inhalt[i]
		j=len(zeile)		
		while x<j:
			a=zeile[x]
			if a == " ":
				#print(wort)
				wortliste.append(wort)
				wort=""
			else:
				wort=wort+str(a)
			x=x+1
		if x==j:
			#print(wort)
			wortliste.append(wort)
			wort=""
		i=i+1
	return wortliste


def check():
	fobj = open("heise-https.csv", "r")
	csvr = csv.reader(fobj, delimiter = ";")
	inhalt=[]
	wortliste=[]
	k=0
	wortliste3 = ["platzini"]
	wortindex = [1]
	for row in csvr:
			artikel=row[0]
			#print(artikel)
			#print(type(artikel))
			if artikel[0]!="<":
				inhalt.append(artikel)
	fobj.close() 			# close file
	print("Worte parsen...\n")
	wortbuch=[]                          	
	wortliste=parsen(inhalt,wortliste)
	(wortbuch,wortliste3,wortindex)=eintragen(wortliste3,wortliste)
	#print(wortbuch)
	i=500
	while i>5:
		j=0
		while (j<len(wortliste3)):
			if wortindex[j]==i:
				print(wortliste3[j]+" kommt "+str(i)+" Mal vor.\n")
			j=j+1
		i=i-1 
	print("\nHeisedaten parsed.\n")

 
			

	
# main program
scrape()
check()

"""
Heisedaten scraped.

Worte parsen...

HTTPS kommt 23 Mal vor.

und kommt 15 Mal vor.

für kommt 13 Mal vor.

bei kommt 12 Mal vor.

mit kommt 11 Mal vor.

von kommt 9 Mal vor.

auf kommt 9 Mal vor.

heise kommt 8 Mal vor.

Let's kommt 7 Mal vor.

als kommt 7 Mal vor.

will kommt 6 Mal vor.

online kommt 6 Mal vor.

Verschlüsselung kommt 6 Mal vor.


Heisedaten parsed.

"""
