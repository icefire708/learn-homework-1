"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def chose_activity(age: int) -> str:
    if age < 0:
        return 'ждать своего рождения'
    if age < 2:
        return 'учиться ползать дома'
    if age < 6:
        return 'учиться в детском саду'
    if age < 18:
        return 'учиться в школе'
    if age < 24:
        return 'учиться в вузе'
    return 'работать'

def main():
    flag = True
    while flag:
        flag = False
        try:
            age = int(input("Введите ваш возраст: "))
            activity = chose_activity(age)
            print(f'Вы должны {activity}!')
        except:
            print('Вводи возраст нормально!!! Целым десятичным числом.')
            flag = True

if __name__ == "__main__":
    main()
