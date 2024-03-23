print("Hello world")
print("World hello")

my_people_list = [
  {
    "name": "Przemex",
    "age": 19
  },
  {
    "name": "Another Name",
    "age": 65
  }
]

print(my_people_list[0]["name"])


my_tuple = ("apple", "banana", "cherry")
first_item = my_tuple[0]

my_set = {"apple", "banana", "cherry"}
exists = "banana" in my_set 

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)

text = "Hello World!"
size = len(text)

text_1 = "Hello"
text_2 = " "
text_3 = "World"

print(text[-1]) # wykrzyknik

print(text[1:5]) # ello

print(text[0:12:2]) # skok co drugą literę

print(text[:8]) # od zera do wskazanej

print(text[2:]) # od wskazanej do końca

print(text[::2]) # od zera do końca co drugi znak

print(text[:size//2]) # Hello - pierwsza połowa
print(text[size//2:]) # world! - druga połowa

scores = [90, 80, 70, 60, 50]
print(scores[:4]) # pokaż 4 zmienne zaczynając od przodu
print(len(scores)) # ilość -> 5 zmiennych na liście
print(70 in scores) # True
print(42 in scores) # False

print(scores + [10, 20]) # jedna lista + druga lista i tworzy się trzecia lista

# METODY

scores.append(40) #dodaj 40 do listy scores) (na końcu)
scores.clear # wyczyści xD
new_scores = scores.copy # kopiuje
scores.remove(70) # usuwa element (wyskoczy błąd jeśli usuwanego elementu nie będzie)
scores.insert(1, 100) # dodaj element na wskazane miejsce UWAGA insert jest mniej wydajne niż append
print(scores.count(90)) # ile razy pojawia się element
print(scores.index(90)) # na której pozycji znajduje się element (wyskoczy błąd jeśli szukanego elementu nie będzie)
# print(scores.extend[40, 30, 20, 10]) # od append różni się tym że można przekazać tylko kolekcje

#SŁOWNIKI
#w słowniku kluczem może być wszystko co niezmienialne

