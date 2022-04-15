print("Привет я калькулятор(вер2.0), я подрос! И наконец научился вычитать, умножать, делить а также всё ещё складывать два любых целых числа!")
operation = (input("Выберите операцию(+, - , * ,/): "))
number_1 = int(input("Введи первое целое число: "))
number_2 = int(input("Введи второе целое число: "))
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation ==  "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)


