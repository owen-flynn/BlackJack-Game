import time

def draw_button(pygame,game_display,but):
    pygame.draw.rect(game_display,but.colour, (but.x,but.y,but.width,but.height))
    font = pygame.font.SysFont(None, 25)
    text = font.render(but.text, True, but.text_colour)
    game_display.blit(text,(but.x + (but.width/2 - text.get_width()/2),but.y + (but.height/2 - text.get_height()/2)))

def draw_hand(pygame,game_display,hand):
    x = hand.x
    y = hand.y

    for card in hand.cards:
        rank = str(card.rank)
        suit = card.suit
        card_image = pygame.image.load("../images/" + rank + suit + ".png")
        game_display.blit(card_image,(x,y))
        x = x + 100

def draw_half_hand(pygame,game_display,colours,hand,back_of_card):
    x_val = hand.x + 100
    y_val =  hand.y
    card = hand.cards[1]
    rank = str(card.rank)
    suit = card.suit
    card_image = pygame.image.load("../images/" + rank + suit + ".png")
    game_display.blit(card_image,(x_val,y_val))
    pygame.draw.rect(game_display,colours.red, (back_of_card.x,back_of_card.y,back_of_card.width,back_of_card.height))

def display_score(pygame,game_display,colours,hand):
      font = pygame.font.SysFont(None, 25)
      text = font.render(hand.name + ": " + str(hand.score), True, colours.black )
      game_display.blit(text,(hand.x,hand.y + 150))

def message_display(pygame,game_display,text,display,colours):
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, colours.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((display.width/2), (display.height/2))
    game_display.blit(text_surface,text_rect)
    pygame.display.update()
    time.sleep(2)
