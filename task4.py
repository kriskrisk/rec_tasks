"""Implementation of solution of fourth task."""
import sys
import string
from task3 import map_reduce


def map_function(key, value):
    """Maps a key to a value."""
    return key, value


def reduce_function(key, list_of_values):
    """Summs list of values."""
    return key, sum(list_of_values)


def main():
    """Main function."""
    word_list = []

    for file in sys.argv[1:]:
        with open(file) as curr_file:
            lines = curr_file.readlines()

            for line in lines:
                curr_line = line.lower().translate(str.maketrans('',
                                                                 '',
                                                                 string.punctuation)).split(" ")

                for word in curr_line:
                    word_list.append(word)

    map_reduce_function = map_reduce(map_function, reduce_function, 4)
    word_count = map_reduce_function(word_list)
    word_count = sorted(word_count, key=lambda element: element[1])
    word_count.reverse()

    for item in word_count[:20]:
        print(item)
    return


if __name__ == '__main__':
    main()
