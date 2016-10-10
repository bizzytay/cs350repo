"""Taylor Herrera October 8 2016"""
"""Game project"""
#Python version 2.7.12


import pygame
import random
import sys

#initializes pygame
pygame.init()


#sets width and height
#x = int(input("Enter a number: "))
#y = int(input("Enter a number: "))
width = 800
height = 600
count = []

#colors: (red, green, blue)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
purple = (100,19,50)


#GUI for pygame as a tuple set with paramaters of 800 by 600
gameDisplay = pygame.display.set_mode((width,height))

#sets the name of the game
pygame.display.set_caption("Taylor's Shooting")


#creates a clock for refreshing the screen
clock = pygame.time.Clock()

#establishes the frames per second
FPS = 30

#creates the font size and to 25
font = pygame.font.SysFont(None,25)

#Intro to enter the game
def Title():
	gameDisplay.fill(white)
	message("WELCOME TO TAYLORS GAME USE THE ARROW KEYS AND SPACEBAR (PRESS P)", black)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					gameLoop()
			

#Displays messages to gui
def message(msg,color):
	screen_text = font.render(msg, True, color)
	#puts the font onton the game display
	gameDisplay.blit(screen_text, [width/12, height/2])


#creates the player
def player(X_cord, Y_cord, player_width, player_height):
	#creates player draws rectangle (name of canvas, color, x-cord, y-cord, width, height)
	player = pygame.draw.rect(gameDisplay, green, [X_cord, Y_cord, player_width, player_height])


#creates the enemy
def enemy(enemy_X,enemy_Y, enemy_width, enemy_height):
	pygame.draw.rect(gameDisplay, red,[enemy_X,enemy_Y, enemy_width, enemy_height])

#when the space bar is pushed, call this function
def shoot(X_cord, Y_cord, enemy_X, enemy_Y, enemy_width ,enemy_height):

	up = 4
	num = 0
	for i in range(0,150):
		pygame.draw.ellipse(gameDisplay, black,[X_cord+20, Y_cord,10,10])
		Y_cord -= up
		pygame.display.update()
		clock.tick(500)
		
		#if the target is hit then you win
		if X_cord == enemy_X or Y_cord == enemy_Y or Y_cord == enemy_Y:
			num += 1
			count.append(num)
			
			size = len(count)
			print(count)
			print(size)			
			while size == 2 or size == 5 or size == 7 or size == 9:
				gameDisplay.fill(white)
				message("YOU WIN (Press q to quit or c to play again)",purple)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							sys.exit("Thank you for playing")
						if event.key == pygame.K_c:
							gameLoop()


def gameLoop():

	#sets the player and enemy size
	player_width = 50
	player_height = 20
	enemy_width = 50
	enemy_height = 20


	gameExit = False
	gameOver = False

	#leader of the x and y blocks
	X_cord = width - 50
	Y_cord = height - 50
	change_x = 0
	change_y = 0
	
	enemy_X = width/14
	enemy_Y	= height/14

	enemy_shoot = round(random.randrange(0, height-player_height)/10)*10
	player_shoot = round(random.randrange(0, height-player_height)/10)*10



	#main loop
	while not gameExit:
		#When the user dies, ask if they want to continue or quit
		while gameOver == True:
			gameDisplay.fill(white)
			message("GAMEOVER!! Press C to play again or Q to quit", red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
						print ("Thank you for playing")
					if event.key == pygame.K_c:
						gameLoop()
						count = []


		#event handeling
		for event in pygame.event.get():
			#allows you to quit game by pressing the X button on the top right(Windows) or left(Unix) of gui
			if event.type == pygame.QUIT:
				gameExit = True
				print ("Thank you for playing")

			#if the key is held push or held down, then move
			if event.type == pygame.KEYDOWN:
				#if user hits arrow keys move left, right, up, or down
				if event.key == pygame.K_LEFT:
					change_x = -player_width
					change_y = 0
				elif event.key == pygame.K_RIGHT:
					change_x = player_width
					change_y = 0
				elif event.key == pygame.K_SPACE:
					shoot(X_cord, Y_cord, enemy_X, enemy_Y, enemy_width ,enemy_height)



			#if user let go of the arrow keys, then stop moving
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					change_x = 0
					change_y = 0



		#if the block goes off the screen make it stop
		if X_cord > width-50:
			X_cord = 750
			Y_cord = 550
		if X_cord < 0:
			X_cord = 0
			Y_cord = 550


		#updates the coordinates
		X_cord += change_x
		Y_cord += change_y
		#print (X_cord,Y_cord)


		
		#if the enemy goes passed the screen you lose
		if enemy_X <= width:
			enemy_X += 4
			if enemy_X > width:
				gameOver = True

		#create a white background
		gameDisplay.fill(white)
				
	
		#creates the enemy
		enemy(enemy_X, enemy_Y, enemy_width, enemy_height)

	
		#creates the player
		player(X_cord, Y_cord, player_width, player_height)


		#refreshes the canvas
		pygame.display.update()

		#frames per second
		clock.tick(FPS)


	#quits pygame
	pygame.quit()

	#exits
	quit()

Title()
