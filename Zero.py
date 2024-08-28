import random
from time import sleep
import os

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

player_score = 0

def welcome_to_hi_low():
    return """\n\t\t\t\t\tWelcome to Hi - Low!\n\t\t\tA game where you have to guess what the next card will be.\n\t\t\t\tWill the next card be Higher or Lower?\n
              The rules are quite simple, pick Higher or Lower, if you pick right you get a point.\n\t\t\t\tMake it through the deck and see what
              \t\t\t\tYour high score will be!!"""

def player_name():
    name = input("Player please tell me your name.\n")
    return name

def welcome_player():
    return "Hi {n}, welcome to the game!\nLet's get right into it!"

def shuffle_the_deck(deck_to_shuffle):
    count = 7
    while count > 0:
        random.shuffle(deck_to_shuffle)
        count -= 1
    return deck_to_shuffle

def play_hi_low(shuffled_deck):
    while len(shuffled_deck) > 0:
        previous_card = ""
        for card in shuffled_deck:
            if previous_card == "":
                previous_card = card
                deck.remove(card)
            else:
                while answer.lower() != "higher" or answer.lower() != "lower":
                    answer = input("Is the next card going to be higher or lower than {p}?".format(p = previous_card))
                print("Flipped card is {c}.")
                if answer.lower == "higher" and previous_card.value < card.value:
                    print("Good guess!")
                    player_score += 1
                    previous_card = card
                    deck.remove(card)
                elif answer.lower() == "lower" and previous_card.value > card.value:
                    print("Good guess!")
                    player_score += 1
                    previous_card = card
                    deck.remove(card)
                else:
                    print("Sorry {c} was not {a} than {p}.".format(p = previous_card, a = answer, c = card))
                    previous_card = card
                    deck.remove(card)



print(welcome_to_hi_low())
input("Press \"Enter\" to continue.")
os.system("cls")
player1 = player_name()
card_in_play = ""
sleep(1)
print(welcome_player())
sleep(2)
print("""\n\t\t\tNow we're just going to shuffle the deck here, just give me a second or two.\n\t\t\t\tA person onece told me that shuffling the deck
      \t\t\t   seven time is the perfect shuffle!  So that's what we are doing. :D""")
shuffle_the_deck(deck)
sleep(3)
print("\n\t\t\tOk the deck is shuffled, lets get on with the game!!")
