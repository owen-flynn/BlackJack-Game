def draw_button(pygame,game_display,but):
    pygame.draw.rect(game_display,but.colour, (but.x,but.y,but.width,but.height))
    font = pygame.font.SysFont(None, 25)
    text = font.render(but.text, True, but.text_colour)
    game_display.blit(text,(but.x + (but.width/2 - text.get_width()/2),but.y + (but.height/2 - text.get_height()/2)))
