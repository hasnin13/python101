### exercise 7.1:
carname = input("What kind of rental car would you like? \n")

print(f"Let me see if I can find you a {carname}.")

### exercise 7.2:
num_of_people = input("How many people are in your dinner group?\n")
num_of_people = int(num_of_people)

if num_of_people < 8:
        print("The table is ready")

else:
        print("Y'all have to wait :(")


### exercise 7.3:
number = int(input("Enter a number : \n"))
if number % 10 == 0:
        print(f"The number {number} is a multiple of 10")
else:
        print(f"the number {number} is not a multiple of 10")


### exercise 7.4:
topping = ""
while topping != "quit":
        topping =  input("Enter your toppings:")
        if topping != 'quit':
                 print(f"I'll add {topping} to your pizza.")
        else:
                print("Finished adding toppings in your pizza.")

### exercise 7.5:
age = 0
while age != "quit":
        age = input("Enter your age:")
        if age != "quit":
                age = int(age)
                if age <= 3:
                        print("The ticket is free")
                if age > 3 and age <= 12:
                        print("The ticket is $10")
                else:
                        print("The ticket is $15")
        else:
                print("The ticket is $15")

### exercise 7.7:
num =0
while num < 2:
        print("loop")