import pygame #lấy thư viện game
pygame.init() #khởi tạo

import time   #Khởi tạo thời gian trong game
import random

width=800
height=600

screen=pygame.display.set_mode((width,height))
carimg=pygame.image.load("car1.jpg")      #xe của người chơi 

car_width=56                                                             #Chiều dài của xe 

grass=pygame.image.load("grass.jpg")      #Đua hình ảnh cỏ vào game 
vang=pygame.image.load("vang.png") 
strip=pygame.image.load("strip.jpg")
clock=pygame.time.Clock()                 #khóa không cho xe chạy ra ngoài

#Chữ kết thúc game
myfont=pygame.font.SysFont("None",100)
render_text= myfont.render("Vi Pham Giao Thông",1,(0,0,0))
xe_text=myfont.render("Tai Nan",1,(0,0,0))
pygame.display.set_caption("DuaXe")       #game đua xe
#Thêm các xe vào gamwe để random 
def obstacle(obs_x,obs_y,obs):
    if obs==0:
        obs_pic=pygame.image.load("car2.png")
    elif obs==1:
        obs_pic=pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car4.png")
    elif obs==3:
        obs_pic=pygame.image.load("car5.png")
    elif obs==4:
        obs_pic=pygame.image.load("car6.png")
    elif obs==5:
        obs_pic=pygame.image.load("car7.png")
    screen.blit(obs_pic,(obs_x,obs_y)) 

#Đưa hình cỏ và làn đường vô 
def background():
	screen.blit(grass,(0,0))
	screen.blit(grass,(700,0))
	screen.blit(vang,(400,0))
	screen.blit(vang,(400,100))
	screen.blit(vang,(400,200))
	screen.blit(vang,(400,300))
	screen.blit(vang,(400,400))
	screen.blit(vang,(400,500))
	screen.blit(vang,(400,600))
	screen.blit(vang,(400,600))
	screen.blit(strip,(120,0))
	screen.blit(strip,(680,0))

#  định nghĩa xe 
def car(x,y):
	screen.blit(carimg,(x,y))


#Tạo bảng liên tục#
def game_loop():
	running=False
	x=400
	y=470
	x_change=0 #mũi tên qua phải
#Tạo các kẻ thù
	obstacle_speed= 10
	obs=0
	y_change=0
	obs_x= random.randrange(200,650)
	obs_y= -750
	enemy_width= 56
	enemy_height= 125
#__________________#
	while not running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:          
				running=True
	# Điều khiển qua lại của xe 
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-5
			if event.key==pygame.K_RIGHT:
				x_change=5		
	# Nếu bấm lên thì xe k chạy
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				x_change=0	
		x +=x_change		
		screen.fill((119,119,119))               #bảng tô màu xám
		background()
	#RAndom kẻ thù 
		obs_y -= (obstacle_speed/4)
		obstacle(obs_x,obs_y,obs)
		obs_y += obstacle_speed
		car(x,y)                                 #xuất hiện xe trong background
	
	#Không cho xe ra ngoài 
		if x>680 - car_width or x<120:                                         #Khóa không cho xe chạy ra ngoài
			screen.blit(render_text,(100,200))
			pygame.display.update()
			time.sleep(5)
			game_loop()  
	#Thêm nhiều xe chạy
		if obs_y>height:
			obs_y= 0-enemy_height                   #random 1 xe 
			obs_x= random.randrange(170, width-170) 
			obs= random.randrange(0,6)

		if y<obs_y+enemy_height:
			if x > obs_x and x < obs_x + enemy_width or x+car_width > obs_x and x+car_width < obs_x+enemy_width:
				screen.blit(xe_text,(100,200))
				pygame.display.update()
				time.sleep(5)
				game_loop()    
	#Cập nhật lại game                                                    
		pygame.display.update()
		clock.tick(100)

game_loop()		        
pygame.quit()        
quit()