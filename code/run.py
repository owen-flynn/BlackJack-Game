import blackjack
import graphics
from collections import namedtuple
import pygame
import time

def reset(hands,deck):
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
    PYGAME.screen.fill(COLOURS.background)

    if turn == "players_turn":
        hands.player.calculate_score()
        hands.dealer.calculate_initial_dealer_score()
        graphics.draw_half_hand(PYGAME,COLOURS,hands)
    elif turn == "dealers_turn":
        hands.dealer.calculate_score()
        graphics.draw_hand(PYGAME,hands.dealer)

    graphics.draw_game_elements(PYGAME,COLOURS,BUTTONS,hands)
    PYGAME.pygame.display.update()

def dealer_turn(PYGAME,COLOURS,BUTTONS,hands,deck):
    hands.dealer.calculate_score()

    while(hands.dealer.score < 17):
        hands.dealer.hit(deck)
        hands.dealer.calculate_score()

    update_display("dealers_turn",PYGAME,COLOURS,BUTTONS,hands)

def game_loop(PYGAME,COLOURS,BUTTONS,card,deck,hands):
    crashed = False
    stand_pressed = False

    while not crashed:
        if stand_pressed:
            dealer_turn(PYGAME,COLOURS,BUTTONS,hands,deck)
            stand_pressed = False
            time.sleep(3)

        reset(hands,deck)

        while not stand_pressed:
            if crashed == True:
                break

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    if is_over_buttton(BUTTONS.hit,pos):
                        hands.player.hit(deck)
                    if is_over_buttton(BUTTONS.stand,pos):
                        stand_pressed = True

                if event.type == pygame.QUIT:
                    crashed = True


            update_display("players_turn",PYGAME,COLOURS,BUTTONS,hands)

    pygame.display.quit()
    pygame.quit()

def main():
    width = 1500
    height = 1500

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    pygame_tuple = namedtuple("pygame_tuple","pygame screen")
    PYGAME = pygame_tuple(pygame = pygame, screen = screen)

    card = namedtuple("card","rank suit")

    deck = blackjack.Deck()
    deck.build_deck(card)
    deck.shuffle()

    dealer = blackjack.Hand("dealer",80,200)
    player = blackjack.Hand("player",80,500)

    hand_tuple = namedtuple("hand_tuple", "player dealer")
    hands = hand_tuple(player = player, dealer = dealer)

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

    game_loop(PYGAME,COLOURS,BUTTONS,card,deck,hands)

if __name__ == "__main__":
    main()
