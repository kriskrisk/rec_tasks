from task3 import map_reduce
import sys
import string


def map_function(key, value):
    return key, value


def reduce_function(key, list_of_values):
    return key, sum(list_of_values)


def main():
    word_list = []

    for file in sys.argv[1:]:
        with open(file) as curr_file:
            lines = curr_file.readlines()

            for line in lines:
                curr_line = line.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")

                for word in curr_line:
                    word_list.append(word)

    map_reduce_function = map_reduce(map_function, reduce_function, 4)
    word_count = map_reduce_function(word_list)
    word_count = sorted(word_count, key=lambda item: item[1])

    for item in word_count[:20]:
        print(item)
    return
