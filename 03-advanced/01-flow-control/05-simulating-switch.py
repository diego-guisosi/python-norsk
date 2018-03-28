# Kafka - the adventure game you cannot win.


def play():

    position = (0, 0)
    alive = True

    while position:
        """
        if position == (0, 0):
            print("You are in a maze of twist passages, all alike.")
        elif position == (1, 0):
            print("You on a road in a dark forest. To the north, you can see a tower.")
        elif position == (1, 1):
            print("There is a tall tower here, with no obvious door. A path leads east.")
        else:
            print("There is nothing here.")
        """
        locations = {
            (0, 0): lambda: print("You are in a maze of twist passages, all alike."),
            (1, 0): lambda: print("You on a road in a dark forest. To the north, you can see a tower."),
            (1, 1): lambda: print("There is a tall tower here, with no obvious door. A path leads east."),
        }

        try:
            location_action = locations[position]
        except KeyError:
            print("There is nothing here")
        else:
            location_action()  # since lambdas are callables, we can use () to call them

        command = input()

        i, j = position

        """
        if command == "N":
            position = (i, j + 1)
        elif command == "E":
            position = (i + 1, j)
        elif command == "S":
            position = (i, j - 1)
        elif command == "W":
            position = (i - 1, j)
        elif command == "L":
            pass
        elif command == "Q":
            position = None
        else:
            print("I don't understand")
        """
        commands = {
            "N": (i, j + 1),
            "E": (i + 1, j),
            "S": (i, j - 1),
            "W": (i - 1, j),
            "L": (),
            "Q": None
        }

        try:
            commands[command]
        except KeyError:
            print("I don't understand")
        else:
            position = commands[command]

    print("Game over")


if __name__ == '__main__':
    play()