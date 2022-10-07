# families = ['ubong', 'ruth', 'blessing', 'mfonobong']
# families.sort()
# #print(families)
# print(families[1])

# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average: ', average)

xfile = open('mbox-short.txt')
for line in xfile :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    word = line.split()
    print(word[2])