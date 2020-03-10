imie = "Kamila" 
print("Na imię mam: " + imie)

f = 3.14
i = 1
c = 1 + 3j
L = True
imie = "Kamila"
  

 #zagnieżdżone listy
 nested = [
     [ 
         "Piotr",
    ],
     [
     "Max", "Karolina",
     ],
    [
     "Asia", "Kamila",
    ],
    [
     "Sabina", "Michał", "Grzesiek",
    ],
    [
    "Michał",
],
]

#przy scaleniu kody do mniejszj liczby linijek po przecinuku musi być spacja

print(nested)
print([-1])  #przez indeksacje dostajemy się do elementu w liście
print([-2][1]) #dostajemy się do całej ławki a potem do samego elementu
#len działa na listach, też na stringach
print(len(nested)) #licza ławek
print(len(nested[-2])) # liczba osób w przedostatniej ławce
print ( [nazwisko, tytul] ) #nazwisko to string
lista_wizytówka= [nazwisko, tytul]
pront(lista, wizytówka)
nazwisko= "Piotr Banaszkiewicz" #czytany od góry 

print(lista_wizytówka)


nested.append(["Rafał"]) #dodaje na końcu listy element Rafał ()?
print(nested)  

nested[-1].append( "Rafał")
print(nested) #Rafał siedzi będzie siedział w ostatniej ławce