num=0
while num < 100:
    num+=1
    if num %2 == 0:
        continue
    print(num)

# 0 = false
#1 = true
#all value = true
#[] = false
#none = null = false
#'' = false
#{} = false
#{[]} = true
#[[]] = true

num = [1,2,3,4,5] 
while num:
    print(num.pop())

lang = ['python' , 'java', 'c' ,'python' , 'rust', 'javascript', 'python' ,'c++']
#while 'python' in lang:
#    if 'python' in lang:  
#        lang.remove('python')
#       print(lang)

# to prevent infinity loop from the while loop up there just do:
while 'python' in lang:
        
        lang.remove('python')
        print(lang)

##user list in dictionary:
users = {}
while True:
     name = input('enter your name :')
     place = input('Enter your fvrt place :')

     users[name] = place
     userInput = input('Would you like to add another user? (y/n) :')

     if userInput == 'n':
          break
     
for name, place in users.items():
     print(f'{name} wants to go to {place}')