def median(iterable):
    """ Obtain the central value of a series

    Sorts the iterable and returns the middle value if there is an even number of elements,
    or the arithmetic mean of the middle two elements if there is an even number of elements

    Args:
        iterable: A series of sortable items.

    Returns:
        The median value.
    """
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() args is an empty sequence")
    median_index = (len(items) -1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0


def main():
    try:
        median([])
    except ValueError as e:
        # Although exceptions can receive multiple string parameters in the constructor, it is highly recommended
        # not doing so. In pratice, only a single string argument should be used
        print("Payload: ", e.args)
        print("Payload: ", str(e))


if __name__ == '__main__':
    main()