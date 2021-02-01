import numpy as np
import sys
import csv
from random import seed
from random import random
from random import randrange
import time
import statistics

x = 1
#n = 10
#U = 0.4
n = int(sys.argv[1])
U = float(sys.argv[2])

for i in range(0, 100):
    with open('uuniform.csv', mode='a') as test_file:
        test_writer = csv.writer(test_file)
        start_time = time.time()
        seed(random())
        #RandomArray = np.empty(3, dtype = float)
        while x == 1:
            random_list = []
            for j in range(0,n-1):
                r = np.random.rand() * U
                random_list.insert(i,r)

            #np.append(random_list,np.multiply(U,(np.random.rand(0,(n-1)))))
            #print(randrange(0,(n-1)))
            if np.sum(random_list) <= U:
                break
        #np.append(random_list,(U - np.sum(random_list)))     
        # random_list.insert(n-1,(U - np.sum(random_list)))
        # test_writer.writerow(random_list)
        # elapsed_time = time.time() - start_time
        # elapsed_time = elapsed_time*1000
        # print(elapsed_time)
period = np.random.rand(n)
wcet = np.multiply(random_list, period)
print("The period for every task is ", period)
print("The worst-case execution time for every task is ", wcet)
#print(RandomArray)
