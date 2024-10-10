# Pomóż nauczycielowi w przygotowaniu listy uczniów, którzy:
# Nie zdali egzaminu. Są to wszyscy uczniowie z oceną niedostateczny. Przypisz ich do zmiennej failed_students Zdali egzamin śpiewająco! Są to wszyscy uczniowie z oceną 'bardzo dobry'. Przypisz ich do zmiennej top_students Nauczyciel chciałby też znać imię najlepszego ucznia oraz liczbę punktów, jaką uzyskał podczas egzaminu. Zapisz tę informację w postaci krotki, której pierwszą wartością będzie imię ucznia, a drugą wartością będzie liczba punktów. Przypisz tę krotkę do zmiennej best_student.

# Skala ocen z egzaminu:
# 0 - 45 niedostateczny
# 46 - 60 dopuszczający
# 61 - 75 dostateczny
# 76 - 90 dobry
# 91 - 100 bardzo dobry

exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = [item for item in exam_points.items() if item[1] < 46]
top_students = [item for item in exam_points.items() if item[1] > 90]
best_student = ("",0)
print(failed_students)
print(top_students)

for item in exam_points.items():
  if item[1] > best_student[1]:
    best_student = item
print(best_student)