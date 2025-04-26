dict = {}
print(type(dict))

dict ={
    'rishat': 10,
    'nazme' : 12,
    'abrar' : 15,
}
#adding new input
dict['ruhi'] = 13
dict['rakib'] = 20

dict['nazme']=2 #changing value of input
print(type(dict))
print(dict)
print(dict['rishat'])




###
alien = {
    'x_position' :0,
    'y_position' :0,
    'speed' : 'slow'
}

if alien['speed'] == 'slow':
    alien['x_position'] += 1
elif alien['speed'] == 'medium':
    alien['x_position'] += 2
else:
    alien['x_position'] += 3

print(f'neww position: {alien["x_position"]}')

del alien['y_position']



###
arr = ['rishat',1,1,5]

print(arr[1].bit_count())
print(arr)




langs = {
    "rishat":"python",
    "ruhi" : "java",
    "rakib":"perl",
    "hanna":"c++",
    "nazme":"c",
    "abrar":"javascript",
    "plabon":"html",

}
print(langs.get('sadia', "sadia not found"))

####
user = {
    'username' : "rishat",
    'password' : "1234",
    'mail' : "rst@mail.com"
}

arr = [1,2,3,4,5,6,7]
for i in arr :
    print(i)
    
print(user.keys())

for key in user :
    print(key)

for key,val in user.items():
    print(f"key : {key}")
    print(f"val : {val}")

print('\n' + f"{user.items()}")

for item in user.items() :
    key,val = item
    print(key)
    print(val)

first,second,third = (1,2,3)
print(first)
print(second)
print(third)



