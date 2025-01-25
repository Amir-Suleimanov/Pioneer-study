from time import sleep

from pioneer_sdk import Pioneer

pioneer = Pioneer()

print(pioneer.connected())

pioneer.arm()

pioneer.takeoff()

'''Задаём скорость движения (м/с)'''
pioneer.set_manual_speed(0.3, 0.3, 0.3, 0.1)
pioneer.go_to_local_point(x=0.2, y=0.4, z=0.1)

print(pioneer.point_reached())

'''Задаём нулевую скорость (остановиться на месте)'''
pioneer.set_manual_speed(0, 0, 0, 0)
sleep(3)

pioneer.land()

pioneer.close_connection()