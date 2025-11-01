name=list()  #list
name = [5,2,9,1,'aman']
first, second , *third,= name  #unpacking
print (third)
print(type(name))
print(len(name))
print (name[4])#index 
print(name[-3])#negative indexing


#slicing 
new_list= name [-4:-2]
print(new_list)

#adding item  to list
name.append('hanal')
print(name)

# inserting items in specfic index 
name.insert(2,'kale')
print(name)
#remove
name.remove('hanal')
#clear
name .clear
#copy
new1_list=name.copy()

#join list
number= [6,22,33,4,88]
newest_list = name + number
newest_list=number.extend(name)

print (newest_list.count())

#finding an index
index = name .index ('aman')

#revers
print(name.reverse)

#sort
print(number.sort)
