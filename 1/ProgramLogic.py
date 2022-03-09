import BusinessTrip
from datetime import date, timedelta


def start_program():
    calculate_answer = 'Y'
    start_data()
    id_command = ''
    print('Доступные команды:\nПоказать количество дней в командировках - 1\nРедактирование командировок - '
          '2\nПросмотр моих командировок - 3')

    id_command = check_input()
    if id_command == 1:
        BusinessTrip.calculate_resident()

    elif id_command == 2:
        print('Добавить командировку - 1\nУдалить командировку - 2\nУдалить все командировки - 3')

        id_command = check_input()
        if id_command == 1:
            BusinessTrip.BusinessTrip().create_bt()
            while calculate_answer != 'N':
                if (input("Добавить ещё командировку? (Y/N): ")) == 'Y':
                    BusinessTrip.BusinessTrip().create_bt()
                else:
                    calculate_answer = 'N'
                    continue_program()

        if id_command == 2:
            BusinessTrip.delete_bt(int(input('Введите номер командировки: ')))
            continue_program()

        if id_command == 3:
            BusinessTrip.delete_all_bt()
            continue_program()

    elif id_command == 3:
        BusinessTrip.show_bt()
        continue_program()

    else:
        print('Неверная команда')
        continue_program()


def check_input():
    try:
        id_command = int(input('Введите команду: '))
        print('===============')
        return id_command
    except ValueError:
        print('Неверная команда')
        continue_program()


def start_data():
    today = date.today()
    day_begin_count = today - timedelta(BusinessTrip.leap_year())
    # day_begin_count = today - relativedelta(year = -1)
    print('===================================')
    print("Сегодняшняя дата:", today)
    print("Дата начала отсчёта:", day_begin_count)
    print('===================================')


def continue_program():
    if (input('Продолжить выполнение программы? (Y/N): ')) == 'Y':
        print('=====================')
        start_program()
    else:
        pass
