#stringi
#listy
#Tuple - krotki(jedna krotka) - prawie lista , przetrzymuje, indeksacja od 0, 
#tupla jest niemutowalna 
T1 = ("Kamila ", "Kalisz")
print(T1)

#T2 = ("Kamila") nie jest jednoelementowa bo nie ma przecinka
#T2 = ("Karolina" "Kamila") bez przecinka łączy stringi i wychodzi KarolinaKamila

print(T3[0]) 
T3 = ("Ewa,
"Adam,"
")

print(len(T3)) #sprawdza długość tupli t3

#rozbijanie elementów na zmienne
T1 = ("Kamila", "Kalisz")
imie = T1[0]
nazwisko= T1[1]

imie, nazwisko = T1
print(imie,nazwisko)

#słownik/ typ mapujący, typ haszujący DICT - dictionary
#elementy w liście mogą być float mogą być tuple
D1={
    'klucz: wartość',
    123:' Student',
    (0, 0, 7): "Bond. James Bond"
}

print(D1)
print(D1["klucz"])
print(D1[123])
print(D1[( 0, 0, 7)])

print(list(D1.keys()[1]))
print(list(D1.values()[2]))
print("*" * 20)
print(list(D1.items())) #items - łączymy w pary klucz z wartością 

#Zbiór (set) - kolejny tyo danych
Z1 = {1, 2, 3, 2, 1, 4, ,2, 3, 5, 3}
#print - elementy się nie powtarzają 




