import pygame, sys
from pygame.locals import*
from Player import Player
from Background import Background

pygame.init()

#fps
fpsclock=pygame.time.Clock()
Fps = 120

#Variable
WINDOWWIDTH = 1024
WINDOWHEIGHT = 512
#def create_pipe():
#	new_pipe = pipe_surface.get_rect(midtop=(216,384))
#	return new_pipe
#def draw_pipe(pipe):
#	screen.blit(pipe_surface,pipe)

#dir
pygame.display.set_caption('Pico Park')
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

BG = pygame.image.load('bg.png').convert_alpha()
pl_img = pygame.image.load('phai.png').convert_alpha()
pipe_surface = pygame.image.load('pipe2.png').convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface,(160,32))

bg = Background(BG,0,0,WINDOWWIDTH,WINDOWHEIGHT,3)
player = Player(pl_img,50,int(WINDOWHEIGHT-113),40,47,WINDOWHEIGHT)

left,right = False,False
gravity = 0.25
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if player.flag_jump:
				if event.key == K_UP:
					player.movement = 0
					player.movement -= 9
					player.flag_jump = False
			if event.key == K_LEFT:
				left = True
			if event.key == K_RIGHT:
				right = True
			if event.key == K_p:#pause
				pass
			if event.key == K_n:#new game
				pass
		if event.type == KEYUP:
			if event.key == K_LEFT:
				left = False
			if event.key == K_RIGHT:
				right = False
	player.movement += gravity
	#bg
	bg.draw(DISPLAYSURF)
	bg.move(player)
	#pipe
	DISPLAYSURF.blit(pipe_surface,(200,300))
	#player
	player.draw(DISPLAYSURF)
	player.move(bg,left,right)
	pygame.display.update()
	fpsclock.tick(Fps)