import string
from itertools import groupby


def map_function(key, value):
    return key, value


def reduce_function(key, list_of_values):
    return key, sum(list_of_values)


def group_mappings(list_of_mappings):
    grouped_mappings = []

    for key, group in groupby(list_of_mappings, lambda x: x[0]):
        new_values = []

        for mapping in group:
            new_values.append(mapping[1])

        grouped_mappings.append((key, new_values))

    return grouped_mappings


def map_reduce(map_func, reduce_func, num_workers):
    file_list = input("File list: ")
    list_of_mappings = []

    for file in file_list:
        with open(file) as curr_file:
            lines = curr_file.readlines()

            for line in lines:
                curr_line = line.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")

                for word in curr_line:
                    list_of_mappings.append(map_func(word, 1))

    list_of_mappings = sorted(list_of_mappings, key=lambda item: item[0])

    grouped_mapings = group_mappings(list_of_mappings)

    return reduce_func(grouped_mapings)


def map_reduce(map_func, reduce_func, num_workers):
    def map_reduce_func(word_list):
        list_of_mappings = []

        for word in word_list:
            list_of_mappings.append(map_func(word, 1))

        list_of_mappings = sorted(list_of_mappings, key=lambda item: item[0])
        grouped_mapings = group_mappings(list_of_mappings)
        mapped_and_reduced = []

        for mapping in grouped_mapings:
            mapped_and_reduced.append(reduce_func(mapping))

        return mapped_and_reduced

    return map_reduce_func
