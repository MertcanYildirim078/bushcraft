pempakje = float(input('Vul de prijs van de pemmican pakje in: ')) #orgineel 3,45, in een reep zit er 4 pakjes
vijgen = float(input('Vul de prijs van de vijgenplakken in: ')) #1,24
scheep = float(input('Vul de prijs van de scheepbischuiten in: ')) #2,67
firesteel = float(input('Vul de prijs van de firesteel in: ')) #3,26
lucifer = float(input('Vul de prijs van de lucifers: ')) #0,21
vuursteen = float(input('Vul de prijs van de vuurstenen: ')) #2,23
sisaltouw = float(input('Vul de prijs van de sisaltouw in per 2 meter: '))#0,59
pemreep = pempakje * 4 
pemreepa = float(input('Vul de hoeveelheid in van Pemmican-repen: '))
vijgena = float(input('Vul de hoeveelheid in van vijgenplakken: '))
scheepa = float(input('Vul de hoeveelheid in van scheepsbischuiten: '))
firesteela = float(input('Vul de hoeveelheid in van firesteel: '))
lucifera = float(input('Vul de hoeveelheid in van lucifer: '))
vuursteena = float(input('Vul de hoeveelheid in van vuursteen: '))
sisaltouwa = float(input('Vul de hoeveelheid in van sisaltouw per 2 meter: '))

totaal = (pemreep * pemreepa) + (vijgen * vijgena) + (scheep * scheepa) + (firesteel * firesteela) + (lucifer * lucifera) + (vuursteen * vuursteena) + (sisaltouw * sisaltouwa)
print(totaal, 'euro. De prijs van alle materialen.')
#Opdracht 2 totale kosten: 114,25 euro 