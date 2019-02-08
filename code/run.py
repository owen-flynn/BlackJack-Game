import blackjack
import graphics
from collections import namedtuple
import pygame

def game_loop(display,colours,hit,stand):
    pygame.init()
    game_display = pygame.display.set_mode((display.width, display.height))
    crashed = False

    card = namedtuple("card","rank suit")

    deck = blackjack.Deck()
    deck.build_deck(card)
    deck.shuffle()

    dealer = blackjack.Hand("dealer",0,0)
    player = blackjack.Hand("player",80,500)
    player.deal(deck)
    dealer.deal(deck)

    while not crashed:
        player.calculate_score()
        game_display.fill(colours.background)
        graphics.draw_hand(pygame,game_display,player)
        graphics.display_score(pygame,game_display,colours,player)
        graphics.draw_button(pygame,game_display,hit)
        graphics.draw_button(pygame,game_display,stand)
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                crashed = True

    pygame.display.quit()
    pygame.quit()

def main():
    display_tuple = namedtuple("display_tuple","width height")
    display = display_tuple(width = 600, height = 800)

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
