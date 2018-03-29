"""
Lucas Golden - Started on 12/20/17, all code is original
"""

import pygame
pygame.init()
from pygame.locals import *
import random
pygame.font.init()

black = (0, 0, 0)
white = (255, 255, 255)
myfont = pygame.font.Font(None, 28)
adam = pygame.image.load("adam_gribble.jpg")
box = pygame.image.load("FFIX_Party_Screen.png")
victoria = pygame.image.load("20160901_200328.jpg")
lucasg = pygame.image.load("lucas.jpg")
intense = pygame.mixer.music.load("intense.mp3")
boss = "boxx.mp3"
love = pygame.mixer.music.load("love.mp3")
homer = pygame.image.load("homer.jpg")
mom = pygame.image.load("joyce.png")
dad = pygame.image.load("jim.png")
fighting = pygame.image.load("Fight_Background_test.png")
arrow = pygame.image.load("cursor.jpg")

NAME = "butterball"

class Test(object):
	def __init__(self):
		screen_size = (1200, 800)
		surface = pygame.display.set_mode(screen_size)
		hero = Hero()
		done = False
		okay = False
		step = 0
		counter = 0
		texter = Textbox()
		floor = Floor()
		vix = Hero()
		vix.vy = 0
		lucas = Hero()
		lucas.vx = 0
		lucas.vy = 0
		joyce = Hero()
		jim = Hero()
		boss1 = Hero()
		jim = Hero()
		pygame.mixer.music.play()

		while not done:
			surface.fill(black)
			texter.text("", "Hello, Please say your name into the microphone then press Q", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			surface.fill(black)
			texter.text(
				"",
				"You have said the name '" + NAME + "', is that correct?",
				surface
			)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			surface.fill(black)
			texter.text("", "So be it, you shall hereby be known as 'Douchebag'", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			surface.fill(black)
			texter.text("", "Well Douchebag, our story begins in London, England...", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		x = 255
		done = False
		while not done:
			surface.fill(white)
			surface.fill(black)
			x -= 1
			if x == 0:
				done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			hero.kneeling(surface, adam)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			texter.text("Douchebag", "Oh my sweet sweet victoria, My love for you burns ever so", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Douchebag", "So much so, that it could melt the snowmen across the world", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Victoria", "Oh Adam, your words are more delicious than tea and crumpets.. <3", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Unknown", "Not so fast!", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		pygame.mixer.music.load("intense.mp3")
		done = False
		pygame.mixer.music.play()
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Douchebag", "Who said that?? Don't tell me it's Luc-", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Uknown", "You're damn right it is.", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		while not done:
			floor.create_floor(black, surface)
			surface.fill(white)
			vix.x = 180
			vix.y = 580
			vix.draw_other(surface, 0, victoria)
			hero.kneeling(surface, adam)
			texter.text("Douchebag", "NOOOOOOOOOOOOOO!!", surface)
			pygame.display.flip()
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = True
		done = False
		step = 0
		while not okay:
			hero.maxx = 140
			hero.minx = 60
			vix.vx = 0
			vix.draw(surface, step, victoria)
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				lucas.x = 1000
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Lucas", "Haha.", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Victoria", "Whats the big deal? We see your little brother all the time", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Douchebag", "You dont understand. Hes so much better looking...", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Douchebag", "and athletic", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Douchebag", "and is way cooler.", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				step += 1
				floor.create_floor(black, surface)
				surface.fill(white)
				vix.x = 180
				vix.y = 580
				vix.draw(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Lucas", "You're darn right douchebag, cmon victoria, lets ditch him.", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			okay = True
			while not done:
				step += 1
				surface.fill(white)
				floor.create_floor(black, surface)
				vix.x = 180
				vix.y = 580
				vix.draw_other(surface, 0, victoria)
				hero.draw(surface, step, adam)
				lucas.draw(surface, 0, lucasg)
				texter.text("Victoria", "You got it lucas!", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			count = 0
			counter = 0
			while not done:
				count += 20
				counter += 7
				step += 1
				surface.fill(white)
				floor.create_floor(black, surface)
				vix.x = 180 + count
				lucas.x = 1000 + counter
				vix.y = 580
				vix.maxx = 10000000
				vix.draw(surface, step, victoria)
				hero.draw(surface, 0, adam)
				lucas.draw(surface, step, lucasg)
				pygame.display.flip()
				if vix.x > 1300:
					done = True
			done = False
			while not done:
				step = 0
				surface.fill(white)
				floor.create_floor(black, surface)
				hero.vx = 0
				hero.vy = 0
				vix.x = 180
				vix.y = 580
				hero.draw(surface, step, adam)
				texter.text("Douchebag", "Oh boy, what ever will I do....", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
			while not done:
				surface.fill(white)
				floor.create_floor(black, surface)
				vix.x = 180
				vix.y = 580
				hero.draw(surface, step, adam)
				texter.text("Douchebag", "I know, Im going to go on a quest to get my girl back!", surface)
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type is QUIT:
						done = True
					elif e.type is KEYDOWN:
						if e.key == K_q:
							done = True
			done = False
		pygame.display.toggle_fullscreen()
		x = 0
		y = 0
		background = pygame.image.load("download.jpeg")
		hero.y = 520
		boss1.y = 520
		boss1.x = 900
		boss1.vx = 0
		joyce.x = 400
		joyce.y = 520
		joyce.vx = 0
		jim.x = 500
		jim.y = 520
		jim.vx = 0
		lucas.x = 1180
		lucas.y = 520
		okay = False
		okayy = False
		jim.health = 20
		boss1.health = 60
		hero.health = 40
		boss1.strength = 5
		lucas.x = 1040
		lucas.y = 520
		vix.x = 1080
		vix.y = 520
		lucas.strength = 1000
		vix.vx = 0
		while not done:
			steps = 0
			surface.blit(background, (x, y))
			hero.draw(surface, step, adam)
			boss1.draw(surface, 0, homer)
			joyce.draw(surface, 0, mom)
			jim.draw(surface, 0, dad)
			lucas.draw(surface, 0, lucasg)
			vix.draw(surface, 0, victoria)
			hold1 = x
			pygame.display.flip()
			if hero.x == joyce.x:
				surface.blit(fighting, (0, 0))
				hero.fight(joyce)
				hero.draw(surface, 0, adam)
				joyce.draw(surface, 0, mom)
				okayy = False
				while not okayy:
					texter.text("", "Welcome to your first fight. Press A to attack and D to defend.", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				okayy = False
				while not okayy:
					texter.text("Mom", "Adam, if you press A, you are so grounded.", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				count = 0
				okayy = False
				done = False
				hero.real_fight(joyce, mom, "mom")
				joyce.x = 10000
			if hero.x == jim.x:
				surface.blit(fighting, (0, 0))
				hero.fight(jim)
				hero.draw(surface, 0, adam)
				jim.draw(surface, 0, dad)
				okayy = False
				while not okayy:
					texter.text("Jim", "Can we hurry this up Adam? The Bills game starts soon", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				count = 0
				okayy = False
				done = False
				hero.real_fight(jim, dad, "dad")
				jim.x = 10000
			if hero.x == boss1.x:
				while not okayy:
					texter.text("", "Ha, I bet you thought something would happen, but no I put him here for my enjoyment", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				boss1.x = boss1.x - 10
			if hero.x == lucas.x:
				surface.blit(fighting, (0, 0))
				hero.fight(lucas)
				hero.draw(surface, 0, adam)
				lucas.draw(surface, 0, lucasg)
				hero.real_fight(lucas, lucasg, "luke")
				while not okayy:
					texter.text("Adam", "Prepare to give my love back!", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				okayy = False
				screen_size = (1200, 800)
				surface = pygame.display.set_mode(screen_size)
				surface.fill(black)
				okayy = False
				while not okayy:
					texter.text("", "While you may have lost, its okay, everyone knows one thing.", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				okayy = False
				while not okayy:
					texter.text("", "That Lucas is the better brother, so you really had nothing to lose.", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
				okayy = False
				while not okayy:
					texter.text("", "Thank you very much for playing Saving Victoria, and merry christmas!!", surface)
					pygame.display.flip()
					events = pygame.event.get()
					for e in events:
						if e.type is KEYDOWN:
							if e.key == K_q:
								okayy = True
								okay = True
				done = True
			events = pygame.event.get()
			for e in events:
				if e.type is QUIT:
					done = True
				elif e.type is KEYDOWN:
					if e.key == K_q:
						done = False
					elif e.key == K_RIGHT:
						x -= 10
						jim.x -= 10
						boss1.x -= 10
						joyce.x -= 10
						lucas.x -= 10
						vix.x -= 10
						step += 1
					elif e.key == K_LEFT:
						jim.x += 10
						boss1.x += 10
						joyce.x += 10
						lucas.x += 10
						vix.x += 10
						x += 10
						step += 1
					elif e.key == K_DOWN:
						if hero.y <= 520:
							pass
						else:
							hero.y += 5
							step += 1
					elif e.key == K_UP:
						if hero.y >= 500:
							pass
						else:
							hero.y -= 5 
							step += 1




class Hero(object):
	def __init__(self):
		self.x = 100
		self.y = 600
		self.size = (50, 100)
		self.color = black
		self.strength = 5
		self.health = 10
		self.money = 0
		self.hat = None
		self.experience = 0
		self.vx = 20
		self.vy = 0
		self.maxx = 0
		self.maxy = 0
		self.minx = 0
		self.miny = 0

	def draw(self, surface, step, name):
		if step % 2 == 0:
			pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + 100))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 10, self.y + 155))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 10, self.y + 155))
		else:
			pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + 100))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x, self.y + 155))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x, self.y + 155))
		self.x += self.vx
		self.y += self.vy
		if self.x >= self.maxx or self.x <= self.minx:
			self.vx = self.vx * -1
		if self.y >= self.maxy or self.y <= self.miny:
			self.vy = self.vy * -1

		surface.blit(name, (self.x - 20, self.y))

	def walk(self, surface, step):
		self.x += self.vx
		self.y += self.vy
		if self.x >= self.maxx or self.x <= self.minx:
			self.vx = self.vx * -1
		if self.y >= self.maxy or self.y <= self.miny:
			self.vy = self.vy * -1

	def fight(self, other):
		self.x = 100
		self.y = 520
		other.x = 900
		other.y = 520

	def real_fight(self, other, name, stri):
		steps = 0
		screen_size = (1200, 800)
		surface = pygame.display.set_mode(screen_size)
		okayy = False
		okay = False
		surface.blit(fighting, (0, 0))
		self.fight(other)
		self.draw(surface, 0, adam)
		other.draw(surface, 0, name)
		pygame.display.flip()
		count = 0
		okayy = False
		counter = 0
		while not okay:
				surface.blit(arrow, (70, 400))
				pygame.display.flip()
				events = pygame.event.get()
				for e in events:
					if e.type == KEYDOWN:
						if e.key == K_a:
							self.draw(surface, steps, adam)
							while self.x < other.x - 50:
								count += 20
								self.x = self.x + count
								steps += 1
								pygame.display.flip()
							other.health -= 10
							while not okayy:
								surface.blit(box, (250, 100))
								say = myfont.render("Adam attacks for 10 damage!", 1, self.color)
								surface.blit(say, (300, 175))
								pygame.display.flip()
								events = pygame.event.get()
								for e in events:
									if e.type is KEYDOWN:
										if e.key == K_q:
											okayy = True
							self.x = 100
							surface.blit(arrow, (860, 400))
							pygame.display.flip()
							other.draw(surface, steps, name)
							self.draw(surface, 0, adam)
							pygame.display.flip()
							okayy = False
							while other.x > self.x + 30:
								other.x = other.x - 20
								steps += 1
								pygame.display.flip()
							self.health -= other.strength
							while not okayy:
								if stri == "mom":
									surface.blit(box, (250, 100))
									say = myfont.render("Mom uses Nag! It deals 5 damage", 1, self.color)
									surface.blit(say, (300, 175))
									pygame.display.flip()
								elif stri == "dad":
									counter += 1
									if counter == 1:
										jeff = False
										while not jeff:
											surface.blit(box, (250, 100))
											say = myfont.render("Jim drinks a beer... it does nothing", 1, self.color)
											surface.blit(say, (300, 175))
											pygame.display.flip()
											for e in events:
												if e.type is KEYDOWN:
													if e.key == K_q:
														jeff = True
											okayy = True
									else:
										surface.blit(box, (250, 100))
										say = myfont.render("Jim is still drinking beer, and still does nothing", 1, self.color)
										surface.blit(say, (300, 175))
										pygame.display.flip()
								elif stri == "luke":
									surface.blit(box, (250, 100))
									say = myfont.render("Lucas looks at you and you poop your pants, and die from a heart attack.", 1, self.color)
									surface.blit(say, (300, 175))
									pygame.display.flip()
								events = pygame.event.get()
								for e in events:
									if e.type is KEYDOWN:
										if e.key == K_q:
											okayy = True
							if other.health < 1:
								while not okayy:
									surface.blit(box, (250, 100))
									say = myfont.render("Congrats, you win!", 1, self.color)
									surface.blit(say, (300, 175))
									pygame.display.flip()
									for e in events:
										if e.type == KEYDOWN:
											if e.key == K_a:
												okayy = True
								other.x = 10000
								okay = True
							elif self.health < 1:
								okay = True
						okayy = False
						if e.key == K_d:
							while not okayy:
								surface.blit(box, (250, 100))
								say = myfont.render("Adam defends", 1, self.color)
								surface.blit(say, (300, 175))
								pygame.display.flip()
								events = pygame.event.get()
								for e in events:
									if e.key == K_q:
										okayy = True
								other.draw(surface, steps, name)
								self.draw(surface, 0, adam)
								pygame.display.flip()
								okayy = False
								while other.x > hero.x + 30:
									other.x -= 20
									steps += 1
									pygame.display.flip()
								self.health -= other.strength
								while not okayy:
									if other == joyce:
										surface.blit(box, (250, 100))
										say = myfont.render("Mom uses Nag! It deals 5 damage", 1, self.color)
										surface.blit(say, (300, 175))
										pygame.display.flip()
									elif other == jim:
										counter += 1
										if counter == 1:
											surface.blit(box, (250, 100))
											say = myfont.render("Jim drinks a beer... it does nothing", 1, self.color)
											surface.blit(say, (300, 175))
											pygame.display.flip()
										else:
											surface.blit(box, (250, 100))
											say = myfont.render("Jim is still drinking beer, and still does nothing", 1, self.color)
											surface.blit(say, (300, 175))
											pygame.display.flip()
									elif other == boss1:
										surface.blit(box, (250, 100))
										say = myfont.render("Homer deals actual damage!", 1, self.color)
										surface.blit(say, (300, 175))
										pygame.display.flip()
									events = pygame.event.get()
									for e in events:
										if e.key == K_q:
											okayy = True
				if other.health < 1:
					okay = True
				if self.health < 1:
					okay = True
		okayy = False
		if other.health < 1:
			while not okayy:
				surface.blit(box, (250, 100))
				say = myfont.render("Congrats, you win!", 1, self.color)
				surface.blit(say, (300, 175))
				pygame.display.flip()
				for e in events:
					if e.type == KEYDOWN:
						if e.key == K_q:
							okayy = True
			other.x = 10000
			okay = True
		elif self.health < 1:
			okay = True

	def draw_other(self, surface, step, name):
		if step % 2 == 0:
			pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + 100))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 10, self.y + 155))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 10, self.y + 155))
		else:
			pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + 100))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 40, self.y + 60))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x, self.y + 155))
			pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x, self.y + 155))
		surface.blit(name, (self.x - 20, self.y))

	def kneeling(self, surface, name):
		pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + 100))
		pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x - 40, self.y + 60))
		pygame.draw.line(surface, self.color, (self.x - 40, self.y + 60), (self.x, self.y + 60))
		pygame.draw.line(surface, self.color, (self.x, self.y + 70), (self.x + 40, self.y +60))
		pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x, self.y + 130))
		pygame.draw.line(surface, self.color, (self.x, self.y + 130), (self.x - 25, self.y + 130))
		pygame.draw.line(surface, self.color, (self.x, self.y + 100), (self.x + 25, self.y + 100))
		pygame.draw.line(surface, self.color, (self.x + 25, self.y + 100), (self.x + 25, self.y + 130))
		surface.blit(name, (self.x - 20, self.y))

class Textbox(object):
	def __init__(self):
		self.x = 250
		self.y = 100
		self.color = black

	def text(self, person, text, surface):
		surface.blit(box, (self.x, self.y))
		say = myfont.render(text, 1, self.color)
		surface.blit(say, (self.x + 50, self.y + 75))
		name = myfont.render(person, 1, self.color)
		surface.blit(name, (self.x + 10, self.y))

class Floor(object):
	def __init__(self):
		self.x = 0
		self.y = 800
		self. size = (1200, 600)

	def create_floor(self, color, surface):
		rect = pygame.Rect((self.x, self.y), self.size)
		pygame.draw.rect(surface, color, rect)

Test()