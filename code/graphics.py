import time

def draw_button(PYGAME,COLOURS,but):
    PYGAME.pygame.draw.rect(
        PYGAME.screen,but.colour,
        (but.x,but.y,but.width,but.height))

    font = PYGAME.pygame.font.SysFont(None, 25)
    text = font.render(but.text, True, but.text_colour)

    PYGAME.screen.blit(
        text,
        (but.x + (but.width/2 - text.get_width()/2),
        but.y + (but.height/2 - text.get_height()/2)))

def draw_hand(PYGAME,hand):
    x = hand.x
    y = hand.y

    for card in hand.cards:
        rank = str(card.rank)
        suit = card.suit
        card_image = PYGAME.pygame.image.load("../images/" + rank + suit + ".png")
        PYGAME.screen.blit(card_image,(x,y))
        x = x + 100

def draw_game_elements(PYGAME,COLOURS,BUTTONS,stats,hands,show_full_dealer):
    draw_hand(PYGAME,hands.player)
    display_score(PYGAME,COLOURS,hands.player,show_full_dealer)
    display_score(PYGAME,COLOURS,hands.dealer,show_full_dealer)
    draw_button(PYGAME,COLOURS,BUTTONS.hit)
    draw_button(PYGAME,COLOURS,BUTTONS.stand)
    display_totals(PYGAME,COLOURS,stats)

def draw_half_hand(PYGAME,COLOURS,hands):
    x = 80
    y = 200
    width = 100
    height = 144

    x_val = hands.dealer.x + 100
    y_val =  hands.dealer.y

    card = hands.dealer.cards[1]
    rank = str(card.rank)
    suit = card.suit

    card_image = PYGAME.pygame.image.load("../images/" + rank + suit + ".png")

    PYGAME.screen.blit(card_image,(x_val,y_val))
    PYGAME.pygame.draw.rect(PYGAME.screen,COLOURS.red,
    (x,y,width,height))

def display_score(PYGAME,COLOURS,hand,show_full_dealer):
      font = PYGAME.pygame.font.SysFont(None, 25)
      if hand.name == "dealer" and show_full_dealer == False:
          score = hand.initial_score
      else:
        score = hand.score

      text = font.render(hand.name + ": " + str(score), True, COLOURS.black )
      PYGAME.screen.blit(text,(hand.x,hand.y + 150))

def display_totals(PYGAME,COLOURS,stats):
    font = PYGAME.pygame.font.SysFont(None, 25)
    y = 0
    for stat, count in stats.items():
        text = font.render(stat + ": " + str(count), True, COLOURS.black )
        PYGAME.screen.blit(text,(10, y))
        y += 30

def message_display(PYGAME,COLOURS,DISPLAY,text):
    font = PYGAME.pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, COLOURS.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((DISPLAY.width/2), (DISPLAY.height/2))
    PYGAME.screen.blit(text_surface,text_rect)
    PYGAME.pygame.display.update()
    time.sleep(2)
