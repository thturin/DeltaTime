import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0,310,100,100)
test_rect_pos = test_rect.x
test_speed = 200

previous_time = time.time()
while True:
    #dt = clock.tick(60) /1000 #if you change the frame per second now it wil not change the speed of the cube itself
    dt = time.time() - previous_time #this is much more precise than the line of above
    previous_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    #rect movement and drawing
    test_rect_pos += test_speed * dt #you need to use a variable to calculate this because rec() takes integers?
    test_rect.x = round(test_rect_pos)  #(dt = 1/frames per second)
    pygame.draw.rect(screen,'red',test_rect)

    pygame.display.update() #update the display every frame
    print(dt) #you will get the duration between frames in ms. it varies (1/60) = .0166
    #clock.tick(60) #set framerate small value (10) will goslower and higher (600) faster
