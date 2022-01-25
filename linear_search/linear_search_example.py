from linear_search import linear_search


def main():

    numbers = [8, 5, 15, 50]

    item = 5

    location = linear_search(data=numbers, item=item)

    print(location)


if __name__ == "__main__":
    main()
