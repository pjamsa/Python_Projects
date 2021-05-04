import time
timenow = time.localtime()
print(timenow)
print(timenow.tm_hour)
print(timenow.tm_min)
if ((timenow.tm_hour >= 9) & (timenow.tm_min >= 15)):
    if((timenow.tm_hour <= 15) & (timenow.tm_min <= 30)):
        print('Store open.')
    else:
        print('Store closed.')
