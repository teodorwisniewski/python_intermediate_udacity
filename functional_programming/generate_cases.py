"""Generate an infinite stream of successively larger random lists."""
import random

def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))


def generate_cases():
    i = 0
    while True:
        l = random_list(i,0,10)
        yield l
        i += 1


if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)