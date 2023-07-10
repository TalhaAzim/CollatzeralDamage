class Memo(object):

    cache_factory = dict

    def __init__(self, fn):
        self.fn = fn
        self.cache = self.cache_factory()

    def __call__(self, n):
        #return self.cache.setdefault(n, self.fn(n))
        try:
            n = self.cache[n]
        except KeyError:
            k, n = n, self.fn(n)
            self.cache[k] = n
        finally:
            return n

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

    # just building a cache of results
    [collatzify(i) for i in range(2022)]

    a = [i for i in collatzseq(1987)]
    b = [i for i in collatzseq(1993)]
    c = [i for i in collatzseq(2016)]
    d = [i for i in collatzseq(2021)]

    print(
        ", ".join(
            f'{i[0]}: {len(i)}' for i in (a, b, c, d)
        )
    )


if __name__ == "__main__":
    main()
