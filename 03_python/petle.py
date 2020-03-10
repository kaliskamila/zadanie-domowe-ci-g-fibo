#służą do tego alby wykonywać operacje wielokrotnie
#do przechdzenia różnych typów danych 
#while
#index= 0

#while index < 10:
    #print(f"Hello World x{index}")
    #index += 1 # to samo co index=index+1

#for a la C++    
for i in range(0,10):
    print(f"Hello World x{i}")

#pętla for = umożliwia przejście przez element z danymi
#
#kolekcja="Kamila"
#for element in kolekcja: 
    #print(element)
    #do elementu są przypisane kolejne....wychodzi w pionie

 #kolekcja= ["Jakub", "Piotr", "Artur"]   
 #for element in kolekcja:
 #print(element)    -----wyświetlają się w pionie całe imiona

#for
#olekcja = {
     #"Linux: "Jakub",
     #"Web: "Piotr",
     #"Python: "Piotr",
     #"OOP: "Artur",

 #for klucz, wartość in kolekcja.items():
     #print(klucz, wartość)



lista = list(range(2, 21))
for element in lista:
    print (element, element**2, element**(1/2)),# zamiennie można liczba ** 0.5

lista = ["Adam", "Ewa", "Kain", "Abel"]
for index, element in enumerate(lista):
    print(index, element)
 
 # index mozna zamienić na klucz a element na wartość


 #znajdź wartość n-tego wyrazu ciągu fibbonaciego
 # 1 zmienne, które trzymają poprzednie wartości     ------for i in range():
 #pass        zamiana 
 # lista (.append()) 
 # 3. rekurencja     szukany =10 # F(10)
continue - ignoruje resztę treści przerywa wykonywanie pętli w danym przykładzie i przechodzi dalej
break


  


