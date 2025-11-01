print("Hello, world!")

name = ('aman')

print(name.capitalize())
print(len(name))

age = 55
salary = 25.5

a = 58*54.22

print (a)

print (type(name))


students= ['hana','aman','alex',5,8.8]

#len num of character
print (len(name))
#capital the firs letter
print(name.capitalize())
#isalpha true if all char are alpha
print (name.isalpha())
#is digit true if all char are dig
print(str(age).isdigit())
#isalnum if alphanumerical 
print (name.isalnum())
#is lower() for lower case 
print (name.islower())
#is  upper
print (name.isupper())


#if statment 
if (age > 18):
    print('adult')  #always 4 indentation for if statment. at the begining it wll be another
    gender = input ('inter gender')

    if (gender=="male"):
        pass
    else:
        print('f')
elif(age==18):
    pass 
else:
    print ('not')
