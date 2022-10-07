# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)
    
# xfile = open('mbox.txt')
# count = 0
# for line in xfile:
#     count = count + 1
# print('Line Count:', count)

# xfile = open('mbox-short.txt')
# inp = xfile.read()
# print(len(inp))
# print(inp[:20])

# xfile = open('mbox-short.txt')
# for line in xfile:
#     if line.startswith('From: '):
#         print(line )
        
# xfile = open('mbox-short.txt')
# for line in xfile:
#     line = line.rstrip()
#     if line.startswith('From: '):
#         print(line )

# xfile = open('mbox-short.txt')
# for line in xfile:
#     line = line.rstrip()
#     if line.startswith('From: '):
#         continue
#     print(line)

# xfile = open('mbox-short.txt')
# for line in xfile :
#     line = line.rstrip()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)

xname = input('Enter the file name: ')
xfile = open(xname)
count =  0
for line in xfile :
    if line.startswith('Subject: ') :
        count = count + 1
    print('There were', count, 'subject lines in', xfile)    