import pygame
import sys
import time

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def start_screen(screen, screen_dim, font):
    items = draw_start_screen(screen, screen_dim, font)
    enter_pressed = False
    
    while not enter_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter_pressed = True
                
        redraw_start_window(screen, items)
      
def draw_start_screen(screen, screen_dim, font):
    screen.fill((0, 117, 191))
    text1 = font[0].render("MATH QUIZ TRAINING APP", True, (255, 255, 255))
    text_rect1 = text1.get_rect()
    text_rect1.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 - 100))
    screen.blit(text1, text_rect1)
    
    # PRESS ENTER TO START
    text2 = font[0].render("PRESS ENTER TO START", True, (255, 255, 255))
    text_rect2 = text2.get_rect()
    text_rect2.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 + 100))
    screen.blit(text2, text_rect2)
    
    return [(text1, text_rect1), (text2, text_rect2)]

def redraw_start_window(screen, items):
    # screen.blit(bg, (0, 0))
    
    for item in items:
        screen.blit(item[0], item[1])
    
    pygame.display.update()

def menu_screen(screen, screen_dim, font):
    enter_pressed = False
    selected = 1
    options = ["START", "INSTRUCTIONS", "QUIT"]
    
    while not enter_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter_pressed = True
                elif event.key == pygame.K_UP:
                    selected -= 1
                    selected = max(1, selected)
                elif event.key == pygame.K_DOWN:
                    selected += 1
                    selected = min(3, selected)
        
        items = draw_menu_screen(screen, screen_dim, font, options, selected)
        redraw_menu_window(screen, items)
    
    return (selected, options)

def draw_menu_screen(screen, screen_dim, font, options, selected = 1):
    
    return_val = []
    back_color = (0, 117, 191)
    
    screen.fill(back_color)
    title_text = font[0].render("MATH QUIZ TRAINING APP", True, (255, 255, 255))
    title_text_rect = title_text.get_rect()
    title_text_rect.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 - 250))
    screen.blit(title_text, title_text_rect)
    return_val.append((title_text, title_text_rect))
    
    menu_text = font[1].render("MENU", True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect()
    menu_text_rect.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 - 210))
    screen.blit(menu_text, menu_text_rect)
    return_val.append((menu_text, menu_text_rect))
    
    instruction_text = font[2].render("PRESS THE ARROW KEYS TO NAVIGATE AND PRESS ENTER TO SELECT", True, (255, 255, 255))
    instruction_text_rect = instruction_text.get_rect()
    instruction_text_rect.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 - 180))
    screen.blit(instruction_text, instruction_text_rect)
    return_val.append((instruction_text, instruction_text_rect))    
    
    selected_font = pygame.font.SysFont('comicsans', 20, bold=True)
    
    for i in range(len(options)):
        if i + 1 == selected:
            option_text = selected_font.render(options[i], True, (255, 255, 255))
        else:
            option_text = font[2].render(options[i], True, (255, 255, 255))
        
        option_text_rect = option_text.get_rect()
        option_text_rect.center = ((screen_dim[0] / 2), (screen_dim[1] / 2 - 150 + (25 * i)))
        
        if i + 1 == selected:
            selector_rect = pygame.Rect(option_text_rect.x - 40, option_text_rect.y + option_text_rect.height / 2, 
                                        25, option_text_rect.height - 20)
            color = (0, 0, 0) if time.time() % 1 > 0.5 else back_color
            pygame.draw.rect(screen, color, selector_rect)
            return_val.append((selector_rect, color))
        
        screen.blit(option_text, option_text_rect)
        return_val.append((option_text, option_text_rect))
        
    return return_val

def redraw_menu_window(screen, items):
    # screen.blit(bg, (0, 0))
    
    for item in items:
        if type(item[0]) == pygame.Rect:
            pygame.draw.rect(screen, item[1], item[0])
        else:
            screen.blit(item[0], item[1])
    
    pygame.display.update()

def main_interface(SCREEN_WIDTH, SCREEN_HEIGHT):
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_dim = screen.get_size()
    pygame.display.set_caption("MATH QUIZ TRAINING APP")
    font = pygame.font.SysFont('comicsans', 40)
    font1 = pygame.font.SysFont('comicsans', 30)
    font2 = pygame.font.SysFont('comicsans', 20)
    font3 = pygame.font.SysFont('comicsans', 15)
    fonts = (font, font1, font2, font3)

    start_screen(screen, screen_dim, fonts) 
    selected, options = menu_screen(screen, screen_dim, fonts)
    # selected can be 1, 2, 3, options is "START", "INSTRUCTIONS", "QUIT"
    
    if selected == 1:
        pass
    elif selected == 2:
        pass
    elif selected == 3:
        sys.exit()  

if __name__ == "__main__":
    main_interface(SCREEN_HEIGHT=SCREEN_HEIGHT, SCREEN_WIDTH=SCREEN_WIDTH)