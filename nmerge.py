#!python3
"""Merge arbitrary sorted iterables"""


def nmerge(*args):

    data_sources = list(map(iter, filter(bool, args)))

    data_items = []
    data_source_idx = 0
    while data_source_idx < len(data_sources):
        try:
            data_items.append(next(data_sources[data_source_idx]))
        except StopIteration:
            data_sources.pop(data_source_idx)
            continue
        data_source_idx += 1

    while data_items:

        min_value = min(data_items)

        yield min_value

        min_idx = data_items.index(min_value)

        try:
            data_items[min_idx] = next(data_sources[min_idx])
        except StopIteration:
            data_items.pop(min_idx)
            data_sources.pop(min_idx)

if __name__ == "__main__":
    print(list(nmerge((7, 8, 9), [5, 5, 5, 5, 5, 6], (), range(0, 5), (v for v in ()))))
