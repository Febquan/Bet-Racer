import pygame, sys
import math
from random import choice
import random
from pygame.locals import *
from pygame import mixer

pygame.init()
clock=pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h ), pygame.FULLSCREEN)
mainClock = pygame.time.Clock()

def loadpassword(username):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            if (row[0] == username):
                return row[4]
def updatename(username, newusername):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()

        cur.execute("UPDATE DATABASE SET User=? WHERE User=?", (newusername, username))
        # có tệp user rồi
        # cho biến newuser vào
        con.commit()
def updatepassword(username, newpassword):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()

        cur.execute("UPDATE DATABASE SET Password=? WHERE User=?", (newpassword, username))
        con.commit()
def searchuser(username):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                return False

            if row[0]==username:
                return True
def logupsuccess(username,password):
    import sqlite3 as lite
    import sys
    import os
    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO DATABASE VALUES(?,?,?,?,?)",(username,5000,0,10000000,password))
def loadmoney(username):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            if(row[0]==username):
                return row[1]
def loadrepect(username):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            if (row[0] == username):
                return row[2]
def loadcar(username):
    import sqlite3 as lite
    import sys
    import os


    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    cars = []
    carsbool = 10000000
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            if(row[0]==username):
                carsbool=row[3]
    while carsbool>0 :
         if carsbool%10==1 :
             cars.append(True)
         else :
             cars.append(False)
         carsbool=carsbool//10
    #có mảng xe từ xe thứ 8-->1
    #Đảo ngược bản cars
    return list(reversed(cars))
def updatemoney(username,tien):
        import sqlite3 as lite
        import sys
        import os

        path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
        con = lite.connect(path)

        with con:
            cur = con.cursor()

            cur.execute("UPDATE DATABASE SET Money=? WHERE User=?", (tien, username))
            # có tệp textuser rồi
            # cho biến tiền vào
            con.commit()
def updaterepect(username, repect):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()

        cur.execute("UPDATE DATABASE SET Repect=? WHERE User=?", (repect, username))
        # có tệp textuser rồi
        # cho biến repect vào
        con.commit()
def updatecars(username,cars_x): #xe thứ đứng vị trí thứ mấy vừa được mua
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)
    e=0
    e=cars_x
    cars = []
    carsbool = 10000000
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM DATABASE")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            if (row[0] == username):
                carsbool  = row[3]
    carsbool+=pow(10, 8-e) #cộng 1 đơn vị hàng thứ x từ trái qua phải
    with con:
        cur = con.cursor()

        cur.execute("UPDATE DATABASE SET Cars=? WHERE User=?", (carsbool, username))

def updateallcars(username, allcarBit):
    import sqlite3 as lite
    import sys
    import os

    path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
    con = lite.connect(path)

    with con:
        cur = con.cursor()

        cur.execute("UPDATE DATABASE SET Cars=? WHERE User=?", (allcarBit, username))
        # có tệp user rồi
        # cho biến newuser vào
        con.commit()

fullscreen = False
#KHỞI TẠO THÔNG SỐ
running=True
gameplay = False
optionbool=False
htpbool=False
startbool=True
menubool=False
cars=False
userbool=False
usemenubool = False
signupbool = False
passbool=False
betbool=False
bankbool=False
buycarbool=False
minigamebool=False
accbool=False
GREY= (0,0,0)
obs=50
#HEADING
pygame.display.set_caption("Bet Racer")
pygame.display.set_icon (pygame.image.load("venv/IMG/icon.png"))

#MUSIC

song=["venv/Sound/bg.wav","venv/Sound/Gasgas.wav","venv/Sound/Initial D.wav"]
mixer.music.load(song[0])
volume=0.2
pygame.mixer.music.set_volume (volume)
mixer.music.play(-1)
enter= mixer.Sound("venv/Sound/enter.wav")
move=mixer.Sound("venv/Sound/move.wav")
coin=mixer.Sound("venv/Sound/coin.wav")
count=mixer.Sound("venv/Sound/count.wav")
race=mixer.Sound("venv/Sound/race.wav")
coin.set_volume(0.1)
enter.set_volume(0.1)
move.set_volume(0.1)
count.set_volume(0.2)
race.set_volume(0.1)
soundbua1=mixer.Sound("venv/Sound/bua1.wav")
soundbua1.set_volume(volume)
#IMAGE
menu= pygame.image.load("venv/IMG/menu.png")
start =pygame.image.load("venv/IMG/start.png")
bg=[pygame.image.load("venv/IMG/city.png"),pygame.image.load("venv/IMG/desert.png"),pygame.image.load("venv/IMG/bien.png")]
back=bg[0]
dg=[pygame.image.load("venv/IMG/duong.png"),pygame.image.load("venv/IMG/duong2.png")]
duong=dg[0]
imgcar=pygame.image.load("venv/IMG/1_1.png")





#START
def Start() :
	screen.blit(start, (0, 0))
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_SPACE:
				enter.play()
				global startbool, menubool
				startbool = False
				menubool = True
#MENU
indexmenu=" "
index=1

def Menu() :
		screen.blit(menu, (0, 0))
		global indexmenu,index,gameplay,optionbool,htpbool,userbool,whereop,htpbool
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				global menubool, cars,startbool
				if event.key == K_ESCAPE:
					menubool=False
					startbool=True
				if event.key == K_SPACE:
					enter.play()
					if index==1:
						userbool = True
						menubool = False
					if index==2:
						optionbool = True
						whereop=1
						menubool = False
					if index==3:
						htpbool = True
						menubool = False
				if event.key==K_w:
						indexmenu = "up"
						move.play()
				if event.key==K_s:
						indexmenu="dow"
						move.play()
		#alo=font.render ("index"+str(index),True,(0,0,0))
		#screen.blit(alo,(55,55))
		if indexmenu== "up":
			index=index-1
			indexmenu=" "
		if indexmenu== "dow":
			index=index+1
			indexmenu=" "
		if index>3 :index=1
		if index < 1: index = 3
		if index==1:
			screen.blit(pygame.image.load("venv/IMG/Asset 7.png"),(0,0))
		if index==2:
			screen.blit(pygame.image.load("venv/IMG/Asset 8.png"),(0,0))
		if index==3:
			screen.blit(pygame.image.load("venv/IMG/Asset 9.png"),(0,0))

optiondex=1
opdir= " "
musicbool=True
fontop=pygame.font.SysFont('bahnschrift',70)
fontbet=pygame.font.SysFont('bahnschrift',40,bold=True)
fontmoney=pygame.font.SysFont('bahnschrift',40)
fonttoppas=pygame.font.SysFont('bahnschrift',90)
fontprize=pygame.font.SysFont('source sans variable',100,italic=True)
vol=0
musion=fontop.render ("On",True,(0,0,0))
musioff=fontop.render ("Off",True,(0,0,0))

#screen.blit(alo,(55,55))
a=0
b=0
c=0
hethongbua=0
whereop=0
def Option():
	screen.blit(pygame.image.load("venv/IMG/Asset 27.png"), (0, 0))
	global optiondex,opdir,musicbool,vol,usemenubool

	global song,a, b,c,obs,hethongbua
	flag=" "
	for event in pygame.event.get():
			if event.type == KEYDOWN:
				global menubool, optionbool,volume
				if event.key == K_ESCAPE:
					if whereop==1:
						menubool = True
						optionbool = False
					if whereop==2:
						usemenubool = True
						optionbool = False
				if event.key == K_SPACE:
					enter.play()
					if optiondex==1:
						musicbool=not musicbool
						if (musicbool):
							mixer.music.load(song[a])
							mixer.music.play(-1)
						else:
							mixer.music.stop()

					if optiondex==3:
							a=a+1
							flag= "ye"
					if optiondex == 4:
							b=b+1
					if optiondex == 5:
							c=c+1
				if event.key==K_d :
					if optiondex == 2:
						move.play()
						volume=volume+0.05
				if event.key==K_a :
					if optiondex == 2:
						move.play()
						volume=volume-0.05
				if event.key==K_w:
						opdir = "up"
						move.play()
				if event.key==K_s:
						opdir="dow"
						move.play()
	#direct
	if opdir== "up":
		optiondex=optiondex-1
		opdir=" "
	if opdir== "dow":
		optiondex=optiondex+1
		opdir=" "
	if optiondex>5 : optiondex=1
	if optiondex < 1: optiondex = 5
	if optiondex==1:
		screen.blit(pygame.image.load("venv/IMG/music.png"),(0,0))
	if optiondex==2:
		screen.blit(pygame.image.load("venv/IMG/volume.png"),(0,0))
	if optiondex==3:
		screen.blit(pygame.image.load("venv/IMG/song.png"),(0,0))
	if optiondex == 4:
		screen.blit(pygame.image.load("venv/IMG/back.png"), (0, 0))
	if optiondex == 5:
		screen.blit(pygame.image.load("venv/IMG/gamemode.png"), (0, 0))
	#musiconoff
	if(musicbool):
		screen.blit(musion, (1150, 300))
	else: screen.blit(musioff, (1150, 300))
	#volume
	if volume<0 :volume=0
	if volume>1: volume=1
	vol= fontop.render(str(int(volume * 100)), True, (0, 0, 0))
	pygame.mixer.music.set_volume (volume)
	screen.blit(vol, (1150, 430))
	#song
	listsong=["Futurebass","Gas gas", "Running in The 90"]
	if a>len(listsong)-1: a=0
	if flag=="ye"and musicbool:
		mixer.music.load(song[a])
		mixer.music.play(-1)
		flag= " "

	list = fontop.render(listsong[a], True, (0, 0, 0))
	screen.blit(list, (1150, 560))

	#Background
	global back,bg,duong,dg
	listbg = ["City", "Desert","Beach"]
	if b>len(listbg)-1: b=0

	listback = fontop.render(listbg[b], True, (0, 0, 0))
	screen.blit(listback, (1150, 688))
	back=bg[b]
	duong=dg[b%2]
	#gamemode
	listgamemode = ["Normal", "Mad", "Insane"]
	if c>len(listgamemode)-1: c=0
	listmode = fontop.render(listgamemode[c], True, (0, 0, 0))
	screen.blit(listmode, (1150, 818))
	if c==0:
		obs=25
		hethongbua = bua()
	if c==1:
		obs=50
		hethongbua = bua()
	if c==2:
		obs=80
		hethongbua = bua()



class User() :
	def __init__(self):
		self.name="None"
		self.money=0
		self.cars=[ False,False,False,False,False,False,False,False]
		self.pas="1"
		self.usercarchoose=0
		self.respect=0
		self.stock=0


user1=User()
user2=User()
user3=User()
import sqlite3 as lite
import sys
import os

path = os.path.dirname(__file__) + "\\dulieunguoidung.db"
con = lite.connect(path)

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM DATABASE")

    row = cur.fetchone()
    user1.name=row[0]
    row = cur.fetchone()
    user2.name=row[0]
    row = cur.fetchone()
    user3.name=row[0]

password1=loadpassword(user1.name)


user1.cars=loadcar(user1.name)
user1.respect=loadrepect(user1.name)
user1.money=loadmoney(user1.name)
user1.pas=password1



password2=loadpassword(user2.name)

user2.cars=loadcar(user2.name)
user2.respect=loadrepect(user2.name)
user2.money=loadmoney(user2.name)
user2.pas=password2

password3=loadpassword(user3.name)

user3.cars=loadcar(user3.name)
user3.respect=loadrepect(user3.name)
user3.money=loadmoney(user3.name)
user3.pas=password3





userplay=0
userdex=1
userbool=False
indexuser=0
usedir=" "

def user():
	name1 = fontop.render(user1.name, True, (255, 255, 255))
	name2 = fontop.render(user2.name, True, (255, 255, 255))
	name3 = fontop.render(user3.name, True, (255, 255, 255))
	if user1.money >=1000000 :
		bank1 = fontop.render(str(round(user1.money/1000000,2)) + "M$", True, (255, 255, 255))
	else:
		bank1 = fontop.render(str(user1.money) + "$", True, (255, 255, 255))
	if user2.money >=1000000 :
		bank2 = fontop.render(str(round(user2.money/1000000,2)) + "M$", True, (255, 255, 255))
	else:
		bank2 = fontop.render(str(user2.money) + "$", True, (255, 255, 255))
	if user3.money >=1000000 :
		bank3 = fontop.render(str(round(user3.money/1000000,2)) + "M$", True, (255, 255, 255))
	else:
		bank3 = fontop.render(str(user3.money) + "$", True, (255, 255, 255))
	for event in pygame.event.get():
			if event.type == KEYDOWN:
				global menubool,carbool,userbool,userplay,userdex,usedir,usemenubool,signupbool,passbool,indexuser
				if event.key == K_ESCAPE:
					menubool = True
					userbool = False
				if event.key == K_SPACE:
					enter.play()
					if userdex==1:
						userplay=user1
						indexuser=1
						if userplay.name !="None":
							userbool = False
							passbool=True

						else:
							usemenubool=True
							userbool = False
					if userdex==2:
						userplay=user2
						indexuser = 2
						if userplay.name != "None":
							userbool = False
							passbool = True

						else:
							usemenubool = True
							userbool = False

					if userdex==3:
						indexuser = 3
						userplay = user3
						if userplay != "None":
							userbool = False
							passbool = True

						else:
							usemenubool = True
							userbool = False

				if event.key==K_w:
						usedir = "up"
						move.play()
				if event.key==K_s:
						usedir="dow"
						move.play()
	#direct
	if usedir== "up":
		userdex=userdex-1
		usedir=" "
	if usedir== "dow":
		userdex=userdex+1
		usedir=" "
	if userdex>3 : userdex=1
	if userdex < 1: userdex = 3
	if userdex==1:
		screen.blit(pygame.image.load("venv/IMG/user1.png"),(0,0))
		screen.blit(name1, (1230,340))
		screen.blit(bank1, (730, 340))
	if userdex==2:
		screen.blit(pygame.image.load("venv/IMG/user2.png"),(0,0))
		screen.blit(name2, (1230, 585))
		screen.blit(bank2, (730, 585))
	if userdex==3:
		screen.blit(pygame.image.load("venv/IMG/user3.png"),(0,0))
		screen.blit(name3, (1230, 835))
		screen.blit(bank3, (730, 835))

pasimg= pygame.image.load("venv/IMG/pass-01.png")

inputpas=''
hide=''
hidebool=True
flagtab=False
flagspace=False
flagdelete=False

def passcode():
	screen.blit(pasimg,(0,0))
	for event in pygame.event.get():
			if event.type == KEYDOWN:
				global userbool,userplay,usedir,usemenubool,passbool,inputpas,hide,hidebool,flagtab,flagspace,flagdelete,menubool,indexuser,usename1,usename2,usename3
				if event.key == K_ESCAPE:
					userbool = True
					passbool = False
				if event.key== K_TAB:
					hidebool=not hidebool
					flagtab=True
				if event.key== K_SPACE:
					flagspace = True
					if(userplay.pas==inputpas):
						if (flagdelete == True):
								updatepassword(userplay.name,'1')
								updatemoney(userplay.name,300)
								updaterepect(userplay.name,0)
								updateallcars(userplay.name,10000000)
								updatename(userplay.name, "None")
								pygame.quit()
								sys.exit()
						else:
							inputpas = ''
							hide=''
							passbool=False
							usemenubool=True

				if flagtab==False and flagspace==False:
					if event.key==K_BACKSPACE:
						inputpas=inputpas[0:-1]
						hide = hide[0:-1]
					if event.unicode:
						hide+='*'
					inputpas+=event.unicode
					move.play()

	if len(inputpas) >= 20:
		inputpas = inputpas[0:-1]
	text1=fonttoppas.render (inputpas,True,(255,255,255))
	text2=fonttoppas.render (hide,True,(255,255,255))

	if hidebool:
		screen.blit(text2,(515,583))
	else:
		screen.blit(text1, (515,558))
	flagtab=False
	flagspace = False


dexuserx=0
dexusery=0
dexuser=" "
def usemenu ():
	global dexusery,dexuserx,dexuser,gameplay,usemenubool,menubool,cars,dexuser,bankbool,optionbool,whereop,minigamebool,accbool
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				enter.play()
				if dexuserx == 0 and dexusery==0:
					cars=True
					usemenubool=False
				if dexuserx == 1 and dexusery==0:
					bankbool=True
					usemenubool=False
				if dexuserx == 2 and dexusery==0:
					minigamebool=True
					usemenubool=False
				if dexuserx == 0 and dexusery == 1:
					whereop=2
					optionbool=True
					usemenubool=False
				if dexuserx == 1 and dexusery == 1:
					accbool=True
					usemenubool=False
					pass
				if dexuserx == 2 and dexusery == 1:
					if indexuser==1:
						user1.name=userplay.name
						user1.money=userplay.money
						updatemoney(user1.name,userplay.money)
						user1.respect = userplay.respect
						updaterepect(user1.name,userplay.respect)
					if indexuser==2:
						user2.name = userplay.name
						user2.money=userplay.money
						updatemoney(user2.name,user2.money)
						user2.respect = userplay.respect
						updaterepect(user2.name, userplay.respect)
					if indexuser==3:
						user3.name = userplay.name
						user3.money=userplay.money
						updatemoney(user3.name,userplay.money)
						user3.respect = userplay.respect
						updaterepect(user3.name, userplay.respect)
					menubool = True
					usemenubool=False


			if event.key == K_w:
				dexuser = "up"
				move.play()
			if event.key == K_s:
				dexuser = "dow"
				move.play()
			if event.key == K_d:
				dexuser = "right"
				move.play()
			if event.key == K_a:
				dexuser = "left"
				move.play()
	if dexuser == "up":
		dexusery = dexusery - 1
		dexuser = " "
	if dexuser == "dow":
		dexusery = dexusery + 1
		dexuser = " "
	if dexuser == "right":
		dexuserx = dexuserx + 1
		dexuser = " "
	if dexuser == "left":
		dexuserx = dexuserx - 1
		dexuser = " "
	if dexuserx > 2: dexuserx = 0
	if dexusery > 1: dexusery = 0
	if dexuserx < 0: dexuserx = 2
	if dexusery < 0: dexusery = 1
	if dexuserx == 0 and dexusery == 0:
		screen.blit(pygame.image.load("venv/IMG/usermenu1.png"), (0, 0))
	if dexuserx == 1 and dexusery == 0:
		screen.blit(pygame.image.load("venv/IMG/usermenu2.png"), (0, 0))
	if dexuserx == 2 and dexusery == 0:
		screen.blit(pygame.image.load("venv/IMG/usermenu3.png"), (0, 0))
	if dexuserx == 0 and dexusery == 1:
		screen.blit(pygame.image.load("venv/IMG/usermenu4.png"), (0, 0))
	if dexuserx == 1 and dexusery == 1:
		screen.blit(pygame.image.load("venv/IMG/usermenu5.png"), (0, 0))
	if dexuserx == 2 and dexusery == 1:
		screen.blit(pygame.image.load("venv/IMG/usermenu6.png"), (0, 0))



bankindex=1
bankin=" "

def bankmenu() :
	global usemenubool,bank,bankindex,bankin,bankbool,cars,buycarbool
	userbackac = fontop.render(str(userplay.money), True, (255, 255, 255))
	userres=fontop.render(str(userplay.respect), True, (255, 255, 255))
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				usemenubool=True
				bankbool=False
			if event.key == K_SPACE:
				if bankindex == 1:
					buycarbool=True
					bankbool=False
				if bankindex == 2:
					userplay.money-= random.randrange(int(userplay.money*0.02))
					userplay.respect+=1
				if bankindex == 3:
					pass

			if event.key == K_w:
				bankin = "up"
				move.play()
			if event.key == K_s:
				bankin = "dow"
				move.play()
	if bankin == "up":
		bankindex = bankindex - 1
		bankin = " "
	if bankin == "dow":
		bankindex = bankindex + 1
		bankin = " "
	if bankindex > 3: bankindex = 1
	if bankindex < 1: bankindex = 3
	if bankindex == 1:
		screen.blit(pygame.image.load("venv/IMG/bank1-01.png"), (0, 0))
	if bankindex == 2:
		screen.blit(pygame.image.load("venv/IMG/bank2-01.png"), (0, 0))
	if bankindex == 3:
		screen.blit(pygame.image.load("venv/IMG/bank3-01.png"), (0, 0))
	screen.blit(userbackac,(989,375))
	screen.blit(userres, (886, 265))

indexbuycarx=0
indexbuycary=0
indexbuycar=" "
daco=pygame.image.load("venv/IMG/daco.png")
moneycar1=1000000
car1respect=200
moneycar2=200000
car2respect=50
moneycar3=3000000
car3respect=300
moneycar4=340000
car4respect=400
moneycar5=900000
car5respect=500
moneycar6=463350
car6respect=500
moneycar7=3910
car7respect=20
moneycar8=3400800
car8respect=1000
def buycar ():

	global indexbuycarx,indexbuycary,indexbuycar,bankbool,buycarbool
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				bankbool = True
				buycarbool = False
			if event.key == K_SPACE:
				if (indexbuycarx == 0 and indexbuycary == 0) and userplay.cars[0]== False and userplay.money>= moneycar1 and userplay.respect>= car1respect:
					userplay.money=userplay.money-moneycar1
					updatecars(userplay.name,1)
					userplay.cars[0] =True
				if (indexbuycarx == 1 and indexbuycary == 0) and userplay.cars[1]==False and userplay.money>= moneycar2 and userplay.respect>= car2respect:
					userplay.money = userplay.money - moneycar2
					updatecars(userplay.name, 2)
					userplay.cars[1] = True
				if (indexbuycarx == 2 and indexbuycary == 0) and userplay.cars[2]==False and userplay.money>= moneycar3 and userplay.respect>= car3respect:
					userplay.money = userplay.money - moneycar3
					updatecars(userplay.name, 3)
					userplay.cars[2] = True
				if (indexbuycarx == 3 and indexbuycary == 0) and userplay.cars[3]==False and userplay.money>= moneycar4 and userplay.respect>= car4respect :
					userplay.money = userplay.money - moneycar4
					updatecars(userplay.name, 4)
					userplay.cars[3] = True
				if (indexbuycarx == 0 and indexbuycary == 1) and userplay.cars[4]==False and userplay.money>= moneycar5 and userplay.respect>= car5respect:
					userplay.money = userplay.money - moneycar5
					updatecars(userplay.name, 5)
					userplay.cars[4] = True
				if (indexbuycarx == 1 and indexbuycary == 1) and userplay.cars[5]==False and userplay.money>= moneycar6 and userplay.respect>= car6respect:
					userplay.money = userplay.money - moneycar6
					updatecars(userplay.name, 6)
					userplay.cars[5] = True
				if (indexbuycarx == 2 and indexbuycary == 1) and userplay.cars[6]==False and userplay.money>= moneycar7 and userplay.respect>= car7respect:
					userplay.money = userplay.money - moneycar7
					updatecars(userplay.name, 7)
					userplay.cars[6] = True
				if (indexbuycarx == 3 and indexbuycary == 1) and userplay.cars[7]==False and userplay.money>= moneycar8 and userplay.respect>= car8respect:
					userplay.money = userplay.money - moneycar8
					updatecars(userplay.name, 8)
					userplay.cars[7] = True
			if event.key == K_w:
				indexbuycar = "up"
				move.play()
			if event.key == K_s:
				indexbuycar = "dow"
				move.play()
			if event.key == K_d:
				indexbuycar = "right"
				move.play()
			if event.key == K_a:
				indexbuycar = "left"
				move.play()
	if indexbuycar == "up":
		indexbuycary = indexbuycary - 1
		indexbuycar = " "
	if indexbuycar == "dow":
		indexbuycary = indexbuycary + 1
		indexbuycar = " "
	if indexbuycar == "right":
		indexbuycarx = indexbuycarx + 1
		indexbuycar = " "
	if indexbuycar == "left":
		indexbuycarx = indexbuycarx - 1
		indexbuycar = " "
	if indexbuycarx > 3: indexbuycarx = 0
	if indexbuycary > 1: indexbuycary = 0
	if indexbuycarx < 0: indexbuycarx = 3
	if indexbuycary < 0: indexbuycary = 1
	if (indexbuycarx == 0 and indexbuycary == 0):
		showmoney = fontmoney.render("Price: " + str(moneycar1) + "$ "+ "Respect:" + str(car1respect),True, (255,255,255))
		screen.blit(pygame.image.load("venv/IMG/buycar1-01.png"), (0, 0))

	if (indexbuycarx == 1 and indexbuycary == 0):
		showmoney = fontmoney.render("Price: " + str(moneycar2) + "$ " + "Respect:" + str(car2respect), True,(255, 255, 255))
		screen.blit(pygame.image.load("venv/IMG/buycar2-01.png"), (0, 0))
	if (indexbuycarx == 2 and indexbuycary == 0):
		showmoney = fontmoney.render("Price: " + str(moneycar3) + "$ " + "Respect:" + str(car3respect), True,(255, 255, 255))
		screen.blit(pygame.image.load("venv/IMG/buycar3-01.png"), (0, 0))
	if (indexbuycarx == 3 and indexbuycary == 0):
		screen.blit(pygame.image.load("venv/IMG/buycar4-01.png"), (0, 0))
		showmoney = fontmoney.render("Price: " + str(moneycar4) + "$ " + "Respect:" + str(car4respect), True,(255, 255, 255))
	if (indexbuycarx == 0 and indexbuycary == 1):
		screen.blit(pygame.image.load("venv/IMG/buycar5-01.png"), (0, 0))
		showmoney = fontmoney.render("Price: " + str(moneycar5) + "$ " + "Respect:" + str(car5respect), True,(255, 255, 255))
	if (indexbuycarx == 1 and indexbuycary == 1):
		screen.blit(pygame.image.load("venv/IMG/buycar6-01.png"), (0, 0))
		showmoney = fontmoney.render("Price: " + str(moneycar6) + "$ " + "Respect:" + str(car6respect), True,(255, 255, 255))
	if (indexbuycarx == 2 and indexbuycary == 1):
		screen.blit(pygame.image.load("venv/IMG/buycar7-01.png"), (0, 0))
		showmoney = fontmoney.render("Price: " + str(moneycar7) + "$ " + "Respect:" + str(car7respect), True,(255, 255, 255))
	if (indexbuycarx == 3 and indexbuycary == 1):
		screen.blit(pygame.image.load("venv/IMG/buycar8-01.png"), (0, 0))
		showmoney = fontmoney.render("Price: " + str(moneycar8) + "$ " + "Respect:" + str(car8respect), True,(255, 255, 255))

	if userplay.cars[0] == True:
		screen.blit(daco, (158-15, 350-10))
	if userplay.cars[1] == True:
		screen.blit(daco, (635-15, 350-10))
	if userplay.cars[2] == True:
		screen.blit(daco, (1090-15, 350-10))
	if userplay.cars[3] == True:
		screen.blit(daco, (1570-15, 350-10))
	if userplay.cars[4] == True:
		screen.blit(daco, (150-15, 645-5))
	if userplay.cars[5] == True:
		screen.blit(daco, (627-15, 645-5))
	if userplay.cars[6] == True:
		screen.blit(daco, (1083-15, 645-5))
	if userplay.cars[7] == True:
		screen.blit(daco, (1565-5, 645-5))
	showbank=fontmoney.render("Your money: " + str(userplay.money) + "$ " + " Your respect:" + str(userplay.respect), True,(255, 255, 255))
	screen.blit(showmoney, (690, 1010))
	screen.blit(showbank, (690, 960))
indexcarx=0
indexcary=0
indexcar=" "
donthave=pygame.image.load("venv/IMG/donthave.png")
def Cars():
	screen.blit(imgcar, (0, 0))
	global indexcar,indexcary,indexcarx,usemenubool,cars,userplay,gameplay,car1,car2,car3,car4,car5,car6,car7,car8,listcar,update,betbool
	for event in pygame.event.get():
		if event.type == KEYDOWN:

			if event.key == K_ESCAPE:
					usemenubool = True
					cars = False
			if event.key == K_SPACE:
				if (indexcarx == 0 and indexcary == 0) and userplay.cars[0]:
					player3.img=car1
					listcar = [ car2, car3, car4, car5, car6, car7, car8]
					randomimg()
					userplay.respect+=10
					betbool=True
					cars=False
				if (indexcarx == 1 and indexcary == 0) and userplay.cars[1]:
					player3.img = car2
					listcar = [car1, car3, car4, car5, car6, car7, car8]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
				if (indexcarx == 2 and indexcary == 0 )and userplay.cars[2]:
					player3.img = car3
					listcar = [car2, car1, car4, car5, car6, car7, car8]
					update = random.sample(listcar, len(listcar))
					randomimg()
					userplay.respect += 10
					betbool=True
					cars = False
				if (indexcarx == 3 and indexcary == 0)and userplay.cars[3]:
					player3.img = car4
					listcar = [car2, car3, car1, car5, car6, car7, car8]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
				if (indexcarx == 0 and indexcary == 1)and userplay.cars[4]:
					player3.img = car5
					listcar = [car2, car3, car4, car1, car6, car7, car8]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
				if (indexcarx == 1 and indexcary == 1)and userplay.cars[5]:
					player3.img = car6
					listcar = [car2, car3, car4, car5, car1, car7, car8]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
				if (indexcarx == 2 and indexcary == 1) and userplay.cars[6]:
					player3.img = car7
					listcar = [car2, car3, car4, car5, car6, car1, car8]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
				if (indexcarx == 3 and indexcary == 1) and userplay.cars[7]:
					player3.img = car8
					listcar = [car2, car3, car4, car5, car6, car7, car1]
					randomimg()
					userplay.respect += 10
					betbool = True
					cars = False
			if event.key == K_w:
				indexcar = "up"
				move.play()
			if event.key == K_s:
				indexcar = "dow"
				move.play()
			if event.key == K_d:
				indexcar = "right"
				move.play()
			if event.key == K_a:
				indexcar = "left"
				move.play()
	if indexcar=="up" :
		indexcary =indexcary-1
		indexcar = " "
	if indexcar=="dow" :
		indexcary =indexcary+1
		indexcar = " "
	if indexcar=="right" :
		indexcarx =indexcarx+1
		indexcar = " "
	if indexcar=="left" :
		indexcarx =indexcarx-1
		indexcar = " "
	if indexcarx>3: indexcarx=0
	if indexcary>1: indexcary=0
	if indexcarx<0: indexcarx=3
	if indexcary<0: indexcary=1
	if (indexcarx == 0 and indexcary == 0)  :
		screen.blit(pygame.image.load("venv/IMG/mot.png"),(0,0))
	if (indexcarx == 1 and indexcary == 0)  :
		screen.blit(pygame.image.load("venv/IMG/hai.png"),(0,0))
	if (indexcarx == 2 and indexcary == 0 ) :
		screen.blit(pygame.image.load("venv/IMG/ba.png"),(0,0))
	if (indexcarx == 3 and indexcary == 0) :
		screen.blit(pygame.image.load("venv/IMG/bon.png"),(0,0))
	if (indexcarx == 0 and indexcary == 1) :
		screen.blit(pygame.image.load("venv/IMG/nam.png"),(0,0))
	if (indexcarx == 1 and indexcary == 1) :
		screen.blit(pygame.image.load("venv/IMG/sau.png"),(0,0))
	if (indexcarx == 2 and indexcary == 1)  :
		screen.blit(pygame.image.load("venv/IMG/bay.png"),(0,0))
	if (indexcarx == 3 and indexcary == 1)  :
		screen.blit(pygame.image.load("venv/IMG/tam.png"),(0,0))

	if  userplay.cars[0]==False :
		screen.blit(donthave, (158,350))
	if  userplay.cars[1]==False :
		screen.blit(donthave, (635,350))
	if userplay.cars[2] == False:
		screen.blit(donthave, (1090, 350))
	if userplay.cars[3] == False:
		screen.blit(donthave, (1570, 350))
	if userplay.cars[4] == False:
		screen.blit(donthave, (150,645))
	if userplay.cars[5] == False:
		screen.blit(donthave, (627, 645))
	if userplay.cars[6] == False:
		screen.blit(donthave, (1083, 645))
	if userplay.cars[7] == False:
		screen.blit(donthave, (1565, 645))
	#alo = font.render("index" + str(indexcarx), True, (0, 0, 0))
	#screen.blit(alo, (55, 55))

timei=20
def time():
	global timei
	timei-=1/240


#CHARACTER
randspeed = [0.3,0.37,0.4,0.41,0.29,0.5,0.47,0.36]
class player() :
	def __init__ (self):
		self.name = ''
		self.x = -200
		self.y = 0
		self.acc = 0
		self.speed=choice(randspeed)
		self.acc=0
		self.img=0
		self.index=0
		self.flag=[False,False,False,False,False,False,False,False,False]
		self.flagwin= False
	def update(self) :
		global time,h,rank,k,l
		if self.flag[8]==False :
			screen.blit(self.img[self.index ], (self.x, self.y))
		else:
			screen.blit(pygame.transform.flip(self.img[self.index], True, False), (self.x-20, self.y))
		#win
		if self.x >=1920:
			self.flagwin= True
		#quayze
		if self.flag[8]:

			if limit8() == True:
				pass
			else:
				self.flag[8] = False
				self.speed = 0.5
				self.acc=-self.acc
				l = 0.6
		#stun
		if self.flag[6]:
			if limit4()==True:
				pass
			else :
					self.flag[6]= False
					self.speed=0.5
					h=0.5
		#homerun
		if self.flag[5]:
			self.flag[2]=True
			self.speed=5
		#deaccerlarate
		if self.flag[4] :
			if limit6()==True:
				pass
			else :
				self.acc-= 0.05
				if self.acc <=0 :
					self.flag[4]= False
					self.speed=0.7
					k=0.8

		if self.speed  <= 0 and self.flag[6]==False and self.flag[8]==False:
			self.speed=0.4

		if self.flag[2]== True:
			screen.blit(pygame.image.load("venv/IMG/bua2ef.png"), (self.x+20, self.y-15))
		# Firerocket
		if abs(self.acc+self.speed) >=0.5 and self.flag[6]==False:
			self.flag[1]=True
		else: self.flag[1]=False
		if self.flag[1]== True:
			if self.flag[8]==False:
				if self.acc+self.speed >=1.5 :
					screen.blit(pygame.transform.scale(pygame.image.load("venv/IMG/Layer 33.png"),(50,50)), (self.x - 60, self.y-5))
				else:
					screen.blit(pygame.image.load("venv/IMG/Layer 33.png"), (self.x-40, self.y+10))
			else :
				if self.acc+self.speed <=-3.5 :
					screen.blit(pygame.transform.flip(
						pygame.transform.scale(pygame.image.load("venv/IMG/Layer 33.png"), (50, 50)), True, False),(self.x +100, self.y - 5))
				else:
					screen.blit(pygame.transform.flip(pygame.image.load("venv/IMG/Layer 33.png"), True, False),(self.x + 80, self.y + 10))
		#Runcar
		self.index=self.index+1
		if(self.index==len(self.img)):
			self.index=0
		self.x= self.x + self.speed +self.acc
		if self.x <-200:
			self.x =-200
		#Gameend
		if timei < 0 :
			self.flag[2]=True
			self.speed=7

	def restart(self) :
		self.name = ''
		self.x = -200
		self.y = 0
		self.acc = 0
		self.speed = choice(randspeed)
		self.acc = 0
		self.img = 0
		self.index = 0
		self.flag = [False,False,False,False,False,False,False,False,False]
		self.flagwin = False

#player

car1=[pygame.image.load("venv/IMG/xe1.1.png"),pygame.image.load("venv/IMG/xe1.2.png"),pygame.image.load("venv/IMG/xe1.3.png")]
car2=[pygame.image.load("venv/IMG/xe2.1.png"),pygame.image.load("venv/IMG/xe2.2.png"),pygame.image.load("venv/IMG/xe2.3.png")]
car3=[pygame.image.load("venv/IMG/xe3.1.png"),pygame.image.load("venv/IMG/xe3.2.png"),pygame.image.load("venv/IMG/xe3.3.png")]
car4=[pygame.image.load("venv/IMG/xe4.1.png"),pygame.image.load("venv/IMG/xe4.2.png"),pygame.image.load("venv/IMG/xe4.3.png")]
car5=[pygame.image.load("venv/IMG/xe5.1.png"),pygame.image.load("venv/IMG/xe5.2.png"),pygame.image.load("venv/IMG/xe5.3.png")]
car6=[pygame.image.load("venv/IMG/xe6.1.png"),pygame.image.load("venv/IMG/xe6.2.png"),pygame.image.load("venv/IMG/xe6.3.png")]
car7=[pygame.image.load("venv/IMG/xe7.1.png"),pygame.image.load("venv/IMG/xe7.2.png"),pygame.image.load("venv/IMG/xe7.3.png")]
car8=[pygame.image.load("venv/IMG/xe8.1.png"),pygame.image.load("venv/IMG/xe8.2.png"),pygame.image.load("venv/IMG/xe8.3.png")]

listcar=0
update=0
player1 =player()
player1.y= 625

player2= player()
player2.y= 695

player3= player()
player3.y=770

player4= player()
player4.y=845

player5= player()
player5.y=915

lane1 = 625
lane2 = 695
lane3 = 770
lane4 = 845
lane5 = 915
listlane = [lane1, lane2, lane3, lane4, lane5]
def randomimg():
	global listcar,update
	update = random.sample(listcar, len(listcar))
	player1.img = update[1]
	player2.img = update[2]
	player4.img = update[4]
	player5.img = update[5]
l=0.5
def limit8 ():
	global l
	l-=1/240
	if l>=0 :
		return True
	else:
		return False

k=0.8
def limit6( ):
	global k
	k-=1/240
	if k>=0 :
		return True
	else: return False
h=0.5
def limit4( ):
	global h
	h-=1/240
	if h>=0 :
		return True
	else: return False
imgbua1=pygame.image.load("venv/IMG/bua1.png")
imgbua2=pygame.image.load("venv/IMG/bua2.png")
imgbua3=pygame.image.load("venv/IMG/bua3.png")
imgbua4=pygame.image.load("venv/IMG/bua4.png")
imgbua5=pygame.image.load("venv/IMG/bua5.png")
imgbua6=pygame.image.load("venv/IMG/bua6.png")
imgbua7=pygame.image.load("venv/IMG/bua7.png")
imgbua8=pygame.image.load("venv/IMG/bua8.png")

countobs=0
listbua=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,6,6,6,6,7,8,8,8,8,]
class bua():
	def __init__(self):
		self.img = pygame.image.load("venv/IMG/icon.png")
		self.list=[]
		for i in range(obs):
			x = random.randrange(pygame.display.Info().current_w*2, pygame.display.Info().current_w * 7)+500
			y = random.choice(listlane)
			fun= random.choice(listbua)

			self.list.append([x, y, fun])

	def update(self):
		for i in range(obs):
			self.list[i][0]=self.list[i][0]-2.5
	def buamot(self,id):
		self.m=1
		if id==1:
			player1.acc=player1.acc+self.m
			if player1.x <=1920 :soundbua1.play()
		if id==2:
			player2.acc=player2.acc+self.m
			if player2.x <= 1920: soundbua1.play()
		if id==3:
			player3.acc=player3.acc+self.m
			if player3.x <= 1920: soundbua1.play()
		if id==4:
			player4.acc=player4.acc+self.m
			if player4.x <= 1920: soundbua1.play()
		if id==5:
			if player5.x <= 1920: soundbua1.play()
			player5.acc=player5.acc+self.m
	def buahai(self,id):
			if id == 1:
				player1.flag[2]=True
			if id == 2:
				player2.flag[2]=True
			if id == 3:
				player3.flag[2]=True
			if id == 4:
				player4.flag[2]=True
			if id == 5:
				player5.flag[2]=True
			enter.play()
	def buaba(self,id):
		self.n = -0.5
		self.k=0
		if id==1:
			player1.speed=player1.speed+self.n
			player1.acc=self.k
			if player1.x <=1920 :enter.play()
		if id==2:
			player2.speed=player2.speed+self.n
			player2.acc = self.k
			if player2.x <=1920 :enter.play()
		if id==3:
			player3.speed=player3.speed+self.n
			player3.acc = self.k
			if player3.x <=1920 :enter.play()
		if id==4:
			player4.speed=player4.speed+self.n
			player4.acc = self.k
			if player4.x <=1920 :enter.play()
		if id==5:
			player5.speed=player5.speed+self.n
			player5.acc = self.k
			if player5.x <=1920 :enter.play()

	def buabon(self,id):
		self.q = 1.5
		if id==1 :
			player1.flag[4] = True
			player1.acc=player1.acc+self.q
			if player1.x <=1920 :enter.play()
		if id==2:
			player2.flag[4] = True
			player2.acc = player2.acc + self.q
			if player1.x <= 1920: enter.play()
		if id==3:
			player3.flag[4] = True
			player3.acc = player3.acc + self.q
			if player1.x <= 1920: enter.play()
		if id==4:
			player4.flag[4] = True
			player4.acc = player4.acc + self.q
			if player4.x <= 1920: enter.play()
		if id==5:
			player5.flag[4] = True
			player5.acc = player5.acc + self.q
			if player1.x <= 1920: enter.play()

	def buanam (self,id):
		if id == 1:
			player1.flag[5]=True
		if id == 2:
			player2.flag[5]=True
		if id == 3:
			player3.flag[5]=True
		if id == 4:
			player4.flag[5]=True
		if id == 5:
			player5.flag[5]=True
	def buasau(self,id):
		if id == 1:
			player1.flag[6]=True
			player1.speed=-2.5
			player1.acc=0
		if id == 2:
			player2.flag[6]=True
			player2.speed = -2.5
			player2.acc = 0
		if id == 3:
			player3.flag[6]=True
			player3.speed = -2.5
			player3.acc = 0
		if id == 4:
			player4.flag[6]=True
			player4.speed = -2.5
			player4.acc = 0
		if id == 5:
			player5.flag[6]=True
			player5.speed = -2.5
			player5.acc = 0

	def buabay(self,id):
		if id == 1:
			player1.x= -60
		if id == 2:
			player2.x= -60
		if id == 3:
			player3.x= -60
		if id == 4:
			player4.x= -60
		if id == 5:
			player5.x= -60

	def buatam(self,id):
		if id == 1:
			player1.flag[8]=True
			player1.speed = -(player1.speed + 2.5)
			player1.acc = -player1.acc
		if id == 2:
			player2.flag[8]=True
			player2.speed = -(player2.speed + 2.5)
			player2.acc = -player2.acc
		if id == 3:
			player3.flag[8] = True
			player3.speed = -(player3.speed + 2.5)
			player3.acc = -player3.acc
		if id == 4:
			player4.flag[8] = True
			player4.speed = -(player4.speed + 2.5)
			player4.acc = -player4.acc
		if id == 5:
			player5.flag[8] = True
			player5.speed = -(player5.speed + 2.5)
			player5.acc = -player5.acc
	def funtion(self):
		global countobs
		for i in range(obs):
			if collide(self.list[i][0],player1.x,self.list[i][1],player1.y) :
				countobs+=1
				self.list[i][0] = -100
				if player1.flag[2] == False :
					if self.list[i][2 ] == 1:
						self.buamot(1)
					if self.list[i][2] == 2:
						self.buahai(1)
					if self.list[i][2] == 3:
						self.buaba(1)
					if self.list[i][2] == 4 :
						self.buabon(1)
					if self.list[i][2] == 5 :
						self.buanam(1)
					if self.list[i][2] == 6 :
						self.buasau(1)
					if self.list[i][2] == 7 :
						self.buabay(1)
					if self.list[i][2] == 8 :
						self.buatam(1)
				else:
					player1.flag[2] = False

			if collide(self.list[i][0], player2.x, self.list[i][1], player2.y):
				countobs += 1
				self.list[i][0] = -100
				if player2.flag[2] == False:
					if self.list[i][2] == 1:
						self.buamot(2)
					if self.list[i][2] == 2:
						self.buahai(2)
					if self.list[i][2] == 3:
						self.buaba(2)
					if self.list[i][2] == 4:
						self.buabon(2)
					if self.list[i][2] == 5:
						self.buanam(2)
					if self.list[i][2] == 6:
						self.buasau(2)
					if self.list[i][2] == 7:
						self.buabay(2)
					if self.list[i][2] == 8 :
						self.buatam(2)
				else:
					player2.flag[2] = False
			if collide(self.list[i][0], player3.x, self.list[i][1], player3.y):
				countobs += 1
				self.list[i][0] = -100
				if player3.flag[2] == False:
					if self.list[i][2] == 1:
						self.buamot(3)
					if self.list[i][2] == 2:
						self.buahai(3)
					if self.list[i][2] == 3:
						self.buaba(3)
					if self.list[i][2] == 4:
						self.buabon(3)
					if self.list[i][2] == 5:
						self.buanam(3)
					if self.list[i][2] == 6:
						self.buasau(3)
					if self.list[i][2] == 7:
						self.buabay(3)
					if self.list[i][2] == 8 :
						self.buatam(3)
				else:
					player3.flag[2] = False
			if collide(self.list[i][0], player4.x, self.list[i][1], player4.y):
				countobs += 1
				self.list[i][0] = -100
				if player4.flag[2] == False:
					if self.list[i][2] == 1:
						self.buamot(4)
					if self.list[i][2] == 2:
						self.buahai(4)
					if self.list[i][2] == 3:
						self.buaba(4)
					if self.list[i][2] == 4:
						self.buabon(4)
					if self.list[i][2] == 5:
						self.buanam(4)
					if self.list[i][2] == 6:
						self.buasau(4)
					if self.list[i][2] == 7:
						self.buabay(4)
					if self.list[i][2] == 8 :
						self.buatam(4)
				else:
					player4.flag[2] = False
			if collide(self.list[i][0], player5.x, self.list[i][1], player5.y):
				countobs += 1
				self.list[i][0] = -100
				if player5.flag[2] == False:
					if self.list[i][2] == 1:
						self.buamot(5)
					if self.list[i][2] == 2:
						self.buahai(5)
					if self.list[i][2] == 3:
						self.buaba(5)
					if self.list[i][2] == 4:
						self.buabon(5)
					if self.list[i][2] == 5:
						self.buanam(5)
					if self.list[i][2] == 6:
						self.buasau(5)
					if self.list[i][2] == 7:
						self.buabay(5)
					if self.list[i][2] == 8 :
						self.buatam(5)

				else:
					player5.flag[2] = False
	def draw(self):
		for i in range(obs):
			if self.list[i][2]==1:
				self.img=imgbua1
			if self.list[i][2] == 2:
				self.img =imgbua2
			if self.list[i][2] == 3:
				self.img =imgbua3
			if self.list[i][2] == 4:
				self.img =imgbua4
			if self.list[i][2] == 5:
				self.img =imgbua5
			if self.list[i][2] == 6:
				self.img =imgbua6
			if self.list[i][2] == 7:
				self.img =imgbua7
			if self.list[i][2] == 8:
				self.img =imgbua8
			if near(player1.x,self.list[i][0],player1.y,self.list[i][1]):
				screen.blit(self.img, (self.list[i][0], self.list[i][1]))
			if near(player2.x,self.list[i][0],player2.y,self.list[i][1]):
				screen.blit(self.img, (self.list[i][0], self.list[i][1]))
			if near(player3.x,self.list[i][0],player3.y,self.list[i][1]):
				screen.blit(self.img, (self.list[i][0], self.list[i][1]))
			if near(player4.x,self.list[i][0],player4.y,self.list[i][1]):
				screen.blit(self.img, (self.list[i][0], self.list[i][1]))
			if near(player5.x,self.list[i][0],player5.y,self.list[i][1]):
				screen.blit(self.img, (self.list[i][0], self.list[i][1]))

	def restart(self):
		self.list = []
		for i in range(obs):
			x = random.randrange(pygame.display.Info().current_w, pygame.display.Info().current_w * 6) + 500
			y = random.choice(listlane)
			fun = random.randrange(1, 9)
			if fun == 5:
				fun = random.randrange(1, 9)
			self.list.append([x, y, fun])
hethongbua=bua()
def near (x1,x2,y1,y2):
	if ( math.sqrt (math.pow(x1-x2,2))  <=300) and (y1==y2):
			return True
	else :
		return False
def collide (x1, x2 ,y1,y2) :
	if  math.sqrt (math.pow(x1-x2,2)) + math.sqrt (math.pow(y1-y2,2))  <=5 :
			return True
	else :
		return False
#DRAW BACKGROUNG
xduong = 0
xback =0
def backupdate():
		global xduong , xback
		screen.blit(back,(xback,0))
		screen.blit(back, (xback+1920, 0))
		xduong = xduong - 2.5
		xback=xback-0.1
		screen.blit(duong, (xduong, 0))
		screen.blit(duong, (xduong+1920, 0))
		if (xduong==-1920):
			xduong=0
		if(xback==-1920):
			xback=0


#BET
namelist=["Liam","Olivia","Noah","Emma","Oliver","Ava","William","Sophia","Elijah","Isabella","James","Charlotte","Benjamin","Amelia","Lucas","Mia","Mason","Harper","Ethan","Evelyn"]
nameup=random.sample(namelist, len(namelist))
player1.name= nameup[0]
player2.name= nameup[1]
player4.name= nameup[2]
player5.name= nameup[3]
name1b=fontbet.render(player1.name,True,(255,255,255))
name2b=fontbet.render(player2.name,True,(255,255,255))
name4b=fontbet.render(player4.name,True,(255,255,255))
name5b=fontbet.render(player5.name,True,(255,255,255))
betimg=pygame.image.load("venv/IMG/bet-01.png")

inputbet=''
flagspace1=False
bet1,bet2,bet3,bet4= 0,0,0,0
betsum=0
nhat=0
nhi=0
ba=0
NHAT=0
NHI=0
BA=0
flagbet=False

def bet():
	global usemenubool, betbool, gameplay, inputbet, intbet, flagspace1, bet1, bet2, bet3, bet4, flagbet, betsum, nhat, nhi, ba, NHAT, NHI, BA
	name3b = fontbet.render(userplay.name, True, (255, 255, 255))
	a = userplay.money
	if inputbet !="" :
		a=userplay.money-int(inputbet)
	for event in pygame.event.get():
		if event.type == KEYDOWN:

			if event.key == K_ESCAPE:
				usemenubool = True
				betbool = False
				flagbet=False
				inputbet=""
				nhat = 0
				nhi = 0
				ba = 0
				bet1, bet2, bet3, bet4 = 0, 0, 0, 0
			if event.key == K_SPACE and inputbet !="" :
				flagspace1 =True
				if int(inputbet) <= userplay.money :
					if userplay.money==0:
						pass
					else :
						userplay.money=a
						gameplay=True
						betbool=False
						count.play()
			if  flagspace1 == False:
				if event.key == K_BACKSPACE:
					inputbet = inputbet[0:-1]
				if event.key== K_0 or event.key== K_KP0:
					inputbet += "0"
				if event.key== K_1 or event.key== K_KP1:
					inputbet += "1"
				if event.key == K_2 or event.key== K_KP2:
					inputbet += "2"
				if event.key == K_3 or event.key== K_KP3:
					inputbet += "3"
				if event.key == K_4 or event.key== K_KP4:
					inputbet += "4"
				if event.key == K_5 or event.key== K_KP5:
					inputbet += "5"
				if event.key == K_6 or event.key== K_KP6:
					inputbet += "6"
				if event.key == K_7 or event.key== K_KP7:
					inputbet += "7"
				if event.key == K_8 or event.key== K_KP8:
					inputbet += "8"
				if event.key == K_9 or event.key== K_KP9:
					inputbet += "9"
				flagbet=True
				move.play()


	moneybet = fontmoney.render(str(inputbet) +"$", True, (255, 255, 255))
	if a>=0:
		showbank = fontmoney.render(userplay.name + "'s bank account:"+str(a)+ "$",True,(255,0,0))
	else:
		showbank = fontmoney.render("You dont have enough money!", True, (255, 0, 0))

	if (flagbet==True and inputbet != '') and float(inputbet) !=0:
		bet1 = random.randrange(int(float(inputbet) * 0.9), int(float(inputbet) * 1.3))
		bet2 = random.randrange(int(float(inputbet) * 0.9), int(float(inputbet) * 1.3))
		bet3 = random.randrange(int(float(inputbet) * 0.9), int(float(inputbet) * 1.3))
		bet4 = random.randrange(int(float(inputbet) * 0.9), int(float(inputbet) * 1.3))
		# calculate
		nhat =int ( (float(bet1) + float(bet2) + float(bet3) + float(bet4) + float(inputbet) ) *0.5 )
		nhi =int ( (float(bet1) + float(bet2) + float(bet3) + float(bet4) + float(inputbet) ) *0.3 )
		ba = int((float(bet1) + float(bet2) + float(bet3) + float(bet4) + float(inputbet)) * 0.2)
	if inputbet=="" :
		bet1=0
		bet2=0
		bet3=0
		bet4=0
		nhat=0
		nhi=0
		ba=0
	Bet1 = fontmoney.render(str(bet1) + "$", True, (255, 255, 255))
	Bet2 = fontmoney.render(str(bet2) + "$", True, (255, 255, 255))
	Bet3 = fontmoney.render(str(bet3) + "$", True, (255, 255, 255))
	Bet4 = fontmoney.render(str(bet4) + "$", True, (255, 255, 255))
	NHAT = fontmoney.render(str(nhat) + "$", True, (255, 0, 0))
	NHI = fontmoney.render(str(nhi) + "$", True, (255, 0, 0))
	BA = fontmoney.render(str(ba) + "$", True, (255, 0, 0))
	screen.blit(betimg, (0, 0))
	screen.blit(name1b, (1040, 305))
	screen.blit(name2b, (1471, 303))
	screen.blit(name3b, (222, 870))
	screen.blit(name4b, (1039, 612))
	screen.blit(name5b, (1453, 618))
	screen.blit(player1.img[1], (1102, 371))
	screen.blit(player2.img[1], (1535, 378))
	screen.blit(player3.img[1], (227, 940))
	screen.blit(player4.img[1], (1117, 680))
	screen.blit(player5.img[1], (1539, 690))
	screen.blit(moneybet, (906, 942))
	screen.blit(Bet1, (1122, 422))
	screen.blit(Bet2, (1550, 425))
	screen.blit(Bet3, (1122, 729))
	screen.blit(Bet4, (1550, 729))
	screen.blit(NHAT, (380, 452))
	screen.blit(NHI, (380, 587))
	screen.blit(BA, (380, 717 ))
	screen.blit(showbank, (528, 851))

	flagspace1 = False
	flagbet=False


#WINNER FUNTIONS
rank=[]
gameresult=False
def Rank():
	global rank, gameover,gameplay,gameresult
	if len(rank)>=5:
		gameplay=False
		gameresult=True
	else:
		if player1.x>=1920 and player1.flagwin== False:
			rank.append(1)
			player1.flagwin== True
		if player2.x>=1920 and player2.flagwin== False:
			rank.append(2)
			player2.flagwin == True
		if player3.x>=1920and player3.flagwin== False:
			rank.append(3)
			player3.flagwin == True
		if player4.x>=1920and player4.flagwin== False:
			rank.append(4)
			player4.flagwin == True
		if player5.x>=1920and player5.flagwin== False:
			rank.append(5)
			player5.flagwin == True



indexwin=" "
dexwin=0
prize=0
def Win ():
	global rank,NHAT,NHI,BA,indexwin,nhat,nhi,ba,gameresult,cars,dexwin,usemenubool,prize
	race.fadeout(500)
	count.fadeout(500)
	if rank[0]==3:
		prize=nhat
	if rank[1] == 3:
		prize = nhi
	if rank[2] == 3:
		prize = ba
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_SPACE:
				if dexwin == 1:
					userplay.money= userplay.money+prize
					prize=0
					nhat=0
					nhi=0
					ba=0
				if dexwin == 2:
					userplay.money = userplay.money + prize
					cars=True
					gameresult = False
				if dexwin == 3:
					userplay.money = userplay.money + prize
					usemenubool=True
					gameresult = False
			if event.key == K_w:
				indexwin = "up"
				move.play()
			if event.key == K_s:
				indexwin = "dow"
				move.play()
	showprize=fontmoney.render(str(prize),True,(0,0,0))
	if indexwin == "up":
		dexwin = dexwin - 1
		indexwin = " "
	if indexwin == "dow":
		dexwin = dexwin + 1
		indexwin = " "
	if dexwin > 3: dexwin = 1
	if dexwin < 1: dexwin = 3
	if dexwin == 1:
		screen.blit(pygame.image.load("venv/IMG/rank.png"), (0, 0))
	if dexwin == 2:
		screen.blit(pygame.image.load("venv/IMG/rank2-01.png"), (0, 0))
	if dexwin == 3:
		screen.blit(pygame.image.load("venv/IMG/rank3-01.png"), (0, 0))


	listimgplayer = [0, player1.img[1], player2.img[1], player3.img[1], player4.img[1], player5.img[1]]
	screen.blit(listimgplayer[rank[0]],(500,320))
	screen.blit(listimgplayer[rank[1]], (500, 460))
	screen.blit(listimgplayer[rank[2]], (500, 590))
	screen.blit(listimgplayer[rank[3]], (500, 700))
	screen.blit(listimgplayer[rank[4]], (500, 840))
	textmoney=fontmoney.render(str(userplay.money)+ "$", True, (255, 255, 255))
	screen.blit(showprize, (1438, 137))
	screen.blit(textmoney,(1223,333))
	if gameresult == False:
		gamerestart()


def mini_game():
    #basket
	global usemenubool,minigamebool
	basketImg = pygame.image.load('basket (2).png')
	basketX = 836
	basketY = 900
	basketChange = 0
	# score
	score = 0
	main_font = pygame.font.SysFont('comicsans', 40)
	def show_score(x, y):
		scoreI = main_font.render("Score: " + str(score), 1, (0, 0, 0))
		screen.blit(scoreI, (x, y))
    # Time
	time = 15
	def show_time(x, y):
		timeI = main_font.render("Time: " + str(round(time)), 1, (0, 0, 0))
		screen.blit(timeI, (x, y))
	def over_game(x, y):
		overI = main_font.render("GAME OVER", 1, (0, 0, 0))
		screen.blit(overI, (x, y))
		uScore = main_font.render("YOUR SCORE: " + str(score), 1, (0, 0, 0))
		screen.blit(uScore, (x - 20, y + 30))
    # something
	num_of_st = random.randint(20,40)
	wheelI = []
	wheelX = []
	wheelY = []
	wheelY_change = []
	listChange = [1, 0.8, 0.9, 1.5, 1.25, 0.78,1.8]
	for i in range(num_of_st):
		wheelI.append(pygame.image.load("car.png"))
		wheelX.append(random.randint(30, 1920))
		wheelY.append(random.randint(-1920, -50))
		wheelY_change.append(random.choice(listChange))
    # collision
	def isCollision(x, y, m, n):
		dis = math.sqrt(math.pow(x - m, 2) + (math.pow(y - n, 2)))
		if dis < 60:
			return True
		else:
			return False
	def basket(x, y):
		screen.blit(basketImg, (x, y))
	run=True
	while run:
		clock.tick(240)
		time -= 1 / 240
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					usemenubool=True
					minigamebool=False
					userplay.money = userplay.money + score * 10
					run=False

				if event.key == pygame.K_d:
					basketChange = 7
				if event.key == pygame.K_a:
					basketChange = -7

		screen.fill((255, 255, 255))
		basket(basketX, basketY)
		basketX += basketChange
		for i in range(num_of_st):
			screen.blit(wheelI[i], (wheelX[i], wheelY[i]))
			wheelY[i] += wheelY_change[i]
			collision = isCollision(wheelX[i], wheelY[i], basketX, basketY)
			if collision:
				coin.play()
				score += 1
				wheelY[i] = 1200
		if basketX <= 0:
			basketChange=7
		elif basketX >= 1865:
			basketChange=-7
		show_score(10, 10)
		show_time(1050, 10)
		if time <= 0:
			over_game(1920/2-100, 1080/2)
			time = 0
			for i in range(num_of_st):
				wheelX[i] = 600
		pygame.display.update()
accindex=1
accdex=" "
usename1=user1.name
usename2=user2.name
usename3=user3.name
flagspaceac=False
flagsave=False

pas=0
nam=0
def account():
	global accindex,accdex,nameac,passwordac,flagspaceac,indexuser,usemenubool,accbool,usename2,usename2,usename1,flagsave,pas,nam,passbool,flagdelete
	flagst = False
	if flagst== False:
		pas=userplay.pas
		nam=userplay.name
		flagst=True
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				if event.key == K_ESCAPE:
					usemenubool=True
					accbool=False
					if flagsave==False :
						userplay.pas=pas
						userplay.name=nam
			if event.key == K_SPACE:
				enter.play()
				if accindex == 1:
					flagspaceac = not flagspaceac
				if accindex == 2:
					flagspaceac= not flagspaceac
				if accindex == 3:
					flagsave=True
					enter.play()
					if indexuser==1:
						updatename(usename1, userplay.name)
						updatepassword(userplay.name,userplay.pas)
					if indexuser==2:
						updatename(usename2,userplay.name)
						updatepassword(user2.name, userplay.pas)
					if indexuser==3:
						updatename(usename3,userplay.name)
						updatepassword(user3.name, userplay.pas)
				if accindex == 4:

					flagdelete=True
					accbool=False
					passbool=True
			if event.unicode and accindex==1 and flagspaceac:
				userplay.name+=event.unicode
				move.play()
			if event.unicode and accindex==2 and flagspaceac:
				userplay.pas+=event.unicode
				move.play()
			if event.key == K_BACKSPACE and accindex==1 and flagspaceac :
				userplay.name = userplay.name[0:-1]
				move.play()
			if event.key == K_BACKSPACE and accindex==2 and flagspaceac:
				userplay.pas = userplay.pas[0:-1]
				move.play()
			if event.key == K_w and flagspaceac==False:
				accdex = "up"
				move.play()
			if event.key == K_s and flagspaceac==False:
				accdex = "dow"
				move.play()
	# direct
	nametext = fontop.render(userplay.name, True, (0, 0, 0))
	pastext = fontop.render(userplay.pas, True, (0, 0, 0))
	if accdex == "up":
		accindex = accindex - 1
		accdex = " "
	if accdex == "dow":
		accindex = accindex + 1
		accdex = " "
	if accindex > 4: accindex = 1
	if accindex < 1: accindex = 4
	if accindex == 1:
		screen.blit(pygame.image.load("venv/IMG/acc1-01.png"), (0, 0))
	if accindex == 1 and flagspaceac== True:
		screen.blit(pygame.image.load("venv/IMG/acc1.1-01.png"), (0, 0))
	if accindex == 2:
		screen.blit(pygame.image.load("venv/IMG/acc2-01.png"), (0, 0))
	if accindex == 2 and flagspaceac== True:
		screen.blit(pygame.image.load("venv/IMG/acc2.1-01.png"), (0, 0))
	if accindex == 3:
		screen.blit(pygame.image.load("venv/IMG/acc3-01.png"), (0, 0))
	if accindex == 4:
		screen.blit(pygame.image.load("venv/IMG/acc4-01.png"), (0, 0))
	screen.blit(nametext,(835,385))
	screen.blit(pastext, (829, 535))

def gamerestart():
	global rank,bet1, bet2, bet3, bet4,betsum,nhat ,nhi,ba ,NHAT,NHI ,BA,xduong ,xback ,prize,timei,inputbet,hethongbua
	inputbet=""
	timei = 20
	rank=[]
	bet1, bet2, bet3, bet4 = 0, 0, 0, 0
	betsum = 0
	nhat = 0
	nhi = 0
	ba = 0
	NHAT = 0
	NHI = 0
	BA = 0
	xduong = 0
	xback = 0
	prize=0
	player1.restart()
	player2.restart()
	player3.restart()
	player4.restart()
	player5.restart()
	player1.y = 625
	player2.y = 695
	player3.y = 770
	player4.y = 845
	player5.y = 915
	hethongbua.restart()
updaterepect('hello',10000)
htpbool=False
def htp():
	global htpbool,menubool
	imghtp= pygame.image.load("venv/IMG/htp-01.png");
	screen.blit(imghtp,(0,0))
	for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					htpbool=False
					menubool=True

#GAME LOOP
print(user1.pas);
while running :
	if startbool == True:
		Start()
	if menubool==True:
		Menu()
	if htpbool==True:
		htp()
	if optionbool==True:
		Option()
	if userbool==True:
		user()
	if passbool==True:
		passcode()
	if usemenubool==True:
		usemenu()
	if accbool==True:
		account()
	if minigamebool==True:
		mini_game()
	if bankbool==True:
		bankmenu()
	if buycarbool==True:
		buycar()
	if cars==True:
		Cars()
	if  betbool==True:
		bet()
	if gameplay == True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
		mixer.music.fadeout(1000)

		race.play()
		backupdate()
		player1.update()
		player2.update()
		player3.update()
		player4.update()
		player5.update()
		time()

		hethongbua.update()
		hethongbua.funtion()
		hethongbua.draw()
		Rank()
	if gameresult == True:
		Win()
	clock.tick(240)
	pygame.display.flip()
pygame.quit()
