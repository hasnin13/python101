class Car:
    def details(self):
        print("This is car detail function")

bmw = Car()

bmw.details()

audi = Car()

audi.details()

dummy = [1,2,3,4]
print(dummy.count(1))
print(type(dummy))
print(type(bmw))
#for object differentiate:
class Car:
    def __init__(self,name,release_year):
        self.name = name
        self.year = release_year
        print("this is a initialization method")


    def details(self):
        print(f'Car name: {self.name}')
        print(f'Car release_year: {self.year}')

bmw = Car('BMW',1965)

bmw.details()

audi = Car('AUDI',1980)

audi.details()