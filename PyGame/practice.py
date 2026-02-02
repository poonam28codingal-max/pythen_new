import pygame
pygame.init()
width,height= 500,500
screen= pygame.display.set_mode((width,height))
pygame.display.set_caption('Rectangle Movement')

#Mapping the colors name using RGB values
Color={
    'red':pygame.Color('red'),
    'green':pygame.Color('green'),
    'blue':pygame.Color('blue'),
    'yellow':pygame.Color('yellow'),    
    'white':pygame.Color('white')
}
       
current_color= Color['white']
x,y=30,30
sprite_width,sprite_height=60,60
clock=pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_UP]: y-=3                    
    if pressed[pygame.K_DOWN]: y+=3
    
    x=min(max(0,x),width-sprite_width)
    y=min(max(0,y),height-sprite_height)
    #Changing color based on boundary contact
    
    if x==0: current_color= Color['blue']
    elif x==width-sprite_width: current_color=Color['yellow']
    elif y==0 : current_color=Color['red']
    elif y==height-sprite_height:
        current_color=Color['green']
    else:
        current_color=Color['white']
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,current_color,(x,y,sprite_width,sprite_height))
    pygame.display.flip()
    clock.tick(90)
    
pygame.quit()
if __name__ == "__main__":
    main()