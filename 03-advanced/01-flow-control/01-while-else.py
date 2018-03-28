# else clause will be executed when the condition fail


def is_comment(item):
    # "and" is a short-circuit logical operator
    return isinstance(item, str) and item.startswith('#')


def execute(program):
    """ Execute a stack program

    Args:
        program: Any stack-like containing where each item in the stack is callable operators or non-callable operands.
            The top most items on the stack may be strings beginning with '#' for the purposes of documentation.
            Stack-like means support for:

                item = stack.pop()  # Remove and return the top item
                stack.append(item)  # Push an item to the top
                if stack:           # False in a boolean context when empty
    """
    # Find the start of the 'program' by skipping any item which is a comment
    while program:  # iterables are evaluated to false when they have no elements
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break  # if a break statement is used inside the while loop, else is not executed
    else:  # nobreak
        print("Empty program!")
        return  # this statement will exit the program (not the loop). At this point, the loop does not exist anymore

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break  # if a break statement is used inside the while loop, else is not executed
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:  # nobreak
        print("Program successful.")
        print("Result: ", pending)

    print("Finished")


if __name__ == '__main__':
    import operator

    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul
    )))

    execute(program)