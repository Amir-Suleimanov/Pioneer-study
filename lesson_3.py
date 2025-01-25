from time import sleep

from pioneer_sdk import Pioneer

pioneer = Pioneer()

print(pioneer.connected())

pioneer.arm()

pioneer.takeoff()

"Полёт к координатам выраженных в метрах"
if pioneer.go_to_local_point(x=0.2, y=0.4, z=0.1):
    print("Полет успешен!")
else:
    print("Полет не удался!")
sleep(5)

"Проверка, достигнута ли цель"
if pioneer.point_reached():
    print("Точка достигнут!")
else:
    print("Полет не достигнут!")

"Полёт к координатам выраженных в метрах, по системе координат дрона"
if pioneer.go_to_local_point_body_fixed(x=0, y=0, z=0):
    print("Полет успешен!")
else:
    print("Полет не удался!")
# Пока неизвестно чем они отличаютс друг от друга, возможно это даже не стоит использовать

pioneer.land()

pioneer.close_connection()
