import random
#The Basic Rules to handle and use Variables in Functions , condtions and realtions
#1 variables , types , type casting and their concatination:
from encodings import normalize_encoding

a="This is the string"
print(a)
print(type(a))
b=1
print(type(b))
#concatination of string
another_string="and it is concatenated"
print(a +" "+ another_string)# use " " because contains space
print(a , another_string)
print(f"{a}  {another_string}")
# One stirng and other int type
print(f"{a}  {b}")
print(a,b)
#print(a + b) this line shows error because that can cause error string and int cannot concatenate
#mutliple variable print in one line
print(a,b,another_string)
#Functions:
def var():
    return 5
print("The return value is ", var())

email_adress="mouizumarr22@gamil.com"
if email_adress:
    print("The Email found in function eml",{email_adress})

f=None
print(type(f))


def student_data():
    age=14
    name="mouizumarr22"
    return age,name
student_age , student_name = student_data()

if student_age<=18:
    print(student_name,"Age is under 18")
else:
    print(student_name,"Age is over 18")


# so when we compare function values we must store it in other variables then compare
 # now list and how we call them
names=["Mouiz","Ali","Abdullah","Tayyab"]
print(type(names),names)
print(names[0])# first index
print(names[-1])# bydefault last index without knowing the size of list
print(names[0:3])
# list functions add, delete
names.append("Taha")
print(names)
names.remove("Ali")
print(names)

#check list
name_to_check="Ali"
if name_to_check in names:
    print(names)
    print(name_to_check,"is in the list")
else:
    print(names)
    print(name_to_check,"is not in the list")


# Render list items one by one not in list
for list_item in names:
    print(list_item)

# Random Numbers
#1 store a random number in variable
#2 then make a list 50 random number then check the random variable exist in list

random_no_variable=random.randint(1,10)
print(random_no_variable)

list_of_random_numers=[ ]

for i in range(0,50):
    random_number=random.randint(1,100)
    list_of_random_numers.append(random_number)
    print(list_of_random_numers)

if random_no_variable in list_of_random_numers:
    print(random_no_variable,"is in the list")
else:
    print(random_no_variable,"is not in the list")


# dictionary
'''
stores in key and its value , the key in dictionary always remians different
'''
student_dict={
    "r#":"123",
    "name":"Ali",
    "age":14,
    "courses":["math","english","computer science"]
}
print(student_dict)# All dictionary
print(student_dict["name"])

if "computer science" in student_dict["courses"]:
    print(student_dict["name"]," is computer student")






