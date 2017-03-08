print 'Each Exam is of 100 marks'
a=int(input('Marks of 1st subject:'))
b=int(input('Marks of 2nd subject:'))
c=int(input('Marks of 3rd subject:'))
d=int(input('Marks of 4th subject:'))
e=int(input('Marks of 5th subject:'))
prc=((float(a+b+c+d+e)/500)*100)
print prc
if prc<35.0:
    print 'FAIL'
else:
    print 'PASS'

