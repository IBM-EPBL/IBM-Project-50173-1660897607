import random
temperature=random.randint(0,100)
humidity=random.randint(0,100)
if(temperature>42 and humidity<55):
    print("The temperature and humidity is HIGH\n",temperature,humidity,
          "\n The alarm is ON")
else:
    print("The temperature and humidity is NORMAL\n",temperature,humidity,"\n The alarm is OFF")
