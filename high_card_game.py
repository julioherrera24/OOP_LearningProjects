import random

# constant dictionary to hold the value of the suits
SUITS = {
    "Diamonds": 1,
    "Hearts": 2,
    "Spades": 3,
    "Clubs": 4
}

# constant dictionary to hold the value of the ranks/value of each card
RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}


# class for playing card that has a rank and suit
class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def name(self):
        #  ex: this will return two of diamonds, three of hearts
        return " ".join([self.rank, "of", self.suit])


class Deck:
    def __init__(self):  # constructor that creates deck of cards and does initial shuffle
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(PlayingCard(suit, rank))
        self.shuffle()

    def add_card(self, card):  # at end of the game, cards are added back in the deck
        self.cards.append(card)

    def shuffle(self):   # shuffles cards that are in the deck between rounds
        random.shuffle(self.cards)

    def remove_top_card(self):  # take cards from deck to give to players
        return self.cards.pop()


class Hand:  # class that will contain the cards the player has in hand/current game
    def __init__(self):  # start off by playing having 0 cards
        self.cards = []

    def add_card(self, card):  # adds a card to player
        self.cards.append(card)

    def card_by_index(self, index):  # ability to select a card by index, useful for looking at a particular card in hand
        try:
            return self.cards[index]
        except Exception:
            return None

    def remove_card(self):  # ability to remove card from player hand
        if not self.cards:
            return None
        return self.cards.pop()


class Player:  # class that will hold player name and card(s) they are holding
    def __init__(self, name):
        self.name = name
        self.hand = Hand()


class View:
    def prompt_for_new_player(self):
        new_player = input("Type the name of the player: ")
        if new_player == "":
            return None
        return new_player

    def show_player_and_hand(self, player_name, hand):
        print("[" + player_name + "]")
        for card in hand.cards:
            if card.face_up:
                print(card.name())
            else:
                print("(hidden card)")

    def prompt_for_flip_cards(self):
        print("")
        prompt = input("Ready to see who won?")
        return True

    def show_winner(self, winner_name):
        print("")
        print("Congratulations", winner_name, "!")

    def prompt_for_new_game(self):
        print("")
        while True:
            prompt = input("Play again? Y/N: ")
            if prompt == "Y" or prompt == "y":
                return True
            if prompt == "N" or prompt == "n":
                return False
class Controller:
    def __init__(self, deck, view):
        # Model
        self.players = []
        self.deck = deck

        # View
        self.view = view

    def add_player(self, new_player):
        self.players.append(Player(new_player))

    def start_game(self):
        self.deck.shuffle()  # initially shuffles the deck
        for player in self.players:  # each player receives one card from deck
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)

    def evaluate_game(self):  # compares the cards of all the players and returns name of player with best card
        best_rank = None
        best_rank_suit = None
        best_candidate = None

        for player in self.players:
            this_rank = RANKS[player.hand.card_by_index(0).rank]
            this_suit = SUITS[player.hand.card_by_index(0).suit]
            if (best_rank is None
                    or (this_rank > best_rank)
                    or (this_rank == best_rank and this_suit > best_rank_suit)
                ):
                best_candidate = player.name
                best_rank = this_rank
                best_rank_suit = this_suit

        return best_candidate

    def rebuild_deck(self):  # goes through each player, collects all cards and shuffles cards for new game
        for player in self.players:
            while player.hand.cards:
                this_card = player.hand.remove_card()
                this_card.face_up = False
                self.deck.add_card(this_card)
        self.deck.shuffle()

    def run(self):
        while len(self.players) < 5:   # while there is no more than 5 players
            new_player = self.view.prompt_for_new_player()  # ask the view for the name of player
            if new_player is None:
                break  # ability to start game with less than 5 players
            self.add_player(new_player)

        while True:
            self.start_game()
            for player in self.players:  # next will show the players and their hands and display in view
                self.view.show_player_and_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()  # asks players if they are ready to see cards
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True  # flip cards face up and show players cards
                self.view.show_player_and_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())  # show the winner of the game
            if not self.view.prompt_for_new_game():
                break

            self.rebuild_deck()


deck = Deck()
view = View()

game_controller = Controller(deck, view)
game_controller.run()