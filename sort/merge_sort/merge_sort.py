from typing import List


class MergeSort:
    def __init__(self) -> None:
        """
        Initializes attributes of object
        """
        pass

    def merge_sort(self, data: List) -> List:
        """Sorts a list

        Args:
            data (List): list of data to be sorted

        Returns:
            List: returns the sorted list
        """

        if len(data) < 2:
            return data

        length_of_data: int = len(data)

        middle_index_of_list: int = length_of_data // 2

        left_split: List = data[:middle_index_of_list]
        right_split: List = data[middle_index_of_list:]

        self.merge_sort(left_split)
        self.merge_sort(right_split)

        self.merge_two_sorted_list(left_split, right_split, data)

    def merge_two_sorted_list(self, first_data: List, second_data: List, data: List):
        """Merges two list into one sorted list

        Args:
            first_data (List): first data to be merged
            second_data (List): second data to be merged

        Returns:
            List: sorted data merged
        """

        length_of_first_data = len(first_data)
        length_of_second_data = len(second_data)

        left_split_index_counter: int = 0
        right_split_index_counter: int = 0
        list_index_counter: int = 0

        while (
            left_split_index_counter < length_of_first_data
            and right_split_index_counter < length_of_second_data
        ):

            if (
                first_data[left_split_index_counter]
                < second_data[right_split_index_counter]
            ):
                data[list_index_counter] = first_data[left_split_index_counter]

                left_split_index_counter += 1

            else:

                data[list_index_counter] = second_data[right_split_index_counter]

                right_split_index_counter += 1

            list_index_counter += 1

        while left_split_index_counter < length_of_first_data:
            data[list_index_counter] = first_data[left_split_index_counter]
            left_split_index_counter += 1
            list_index_counter += 1

        while right_split_index_counter < length_of_second_data:
            data[list_index_counter] = second_data[right_split_index_counter]
            right_split_index_counter += 1
            list_index_counter += 1

        return data
