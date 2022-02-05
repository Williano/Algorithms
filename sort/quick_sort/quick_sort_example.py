from quick_sort import QuickSort


def main():

    q_sort = QuickSort()

    test_data = [[10, 5, 2, 3, -1], [], [2], [0, -1, 100, 45]]

    for element in test_data:
        print(q_sort.quick_sort(data=element))


if __name__ == "__main__":
    main()
