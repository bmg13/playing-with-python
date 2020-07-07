import random

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

def run_the_game():

    class Card:

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + " of " + self.suit


    class Deck:

        def __init__(self):
            self.deck = []  # start with an empty list
            for suit in suits:
              for rank in ranks:
                  self.deck.append(Card(suit, rank))

        def __str__(self):
            deck_comp = ""
            for card in self.deck:
                deck_comp = deck_comp + "\n" + card.__str__()
            return "The deck has these cards: \n" + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            # return single card
            return self.deck.pop()


    # represents the player
    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def add_card(self, card):
            self.cards.append(card)
            self.value = self.value + values[card.rank]

        # ace in blackjack is a specific scenario (being able to have the value of 1 or 11)
        # and an adjustement must be made
        def adjust_for_ace(self):
            # the (self.aces) predicate is a bool and represents the same as (self.aces > 0)
            while self.value > 21 and self.aces:
                self.value = self.value - 10
                self.aces = self.aces - 1


    class Chips:

        # the total value is arbitrary and other default value can be used
        def __init__(self, total=100):
            self.total = total
            self.bet = 0

        def win_bet(self):
            self.total = self.total + self.bet

        def lose_bet(self):
            self.total = self.total - self.bet


    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input("What is your bet?   "))
            except:
                print("Please provide a valid value.")
            else:
                if (chips.bet > chips.total):
                    print("You do not have that ammount of chips. You have {} chips.".format(chips.total))
                else:
                    break


    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()


    def hit_or_stand(deck, hand):
        global playing

        while True:
            value = input("Hit or Stand? H or S")
            if(value[0].upper() == "H"):
                hit(deck, hand)
            elif(value[0].upper() == "S"):
                print("Dealer's turn")
                playing = False
            else:
                print("Provide valid value. H or S only.")
                continue
            break
        
        return playing

    def player_busts(player, dealer, chips):
        print("Bust player. Dealer wins")
        chips.lose_bet()

    def player_wins(player, dealer, chips):
        print("Player wins")
        chips.win_bet()


    def dealer_busts(player, dealer, chips):
        print("Bust dealer. Player wins")
        chips.win_bet()


    def dealer_wins(player, dealer, chips):
        print("Dealer wins")
        chips.lose_bet()


    def push(player, dealer):
        print("TIE")


    def show_some(player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')


    def show_all(player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)


    while True:
        print("Let's start the game")

        # create a deck
        deck = Deck()
        # shuffle the deck
        deck.shuffle()

        # create a player
        player_hand = Hand()
         # pull a card
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)
        playing = True
        
        while playing:
            playing = hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)

            show_some(player_hand, dealer_hand)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if (player_hand.value > 21):
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if(dealer_hand.value > 21):
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print("\n Player's total chips: {}".format(player_chips.total))
        # Ask to play again
        new_game = input("New game? Y or N")
        if (new_game[0].upper() == "Y"):
            playing = True
        else:
            print("Thank you for playing")
            break
