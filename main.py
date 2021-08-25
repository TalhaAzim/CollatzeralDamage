def collatzify(n):
    return 3 * n + 1 if n % 2 else n // 2


def collatz(n, *, memo={2: 1}):
    yield n
    while n != 1:
        n = memo.setdefault(n, collatzify(n))
        yield n


m = {i: collatzify(i) for i in range(1, 2022)}

a = [i for i in collatz(1987, memo=m)]
b = [i for i in collatz(1993, memo=m)]
c = [i for i in collatz(2016, memo=m)]
d = [i for i in collatz(2021, memo=m)]

print(f'Calc saved {len(a)+ len(b) + len(c) + len(d) - len(m)}')

print(len(a), len(b), len(c))
