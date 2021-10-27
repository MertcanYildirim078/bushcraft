afstand = 488 #km
liter = 12 #km
dieselprijs = float(input('voer de dieselprijs in: '))
persoonk = 8
afstandkosten = afstand / liter

totaal = (afstandkosten * dieselprijs) + (persoonk * 5) * 2
print(totaal, 'euro. De kosten voor de heen en weer reis.')