"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
 и завершать скрипт.
"""

import time


class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def _set_light(self, name, seconds, sgr):
        self.__color = name
        print(f'the light is {sgr}{name}\x1b[30m')
        time.sleep(seconds)

    def running(self):
        while True:
            self._set_light('red', 7, '\x1b[31m')
            self._set_light('yellow', 2, '\x1b[33m')
            self._set_light('green', 7, '\x1b[32m')
            self._set_light('yellow', 2, '\x1b[33m')


traffic_light = TrafficLight()
traffic_light.running()
