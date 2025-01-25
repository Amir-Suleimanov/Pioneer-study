from pioneer_sdk import Pioneer

pioneer = Pioneer()

print(pioneer.connected())

pioneer.arm()

"Взлёт на высоту takeoffAlt прописанную в автопилоте"
pioneer.takeoff()

"Посадка"
pioneer.land()

pioneer.close_connection()
