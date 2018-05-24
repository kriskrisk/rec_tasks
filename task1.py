"""Implementation of solution of first task."""


def slice_seq(seq, size):
    """Returns list of pages."""
    pages_list = []
    current_beginning_index = 0
    current_end_index = current_beginning_index + size

    while current_end_index <= len(seq):
        pages_list.append(seq[current_beginning_index:current_end_index])
        current_beginning_index = current_end_index
        current_end_index = current_beginning_index + size

    pages_list.append(seq[current_beginning_index:])

    return pages_list


def paginate(seq, pages=0, items=0):
    """Returns slice_seq with correct size."""
    if pages == 0:
        if items == 0:
            print('Wrong arguments!')

        return slice_seq(seq, items)
    else:
        return slice_seq(seq, len(seq) / pages)
