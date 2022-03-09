from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import json
import os

bt_id = 0


def show_bt():
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        for bt in data['bt']:
            print("Командировка №", bt['btId'], ":\n", "Дата начала: ", bt['bt_start_date'], "\n",
                  "Дата окончания: ", bt['bt_finish_date'], "\n" + "Продолжительность: ", bt['bt_days_count'])
            print('=====================')
    except:
        print('Записи командирований отсутствуют')


def delete_bt(delete_bt_id):
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        data['bt'].pop(delete_bt_id - 1)
        i = 1
        for bt in data['bt']:
            bt['btId'] = i
            i += 1

        with open('data.json', 'w') as write_file:
            json.dump(data, write_file, indent=2)

    except:
        print('Записи командирований отсутствуют')


def delete_all_bt():
    try:
        os.remove("data.json")
    except:
        print('Записи командирований отсутствуют')


def leap_year():
    today = date.today()
    today_year = today.year
    if today_year % 4 == 0 and today_year % 100 != 0 or today_year % 400 == 0:
        return 366
    else:
        return 365


def calculate_resident():
    bt_all_count = 0
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)

    except:
        print('Записи командирований отсутствуют')

    for bt in data['bt']:
        today = date.today()
        day_begin_count = today - timedelta(leap_year())
        bt_start_input = tuple(int(item) for item in bt['bt_start_date'].split(','))
        bt_start_date = date(bt_start_input[0], bt_start_input[1], bt_start_input[2])
        if bt_start_date > day_begin_count:
            bt_all_count += int(bt['bt_days_count'])
            bt_id = bt['btId']
        else:
            bt_finish_input = tuple(int(item) for item in bt['bt_finish_date'].split(','))
            bt_finish_date = date(bt_finish_input[0], bt_finish_input[1], bt_finish_input[2])
            bt_all_count += (bt_finish_date - day_begin_count).days + 1
            bt_id = bt['btId']

    print('Количество дней в командировках: ', bt_all_count)
    bt_road_days = bt_id * 2
    print('Количество дней в дороге: ', bt_road_days)
    bt_resident_days = bt_all_count - bt_road_days
    print('Количество дней нерезидентсва: ', bt_resident_days)
    bt_notresident_days = leap_year() - bt_resident_days
    print('Осталось дней: ', bt_notresident_days)


class BusinessTrip:
    bt_start_date = ''
    bt_finish_date = ''
    bt_duration = 0

    def create_bt(self):
        global bt_id
        bt_id += 1
        id_list = []
        bt_start_input = input("Введите дату начала командировки (ГГГГ,ММ,ДД):  ")
        bt_finish_input = input("Введите дату окончания командировки (ГГГГ,ММ,ДД):  ")
        bt_start_input = tuple(int(item) for item in bt_start_input.split(','))
        bt_finish_input = tuple(int(item) for item in bt_finish_input.split(','))
        self.bt_start_date = datetime(bt_start_input[0], bt_start_input[1], bt_start_input[2])
        self.bt_finish_date = datetime(bt_finish_input[0], bt_finish_input[1], bt_finish_input[2])
        self.bt_duration = self.bt_finish_date - self.bt_start_date
        try:
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
        except:
            bt_id = 1
            data = {'bt': []}
            data['bt'].append({
                "btId": bt_id,
                "bt_start_date": self.bt_start_date.strftime("%Y,%m,%d"),
                "bt_finish_date": self.bt_finish_date.strftime("%Y,%m,%d"),
                "bt_days_count": self.bt_duration.days + 1
            })

            with open('data.json', 'w') as write_file:
                json.dump(data, write_file, indent=2)
        else:
            for bt in data['bt']:
                id_list.append(bt['btId'])
            bt_id = id_list[-1] + 1
            data['bt'].append({
                "btId": bt_id,
                "bt_start_date": self.bt_start_date.strftime("%Y,%m,%d"),
                "bt_finish_date": self.bt_finish_date.strftime("%Y,%m,%d"),
                "bt_days_count": self.bt_duration.days + 1
            })

            with open('data.json', 'w') as write_file:
                json.dump(data, write_file, indent=2)
