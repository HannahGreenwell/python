classmates = ['Jalal', 'Emily', 'Marco', 'Adria', 'Paul']

# counter = 0
#
# for each_name in classmates:
#     print('Item #', counter)
#     print('Item using []:', classmates[counter])
#     print('Hello, ', each_name.upper(), '!', sep='')
#
#     classmates[counter] = each_name.upper()
#
#     counter += 1
#
# print(classmates)

# for i in range(len(classmates)):
#     print('i:', i)
#     print(classmates[i])
#     classmates[i] = classmates[i].upper()
#
# print(classmates)

for index, item in enumerate(classmates):
    print(index, item)
    classmates[index] = item.upper()

print(classmates)    
