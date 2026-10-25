# MultiThreading
from threading import Thread
from time import sleep, time
from multiprocessing import Process

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello ", i+1)
#             sleep(0.2)

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi ", i+1)

# if __name__ == '__main__':

#     t1 = Hello()
#     sleep(0.2)
#     t2 = Hi()

#     t1.start()
#     t2.start()

# Threads using Functions

# print("Threads using Functions")
def hello():
    for i in range(5):
        print("Hello ", i+1)
        sleep(0.3)

def hi():
    for i in range(5):
        print("Hi ", i+1)

if __name__ == '__main__':

    t1 = Thread(target=hello)
    sleep(0.2)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Bye")


# CPU bound example
def download(file_name):
    print("Downloading file....", file_name)
    sleep(0.5)
    print("Dowload Complete")

if __name__ == '__main__':

    files = ['video.mp4', 'image.png', 'data.csv']

    start = time()
    for f in files:
        download(f)
    end = time()
    print(f" serial time {end - start:.2f} seconds")

    threads = []

    start = time()
    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end = time()

    print(f"parallel with threads time {end - start:.2f} seconds")
    print('Bye')

# understand with one more example
def calculate(n1, n2):
    sum = 0
    for n in range(n1, n2):
        sum += n*n

if __name__ == '__main__':

    num = 50_000_000
    start = time()
    calculate(0, num)
    end = time()

    print(f"serial time {end - start:.2f} seconds")

    mid = num // 2

    t1 = Thread(target=calculate, args=(0, mid))
    t2 = Thread(target=calculate, args=(mid, num))

    start = time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time()

    print(f"parallel with threads time {end - start:.2f} seconds")

# Multiprocessing
def calculate(n1, n2):
    sum = 0
    for n in range(n1, n2):
        sum += n*n

if __name__ == '__main__':

    num = 50_000_000
    start = time()
    calculate(0, num)
    end = time()

    print(f"serial time {end - start:.2f} seconds")

    mid = num // 2

    t1 = Process(target=calculate, args=(0, mid))
    t2 = Process(target=calculate, args=(mid, num))

    start = time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time()

    print(f"parallel with process time {end - start:.2f} seconds")
