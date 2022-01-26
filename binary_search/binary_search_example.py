from binary_search import BinarySearch


def main():

    my_list = [1, 3, 5, 7, 9]

    search = BinarySearch(data=my_list, item=3)

    print(search.binary_search())


if __name__ == "__main__":
    main()
