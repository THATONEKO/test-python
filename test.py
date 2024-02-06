"""class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_engine_running = False
        self.current_speed = 0

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine is started.")
        self.is_engine_running = True

    def drive_car(self, speed):
        if self.is_engine_running:
            self.current_speed = speed
            print(f"{self.make} {self.model} is now being driven at {self.current_speed} mph.")
        else:
            print(f"Please start the engine of {self.make} {self.model} first.")

    def accelerate(self, speed_increase):
        if self.is_engine_running:
            self.current_speed += speed_increase
            print(f"{self.make} {self.model} is accelerating. Current speed: {self.current_speed} mph.")
        else:
            print(f"Please start the engine of {self.make} {self.model} first.")


# Create an instance of the Car class
my_car = Car("Toyota", "Camry")

# Start the engine
my_car.start_engine()

# Drive the car at a specific speed
my_car.drive_car(30)

# Accelerate the car
my_car.accelerate(20)"""


'''class Car:
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = 'new'

    def display_car(self):
        print(f"This is a {self.color}, {self.model} with {self.mpg}MPG.")

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

    def drive_car(self):
        self.condition = "like new"
my_car = ElectricCar("molten salt", "tesla", "silver", 500)
my_car.drive_car()
print (my_car.condition)


my_car = Car("Mustang", "red", 120)
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)'''

'''class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(x=1, y=2, z=3)
print (my_point)'''

'''import datetime

x = datetime.datetime.now()
print (x)'''


"""class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print ("Move!")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("fly!")

class Ship(Vehicle):
    def move(self):
        print("sail")

car = Car("Mustang", "Ford")
plane = Plane(925, "boeing")
ship = Ship('cruse', "ibiza")

for x in(car, plane, ship):
    print(x.model)
    print(x.brand)
    x.move()"""

import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FSP = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    COLOR = WHITE
    VEL = 4


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def handle_paddle_movement(keys, laft_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s:]

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    while run:
        clock.tick(FSP)
        draw(WIN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handdle_paddle_movement(keys, left_paddle, right_paddle)
    pygame.quit()

if __name__ == '__main__':
    main()

