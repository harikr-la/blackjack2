import pygame

pygame.init()
screen=pygame.display.set_mode([640,640])
clock = pygame.time.Clock()

chess_board = pygame.Surface([8,8])
for x in range (8):
    for y in range (x%2,8,2):
        chess_board.fill ("white",[x,y,1,1])
chess_board = pygame.transform.scale(chess_board,[640,640])
font = pygame.font.Font("Game Of Squids.ttf",25)
letters = "ABCDEFGH"
for x, l in enumerate(letters): 
    for y in range(8): 
        text = font.render(f"{l}{y+1}", 1,"red")
        text.set_alpha(127)
        text_rect = text.get_rect(center= (x*80+40,y*80+40))
        chess_board.blit(text,text_rect)
img = pygame.image.load("chess-removebg-preview.png")
white = img.subsurface([0,0,577,220])
black = img.subsurface([0,220,577,210])
while True:
    mos = pygame.mouse.get_pos()
    m_rect = pygame.Rect(mos,[80]*2)
    m_rect.x -= m_rect.x%80
    m_rect.y -= m_rect.y%80

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()   

    screen.blit(chess_board, [0,0])             
    pygame.draw.rect(screen, " red", m_rect,5)   
    screen.blit(black, [0,0])      
    pygame.display.update()
    clock.tick(60)
    
