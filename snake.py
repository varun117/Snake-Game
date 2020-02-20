import pygame
import random
import tkinter as tk
from tkinter import messagebox
pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake Game!")


class Snakes():
	def __init__(self, x, y, color, face, left, right, up, down):
		self.x = x
		self.y = y
		self.color = color
		self.face = face
		self.left = left
		self.right = right
		self.up = up
		self.down = down

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, 25, 25))
		if self.face:
			pygame.draw.circle(win, (255,255,255), (self.x+5, self.y+5), 4)
			pygame.draw.circle(win, (40,40,40), (self.x+4, self.y+6), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+20, self.y+5), 4)
			pygame.draw.circle(win, (40,40,40), (self.x+19, self.y+6), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+5, self.y+17), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+7, self.y+18), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+9, self.y+19), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+11, self.y+19), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+13, self.y+19), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+15, self.y+19), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+17, self.y+18), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+19, self.y+17), 1)

	def drawsadface(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, 25, 25))
		if self.face:
			pygame.draw.circle(win, (255,255,255), (self.x+5, self.y+5), 3)
			pygame.draw.circle(win, (40,40,40), (self.x+4, self.y+6), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+20, self.y+5), 3)
			pygame.draw.circle(win, (40,40,40), (self.x+19, self.y+6), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+5, self.y+19), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+7, self.y+18), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+9, self.y+17), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+11, self.y+17), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+13, self.y+17), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+15, self.y+17), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+17, self.y+18), 1)
			pygame.draw.circle(win, (255,255,255), (self.x+19, self.y+19), 1)
	

	def move(self):
		if self.left:
			if self.x-25 < 0:
				self.x = 475
			else:
				self.x -= 25
		elif self.right:
			if self.x+25 >= 500:
				self.x = 0
			else:
				self.x += 25
		elif self.up:
			if self.y-25 < 0:
				self.y = 475
			else:
				self.y -=25
		elif self.down:
			if self.y+25 >= 500:
				self.y = 0
			else:
				self.y +=25


class Food():
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, 25, 25))

def drawcube():
	win.fill((0,0,0))
	for i in range(0,500,25):
		for j in range(0,500,25):
			pygame.draw.rect(win, (150,150,150), (i,j,25,25), 1)

def updatescreen():
	#drawcube()
	win.fill((50,50,50))
	food.draw(win)
	for s in snake:
		s.move()
		s.draw(win)
	snake[0].draw(win)
	pygame.display.update()

def trail():
	for s in range(1,len(snake)):
		if len(snakepos[s]) > 0 and snake[s].x == snakepos[s][0][0] and snake[s].y == snakepos[s][0][1]:
			snake[s].left = snakepos[s][0][2]
			snake[s].right = snakepos[s][0][3]
			snake[s].up = snakepos[s][0][4]
			snake[s].down = snakepos[s][0][5]
			snakepos[s].pop(0)

drawcube()
snake = [Snakes(50, 50, (255,0,0), True, False, False, False, False)]
snakepos = []
snakepos.append([])
i = random.randint(2,19)*25
j = random.randint(2,19)*25
if i == snake[0].x:
	i = random.randint(2,20)*25
if j == snake[0].x:
	j = random.randint(2,20)*25
food = Food(i,j,(0,255,0))

timedelay = 100
run = True
while(run):
	pygame.time.delay(timedelay)
	#clock.tick(10)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run=False

	k = pygame.key.get_pressed()
	if k[pygame.K_LEFT]:
		snake[0].left = True
		snake[0].right = False
		snake[0].up = False
		snake[0].down = False
		if len(snake) > 1:
			for s in range(1,len(snake)):
				snakepos[s].append([snake[0].x, snake[0].y, snake[0].left, snake[0].right, snake[0].up, snake[0].down])
	elif k[pygame.K_RIGHT]:
		snake[0].right = True
		snake[0].left = False
		snake[0].up = False
		snake[0].down = False
		if len(snake) > 1:
			for s in range(1,len(snake)):
				snakepos[s].append([snake[0].x, snake[0].y, snake[0].left, snake[0].right, snake[0].up, snake[0].down])
	elif k[pygame.K_UP]:		
		snake[0].up = True
		snake[0].left = False
		snake[0].right = False
		snake[0].down = False
		if len(snake) > 1:
			for s in range(1,len(snake)):
				snakepos[s].append([snake[0].x, snake[0].y, snake[0].left, snake[0].right, snake[0].up, snake[0].down])
	elif k[pygame.K_DOWN]:		
		snake[0].down = True
		snake[0].right = False
		snake[0].up = False
		snake[0].left = False
		if len(snake) > 1:
			for s in range(1,len(snake)):	
				snakepos[s].append([snake[0].x, snake[0].y, snake[0].left, snake[0].right, snake[0].up, snake[0].down])

	if food.x == snake[0].x and food.y == snake[0].y:
                timedelay -= 3
                while True:
                	food.x = random.randint(2,19)*25
                	food.y = random.randint(2,19)*25
                	for s in snake:
                		if food.x == s.x and food.y == s.y:
                			continue
                	break
                if snake[len(snake)-1].right:
                        snake.append(Snakes(snake[len(snake)-1].x-25, snake[len(snake)-1].y, (255,0,0), False, snake[len(snake)-1].left, snake[len(snake)-1].right, snake[len(snake)-1].up, snake[len(snake)-1].down))
                        snakepos.append([])
                        snakepos[len(snakepos)-1] += snakepos[len(snakepos)-2]
                elif snake[len(snake)-1].left:
                        snake.append(Snakes(snake[len(snake)-1].x+25, snake[len(snake)-1].y, (255,0,0), False, snake[len(snake)-1].left, snake[len(snake)-1].right, snake[len(snake)-1].up, snake[len(snake)-1].down))
                        snakepos.append([])
                        snakepos[len(snakepos)-1] += snakepos[len(snakepos)-2]
                elif snake[len(snake)-1].up:
                        snake.append(Snakes(snake[len(snake)-1].x, snake[len(snake)-1].y+25, (255,0,0), False, snake[len(snake)-1].left, snake[len(snake)-1].right, snake[len(snake)-1].up, snake[len(snake)-1].down))
                        snakepos.append([])
                        snakepos[len(snakepos)-1] += snakepos[len(snakepos)-2]
                elif snake[len(snake)-1].down:
                        snake.append(Snakes(snake[len(snake)-1].x, snake[len(snake)-1].y-25, (255,0,0), False, snake[len(snake)-1].left, snake[len(snake)-1].right, snake[len(snake)-1].up, snake[len(snake)-1].down))
                        snakepos.append([])
                        snakepos[len(snakepos)-1] += snakepos[len(snakepos)-2]

	trail()
	updatescreen()

	for s in range(1,len(snake)):
		if snake[0].x == snake[s].x and snake[0].y == snake[s].y:
			snake[0].drawsadface(win)
			pygame.display.update()
			pygame.time.delay(300)
			root = tk.Tk()
			root.attributes("-topmost", True)
			root.withdraw()
			messagebox.showinfo('You Lost!', 'Your score was: '+str(len(snakepos)))
			drawcube()
			snake = [Snakes(50, 50, (255,0,0), True, False, False, False, False)]
			snakepos = []
			snakepos.append([])
			i = random.randint(2,19)*25
			j = random.randint(2,19)*25
			if i == snake[0].x:
				i = random.randint(2,20)*25
			if j == snake[0].x:
				j = random.randint(2,20)*25
			food = Food(i,j,(0,255,0))
			timedelay = 100
			break


pygame.quit()