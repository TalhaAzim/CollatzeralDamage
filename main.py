class Memo(object):

    cache_factory = dict

    def __init__(self, fn):
        self.fn = fn
        self.cache = self.cache_factory()

    def __call__(self, n):
        return self.cache.setdefault(n, self.fn(n))

    def __repr__(self):
        return self.fn.__repr__()


@Memo
def collatzify(n):
    return 3 * n + 1 if n % 2 else n // 2


def collatzseq(n):
    yield n
    while n != 1:
        n = collatzify(n)
        yield n


def main():

    [collatzify(i) for i in range(2022)]
    [fib(i) for i in range(10)]

    a = [i for i in collatzseq(1987)]
    b = [i for i in collatzseq(1993)]
    c = [i for i in collatzseq(2016)]
    d = [i for i in collatzseq(2021)]

    print(
        f'{a[0]}: {len(a)}, {b[0]}: {len(b)}, {c[0]}: {len(c)}, {d[0]}: {len(d)}'
    )


if __name__ == "__main__":
    main()
