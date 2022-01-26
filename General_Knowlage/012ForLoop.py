# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#               while loop = unlimited
#               for loop = limited

import time

for i in range(10): # i means shortcut of index we can give any name
    print(i+1)

for i in range(50,100+1,2): # 50 starting point inclusive
                            # 101 ending point exclusive
                            # 2 count by 2 or which number you need
    print(i)

for i in "Bro Code":
    print(i) # print each letter in new line

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

