number1 = int(input('Введите 1 число: '))
number2 = int(input('Введите 2 число: '))
if number1%number2 == 0:
    print("%d делится на %d" % (number1,number2))
else:
    print("%d не делится на %d" % (number1,number2))
    print("Остаток: %d" % (number1%number2))
print("Частное: %d" % (number1//number2))
