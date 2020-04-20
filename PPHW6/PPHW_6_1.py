# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time
import functools


class TrafficLight:
    # Атребуты
    __color = None

    # Метод
    def running(self):
        def switching_colors(name_color, time_switch):
            TrafficLight.__color = name_color
            print(TrafficLight.__color)
            time.sleep(time_switch)

        score = 0
        while True:
            score += 1
            switching_colors('Красный', 7)
            switching_colors('Желтый', 2)
            switching_colors('Зеленый', 7)
            if score == 3:
                break
            switching_colors('Желтый', 2)


run = TrafficLight()

run.running()
