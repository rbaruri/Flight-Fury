import pygame
import sys


pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flight Fury')


jet_image = pygame.image.load('images/jetplane.png')
bomb_image = pygame.image.load('images/bomb.png')
house1_image = pygame.image.load('images/hut.png')  
house2_image = pygame.image.load('images/building.png')  
house3_image = pygame.image.load('images/hut.png')  
exp_image = pygame.image.load('images/explosion.png')
background_image = pygame.image.load('images/cl_sky.jpg')  
land_image = pygame.image.load('images/land.png')  

favicon = pygame.image.load('images/jetplane.png')


favicon_size = (32, 32)  
favicon = pygame.transform.scale(favicon, favicon_size)


pygame.display.set_icon(favicon)


jet_width, jet_height = 60, 30
jet_image = pygame.transform.scale(jet_image, (jet_width, jet_height))

bomb_width, bomb_height = 20, 20
bomb_image = pygame.transform.scale(bomb_image, (bomb_width, bomb_height))

exp_width, exp_height = 40, 40
exp_image = pygame.transform.scale(exp_image, (exp_width, exp_height))

house1_width, house1_height = 100, 75
house1_image = pygame.transform.scale(house1_image, (house1_width, house1_height))

house2_width, house2_height = 100, 100  
house2_image = pygame.transform.scale(house2_image, (house2_width, house2_height))

house3_width, house3_height = 100, 75
house3_image = pygame.transform.scale(house3_image, (house3_width, house3_height))

land_width = SCREEN_WIDTH
land_height = 50  
land_image = pygame.transform.scale(land_image, (land_width, land_height))


background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


jet_x = 0
jet_y = 50
jet_speed = 5


base_y = SCREEN_HEIGHT - land_height - 50  


house1_x = 50  
house2_x = SCREEN_WIDTH // 2 - house2_width // 2  
house3_x = SCREEN_WIDTH - 50 - house3_width  


house1_y = base_y - house1_height  
house2_y = base_y - house2_height  
house3_y = base_y - house3_height  


house_positions = [(house1_x, house1_y), (house2_x, house2_y), (house3_x, house3_y)]


class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10  
    
    def update(self):
        self.y += self.speed  
        
    def draw(self):
        screen.blit(bomb_image, (self.x, self.y))


bombs = []


explosion_timer = 0
explosion_x = 0
explosion_y = 0
score = 0  


font = pygame.font.Font(None, 36)  


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bomb_x = jet_x + jet_image.get_width() / 2
            bomb_y = jet_y + jet_image.get_height()
            bombs.append(Bomb(bomb_x, bomb_y))

    
    jet_x += jet_speed
    if jet_x > SCREEN_WIDTH:  
        jet_x = -jet_image.get_width()

    
    for bomb in bombs:
        bomb.update()
        
        for i, (house_x, house_y) in enumerate(house_positions):
            house_width = house1_width if i == 0 else (house2_width if i == 1 else house3_width)
            house_height = house1_height if i == 0 else (house2_height if i == 1 else house3_height)
            if bomb.y + bomb_image.get_height() > house_y and bomb.x > house_x and bomb.x < house_x + house_width:
                print('Hit!')  
                
                explosion_timer = 30  
                explosion_x = house_x + (house_width - exp_width) // 2
                explosion_y = house_y + (house_height - exp_height) // 2
                bombs.remove(bomb)
                
                score += 1
                break  

    
    screen.blit(background_image, (0, 0))  

    
    screen.blit(jet_image, (jet_x, jet_y))

    
    screen.blit(house1_image, house_positions[0])
    screen.blit(house2_image, house_positions[1])
    screen.blit(house3_image, house_positions[2])

    
    for bomb in bombs:
        bomb.draw()

    
    if explosion_timer > 0:
        screen.blit(exp_image, (explosion_x, explosion_y))
        explosion_timer -= 1

    
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    
    screen.blit(land_image, (0, SCREEN_HEIGHT))

    
    pygame.display.flip()

    
    clock.tick(30)
