name = input('enter your name:')

count = 0
while True:
    print(name.title())
    if count == 10:
        break

    count += 1
# This code will print the name entered by the user 10 times.
# The name is printed in title case using the title() method.

##function wrapping
def print_10_times():
    name = input('enter your name:')

count = 0
while True:
    print(name.title())
    if count == 10:
        break

    count += 1

print_10_times()