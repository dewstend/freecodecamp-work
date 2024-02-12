import numpy as np


def calculate(list):
    arr = np.array(list)

    if arr.shape[0] != 9:
        raise ValueError("List must contain nine numbers.")

    arr = arr.reshape((3, 3))

    operations = [
        ["mean"],
        ["variance", "var"],
        ["standard deviation", "std"],
        ["max"],
        ["min"],
        ["sum"],
    ]

    calculations = {}

    # You'd wonder if developing this approach was cleaner/faster... idk, looks cool
    for operation in operations:
        name = operation[0]

        if len(operation) == 2:
            method = operation[1]
        else:
            method = name

        np_func = getattr(np, method)

        calculations[name] = [
            np_func(arr, axis=0).tolist(),
            np_func(arr, axis=1).tolist(),
            np_func(arr),
        ]

    return calculations
