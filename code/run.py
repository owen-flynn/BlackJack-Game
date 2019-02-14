import blackjack
import graphics
from collections import namedtuple
import pygame
import time

def reset(player,dealer,deck):
    player.reset()
    dealer.reset()
    player.deal(deck)
    dealer.deal(deck)

def is_over_buttton(but,pos):
    if pos[0] > but.x and pos[0] < but.x + but.width:
        if pos[1] > but.y and pos[1] < but.y + but.height:
            return True
    return False

def update_display(turn,params,colours,hit,stand,back_of_card,player,dealer,deck):
    params.game_display.fill(colours.background)

    if turn == "players_turn":
        player.calculate_score()
        dealer.calculate_initial_dealer_score()
        graphics.draw_half_hand(params,colours,dealer,back_of_card)
    elif turn == "dealers_turn":
        dealer.calculate_score()
        graphics.draw_hand(params,dealer)

    graphics.draw_game_elements(params,colours,hit,stand,player,dealer)
    params.pygame.display.update()

def dealer_turn(params,colours,hit,stand,back_of_card,player,dealer,deck):
    while(dealer.score < 17):
        dealer.hit(deck)
        dealer.calculate_score()

    update_display("dealers_turn",params,colours,hit,stand,back_of_card,player,dealer,deck)

def game_loop(display,colours,hit,stand):
    pygame.init()
    game_display = pygame.display.set_mode((display.width, display.height))
    crashed = False

    card = namedtuple("card","rank suit")

    shape_coordinates = namedtuple("shape_coordinates","x y width height")
    back_of_card = shape_coordinates(x = 80, y = 200, width = 100, height = 144)

    deck = blackjack.Deck()
    deck.build_deck(card)
    deck.shuffle()

    dealer = blackjack.Hand("dealer",80,200)
    player = blackjack.Hand("player",80,500)

    crashed = False
    stand_pressed = False

    parameters = namedtuple("parameters","pygame game_display")
    params = parameters(pygame = pygame, game_display = game_display)

    while not crashed:
        if stand_pressed:
            dealer_turn(params,colours,hit,stand,back_of_card,player,dealer,deck)
            stand_pressed = False
            time.sleep(3)

        reset(player,dealer,deck)

        while not stand_pressed:
            if crashed == True:
                break

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    if is_over_buttton(hit,pos):
                        player.hit(deck)
                    if is_over_buttton(stand,pos):
                        stand_pressed = True

                if event.type == pygame.QUIT:
                    crashed = True


            update_display("players_turn",params,colours,hit,stand,back_of_card,player,dealer,deck)

    pygame.display.quit()
    pygame.quit()

def main():
    display_tuple = namedtuple("display_tuple","width height")
    display = display_tuple(width = 1500, height = 1500)

    colours_tuple = namedtuple("colours_tuple","black green red yellow background")
    colours = colours_tuple(black = (0,0,0), green = (0,255,0), red = (255,0,0),
        yellow = (255,255,0), background = (152,198,195))

    button = namedtuple("button"," x y width height colour text text_colour")
    hit = button(x = 80, y = 700, width = 100, height = 80 ,
        colour = colours.green, text = "hit", text_colour = colours.black)
    stand = button(x = 200, y = 700, width = 100, height = 80,
        colour = colours.yellow, text = "stand", text_colour = colours.black)

    game_loop(display,colours,hit,stand)

if __name__ == "__main__":
    main()
