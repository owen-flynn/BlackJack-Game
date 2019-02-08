import blackjack
import graphics
from collections import namedtuple
import pygame

def is_over_buttton(but,pos):
    if pos[0] > but.x and pos[0] < but.x + but.width:
        if pos[1] > but.y and pos[1] < but.y + but.height:
            return True
    return False

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
    player.deal(deck)
    dealer.deal(deck)
    
    while not crashed:
        player.calculate_score()
        dealer.calculate_initial_dealer_score()
        game_display.fill(colours.background)
        graphics.draw_hand(pygame,game_display,player)
        graphics.draw_half_hand(pygame,game_display,colours,dealer,back_of_card)
        graphics.display_score(pygame,game_display,colours,player)
        graphics.display_score(pygame,game_display,colours,dealer)
        graphics.draw_button(pygame,game_display,hit)
        graphics.draw_button(pygame,game_display,stand)
        pygame.display.update()


        if player.score > 21:
            text = "Plyer Bust"
            graphics.message_display(pygame,game_display,text,display,colours)
            player.reset()
            player.deal(deck)
            dealer.reset()
            dealer.deal(deck)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                    if is_over_buttton(hit,pos):
                        player.hit(deck)

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
