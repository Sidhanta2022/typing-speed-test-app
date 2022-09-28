from time import *
import random as r

def wrong(para,user_input):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user_input[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_start , time_end, user_input_2):
    time_delay = time_end - time_start
    time_complete = round(time_delay,2)
    speed = len(user_input_2)/time_complete
    return round(speed)


test = [ "you-tube is a social media having a huge fan base and visitor, conent maker ","google is a better platform for a data hungry person","face-book is a social media platform to connect with your loved ones"]
test1 = r.choice(test)
print("****** typing speed per second*****")
print(test1)
print()
print()
time_1 = time()
user_input_2 = input("type here = ")
time_2 = time()

print("speed = " ,speed_time(time_1 , time_2, user_input_2),"word per second")
print("error = ", wrong(test1,user_input_2))
