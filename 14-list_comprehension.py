# ============One ===============

my_list = [ 1, 3, 5, 7, 9]
squares = []
for i in my_list:
  squares.append(i * i)
print(squares)

squares2 = [i*i for i in my_list]
print(squares2)
print(type(squares2))

# ========= Two ==================
my_list = [0, 1, 4, 5, 6, 0, 3, 7]
bezer = []
for item in my_list:
  if item != 0:
    bezer.append(item)
print(bezer)

my_list = [0, 1, 4, 5, 6, 0, 3, 7]
bezer = [item for item in my_list if item != 0]
print(bezer)

# ============ Three ============================
#Zakoduj listę składaną, która tworzy nową listę z liczbami długość słów (obliczysz je funkcją len). Oto lista do przerobienia: ['Arystoteles','Platon','Sokrates']
philosopher = ['Arystoteles','Platon','Sokrates']
length = [len(item) for item in philosopher]
print(length)