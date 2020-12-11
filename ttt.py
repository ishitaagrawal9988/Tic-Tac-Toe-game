import pygame
import random
import math
from pygame import mixer

#initialising pygame
pygame.init()

#display window
screen=pygame.display.set_mode((550,550))
pygame.display.set_caption("tic-tac-toe")

#flag for tic tac toe
board=[[0,0,0],[0,0,0],[0,0,0]]
#score
score1=0
score2=0
score_flag=0

font=pygame.font.Font("freesansbold.ttf",16)

#score of ractangle
def show_score1(x,y):
	score=font.render("Player1(Rectangle):"+str(score1),True,(0,0,255))
	screen.blit(score,(x,y))

#score of circle
def show_score2(x,y):
	score=font.render("Player2(Circle):"+str(score2),True,(0,0,255))
	screen.blit(score,(x,y))


#inital score of rectangle
def show_score1_initial(x,y):
	score=font.render("Player1(Rectangle):"+str(score1),True,(0,0,255))
	screen.blit(score,(x,y))

#initial score of circle
def show_score2_initial(x,y):
	score=font.render("Player2(Circle):"+str(score2),True,(0,0,255))
	screen.blit(score,(x,y))
initial=0


#screen-where need to draw (255,255,255)=color based on rgb *25,25,150,150-(x-coordinate,y-coordinate,lenght,width) for rectangle
first=pygame.draw.rect(screen,(255,255,255),(25,25,150,150))
second=pygame.draw.rect(screen,(255,255,255),(200,25,150,150))
third=pygame.draw.rect(screen,(255,255,255),(375,25,150,150))

fourth=pygame.draw.rect(screen,(255,255,255),(25,200,150,150))
fifth=pygame.draw.rect(screen,(255,255,255),(200,200,150,150))
sixth=pygame.draw.rect(screen,(255,255,255),(375,200,150,150))

seventh=pygame.draw.rect(screen,(255,255,255),(25,375,150,150))
eighth=pygame.draw.rect(screen,(255,255,255),(200,375,150,150))
nineth=pygame.draw.rect(screen,(255,255,255),(375,375,150,150))

def win_check(num):

	for row in board:
		for title in row:
			if title==num:
				continue
			else:
				break
		else:
			return True


	for column in range(3):
		for row in board:
			if row[column]==num:
				continue
			else:
				break
		else:
			return True

	#0,0 1,1 2,2
	for title in range(3):
		if board[title][title]==num:
			continue
		else:
			break
	else:
		return True

    #0,2  1,1  2,0
	for title in range(3):
		if board[title][2-title]==num:
			continue
		else:
			break
	else:
		return True

run=True
#to draw only one shape either rectange or circle
draw_object='rect'
#to fill boxes only once
first_open=True
second_open=True
third_open=True
fourth_open=True
fifth_open=True
sixth_open=True
seventh_open=True
eighth_open=True
nineth_open=True

#staring win=false
win=False
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		#with space key everything will restart again
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				initial=1
				score_flag=0

				#reset everything on screen
				screen.fill((0,0,0))
				#print score
				show_score1(2,2)
				show_score2(400,2)
				first=pygame.draw.rect(screen,(255,255,255),(25,25,150,150))
				second=pygame.draw.rect(screen,(255,255,255),(200,25,150,150))
				third=pygame.draw.rect(screen,(255,255,255),(375,25,150,150))

				fourth=pygame.draw.rect(screen,(255,255,255),(25,200,150,150))
				fifth=pygame.draw.rect(screen,(255,255,255),(200,200,150,150))
				sixth=pygame.draw.rect(screen,(255,255,255),(375,200,150,150))

				seventh=pygame.draw.rect(screen,(255,255,255),(25,375,150,150))
				eighth=pygame.draw.rect(screen,(255,255,255),(200,375,150,150))
				nineth=pygame.draw.rect(screen,(255,255,255),(375,375,150,150))

				first_open=True
				second_open=True
				third_open=True
				fourth_open=True
				fifth_open=True
				sixth_open=True
				seventh_open=True
				eighth_open=True
				nineth_open=True
				run=True
				win=False
				board=[[0,0,0],[0,0,0],[0,0,0]]
		#with mouse click get the position of coordinates
		if event.type==pygame.MOUSEBUTTONUP:
			pos=pygame.mouse.get_pos()
			#no one win yet
			if win==False:
				#if click on first
				if first.collidepoint(pos) and first_open:
					#draw rectange and circle((100,100)-center of circle(x,y) and radius-50)
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(50,50,100,100))
						draw_object="circle"
						board[0][0]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(100,100),50)
						draw_object="rect"
						board[0][0]=2
					first_open=False

				if second.collidepoint(pos) and second_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(225,50,100,100))
						draw_object="circle"
						board[0][1]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(275,100),50)
						draw_object="rect"
						board[0][1]=2
					second_open=False

				if third.collidepoint(pos) and third_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(400,50,100,100))
						draw_object="circle"
						board[0][2]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(450,100),50)
						draw_object="rect"
						board[0][2]=2
					third_open=False

				if fourth.collidepoint(pos) and fourth_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(50,225,100,100))
						draw_object="circle"
						board[1][0]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(100,275),50)
						draw_object="rect"
						board[1][0]=2
					fourth_open=False

				if fifth.collidepoint(pos) and fifth_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(225,225,100,100))
						draw_object="circle"
						board[1][1]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(275,275),50)
						draw_object="rect"
						board[1][1]=2
					fifth_open=False

				if sixth.collidepoint(pos) and sixth_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(400,225,100,100))
						draw_object="circle"
						board[1][2]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(450,275),50)
						draw_object="rect"
						board[1][2]=2
					sixth_open=False

				if seventh.collidepoint(pos) and seventh_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(50,400,100,100))
						draw_object="circle"
						board[2][0]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(100,450),50)
						draw_object="rect"
						board[2][0]=2
					seventh_open=False

				if eighth.collidepoint(pos) and eighth_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(225,400,100,100))
						draw_object="circle"
						board[2][1]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(275,450),50)
						draw_object="rect"
						board[2][1]=2
					eighth_open=False

				if nineth.collidepoint(pos) and nineth_open:
					if draw_object=='rect':
						pygame.draw.rect(screen,(255,0,0),(400,400,100,100))
						draw_object="circle"
						board[2][2]=1
					else:
						pygame.draw.circle(screen,(0,255,0),(450,450),50)
						draw_object="rect"
						board[2][2]=2
					nineth_open=False



	if win_check(1):
		win=True
		if win_check(1) and score_flag==0:
			score1+=1
			score_flag=1


	if win_check(2):
		win=True
		if win_check(2) and score_flag==0:
			score2+=1
			score_flag=1

	if initial==0:
		show_score1_initial(2,2)

		show_score2_initial(400,2)

	pygame.display.update()

pygame.quit()
