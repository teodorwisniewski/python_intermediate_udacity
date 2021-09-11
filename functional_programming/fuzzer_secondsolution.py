from itertools import count
import random


def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))


def generate_cases():
    generator_expr = (
        random_list(i) for i in count()
    )
    return generator_expr

if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)

    for i in count():
        if i > 10:
            break
        print(i, "Teodor"*i)