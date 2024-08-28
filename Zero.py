class Card:
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value
    def __repr__(self):
        return "{n} of {s}".format(n = self.number, s = self.suit)

Ace_of_Spades = Card("Spades", "Ace", 14)     
Two_of_Spades = Card("Spades", "Two", 2)
Three_of_Spades = Card("Spades", "Three", 3)
Four_of_Spades = Card("Spades","Four", 4)
Five_of_Spades = Card("Spades","Five", 5)
Six_of_Spades = Card("Spades","Six", 6)
Seven_of_Spades = Card("Spades","Seven", 7)
Eight_of_Spades = Card("Spades","Eight", 8)
Nine_of_Spades = Card("Spades", "Nine", 9)
Ten_of_Spades = Card("Spades", "Ten", 10)
Jack_of_Spades = Card("Spades", "Jack", 11)
Queen_of_Spades = Card("Spades", "Queen", 12)
King_of_Spades = Card("Spades", "King", 13)
Ace_of_Diamonds = Card("Diamonds", "Ace", 14)
Two_of_Diamonds = Card("Diamonds", "Two", 2)
Three_of_Diamonds = Card("Diamonds", "Three", 3)
Four_of_Diamonds = Card("Diamonds", "Four", 4)
Five_of_Diamonds = Card("Diamonds", "Five", 5)
Six_of_Diamonds = Card("Diamonds", "Six", 6)
Seven_of_Diamonds = Card("Diamonds", "Seven", 7)
Eight_of_Diamonds = Card("Diamonds", "Eight", 8)
Nine_of_Diamonds = Card("Diamonds", "Nine", 9)
Ten_of_Diamonds = Card("Diamonds", "Ten", 10)
Jack_of_Diamonds = Card("Diamonds", "Jack", 11)
Queen_of_Diamonds = Card("Diamonds", "Queen", 12)
King_of_Diamonds = Card("Diamonds", "King", 13)
Ace_of_Clubs = Card("Clubs", "Ace", 14)
Two_of_Clubs = Card("Clubs", "Two", 2)
Three_of_Clubs = Card("Clubs", "Three", 3)
Four_of_Clubs = Card("Clubs", "Four", 4)
Five_of_Clubs = Card("Clubs", "Five", 5)
Six_of_Clubs = Card("Clubs", "Six", 6)
Seven_of_Clubs = Card("Clubs", "Seven", 7)
Eight_of_Clubs = Card("Clubs", "Eight", 8)
Nine_of_Clubs = Card("Clubs", "Nine", 9)
Ten_of_Clubs = Card("Clubs", "Ten", 10)
Jack_of_Clubs = Card("Clubs", "Jack", 11)
Queen_of_Clubs = Card("Clubs", "Queen", 12)
King_of_Clubs = Card("Clubs", "King", 13)
Ace_of_Hearts = Card("Hearts", "Ace", 14)
Two_of_Hearts = Card("Hearts", "Two", 2)
Three_of_Hearts = Card("Hearts","Three", 3)
Four_of_Hearts = Card("Hearts", "Four", 4)
Five_of_Hearts = Card("Hearts", "Five", 5)
Six_of_Hearts = Card("Hearts", "Six", 6)
Seven_of_Hearts = Card("Hearts", "Seven", 7)
Eight_of_Hearts = Card("Hearts", "Eight", 8)
Nine_of_Hearts = Card("Hearts", "Nine", 9)
Ten_of_Hearts = Card("Hearts", "Ten", 10)
Jack_of_Hearts = Card("Hearts", "Jack", 11)
Queen_of_Hearts = Card("Hearts", "Queen", 12)
King_of_Hearts = Card("Hearts", "King", 13)


deck = [Ace_of_Hearts, Two_of_Hearts, Three_of_Hearts, Four_of_Hearts, Five_of_Hearts, Six_of_Hearts, Seven_of_Hearts, Eight_of_Hearts,
        Nine_of_Hearts, Ten_of_Hearts, Jack_of_Hearts, Queen_of_Hearts, King_of_Hearts, Ace_of_Clubs, Two_of_Clubs, Three_of_Clubs, Four_of_Clubs,
        Five_of_Clubs, Six_of_Clubs, Seven_of_Clubs, Eight_of_Clubs, Nine_of_Clubs, Ten_of_Clubs, Jack_of_Clubs, Queen_of_Clubs, King_of_Clubs,
        King_of_Diamonds, Queen_of_Diamonds, Jack_of_Diamonds, Ten_of_Diamonds, Nine_of_Diamonds, Eight_of_Diamonds, Seven_of_Diamonds, Six_of_Diamonds,
        Five_of_Diamonds, Four_of_Diamonds, Three_of_Diamonds, Two_of_Diamonds, Ace_of_Diamonds, King_of_Spades, Queen_of_Spades, Jack_of_Spades,
        Ten_of_Spades, Nine_of_Spades, Eight_of_Spades, Seven_of_Spades, Six_of_Spades, Five_of_Spades, Four_of_Spades, Three_of_Spades, Two_of_Spades,
        Ace_of_Spades]

def welcome_to_hi_low():
    return """\n\t\t\t\t\tWelcome to Hi - Low!\n\t\t\tA game where you have to guess what the next card will be.\n\t\t\t\tWill the next card be Higher or Lower?\n
              The rules are quite simple, pick Higher or Lower, if you pick right you get a point.\n\t\t\t\tMake it through the deck and see what
              \t\t\t\tYour high score will be!!"""
