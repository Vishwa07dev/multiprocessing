import time

start = time.perf_counter()


def func1():
    print('Waiting for some time')
    time.sleep(2)
    print('done waiting')

# Here both the below functions are running on the same process
func1()
func1()

'''
   We can make use of multi processing to speed things up
'''

finish = time.perf_counter()

print("Finished in " + str(round(finish - start, 2)))
