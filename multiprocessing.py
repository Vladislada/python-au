import time
import multiprocessing

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


answer = 0

for i in range(1000000):
    answer += if_prime(i)
def test_all(pool):
    answer = sum(pool.map(if_prime, list(range(1000000))))
    return answer

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print(__name__)
