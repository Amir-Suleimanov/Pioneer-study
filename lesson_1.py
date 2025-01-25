from time import sleep

from pioneer_sdk import piosdk


"""
Подключение к дрону 
Нужно ввести свои данные от дрона
"""
pioneer = piosdk.Pioneer(logger=False, log_connection=False) # Отключаем логгирование
print(pioneer.connected()) # Проверка соедения


"Перезагрузка дрона"
if pioneer.reboot_board(): 
    print("Дрон перезагружен")
else: 
    print("Ошибка перезагрузки")

"Включение логгера MAVLink"
pioneer.set_logger(True)

sleep(3)

"Повторное отключение логгера MAVLink"
pioneer.set_logger(False)

"Включение логгера состояния подключения"
pioneer.set_log_connection(True)

sleep(3)

"Выключение логгера состояния подключения"
pioneer.set_log_connection(False)

"Запуск моторов дрона"
if pioneer.arm():
    print("Дрон запущен")
else:
    print("Ошибка запуска дрона")

sleep(3)

"Остановка моторов дрона"
if pioneer.disarm():
    print("Дрон остановлен")
else:
    print("Ошибка остановки дрона")


" Отключение от дрона "
pioneer.close_connection()

print(pioneer.connected()) # Проверка что отключился
