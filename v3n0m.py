import random
x = int(input('How many bins do you want to generate? '))
suff = int(input('Enter \n4.Visa\n5.Mastercard\n'))
z = 0
list_of_bins = list()
while z < x:
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.randint(1,9)
    e = random.randint(1,9)
    before_final = int(str(a)+str(b)+str(c)+str(d)+str(e))
    final = int(str(suff)+str(before_final))
    list_of_bins.append(final)
    z+=1
for i in list_of_bins:
    print(i)