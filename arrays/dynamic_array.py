

def dynamicArray():
    mylist = []
    # append
    mylist.append(3)
    mylist.append(4)

    print(mylist)

    # fill it with values
    fill = [0 for x in range(5)]
    print(fill)

    # multi dimensional array
    row = 5
    col = 6
    multi = [[0 for x in range(row)], [0 for y in range(col)]]
    print(multi)


def dynamicArray2(n, queries):
    arr = [[] for xx in range(n)]
    lastAnswer = 0
    answerlist = []

    for q in queries:
        idx = (q[1] ^ lastAnswer) % n

        if q[0] == 1:
            arr[idx].append(q[2])

        elif q[0] == 2:
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            answerlist.append(lastAnswer)

    return answerlist


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    lastArray = []
    for i in range(len(queries)):
        idx = (queries[i][1] ^ lastAnswer) % n
        if queries[i][0] == 1:
            arr[idx].append(queries[i][2])
        elif queries[i][0] == 2:
            lastAnswer = arr[idx][queries[i][2] % len(arr[idx])]
            lastArray.append(lastAnswer)
    return lastArray


def dynamicArrayMine():
    arr = [[] for x in range(n)]
    answers = []
    lastAnswer = 0

    for q in queries:
        idx = q[1] ^ lastAnswer % n

        if q[0] == 1:
            arr[idx].append(q[2])

        elif q[0] == 2:
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


if __name__ == "__main__":
    dynamicArray()
