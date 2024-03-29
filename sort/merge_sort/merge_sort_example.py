from merge_sort import MergeSort


def main():

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [2, 7, 8, 9],
        [1, 2, 3, 4, 5],
    ]

    m_sort = MergeSort()

    for test_case in test_cases:
        print(f"Version 1: {m_sort.merge_sort(test_case)}")
        print(f"Version 2: {m_sort.merge_sort_version_2(test_case)}")


if __name__ == "__main__":
    main()
