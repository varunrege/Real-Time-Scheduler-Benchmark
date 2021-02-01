import numpy as np
import sys
import csv
from random import seed
from random import random
from random import randrange
import time
import statistics
#n = int(input("Enter value of n: "))
#U = float(input("Enter upLimit: "))
#n = 10
#U = 1
n = int(sys.argv[1])
U = float(sys.argv[2])

avg_time = []
for i in range(0, 100):
    upLimit = U
    random_list = [0]*n

    with open('ufitting.csv', mode='a') as test_file:
        test_writer = csv.writer(test_file)
        start_time = time.time()

        seed(random())
        for j in range(0, n-1):
            random_list[j] = (randrange(0, 10)/10.0)*upLimit
            #print(randrange(0, 10)/10.10)
            upLimit = upLimit - random_list[j]
        
        random_list[n-1] = upLimit

        test_writer.writerow(random_list)

#     elapsed_time = time.time() - start_time
#     elapsed_time = elapsed_time*1000
#     avg_time.append(elapsed_time)
# print(statistics.mean(avg_time))
period = np.random.rand(n)
wcet = np.multiply(random_list, period)
print("The period for every task is ", period)
print("The worst-case execution time for every task is ", wcet)


# for i in range(0,100):
#     with open('ufitting_0.5.csv', mode='a') as employee_file:
#         employee_writer = csv.writer(employee_file)

#         RandomArray = np.empty(3, dtype = float)
#         for x in range(0,n-1):
#             seed(1)
#             # RandomArray = np.random.rand(n)
#             # np.append(RandomArray,(random()*U))
#             RandomArray[x] += random()*U
#             U = U - RandomArray[x]
#             np.append(RandomArray,U)
#             employee_writer.writerow(RandomArray)


#print(RandomArray)

