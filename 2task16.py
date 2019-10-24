# numbers = int(input("Введите числа: "))
# # numbers = numbers.split('')
# numbers = []

# print(numbers)

n = list(map(int, input("Введите числа: ").split()))
n.sort()
for i in list(n):
    if i % 2 == 0:
        print(i)
