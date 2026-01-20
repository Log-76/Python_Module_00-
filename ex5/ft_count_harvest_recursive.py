def help(n):
    if n > 0:
        help(n - 1)
    print('day', n)


def ft_count_harvest_recursive():
    n = int(input('Days until harvest:'), 10)
    help(n - 1)
    print('Harvest time!')
