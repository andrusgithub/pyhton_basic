# Курс от Skillbox

balance = int(input('Сколько денег на счету?: '))
if balance > 75000:
  balance -= 75000
  print('Курс успешно приобретён')
  print('Баланс:', balance)
else:
  print('Нехватает денег на счету')
print('Хорошего дня!')

# =========================================================
# Угадай число (Угадал)

father = 5
son = int(input('Сколько денег на счету?: ')) 
if father != son:
  print('Не угадал')
else:
  print('Угадал')
print('Конец игры!')

# =========================================================

# Датчик погоды.
rain = int(input('На улице идёт дождь? введите 0 или 1 '))
if rain == 1:
  print('Пошёл дождь. Возьмите зонтик!')

# Поступление.
russian_leng = int(input('Введите количество баллов по русскому языку: '))
mathematics = int(input('Введите количество баллов по математике: '))
informatics = int(input('Введите количество баллов по информатике: '))
if russian_leng + mathematics + informatics >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')
  
# Следим за зубами.
even = int(input('Введите число: '))
if even % 2 == 0:
  print('Использовать зубную нить')
else:
  print('Завтра: используй зубную нить')
  
# Калькулятор скидки.
a = int(input('Введите сумму товара 1: '))
b = int(input('Введите сумму товара 2: '))
c = int(input('Введите сумму товара 3: '))
sum = a + b + c
if sum >= 10000:
  sum = sum - (sum / 100 * 10)
  print(sum, '- cумма со скидкой - 10 %')
else:
  print('без скидки')
  
# Модуль числа.
a = int(input('Введите число: '))
if a > 0:
  print(a)
else:
  print(-a)

# Игра в кубики.
a = int(input('Кубик Кости: '))
b = int(input('Кубик владельца: '))
if a >= b:
  print('Разность: ',a - b)
  print('Костя платит')
else:
  print('Сумма: ', a + b)
  print('Владелец платит')
print('Игра окончена')

# Банкомат.
a = int(input('Введите сумму, которую хотите снять: '))
b = a % 100
if b > 0:
  print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
else:
  print('Такую сумму снять можно')
  
# Хватит ли зарплаты.
hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
salary = 200 * hours / 2 ** 3 + hours
if salary >= credit + food:
  print('Часов хватает. Можно отдохнуть.')
else:
  print('Часов не хватает. Придётся работать!')

# Плохой циферблат.
mileage = int(input('Введите пробег: '))
date_today = int(input('Введите сегодняшнее число: '))
amount = (mileage % 10) + (mileage % 10 // 10) + (mileage // 100)
if amount >= date_today:
  mileage = 0
  print('Cброс.')
else:
  print('Сегодня не сломался')
print('Пробег:',mileage)

# По желанию. Максимальное число.
a = int(input('Введите часло: '))
b = int(input('Введите часло: '))
c = int(input('Введите часло: '))
if a > c:
  max = a
else:
  max = c
if b > max:
  max = b
print(max)