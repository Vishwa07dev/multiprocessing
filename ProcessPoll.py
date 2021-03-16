import time
import concurrent.futures

start = time.perf_counter()


def func1():
    print('Waiting for some time')
    time.sleep(2)
    print('done waiting')


def func2(wait_time):
    print('Waiting for  time : '+ str( wait_time) + ' seconds in func2')
    time.sleep(wait_time)
    return 'done waiting for some time '+ str( wait_time) + 'in func2'

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
with concurrent.futures.ProcessPoolExecutor() as executor :
    '''
    f1 = executor.submit(func1)
    f2 = executor.submit(func1)
    '''
    '''
    results = [executor.submit(func2, 2) for _ in range(10)]
    '''
    secs = [5,4,3,2,1]
    '''
    results = [executor.submit(func2,sec) for sec in secs]
    '''
    results = executor.map(func2 , secs) #every item from secs will be applied to func2

    for result in results:   # Exception will be raised only during iteration

        print(result)
    '''
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    '''


'''
   We can make use of multi processing to speed things up
'''

finish = time.perf_counter()

print("Finished in " + str(round(finish - start, 2)))
