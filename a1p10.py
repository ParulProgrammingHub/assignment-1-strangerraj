rate = input('Enter Interest rate in percentage')
principle = input('Enter the principle amount')
x = input('Select 1 for duration of time in days  \n2 for time in months and \n3 for time in years')
principle = float(principle)
if(x == 1):
	time = input('Enter number of days')
	time = time /(12*30)
elif(x == 2):
        time = input('Enter number of months')
        time = time / 12
else:
        time = input(' Enter number of years')
def Simple_Interest(rate,principle,time):
    simple_Interest = ( principle * rate * time ) / 100
    print(' Simple Interest = %f ' %simple_Interest)

    total = principle + simple_Interest
    print(' Total amount = %f ' %total )
Simple_Interest(rate,principle,time)

