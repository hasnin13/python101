print("Enter your username :" , end ='')


name = input()

print(name)
print(f"hello, {name}")

a = input('Enter the 1st value:')
a = int(a)

b = input('Enter the 2nd value:')
b = int(b)
print(f'type of a: {type(a)}\ntype of b : {type(b)}')
print(a+b)

##########
num = input('Enter the number of time you want to print your name :')
num = int(num)

for i in range(num):
    print(f"Hello, {name.title()}!")

print(a%b)