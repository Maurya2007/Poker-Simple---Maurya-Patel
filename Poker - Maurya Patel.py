import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [(rank, suit) for suit in suits for rank in ranks]

def deal_hand(deck, num_cards):
    return random.sample(deck, num_cards)

def evaluate_hand(hand):
    return "High card"

def display_hand(hand, player_name):
    print(f"{player_name}'s hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}. {card[0]} of {card[1]}")

def play_poker():
    print("Welcome to Poker!")
    
    player_hand = deal_hand(deck, 5)
    computer_hand = deal_hand(deck, 5)
    
    print("\n")
    display_hand(player_hand, "Your")
    print("\n")
    print("Computer's hand:")
    print("Face down card")
    for _ in range(1, len(computer_hand)):
        print("Unknown card")
    
    discard = input("\nEnter the positions of cards you want to discard (e.g., 1 3 5), or press Enter to keep your hand: ")
    if discard:
        discard_positions = [int(pos) - 1 for pos in discard.split()]
        for pos in discard_positions:
            player_hand[pos] = deal_hand(deck, 1)[0]
    
    print("\n")
    display_hand(computer_hand, "Computer's")
    
    player_hand_value = evaluate_hand(player_hand)
    computer_hand_value = evaluate_hand(computer_hand)
    
    print("\nResult:")
    print("Your hand:", player_hand_value)
    print("Computer's hand:", computer_hand_value)
    if player_hand_value > computer_hand_value:
        print("Congratulations! You win!")
    elif player_hand_value < computer_hand_value:
        print("Computer wins!")
    else:
        print("It's a tie!")

play_poker()
