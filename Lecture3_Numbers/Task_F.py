# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести
# количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.
# Формат входных данных:
# Во входных данных вводится последовательность целых чисел (каждое на новой строке), оканчивающаяся числом 0. Число 0 в последовательность не входит.#
# Формат выходных данных:
# Вывести длину последовательности.
nums = []
k = None
while k != 0:
    k = int(input())
    nums.append(k)
print(len(nums) - 1)