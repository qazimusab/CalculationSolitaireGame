from objects import FoundationStacks
from objects import WastePiles
from objects import RevealedStack
from objects import ShuffledDeck


def main():
    foundation_stacks = FoundationStacks()
    waste_piles = WastePiles()
    reveal_stack = RevealedStack()
    shuffled_deck = ShuffledDeck()
    command = raw_input('Here are a list of commands to play the game: \n'
                        'F1 is Foundation Stack 1\n'
                        'F2 is Foundation Stack 2\n'
                        'F3 is Foundation Stack 3\n'
                        'F4 is Foundation Stack 4\n'
                        'W1 is Waste Pile 1\n'
                        'W2 is Waste Pile 2\n'
                        'W3 is Waste Pile 3\n'
                        'W4 is Waste Pile 4\n'
                        '\'D\' to draw\n'
                        '\'F1\' to move the revealed card into foundation stack 1\n'
                        '\'F2\' to move the revealed card into foundation stack 2\n'
                        '\'F3\' to move the revealed card into foundation stack 3\n'
                        '\'F4\' to move the revealed card into foundation stack 4\n'
                        '\'W1\' to move the revealed card into waste pile 1\n'
                        '\'W2\' to move the revealed card into waste pile 2\n'
                        '\'W3\' to move the revealed card into waste pile 3\n'
                        '\'W4\' to move the revealed card into waste pile 4\n'
                        '\'Move\' to move a card from a waste pile to a foundation stack\n'
                        '\'exit\' to exit the game\n'
                        'Type anything to start playing!\n\n')
    while command != "exit":
        command = raw_input('Enter a command\n')
        if command == 'D' or command == 'd':
            if reveal_stack.can_add_to_reveal_stack():
                reveal_stack.add_to_reveal_stack(shuffled_deck.draw())
            else:
                print "\nYou already have drawn a card.\n"
        elif command == 'F1' or command == 'f1':
            if not reveal_stack.is_empty() and foundation_stacks.is_valid_move_to_stack_1(
                    reveal_stack.get_card_in_reveal_stack()):
                foundation_stacks.add_to_foundation_stack_1(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'F2' or command == 'f2':
            if not reveal_stack.is_empty() and foundation_stacks.is_valid_move_to_stack_2(
                    reveal_stack.get_card_in_reveal_stack()):
                foundation_stacks.add_to_foundation_stack_2(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'F3' or command == 'f3':
            if not reveal_stack.is_empty() and foundation_stacks.is_valid_move_to_stack_3(
                    reveal_stack.get_card_in_reveal_stack()):
                foundation_stacks.add_to_foundation_stack_3(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'F4' or command == 'f4':
            if not reveal_stack.is_empty() and foundation_stacks.is_valid_move_to_stack_4(
                    reveal_stack.get_card_in_reveal_stack()):
                foundation_stacks.add_to_foundation_stack_4(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'W1' or command == 'w1':
            if not reveal_stack.is_empty():
                waste_piles.add_to_waste_pile_1(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'W2' or command == 'w2':
            if not reveal_stack.is_empty():
                waste_piles.add_to_waste_pile_2(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'W3' or command == 'w3':
            if not reveal_stack.is_empty():
                waste_piles.add_to_waste_pile_3(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'W4' or command == 'w4':
            if not reveal_stack.is_empty():
                waste_piles.add_to_waste_pile_4(reveal_stack.get_and_remove_card_in_reveal_stack())
            else:
                print "\nThis is not a valid move\n"
        elif command == 'Move':
            move_is_valid = True
            command = raw_input("\nWhich Waste Pile do you want to move from?\n")
            if command == "W1" or command == "W2" or command == "W3" or command == "W4" or \
                            command == "w1" or command == "w2" or command == "w3" or command == "w4":
                waste_pile_to_move_from = command
                if waste_pile_to_move_from == "W1" and waste_piles.is_waste_pile_1_empty():
                    move_is_valid = False
                elif waste_pile_to_move_from == "W2" and waste_piles.is_waste_pile_2_empty():
                    move_is_valid = False
                elif waste_pile_to_move_from == "W3" and waste_piles.is_waste_pile_3_empty():
                    move_is_valid = False
                elif waste_pile_to_move_from == "W4" and waste_piles.is_waste_pile_4_empty():
                    move_is_valid = False
                if move_is_valid:
                    command = raw_input("\nWhich Foundation Stack do you want to move this card to?\n")
                    if command == "F1" or command == "F2" or command == "F3" or command == "F4" or \
                                    command == "f1" or command == "f2" or command == "f3" or command == "f4":
                        foundation_stack_to_move_to = command
                        if not foundation_stacks.is_valid_move_to_foundation_stack(
                                waste_piles.peek_at_top_card_from_waste_pile(waste_pile_to_move_from),
                                foundation_stack_to_move_to):
                            move_is_valid = False
                        if move_is_valid:
                            foundation_stacks.add_to_foundation_stack(
                                waste_piles.draw_from_waste_pile(waste_pile_to_move_from), foundation_stack_to_move_to)
                        else:
                            print "\nThat is not a valid move.\n"
                    else:
                        print "\nYou entered an invalid foundation pile.\n"
                else:
                    print "\nThe waste pile you selected is empty.\n"
            else:
                print "\nYou entered an invalid waste pile.\n"
        else:
            print "\nYou entered an invalid command.\n"
        foundation_stacks.print_all_foundation_stacks()
        waste_piles.print_all_waste_piles()
        reveal_stack.print_revealed_card()
        print "The amount of cards remaining in the deck are: ", shuffled_deck.get_remaining_stack_size()
        print
        if shuffled_deck.get_remaining_stack_size() == 0 and waste_piles.are_all_empty() and \
                reveal_stack.is_empty() and foundation_stacks.are_all_foundation_stacks_filled():
            print "\nCongratulations! You won!\n"
            break
        if shuffled_deck.get_remaining_stack_size() == 0:
            waste_pile_1_card_can_not_go_in_any_foundation = False
            waste_pile_2_card_can_not_go_in_any_foundation = False
            waste_pile_3_card_can_not_go_in_any_foundation = False
            waste_pile_4_card_can_not_go_in_any_foundation = False
            if waste_piles.is_waste_pile_1_empty():
                waste_pile_1_card_can_not_go_in_any_foundation = True
            elif not foundation_stacks.is_valid_move_to_any_stack(waste_piles.peek_at_top_card_from_waste_pile_1()):
                waste_pile_1_card_can_not_go_in_any_foundation = True
            if waste_piles.is_waste_pile_2_empty():
                waste_pile_2_card_can_not_go_in_any_foundation = True
            elif not foundation_stacks.is_valid_move_to_any_stack(waste_piles.peek_at_top_card_from_waste_pile_2()):
                waste_pile_2_card_can_not_go_in_any_foundation = True
            if waste_piles.is_waste_pile_3_empty():
                waste_pile_3_card_can_not_go_in_any_foundation = True
            elif not foundation_stacks.is_valid_move_to_any_stack(waste_piles.peek_at_top_card_from_waste_pile_3()):
                waste_pile_3_card_can_not_go_in_any_foundation = True
            if waste_piles.is_waste_pile_4_empty():
                waste_pile_4_card_can_not_go_in_any_foundation = True
            elif not foundation_stacks.is_valid_move_to_any_stack(waste_piles.peek_at_top_card_from_waste_pile_4()):
                waste_pile_4_card_can_not_go_in_any_foundation = True
            if waste_pile_1_card_can_not_go_in_any_foundation and \
                    waste_pile_2_card_can_not_go_in_any_foundation and \
                    waste_pile_3_card_can_not_go_in_any_foundation and \
                    waste_pile_4_card_can_not_go_in_any_foundation:
                print "\nYou lost. Better luck next time!"
                break


if __name__ == '__main__':
    main()
