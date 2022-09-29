

def main():
    arr_len = len(arr)
    res = [0] * arr_len
    for i in range(arr_len):
        original_index = i
        new_index = original_index - d
        res[new_index] = arr[original_index]


if __name__ == "__main__":
    main()
