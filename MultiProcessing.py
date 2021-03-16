import time
import multiprocessing

start = time.perf_counter()


def func1():
    print('Waiting for some time')
    time.sleep(2)
    print('done waiting')


def func2(wait_time):
    print('Waiting for some time in func2')
    time.sleep(wait_time)
    print('done waiting for some time in func2')

# Here both the below functions are running on the same process

'''
p1 =  multiprocessing.Process(target=func1)
p2 = multiprocessing.Process(target=func1)

p1.start()
p2.start()

p1.join()
p2.join()

'''

'''
Creating processes in loop
'''

processess = []

for _ in range(12):
    p = multiprocessing.Process(target=func2 , args=[1.5])
    p.start()
    processess.append(p)


for process in processess:
    process.join()

'''
   We can make use of multi processing to speed things up
'''

finish = time.perf_counter()

print("Finished in " + str(round(finish - start, 2)))
