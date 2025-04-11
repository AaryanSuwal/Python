#[]Lists
# ()Tuple
# {}Sets   

    #lists
list_1 = [123, "Ram", 23.45, True]
tinylist_2 = [123, "Aaryan"]


print(list_1)                 #prints  complete list
print(list_1[0])              #prints first element of the list
list_1[0] = 1234              #update the list
print(list_1[1:3])            #prints elements starting from 2nd
print(list_1[2:])             #prints elements starting from 3rd
print(list_1 * 2)             #prints list two times
print(list_1 + tinylist_2)    #print concatenated lists

# implicit are those which are done by the interpreter automatically
# explicit are  those which are done by the user

    #tupel
tuple_1 = (2137, "Aaryan", 21.37, False)
tuple_2 = (123, "Suwal")

print(tuple_1)                 #prints  complete tuple
print(tuple_1[0])              #prints first element of the tuple
print(tuple_1[1:3])            #prints elements starting from 2nd
print(tuple_1[2:])             #prints elements starting from 3rd
print(tuple_1 * 2)             #prints tuple two times
print(tuple_1 + tuple_2)       #print concatenated lists

    #sets
set_1 = {2, 1, 4, 5, 6, 3}
print(set_1)                    #prints output in ascending order

set_2 = {"ram", "shyam", "hari", "laxman"}
print(set_2)                    #print output in random order

set_3 = {"A", "c", "B", "d"}
print(set_3)

set_4 = {"Apple", "Banana", "Mango", "Mango"}
print(set_4)                    #print output but doesnot include repeteated items

set_5 = {"ram", 1001, 102.1, True, 1, False, 0, "sita"}
print(set_5)

    #converting list into sets
list_10 = [123, "Ram", 23.45, True, 1, False, 0]
print(list_10)
set_10 = set(list_10)
print(set_10)
