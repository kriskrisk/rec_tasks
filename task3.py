from itertools import groupby
import multiprocessing
import queue


def group_mappings(list_of_mappings):
    grouped_mappings = []

    for key, group in groupby(list_of_mappings, lambda x: x[0]):
        new_values = []

        for mapping in group:
            new_values.append(mapping[1])

        grouped_mappings.append((key, new_values))

    return grouped_mappings


def map_reduce(map_func, reduce_func, num_workers):
    def map_function(process_name, tasks, results):
        print('[%s] evaluation routine starts' % process_name)

        # while True:
        #     try:
        #         word = tasks.get()
        #     except queue.Empty:
        #         results.put(-1)
        #         break
        #     else:
        #         results.put(map_func(word[0], word[1]))

        # while not tasks.empty():
        #     word = tasks.get()
        #     results.put(map_func(word[0], word[1]))
        #
        # results.put(-1)

        while True:
            word = tasks.get()
            if word == -1:

                results.put(-1)
                break
            else:
                results.put(map_func(word[0], word[1]))

        return

    def reduce_function(process_name, tasks, results):
        print('[%s] evaluation routine starts' % process_name)

        # while True:
        #     try:
        #         map_object = tasks.get()
        #     except queue.Empty:
        #         results.put(-1)
        #         break
        #     else:
        #         results.put(reduce_func(map_object[0], sum(map_object[1])))

        # while not tasks.empty():
        #     map_object = tasks.get()
        #     results.put(reduce_func(map_object[0], sum(map_object[1])))
        #
        # results.put(-1)

        while True:
            map_object = tasks.get()
            if map_object == -1:

                results.put(-1)
                break
            else:
                results.put(reduce_func(map_object[0], map_object[1]))

        return

    def map_reduce_func(word_list):
        list_of_mappings = []

        if __name__ == "task3":
            manager = multiprocessing.Manager()
            tasks = manager.Queue()
            results = manager.Queue()
            pool = multiprocessing.Pool(processes=num_workers)
            processes = []

            for i in range(num_workers):
                process_name = 'P%i' % i
                new_process = multiprocessing.Process(target=map_function, args=(process_name, tasks, results))
                processes.append(new_process)
                new_process.start()

            for word in word_list:
                tasks.put((word, 1))

            num_finished_processes = 0

            for i in range(num_workers):
                tasks.put(-1)

            while True:
                if not results.empty():
                    new_result = results.get()

                    if new_result == -1:
                        num_finished_processes += 1

                        if num_finished_processes == num_workers:
                            break
                    else:
                        list_of_mappings.append(new_result)

        list_of_mappings = sorted(list_of_mappings, key=lambda item: item[0])
        grouped_mapings = group_mappings(list_of_mappings)
        mapped_and_reduced = []

        if __name__ == "task3":
            manager = multiprocessing.Manager()
            tasks = manager.Queue()
            results = manager.Queue()
            pool = multiprocessing.Pool(processes=num_workers)
            processes = []

            for i in range(num_workers):
                process_name = 'P%i' % i
                new_process = multiprocessing.Process(target=reduce_function, args=(process_name, tasks, results))
                processes.append(new_process)
                new_process.start()

            for mapping in grouped_mapings:
                tasks.put(mapping)

            num_finished_processes = 0

            for i in range(num_workers):
                tasks.put(-1)

            while True:
                if not results.empty():
                    new_result = results.get()

                    if new_result == -1:
                        num_finished_processes += 1

                        if num_finished_processes == num_workers:
                            break
                    else:
                        mapped_and_reduced.append(new_result)

        return mapped_and_reduced

    return map_reduce_func
