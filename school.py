# Робота з відеоуроку номер 1
import random
spysok = []
for nomer in range(10):
    spysok.append(random.randint(1, 100))
    spysok.append(k)
print(spysok)
parni = 0
for nomer in range(10):
    if spysok[nomer] % 2 == 0:
        parni += 1
    print("Парні",parni)
# Робота з відеоуроку номер 2
for nomer in range(10):
    if spysok[nomer]>0:
        print(spysok[nomer], end=" ")
# Дороблена задача номер 3
heights = [170, 160, 180, 150, 165, 175, 155]
heights.sort()
print("Список за зростанням:", heights)
average_height = sum(heights) / len(heights)
print("Середній зріст учнів:", round(average_height, 2))
greater_than_average = [height for height in heights if height > average_height]
print("Зріст, більший за середній:", greater_than_average)
print("Кількість учнів зі зростом більшим за середній:", len(greater_than_average))