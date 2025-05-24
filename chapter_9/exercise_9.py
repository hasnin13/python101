#exercise 9.1:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name : {self.name}')
        print(f'Food type :{self.type}')

    def open_restaurant(self):
        print(f'{self.name} is open now')
restaurant = Restaurant("Blehh","Korean")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#exercise 9.2:
restaurant1 = Restaurant("caspachino", "Cafe")
restaurant2 = Restaurant("Bhat_ Mach", "Bangladeshi")
restaurant3 = Restaurant("Akhri_Pasta", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#exercise 9.3:
class User:
    def __init__(self,first_name,last_name,location,age):
        self.first_name = first_name
        self.last_name = last_name
        self.address = location
        self.age = age

    def describe_user(self):
        print(f'user name : {self.first_name} {self.last_name}')
        print(f'users age :{self.age}')
        print(f'users location : {self.address}')
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome.")

user1 = User("Hasnin", "Jahan", "Basha", 22)
user2 = User("Oreo", "theMissingCat", "Basha", 2)
user3 = User("Harano", "Prima", "Jongol", 22)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()