def add(*args ):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return print(n)


calculate(2, add=3, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
my_car = Car(make="Ford", model="Mustang")

print(my_car.make)
print(my_car.model)