import pygame

from bezier import Curve

def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**.5

def nearest(c, point, dist=5):
    for k,p in enumerate(c.points):
        if distance(p, point) <= dist:
            return k
    return -1

pygame.init()
pygame.display.set_caption("Bezier Curve Editor")
display = pygame.display.set_mode((600, 600))
display.fill((255, 255, 255))

font = pygame.font.Font('freesansbold.ttf', 15)
controls_text = "Left click: add point | Right click: remove point | Drag: Move point"

controls = font.render(controls_text, True, (0,0,0), (255,255,255))
textRect = controls.get_rect()
display.blit(controls, textRect)

c = Curve(auto_generate = False)
moving_point = -1
modified = False
mouse_down = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = pygame.mouse.get_pressed()[0]
            modified = True
            coord = pygame.mouse.get_pos()
            moving_point = nearest(c, coord)
            if pygame.mouse.get_pressed()[0]:
                if moving_point == -1:
                    c.points.append(coord)
                else:
                    c.points[moving_point] = coord
                    
            elif pygame.mouse.get_pressed()[2] and moving_point > -1:
                del c.points[moving_point]
                
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            c.points[moving_point] = pygame.mouse.get_pos()
            modified = True
       

        if modified:
            modified = False

            display.fill((255, 255, 255))
            display.blit(controls, textRect)

            print(c.points)
            for p in c.points:
                pygame.draw.circle(display, (255, 0, 0), p, 5)

            c.generate()
            for i in range(1, len(c.curve)):
                pygame.draw.line(display, (0, 255, 0), c.curve[i-1], c.curve[i])
                
            
    pygame.display.update()

pygame.quit()
