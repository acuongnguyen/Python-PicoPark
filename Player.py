import pygame

class Player():
    def __init__(self,player_img,x,y,width,height,WINDOWHEIGHT):
        self.x, self.y, self.width, self.height, self.WINDOWHEIGHT = x, y, width, height, WINDOWHEIGHT
        self.player = pygame.transform.scale(player_img,(self.width,self.height))
        self.player_rect = self.player.get_rect(topleft = (self.x,self.y)) #real
        self.player_rect_ref = self.player.get_rect(topleft = (self.x,self.y)) #ref
        self.speed = 3
        self.movement = 0
        self.BOTTOM = self.WINDOWHEIGHT
        self.flag_jump = False
    def draw(self,DISPLAYSURF):
        DISPLAYSURF.blit(self.player,(self.player_rect_ref.left,self.player_rect_ref.top))
        
    def move(self,bg,left,right):
        if right:
            self.player_rect.centerx += self.speed
        if left:
            self.player_rect.centerx -= self.speed
        #boundary
        if self.player_rect.right > bg.BG.get_width():
            self.player_rect.right = bg.BG.get_width()
        if self.player_rect.left < 0:
            self.player_rect.left = 0

        self.player_rect.bottom += self.movement
        if self.player_rect.bottom >= self.BOTTOM-66:
            self.player_rect.bottom = self.BOTTOM-66
            self.flag_jump = True    
        self.player_rect_ref.centerx = self.player_rect.centerx + bg.x
        self.player_rect_ref.centery = self.player_rect.centery + bg.y