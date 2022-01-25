from linear_search import LinearSearch


def main():

    numbers = [8, 5, 15, 50]

    item = 5

    location = LinearSearch(data=numbers, item=item)

    print(location.search())


if __name__ == "__main__":
    main()
