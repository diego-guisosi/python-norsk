# repr has the role of uniquely represents an object
# it does not have to be bigger than str (because of detailed information).
# take a look at the following example:


class Table:

    def __init__(self, header, *data):
        self.header = header
        self.data = data
        assert len(header) == len(data)

    def _column_width(self, i):
        """
        Iterates all of the elements of the provided column to determine which one has the biggest string length
            Args
                i: column index of the elements that must be inspected
            Return
                The length of the biggest string of the provided column or the length of the header, if the header is
                bigger than the biggest string of the elements of the column
        """
        rslt = max(len(str(x)) for x in self.data[i])
        return max(len(self.header[i]), rslt)

    def __str__(self):
        col_count = len(self.header)
        col_widths = [self._column_width(i) for i in range(col_count)]
        format_specs = ['{{:{}}}'.format(col_widths[i]) for i in range(col_count)]

        rslt = []

        rslt.append(format_specs[i].format(self.header[i]) for i in range(col_count))
        rslt.append(('=' * col_widths[i] for i in range(col_count)))

        for row in zip(*self.data):
            rslt.append(
                [format_specs[i].format(row[i]) for i in range(col_count)]
            )

        rslt = (' '.join(r) for r in rslt)

        return '\n'.join(rslt)

    def __repr__(self):
        return 'Table(header={})'.format(self.header)


if __name__ == '__main__':
    t = Table(['First name', 'Last name'],
              ['Fred', 'George', 'Scooby'],
              ['Flinstone', 'Jetson', 'Doo'])

    print(str(t))
    print()
    print(repr(t))