"""
__getitem__ special method example

obj[key] is supported by the __getitem__ special method. In order to evaluate
my_collection[key], the interpreter calls my_collection.__getitem__(key).
"""
from collections import namedtuple

my_collection = ["A", "B", "C"]
print(type(my_collection))

# using a key on my list collection
# setting key as integer to access list indices
key = 1
# both return same value
print(my_collection[key])
print(my_collection.__getitem__(key))

my_collection_dict = {"X": 2, "Y": 1, "Z": 3}
print(my_collection[key])
print(my_collection_dict.__getitem__("Y"))


# Example 1-1 __getitem__ and __len__ methods
Card = namedtuple("Card", ["rank", "suit"])
# namedtuple builds classes of objects are just bundles of attributes with no custom methods.


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list("JQKA")]
    suits = "spades diamonds clubs hearts".split()

    def __int__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print(Card)
