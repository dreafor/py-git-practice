from calculator import Calculator

print("Проверка калькулятора")

print("Сложение:", Calculator.add(10, 5))
print("Вычитание:", Calculator.subtract(10, 5))
print("Умножение:", Calculator.multiply(10, 5))
print("Деление:", Calculator.divide(10, 5))

try:
    Calculator.divide(10, 0)
except ZeroDivisionError as error:
    print("Проверка деления на ноль:", error)

print("Все проверки выполнены")
