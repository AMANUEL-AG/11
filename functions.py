# def for function 

#def greeting ( name):
 #   return'hello'+  name

#print(greeting('amn'))
#key word argument based on the key  , positional argumaent based on the position , defolt argumnet 


name = input ('input name')
weight = input ('input WEIGHT ')
height = input ('input height')
age = input ('input age')
gender = input ( 'input gender')

def BMI (weight,height) :
    return (weight/(height*height))

BMI1= BMI(weight,height)

print(BMI1)