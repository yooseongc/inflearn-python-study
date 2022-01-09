
def sum_from_one(n):
    print(f'>>> sum from 1 to {n}\n')
    res = sum(n for n in range(1, n + 1))
    print(f'>>> sum from 1 to {n} finished.\n')
    return res

    