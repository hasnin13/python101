##Function
#Example 1:
def odd_even(n):
    if (n %2 ==0):
        print("even")
    else:
        print("odd")
odd_even(3)
odd_even(10)

#Example 2:
def fun():
    print("ABC")
fun()

#Example 3:
def add(n1,n2):
    n3=n1+n2
    return n3
n1, n2=3,5
n = add(n1,n2)
print(f'The sum of {n1} and {n2} is {n}')
