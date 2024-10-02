number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))

if number2 !=0:
    if number1 % number2 ==0 :
         print('Делится' )
    elif number1%number2 :
        print('Делиться', number1%number2)
else:
     print('Не делиться')

