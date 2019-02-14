import time

def draw_button(params,but):
    params.pygame.draw.rect(params.game_display,but.colour, (but.x,but.y,but.width,but.height))
    font = params.pygame.font.SysFont(None, 25)
    text = font.render(but.text, True, but.text_colour)
    params.game_display.blit(text,(but.x + (but.width/2 - text.get_width()/2),but.y + (but.height/2 - text.get_height()/2)))

def draw_card(params,card,x,y):
    rank = str(card.rank)
    suit = card.suit
    card_image = params.pygame.image.load("../images/" + rank + suit + ".png")
    params.game_display.blit(card_image,(x,y))

def draw_hand(params,hand):
    x = hand.x
    y = hand.y

    for card in hand.cards:
        rank = str(card.rank)
        suit = card.suit
        card_image = params.pygame.image.load("../images/" + rank + suit + ".png")
        params.game_display.blit(card_image,(x,y))
        x = x + 100

def draw_game_elements(params,colours,hit,stand,player,dealer):
    draw_hand(params,player)
    display_score(params,colours,player)
    display_score(params,colours,dealer)
    draw_button(params,hit)
    draw_button(params,stand)

def draw_half_hand(params,colours,hand,back_of_card):
    x_val = hand.x + 100
    y_val =  hand.y
    card = hand.cards[1]
    rank = str(card.rank)
    suit = card.suit
    card_image = params.pygame.image.load("../images/" + rank + suit + ".png")
    params.game_display.blit(card_image,(x_val,y_val))
    params.pygame.draw.rect(params.game_display,colours.red, (back_of_card.x,back_of_card.y,back_of_card.width,back_of_card.height))

def display_score(params,colours,hand):
      font = params.pygame.font.SysFont(None, 25)
      text = font.render(hand.name + ": " + str(hand.score), True, colours.black )
      params.game_display.blit(text,(hand.x,hand.y + 150))

def message_display(params,text,display,colours):
    font = params.pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, colours.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((display.width/2), (display.height/2))
    params.game_display.blit(text_surface,text_rect)
    params.pygame.display.update()
    time.sleep(2)
