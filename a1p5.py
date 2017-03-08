days=int(input('Enter number of days'))
year=days/360
a=days%360
b=a//30
c=a%30
print 'Number of year=',year
print 'Number of months=',b
print 'Number of days=',c
