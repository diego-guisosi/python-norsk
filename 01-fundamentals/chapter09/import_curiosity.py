from chapter09.airtravel import make_flights, console_card_printer
from pprint import pprint as pp

f, g = make_flights()
f.number()  # this method call structure is just a shortcut for the following call: Flight.number(f)

print(f.airline())
print(f.aircraft_model())
pp(f._seating)
print(f.num_available_seats())
print(f.num_seats())

# observe that the import of make_flight function is enough to make it work, even though Flight and Aircraft were not
# directly imported
# python resolves the function dependencies

# since functions are objects, it's possible to pass them as parameters to other functions
# this enable us to avoid creating unecessary classes and objects to simple solutions like console_card_printer
f.make_boarding_cards(console_card_printer)
# using delegation make possible to pass other implementations of card_printers to the same make_boarding_cards method

# showing polymorphism
print(g.airline())
print(g.aircraft_model())
pp(g._seating)
print(g.num_available_seats())
print(g.num_seats())

