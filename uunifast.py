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
    with open('uunifast.csv', mode='a') as test_file:
        test_writer = csv.writer(test_file)
        start_time = time.time()
        
        seed(random())
        
        #RandomArray = np.empty(3, dtype = float)
        sumU = U
        random_list = []
        for j in range(0,n-1):
            
            nextSumU = np.multiply(sumU,(np.random.rand()**(1/(n-1))))
            #np.append(random_list,(sumU - nextSumU))
            random_list.insert(i,sumU - nextSumU)
            sumU = nextSumU
        #np.append(random_list,sumU)
        random_list.insert(n-1,sumU)
        test_writer.writerow(random_list)
    # elapsed_time = time.time() - start_time
    # elapsed_time = elapsed_time*1000
    # avg_time.append(elapsed_time)
#print(statistics.mean(avg_time))
period = np.random.rand(n)
wcet = np.multiply(random_list, period)
print("The period for every task is ", period)
print("The worst-case execution time for every task is ", wcet)      
#print(RandomArray)