stock_prices = [101, 102, 103]


def print_position():
    # print the position
    for i in range(len(stock_prices)):
        if stock_prices[i] == 102:
            return i


def print_all():
    for i in stock_prices:
        print(i)


def instert_new():
    stock_prices.insert(1, 303)
    print(stock_prices)


def remove_item():
    print(stock_prices)
    stock_prices.remove(1)
    print(stock_prices)


def twod_arrays():
    # example
    a = [
        [1, 2, 3, 4, 5],
        ["a", "b", "t", 7]
    ]

    for i in a:
        for j in i:
            print(j)


def exercise_one():
    # initialize the 2d array
    a_2d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # replace no 6 with 99
    a_2d[1][1] = 99
    print(a_2d[1][1])

    # print
    for i in a_2d:
        for j in i:
            print(j)

    # diagonal elements
    # which are 1,6,10
    total = 0
    for i in range(len(a_2d)):
        total += a_2d[i][i]
    print(total)


if __name__ == "__main__":
    #print("print_position---> "+str(print_position()))
    #print("print_all---> "+str(print_all()))
    # instert_new()
    # remove_item()
    # twod_arrays()
    exercise_one()
