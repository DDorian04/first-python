value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value) 
# else:
#     print("Value is now equal to " + str(value))
    	
# names = ["Dorian","Sara","John"]
# for x in names:
#     print(x + " Mississippi")
    # print("Mississippi")
    
# for x in "Mississippi":
#     print(x)
    
# for x in names:
#     if x == "Sara":
#     print(x)	
#         break
    
# for x in names:
#     if x == "Sara":
#         continue
#     print(x)	

# for x in range(4):
#     print(x)
    
# for x in range(2, 4):
#     print(x)
    
# for x in range(5,101,5):
#     print(x)
# else:
#     print("Glad that\'s over!")    

names = ["Dorian","Sara","John"]
actions = ["codes", "eats","sleeps"]   	

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
        
for action in actions:
    for name in names:
        print(name + " " + action + ".")
        