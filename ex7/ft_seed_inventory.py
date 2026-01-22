def ft_seed_inventory(str, num, type):
    if type == "packets":
        print(str.capitalize() + ' seeds:', num, type, "available")
        return
    if type == "grams":
        print(str.capitalize() + ' seeds:', num, type, "total")
        return
    if type == "area":
        print(str.capitalize() + ' seeds:', num, "square meters")
        return
