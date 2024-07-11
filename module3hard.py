# Подробнее о функциях
def calculate_structure_sum(*args):
    # print(args)
    args = args[0]
    summa = 0
    if isinstance(args, int):
        return summa + args
    elif isinstance(args, str):
        return summa + len(args)
    elif isinstance(args, list) or isinstance(args, set) or isinstance(args, tuple):
        for i in args:
            summa += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for i, j in args.items():
            summa += calculate_structure_sum(i)
            summa += calculate_structure_sum(j)
    else:
        print("Неизвестный тип данных args: ", type(args))
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

# Выходные данные (консоль):
# 99