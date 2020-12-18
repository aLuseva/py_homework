from time import sleep

# exercise 1
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f"Переключение светофора {TrafficLight.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 3:
                sleep(4)
            i += 1

trafficlight = TrafficLight()
trafficlight.running()

# exercise 2
class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calc_mass(self):
        return self.__length * self.__width * 25 * 5

road = Road(20, 5000)
print(f"Масса асфальта = {road.calc_mass()}")

# exercise 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position (Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"Полное имя сотрудника - {self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

position = Position('Уолтер', 'Уайт', 'учитель', 10000, 5000)
print(position.get_full_name())
print("Доход с учетом премии - ", position.get_total_income())

# exercise 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.color} автомобиль марки {self.name} начал движение."

    def stop(self):
        return f"{self.color} автомобиль марки {self.name} остановился."

    def turn_right(self):
        return f"{self.color} автомобиль марки {self.name} повернул направо."

    def turn_left(self):
        return f"{self.color} автомобиль марки {self.name} повернул налево."

    def show_speed(self):
        return f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч."


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"{self.color} автомобиль марки {self.name} превысил скорость! Текущая скорость - {self.speed} км/ч."
        else:
            return f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч."


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"{self.color} автомобиль марки {self.name} превысил скорость!"
        else:
            return f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч."

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police is True:
            return f"Это полицейская машина."
        else:
            return f"Это не полицейская машина."

car = Car(65, 'Красный', 'Mazda', False)
print(car.go())
print(car.show_speed())
print(car.turn_left())
print(car.turn_right())
print(car.stop())

towncar = TownCar(70, 'Синий', 'Opel', False)
print(towncar.go())
print(towncar.show_speed())

sportcar = SportCar(160, 'Зеленый', 'Porsche 718 Boxster', False)
print(sportcar.go())
print(sportcar.show_speed())
print(sportcar.stop())

policecar = PoliceCar(60, 'Белый', 'Volvo', True)
print(policecar.go())
print(policecar.show_speed())
print(policecar.police())

# exercise 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки в режиме - {self.title}'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки в режиме - {self.title}'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки в режиме - {self.title}'

pen = Pen('Ручка')
print(pen.draw())

pencil = Pencil('Карандаш')
print(pencil.draw())

handle = Handle('Маркер')
print(handle.draw())