# functions can be defined inside other functions: local functions
# everytime the outer function runs, the inner function is created again and assigned to last_letter

store = []


def sort_by_last_letter(strings):
    # local  function below
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)


if __name__ == '__main__':
    sorted_by_last_letter = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
    sorted_by_last_letter = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
    sorted_by_last_letter = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
    print(sorted_by_last_letter)
    print(store)


# it's important to know that local functions are not members of the containing functions
# they are only function name binding on the containing function body
# so, this kind of call does not work: sort_by_last_letter.last_letter
