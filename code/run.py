import blackjack
import graphics
from collections import namedtuple
import pygame
import time

def reset(hands,deck,card):
    if len(deck.cards) < 4:
        reshuffle(deck,card)
    hands.player.reset()
    hands.dealer.reset()
    hands.player.deal(deck)
    hands.dealer.deal(deck)

def is_over_buttton(but,pos):
    if pos[0] > but.x and pos[0] < but.x + but.width:
        if pos[1] > but.y and pos[1] < but.y + but.height:
            return True
    return False

def update_display(turn,PYGAME,COLOURS,BUTTONS,hands):
    show_full_dealer = False

    PYGAME.screen.fill(COLOURS.background)

    if turn == "players_turn":
        graphics.draw_half_hand(PYGAME,COLOURS,hands)

    elif turn == "dealers_turn":
        graphics.draw_hand(PYGAME,hands.dealer)
        show_full_dealer = True

    graphics.draw_game_elements(PYGAME,COLOURS,BUTTONS,hands,show_full_dealer)
    PYGAME.pygame.display.update()

def dealer_turn(PYGAME,COLOURS,BUTTONS,hands,deck,card):
    hands.dealer.adjust_for_ace()

    while(hands.dealer.score < 17):
        if len(deck.cards) == 0:
            reshuffle(deck,card)
        hands.dealer.hit(deck)
        #hands.dealer.calculate_score()
        hands.dealer.adjust_for_ace()

    update_display("dealers_turn",PYGAME,COLOURS,BUTTONS,hands)

def compare(hands):
    result = " hello"
    if hands.dealer.score > 21:
        result = "dealer bust"
    else:
        if hands.player.score == hands.dealer.score:
            result = "tie"
        elif hands.player.score > hands.dealer.score:
            result = "player wins"
        else:
            result = "dealer wins"

    return result

def reshuffle(deck,card):
    deck.build_deck(card)
    deck.shuffle()

def game_loop(PYGAME,COLOURS,BUTTONS,DISPLAY,card,deck,hands):
    crashed = False
    stand_pressed = False

    while not crashed:
        if stand_pressed:
            dealer_turn(PYGAME,COLOURS,BUTTONS,hands,deck,card)
            result = compare(hands)
            graphics.message_display(PYGAME,COLOURS,DISPLAY,result)
            stand_pressed = False

        reset(hands,deck,card)

        while not stand_pressed:
            if crashed == True:
                break

            if hands.player.score >= 21:
                if hands.player.score > 21:
                    text = "player bust"
                elif hands.player.score == 21:
                    text = "player has 21"

                graphics.message_display(PYGAME,COLOURS,DISPLAY,text)
                break

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    if is_over_buttton(BUTTONS.hit,pos):
                        if len(deck.cards) == 0:
                            reshuffle(deck,card)

                        hands.player.hit(deck)
                    if is_over_buttton(BUTTONS.stand,pos):
                        stand_pressed = True

                if event.type == pygame.QUIT:
                    crashed = True

            hands.player.adjust_for_ace()
            hands.dealer.calculate_initial_dealer_score()
            update_display("players_turn",PYGAME,COLOURS,BUTTONS,hands)

    pygame.display.quit()
    pygame.quit()

def main():
    card = namedtuple("card","rank suit")

    deck = blackjack.Deck()
    deck.build_deck(card)
    deck.shuffle()

    dealer = blackjack.Hand("dealer",80,200)
    player = blackjack.Hand("player",80,500)

    width = 1500
    height = 1500

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    hand_tuple = namedtuple("hand_tuple", "player dealer")
    hands = hand_tuple(player = player, dealer = dealer)

    pygame_tuple = namedtuple("pygame_tuple","pygame screen")
    PYGAME = pygame_tuple(pygame = pygame, screen = screen)

    width_height = namedtuple("width_height","width height")
    DISPLAY = width_height(width = width, height = height)

    colours = namedtuple("colours","black green red yellow background")

    COLOURS = colours(
        black = (0,0,0),
        green = (0,255,0),
        red = (255,0,0),
        yellow = (255,255,0),
        background = (152,198,195))

    button = namedtuple("button"," x y width height colour text text_colour")

    hit = button(
        x = 80, y = 700, width = 100, height = 80 ,
        colour = COLOURS.green,
        text = "hit",
        text_colour = COLOURS.black)

    stand = button(
        x = 200, y = 700, width = 100, height = 80,
        colour = COLOURS.yellow,
        text = "stand",
        text_colour = COLOURS.black)


    buttons = namedtuple("button", "hit stand")
    BUTTONS = buttons(hit = hit, stand = stand)

    game_loop(PYGAME,COLOURS,BUTTONS,DISPLAY,card,deck,hands)

if __name__ == "__main__":
    main()
