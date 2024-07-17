'''
class Car:
    model = "BMW"
    color = "white"

    def speedChange(self, v):
        print("speedChange", v)
        self.speed = v
bmw = Car()
bmw.speedChange(20)


class Car:
    model = "BMW"
    color = "white"

bmw = Car()
benz = Car()

benz.model = "Benz"
benz.color = "black"

print(bmw.model)
print(bmw.color)

print(benz.model)
print(benz.color)


class Car:
    count = 0
    speed = 0

    def speedChange(self, v):
        Car.count += 1#클래스가 가지고있는 변수
        self.speed = v#self에 해당되는 자기자신의 변수

bmw = Car()
benz = Car()

bmw.speedChange(100)
print("bmw speed :", bmw.speed)
print("number of speedChange :", Car.count)

benz.speedChange(120)
print("Benz speed :", benz.speed)
print("number of speedChange :", Car.count)


class Car:
    def setData(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Model :", self.model, ", Color :", self.color)

bmw = Car()
bmw.setData("BMW", "white")
bmw.info()


class Car:
    def __init__(self, model, color):#__init__는 무조건 이걸로 한개의 클래스당 한개
        self.model = model
        self.color = color

    def info(self):
        print("Model :", self.model, ", Color :", self.color)

bmw = Car("BMW", "white")
bmw.info()


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Model :", self.model, ", Color :", self.color)

bmw = Car("BMW", "white")
Benz = Car("Benz", "black")
bmw.info()
Benz.info()


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def info(self):
        print("Model :", self.model, ", Color :", self.color)

class CarDrive(Car):
    def speedChange(self, v):
        self.speed = v
        print("speedChange :", self.speed)

bmw = CarDrive("BMW", "white")
bmw.info()
bmw.speedChange(100)


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info (self):
        print("Model :", self.model, ", color :", self.color)

class CarDrive(Car):
    def info(self):
        print("the model of this car is %s" % self.model)
        print("the color is %s" % self.color)

    def speedChange(self, v):
        self.speed = v
        print("speedChange :", self.speed)

bmw = CarDrive("BMW", "white")
bmw.info()


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print("Namg :", self.name)
        print("Weapon :", self.weapon)

lugo = Character("Lugo", "gun")
lugo.intro()


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print("Namg :", self.name)
        print("Weapon :", self.weapon)

class Action(Character):
    step = 0

    def move_forward(self, n):
        self.step += n
        print("Current location is %d" % self.step)
    def move_beckward(self, n):
        self.step -= n
        print("Current location is %d" % self.step)
    def turn_right(self):
        print("Turn right")
    def turn_left(self):
        print("Turn right")

lugo = Action("Lugo", "gun")
lugo.intro()
lugo.move_forward(10)
lugo.move_beckward(3)
lugo.turn_right()
lugo.turn_left()
'''

class tv():

    def __init__(self, ch, vo):
        self.channel = ch
        self.volume = vo
        self.power = True
        
    def on_off(self):
        if self.power:
            self.power = False
            print("Trun off")
        else:
            self.power = True
            print("Trun on")

    def info(self):
        if self.power:
            print("Power =", self.power)
            print("Channel =", self.channel)
            print("Volume =", self.volume)
        else:
            print("Power off")
    def set_channel(self, ch):
        if self.power:
            self.chammel = ch
        else:
            print("Power off")

    def set_volume(self,vo):
        if  self.power:
            self.volume = vo
        else:
            print("Power off")
            
t = tv(1, 16)
t.info()
t.set_channel(5)
t.set_volume(12)
t.on_off()
t.on_off()
