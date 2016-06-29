# sashnat. Functions and recursion / Функции и рекурсия
# «Возведение в степень» / "Exponentiation"
# Дано действительное положительное число a и целое неотрицательное число n. 
# Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
# а используя рекуррентное соотношение an=a⋅an-1.

# Решение оформите в виде функции power(a, n).

a = float(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(a, n))
