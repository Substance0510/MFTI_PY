# Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел
#(не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
#Числа, следующие за числом 0, считывать не нужно.
# Формат входных данных:
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
# Формат выходных данных:
# Выведите ответ на задачу (одно число).
k = None
nums = []
result = 0
#count = 0 #для альтернативного варианта подсчёта.
while True:
    k = int(input())
    if k == 0:
        break
    elif result <= k:
        result = k
        nums.append(k)
print(nums.count(result))

#Альтернативный вариант подсчёта результата:
# for i in nums:
#     if i == result:
#         count += 1
# print(count)