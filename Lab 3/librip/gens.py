import random

def field(items, *args):
    assert len(args) > 0
    for item in items:
        for j in args:
            if item[j] is not None:
                yield (item[j])


def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin,end)