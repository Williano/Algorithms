from selection_sort import SelectionSort


def main():

    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5],
        [5, 3, 6, 2, 10],
    ]

    for element in tests:

        selection_sort = SelectionSort(data=element)

        print(selection_sort.selection_sort())


if __name__ == "__main__":
    main()
