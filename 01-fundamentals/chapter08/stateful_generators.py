def take(count, iterable):
    """
    Take items from the front of an iterable
    :param count: The maximum number of items to retrieve
    :param iterable: The source series
    :return: At most 'count' items from 'iterable'
    """
    counter = 0  # note that local variables state are kept during generator iteration
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :return: Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)  # it'll only be added to the set when the generator resumes


def run_pipeline():
    # it's possible to pipeline generators
    for item in take(3, distinct([1, 2, 3, 4, 5, 6, 7, 8])):
        print(item)


if __name__ == "__main__":
    run_pipeline()
