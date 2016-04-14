import random
import sys


class CardStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def shuffle(self):
        random.shuffle(self.items)

    def print_stack(self):
        all_cards = "[]"
        if self.size() > 0:
            all_cards = ""
            for i in range(len(self.items)):
                card = self.items[len(self.items) - 1 - i]
                all_cards += "[" + card.get_number() + " of " + card.get_suit() + "] "
        print all_cards


class Card:
    def __init__(self, suit, number):
        self.__suit = suit
        self.__number = number

    def get_suit(self):
        return self.__suit

    def get_number(self):
        return self.__number


def get_suit(suit_number):
    if suit_number == 0:
        return "Spades"
    elif suit_number == 1:
        return "Clubs"
    elif suit_number == 2:
        return "Diamonds"
    elif suit_number == 3:
        return "Hearts"


def get_next_card(number):
    if number == "A":
        return "2"
    elif number == "2":
        return "3"
    elif number == "3":
        return "4"
    elif number == "4":
        return "5"
    elif number == "5":
        return "6"
    elif number == "6":
        return "7"
    elif number == "7":
        return "8"
    elif number == "8":
        return "9"
    elif number == "9":
        return "10"
    elif number == "10":
        return "J"
    elif number == "J":
        return "Q"
    elif number == "Q":
        return "K"
    elif number == "K":
        return "A"


class ShuffledDeck:
    __shuffled_deck = CardStack()

    def __init__(self):
        for i in range(0, 4):
            if i != 1:
                ace = Card(get_suit(i), "A")
                self.__shuffled_deck.push(ace)
                two = Card(get_suit(i), "2")
                self.__shuffled_deck.push(two)
                three = Card(get_suit(i), "3")
                self.__shuffled_deck.push(three)
                four = Card(get_suit(i), "4")
                self.__shuffled_deck.push(four)
            five = Card(get_suit(i), "5")
            self.__shuffled_deck.push(five)
            six = Card(get_suit(i), "6")
            self.__shuffled_deck.push(six)
            seven = Card(get_suit(i), "7")
            self.__shuffled_deck.push(seven)
            eight = Card(get_suit(i), "8")
            self.__shuffled_deck.push(eight)
            nine = Card(get_suit(i), "9")
            self.__shuffled_deck.push(nine)
            ten = Card(get_suit(i), "10")
            self.__shuffled_deck.push(ten)
            jack = Card(get_suit(i), "J")
            self.__shuffled_deck.push(jack)
            queen = Card(get_suit(i), "Q")
            self.__shuffled_deck.push(queen)
            king = Card(get_suit(i), "K")
            self.__shuffled_deck.push(king)
        self.__shuffled_deck.shuffle()

    def get_remaining_stack_size(self):
        return self.__shuffled_deck.size()

    def draw(self):
        return self.__shuffled_deck.pop()

    def print_all_cards(self):
        print "Shuffled Deck Size: ", self.__shuffled_deck.size()
        self.__shuffled_deck.print_stack()


class FoundationStacks:
    __stack_plus_1 = CardStack()
    __stack_plus_2 = CardStack()
    __stack_plus_3 = CardStack()
    __stack_plus_4 = CardStack()

    def __init__(self):
        ace = Card(get_suit(1), "A")
        self.__stack_plus_1.push(ace)
        two = Card(get_suit(1), "2")
        self.__stack_plus_2.push(two)
        three = Card(get_suit(1), "3")
        self.__stack_plus_3.push(three)
        four = Card(get_suit(1), "4")
        self.__stack_plus_4.push(four)

    def is_valid_move_to_stack_1(self, card):
        return card.get_number() == get_next_card(self.__stack_plus_1.peek().get_number())

    def is_valid_move_to_stack_2(self, card):
        return card.get_number() == get_next_card(get_next_card(self.__stack_plus_2.peek().get_number()))

    def is_valid_move_to_stack_3(self, card):
        return card.get_number() == get_next_card(get_next_card(get_next_card(self.__stack_plus_3.peek().get_number())))

    def is_valid_move_to_stack_4(self, card):
        return card.get_number() == get_next_card(
            get_next_card(get_next_card(get_next_card(self.__stack_plus_4.peek().get_number()))))

    def is_valid_move_to_any_stack(self, card):
        return self.is_valid_move_to_stack_1(card) and self.is_valid_move_to_stack_2(card) and \
               self.is_valid_move_to_stack_3(card) and self.is_valid_move_to_stack_4(card)

    def is_valid_move_to_foundation_stack(self, card, stack):
        if stack == "F1" or stack == "f1":
            return self.is_valid_move_to_stack_1(card)
        elif stack == "F2" or stack == "f2":
            return self.is_valid_move_to_stack_2(card)
        elif stack == "F3" or stack == "f3":
            return self.is_valid_move_to_stack_3(card)
        elif stack == "F4" or stack == "f4":
            return self.is_valid_move_to_stack_4(card)

    def get_next_card_to_foundation_1(self):
        return get_next_card(self.__stack_plus_1.peek().get_number())

    def get_next_card_to_foundation_2(self):
        return get_next_card(get_next_card(self.__stack_plus_2.peek().get_number()))

    def get_next_card_to_foundation_3(self):
        return get_next_card(get_next_card(get_next_card(self.__stack_plus_3.peek().get_number())))

    def get_next_card_to_foundation_4(self):
        return get_next_card(
            get_next_card(get_next_card(get_next_card(self.__stack_plus_4.peek().get_number()))))

    def add_to_foundation_stack_1(self, card):
        self.__stack_plus_1.push(card)

    def add_to_foundation_stack_2(self, card):
        self.__stack_plus_2.push(card)

    def add_to_foundation_stack_3(self, card):
        self.__stack_plus_3.push(card)

    def add_to_foundation_stack_4(self, card):
        self.__stack_plus_4.push(card)

    def add_to_foundation_stack(self, card, stack):
        if stack == "F1" or stack == "f1":
            self.add_to_foundation_stack_1(card)
        elif stack == "F2" or stack == "f2":
            self.add_to_foundation_stack_2(card)
        elif stack == "F3" or stack == "f3":
            self.add_to_foundation_stack_3(card)
        elif stack == "F4" or stack == "f4":
            self.add_to_foundation_stack_4(card)

    def print_foundation_stack_1(self):
        sys.stdout.write("Foundation Stack 1: ")
        self.__stack_plus_1.print_stack()
        print "Next Card Required: " + self.get_next_card_to_foundation_1() + "\n"

    def print_foundation_stack_2(self):
        sys.stdout.write("Foundation Stack 2: ")
        self.__stack_plus_2.print_stack()
        print "Next Card Required: " + self.get_next_card_to_foundation_2() + "\n"

    def print_foundation_stack_3(self):
        sys.stdout.write("Foundation Stack 3: ")
        self.__stack_plus_3.print_stack()
        print "Next Card Required: " + self.get_next_card_to_foundation_3() + "\n"

    def print_foundation_stack_4(self):
        sys.stdout.write("Foundation Stack 4: ")
        self.__stack_plus_4.print_stack()
        print "Next Card Required: " + self.get_next_card_to_foundation_4() + "\n"

    def print_all_foundation_stacks(self):
        self.print_foundation_stack_1()
        self.print_foundation_stack_2()
        self.print_foundation_stack_3()
        self.print_foundation_stack_4()

    def is_foundation_1_filled(self):
        return self.__stack_plus_1.peek().get_number == "K"

    def is_foundation_2_filled(self):
        return self.__stack_plus_1.peek().get_number == "K"

    def is_foundation_3_filled(self):
        return self.__stack_plus_1.peek().get_number == "K"

    def is_foundation_4_filled(self):
        return self.__stack_plus_1.peek().get_number == "K"

    def are_all_foundation_stacks_filled(self):
        return self.is_foundation_1_filled() and self.is_foundation_2_filled() \
               and self.is_foundation_3_filled() and self.is_foundation_4_filled()


class WastePiles:
    __waste_stack_1 = CardStack()
    __waste_stack_2 = CardStack()
    __waste_stack_3 = CardStack()
    __waste_stack_4 = CardStack()

    def __init__(self):
        pass

    def add_to_waste_pile_1(self, card):
        self.__waste_stack_1.push(card)

    def add_to_waste_pile_2(self, card):
        self.__waste_stack_2.push(card)

    def add_to_waste_pile_3(self, card):
        self.__waste_stack_3.push(card)

    def add_to_waste_pile_4(self, card):
        self.__waste_stack_4.push(card)

    def draw_from_waste_pile_1(self):
        return self.__waste_stack_1.pop()

    def draw_from_waste_pile_2(self):
        return self.__waste_stack_2.pop()

    def draw_from_waste_pile_3(self):
        return self.__waste_stack_3.pop()

    def draw_from_waste_pile_4(self):
        return self.__waste_stack_4.pop()

    def draw_from_waste_pile(self, waste_pile):
        if waste_pile == "W1" or waste_pile == "w1":
            return self.draw_from_waste_pile_1()
        elif waste_pile == "W2" or waste_pile == "w2":
            return self.draw_from_waste_pile_2()
        elif waste_pile == "W3" or waste_pile == "w3":
            return self.draw_from_waste_pile_3()
        elif waste_pile == "W4" or waste_pile == "w4":
            return self.draw_from_waste_pile_4()

    def peek_at_top_card_from_waste_pile_1(self):
        return self.__waste_stack_1.peek()

    def peek_at_top_card_from_waste_pile_2(self):
        return self.__waste_stack_2.peek()

    def peek_at_top_card_from_waste_pile_3(self):
        return self.__waste_stack_3.peek()

    def peek_at_top_card_from_waste_pile_4(self):
        return self.__waste_stack_4.peek()

    def peek_at_top_card_from_waste_pile(self, waste_pile):
        if waste_pile == "W1" or waste_pile == "w1":
            return self.peek_at_top_card_from_waste_pile_1()
        elif waste_pile == "W2" or waste_pile == "w2":
            return self.peek_at_top_card_from_waste_pile_2()
        elif waste_pile == "W3" or waste_pile == "w3":
            return self.peek_at_top_card_from_waste_pile_3()
        elif waste_pile == "W4" or waste_pile == "w4":
            return self.peek_at_top_card_from_waste_pile_4()

    def print_waste_pile_1(self):
        sys.stdout.write("Waste Pile 1: ")
        self.__waste_stack_1.print_stack()
        print

    def print_waste_pile_2(self):
        sys.stdout.write("Waste Pile 2: ")
        self.__waste_stack_2.print_stack()
        print

    def print_waste_pile_3(self):
        sys.stdout.write("Waste Pile 3: ")
        self.__waste_stack_3.print_stack()
        print

    def print_waste_pile_4(self):
        sys.stdout.write("Waste Pile 4: ")
        self.__waste_stack_4.print_stack()
        print

    def print_all_waste_piles(self):
        self.print_waste_pile_1()
        self.print_waste_pile_2()
        self.print_waste_pile_3()
        self.print_waste_pile_4()

    def is_waste_pile_1_empty(self):
        return self.__waste_stack_1.is_empty()

    def is_waste_pile_2_empty(self):
        return self.__waste_stack_2.is_empty()

    def is_waste_pile_3_empty(self):
        return self.__waste_stack_3.is_empty()

    def is_waste_pile_4_empty(self):
        return self.__waste_stack_4.is_empty()

    def are_all_empty(self):
        return self.is_waste_pile_1_empty() and self.is_waste_pile_2_empty() \
               and self.is_waste_pile_3_empty() and self.is_waste_pile_4_empty()


class RevealedStack:
    __reveal_stack = CardStack()

    def __init__(self):
        pass

    def can_add_to_reveal_stack(self):
        return self.__reveal_stack.size() == 0

    def add_to_reveal_stack(self, card):
        self.__reveal_stack.push(card)

    def get_card_in_reveal_stack(self):
        return self.__reveal_stack.peek()

    def get_and_remove_card_in_reveal_stack(self):
        return self.__reveal_stack.pop()

    def print_revealed_card(self):
        sys.stdout.write("Revealed Card: ")
        self.__reveal_stack.print_stack()
        print

    def is_empty(self):
        return self.__reveal_stack.size() == 0
