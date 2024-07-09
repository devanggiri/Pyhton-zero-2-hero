#read current tiemand give a greeting for morning, afternoon, eveving, night
import time
timetotal = time.strftime('%H:%M:%S')
print(timetotal)
'''timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)'''


#morning 00:00:00 - 11:59:59
#afternoon 12:00:00 - 15:59:59
#eveing 16:00:00 - 20:59:59
#night 21:00:00 - 23:59:59

print(timetotal[0:2],timetotal[3:5],timetotal[6:8])
hour=timetotal[0:2]
x=int(hour)
if x>=0 and x<=11:
    print("Good Morning")
elif x>=12 and x<=15:
    print("Good afternoon")
elif x>=16 and x<=20:
    print("Good evening")
else:
    print("Good Night")
    
    
    
    
#alternative

import time

def greet_based_on_time():
    # Get the current hour
    current_hour = int(time.strftime('%H'))
    
    # Determine the appropriate greeting
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    # Print the greeting
    print(greeting)

# Call the function
greet_based_on_time()
