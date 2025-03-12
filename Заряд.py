def check_battery(level):
    if level <= 20:
        print("Подключите к источнику питания!")
        return True
    else:
        print("Заряд достаточный.")
        return False

battery_level = int(input("Введите уровень заряда батареи (%): "))
check_battery(battery_level)

def check_store_status(current_time):
    if current_time >= 22 or current_time < 11:
        print("Магазин открыт.")
    else:
        print("Магазин закрыт.")

battery_level = int(input("Введите уровень заряда батареи (%): "))
check_battery(battery_level)

current_time = int(input("Введите текущее время (часы в 24-часовом формате): "))
check_store_status(current_time)
