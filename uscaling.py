import numpy as np
import sys
import csv
import time
import statistics
#n = 10
#U = 1
n = int(sys.argv[1])
U = float(sys.argv[2])
avg_time = [] 
for i in range(0,100):
    with open('uscaling.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file)
        start_time = time.time()
        RandomArray = np.random.rand(n)
        RandomArray = np.multiply(RandomArray,(np.divide(U,np.sum(RandomArray))))
        employee_writer.writerow(RandomArray)
        elapsed_time = time.time() - start_time
#     elapsed_time = elapsed_time*1000
#     avg_time.append(elapsed_time)
# print(statistics.mean(avg_time))
period = np.random.rand(n)
wcet = np.multiply(RandomArray, period)
print("The period for every task is ", period)
print("The worst-case execution time for every task is ", wcet)    

#print(RandomArray)
#output_array = np.array(my_data)
#np.savetxt("uscaling_0.5.csv", RandomArray, delimiter=",")
        #for x in range(0,n):
#for i in range(0,n-1):
#   print(RandomArray[i]),
#   print(","),
#print(RandomArray[n-1])
