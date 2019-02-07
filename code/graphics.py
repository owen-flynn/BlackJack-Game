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
