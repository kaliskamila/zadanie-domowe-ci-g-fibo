wiek = int(input("Podaj mi swój wiek: "))
plec = input('Podaj płeć [K/M]:')
plec = plec[0].upper()
wiek_emerytalny = 60

wiek_emerytalny = 65
if plec =='K':
    wiek_emerytalny = 60

elif plec == "M":
    wiek_emerytalny = 65

else:
    wiek_emerytalny= 65

if 18 <= wiek < wiek_emerytalny:
     print('Musisz pracować') # instrukcja, komenda
     print('Taki may klimat')   #jeżeli w linii pojawia się dwukropek to nastepna linia musi rozpoczać się od wcięcia
elif wiek < 18:
    
    print("Ucz się młokosie")

elif wiek >= wiek_emerytalny:
    print("Grtulujemy emeryturty. -ZUS")


else:
    print('Nie musisz pracować, wiec ucz się i baluj') #mowi że jeżeli warunek w ifie nie niest dpełniony to drukuje ''

print('Po ifie.') # nie ma związku z if





wiek_emerytalny = 60 if plec == 'K' else 65


# niejawna konwersja do typu logicznego
lista = [] #jeżeli w liście będzie się coś pojawiać lista pusta
if lista:  # przeciwny warunek to if not
    pass # bez pass jest błąd składni

print(bool(lista)) #pusta lista to false, jak jest to true 
print(bool(''))
print(bool("Piotr"))

print(bool(0))
print(bool(0.000001)) # 0 będzie interpretowana jako false jakiekolwiek inne jako true

#operatory logiczne
#and
#or
#not
#and i or zwracają/spełniają pierwszą wartość spełniającą operację logiczną
#"kamila" or "Kalisz"
#'Kamila'

#"" or []
#[  ]  musi przejść przez wszystkie wartości które są spełnione więc i tka zwraca drugą wartość

# " " or [] or 0
#0
#wiek = input ("Podaj wiek") or 18
#18

#"Piotr" and "Banaszkiewicz"
#Banaszkiewicz

#"" and "Piotr"
#""

#"" and ""
#""

#"" and [] 
#[]

#"" and []
#[]


