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
if number%10:
        print(f"The number {number} is a multiple of 10")
else:
        print(f"the number {number} is not a multiple of 10")