def ft_plant_age():
    nb = int(input('Enter plant age in days: '), 10)
    if nb > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
