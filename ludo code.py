'''
Made by NEELANGSHU ROY
Student of B.Tech in Computer Science and Engineering at NIT Allahabad
Batch of 2021-25
'''
import sys
import random
import pygame
from pygame.locals import *
from functools import cmp_to_key

SCREEN = pygame.display.set_mode((1500,780))
FPS = 30
GAME_SPRITES,GAME_SOUNDS={},{}
def roll():
    gamedet={
        "game mode": 0,
        "chosen colours": []
    }
    bgimg=GAME_SPRITES['background']
    ldname=GAME_SPRITES['ludoname']
    myname=GAME_SPRITES['myname']
    ldboard=GAME_SPRITES['gameboard']
    colpick=GAME_SPRITES['colpick']

    modpick=GAME_SPRITES['modpick']
    modhov=[0,0,0,0]

    redopt=GAME_SPRITES['red_opt']
    yellowopt=GAME_SPRITES['yellow_opt']
    blueopt=GAME_SPRITES['blue_opt']
    greenopt=GAME_SPRITES['green_opt']
    colhov=[0,0,0,0]

    turn=GAME_SPRITES['gameturn']
    whosturn=GAME_SPRITES['whosturn']
    diceroller=GAME_SPRITES['dice_roller']
    dice=GAME_SPRITES['dicelabel']

    start_button=GAME_SPRITES['start']
    starthov=0

    roll=GAME_SPRITES['roll']
    activate=GAME_SPRITES['activate']
    movpawns=GAME_SPRITES['movepawns']

    modchoose=-1

    compcol=''
    playerscol=['','','','']

    who_turn=1
    reds=GAME_SPRITES['redpawn']
    yellows=GAME_SPRITES['yellowpawn']
    blues=GAME_SPRITES['bluepawn']
    greens=GAME_SPRITES['greenpawn']

    GAMESTART=0
    t=-1
    counter=-1
    songend=0
    while True:
        if songend<=195:songend+=1
        if songend>=195:
            counter+=1
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                GAME_SOUNDS['buttonclick'].play()
                pygame.quit()
                sys.exit()

            if(modchoose!=-1 and who_turn>modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 1230<=x<=1370 and 270<=y<=336):
                GAME_SOUNDS['startbuttonclick'].play()
                GAMESTART=1
                GAME_SOUNDS['welcome'].stop()
                return gamedet
            
            x,y=pygame.mouse.get_pos()
            if(modchoose==-1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 30<=x<=230 and 77+10<=y<=131+10):
                GAME_SOUNDS['buttonclick'].play()
                modchoose=0
                gamedet['game mode']=modchoose
            elif(modchoose==-1 and 30<=x<=230 and 77+10<=y<=131+10):#modes hover
                modhov[0]=1
            elif(modchoose!=0):
                modhov[0]=0
            
            if(modchoose==-1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 30<=x<=230 and 136+10<=y<=190+10):
                GAME_SOUNDS['buttonclick'].play()
                modchoose=1
                gamedet['game mode']=modchoose
            elif(modchoose==-1 and 30<=x<=230 and 136+10<=y<=190+10):
                modhov[1]=1
            elif(modchoose!=1):
                modhov[1]=0
            
            if(modchoose==-1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 30<=x<=230 and 195+10<=y<=249+10):
                GAME_SOUNDS['buttonclick'].play()
                modchoose=2
                gamedet['game mode']=modchoose
            elif(modchoose==-1 and 30<=x<=230 and 195+10<=y<=249+10):
                modhov[2]=1
            elif(modchoose!=2):
                modhov[2]=0
            
            if(modchoose==-1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 30<=x<=230 and 254+10<=y<=307+10):
                GAME_SOUNDS['buttonclick'].play()
                modchoose=3
                gamedet['game mode']=modchoose
            elif(modchoose==-1 and 30<=x<=230 and 254+10<=y<=307+10):
                modhov[3]=1
            elif(modchoose!=3):
                modhov[3]=0

            if(GAMESTART==0 and 35<=x<=165 and 578<=y<=626):#colours hover
                colhov[0]=1
            elif(playerscol[0]!='red' and playerscol[1]!='red' and playerscol[2]!='red' and playerscol[3]!='red'):
                colhov[0]=0
            if(GAMESTART==0 and 35<=x<=165 and 632<=y<=680):
                colhov[1]=1
            elif(playerscol[0]!='yellow' and playerscol[1]!='yellow' and playerscol[2]!='yellow' and playerscol[3]!='yellow'):
                colhov[1]=0
            if(GAMESTART==0 and 175<=x<=305 and 578<=y<=626):
                colhov[2]=1
            elif(playerscol[0]!='blue' and playerscol[1]!='blue' and playerscol[2]!='blue' and playerscol[3]!='blue'):
                colhov[2]=0
            if(GAMESTART==0 and 175<=x<=305 and 632<=y<=680):
                colhov[3]=1
            elif(playerscol[0]!='green' and playerscol[1]!='green' and playerscol[2]!='green' and playerscol[3]!='green'):
                colhov[3]=0

            if(modchoose==0):
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 578<=y<=626 and 'red' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='red'
                    compcol='yellow'
                    who_turn+=1
                    gamedet['chosen colours']=['yellow','red']
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 632<=y<=680 and 'yellow' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='yellow'
                    compcol='red'
                    who_turn+=1
                    gamedet['chosen colours']=['red','yellow']
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 578<=y<=626 and 'blue' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='blue'
                    compcol='green'
                    who_turn+=1
                    gamedet['chosen colours']=['green','blue']
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 632<=y<=680 and 'green' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='green'
                    compcol='blue'
                    who_turn+=1
                    gamedet['chosen colours']=['blue','green']
            elif(modchoose==1):
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 578<=y<=626 and 'red' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='red'
                    who_turn+=1
                    gamedet['chosen colours'].append('red')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 632<=y<=680 and 'yellow' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='yellow'
                    who_turn+=1
                    gamedet['chosen colours'].append('yellow')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 578<=y<=626 and 'blue' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='blue'
                    who_turn+=1
                    gamedet['chosen colours'].append('blue')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 632<=y<=680 and 'green' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='green'
                    who_turn+=1
                    gamedet['chosen colours'].append('green')
            elif(modchoose==2):
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 578<=y<=626 and 'red' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='red'
                    who_turn+=1
                    gamedet['chosen colours'].append('red')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 632<=y<=680 and 'yellow' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='yellow'
                    who_turn+=1
                    gamedet['chosen colours'].append('yellow')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 578<=y<=626 and 'blue' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='blue'
                    who_turn+=1
                    gamedet['chosen colours'].append('blue')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 632<=y<=680 and 'green' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='green'
                    who_turn+=1
                    gamedet['chosen colours'].append('green')
            elif(modchoose==3):
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 578<=y<=626 and 'red' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='red'
                    who_turn+=1
                    gamedet['chosen colours'].append('red')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 35<=x<=165 and 632<=y<=680 and 'yellow' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='yellow'
                    who_turn+=1
                    gamedet['chosen colours'].append('yellow')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 578<=y<=626 and 'blue' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='blue'
                    who_turn+=1
                    gamedet['chosen colours'].append('blue')
                if(who_turn<=modchoose+1 and event.type==MOUSEBUTTONDOWN and event.button==1 and 175<=x<=305 and 632<=y<=680 and 'green' not in gamedet['chosen colours']):
                    GAME_SOUNDS['buttonclick'].play()
                    playerscol[who_turn-1]='green'
                    who_turn+=1
                    gamedet['chosen colours'].append('green')
            
            if(x<=1300):#elliptical curvature approximation
                yd=33*(1-((70-1300+x)/70) )
            else:
                yd=33*(1-((70-x+1300)/70) )
            if(1230<=x<=1370 and 270+yd/2.95 <=y<= 336-yd/2):#start button hover
                starthov=1
            else:
                starthov=0
        
        SCREEN.blit(bgimg,(0,0))
        SCREEN.blit(ldname,(355,-20))
        SCREEN.blit(myname,(625,20))
        SCREEN.blit(ldboard,(410,87))
        if counter==0:GAME_SOUNDS['clickbaitsound'].play()
        if modchoose==-1 and 0<=counter<=15:
            for i in range(0,283,13):
                SCREEN.blit(GAME_SPRITES['rotator'],(24+i,75))
                SCREEN.blit(GAME_SPRITES['rotator'],(24+i,13))

            SCREEN.blit(GAME_SPRITES['rotator'],(24,74))
            SCREEN.blit(GAME_SPRITES['rotator'],(24,61))
            SCREEN.blit(GAME_SPRITES['rotator'],(24,48))
            SCREEN.blit(GAME_SPRITES['rotator'],(24,35))
            SCREEN.blit(GAME_SPRITES['rotator'],(24,23))
            SCREEN.blit(GAME_SPRITES['rotator'],(24,13))

            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,74))
            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,61))
            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,48))
            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,35))
            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,23))
            SCREEN.blit(GAME_SPRITES['rotator'],(283+24,13))
        
        if modchoose!=-1 and who_turn<=1+modchoose and 0<=counter<=15:
            SCREEN.blit(GAME_SPRITES['rotator'],(26,518-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(26,531-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(26,544-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(26,557-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(26,570-8))

            for i in range(0,264,13):
                SCREEN.blit(GAME_SPRITES['rotator'],(26+i,572-8))
                SCREEN.blit(GAME_SPRITES['rotator'],(26+i,517-8))

            SCREEN.blit(GAME_SPRITES['rotator'],(264+26,518-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(264+26,531-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(264+26,544-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(264+26,557-8))
            SCREEN.blit(GAME_SPRITES['rotator'],(264+26,570-8))
        
        if modchoose!=-1 and who_turn>1+modchoose and 0<=counter<=15:
            elliptical=[
            (1308,338.8),(1299,338.8),(1290,338.8),(1281,338.5),(1272,338),(1263,336),(1254,333),(1245,330),
            (1236,325),(1228,317),(1223,309),(1221,301),(1221,292),(1227,283),(1235,275),(1244,269),(1253,266),
            (1262,264),(1271,262),(1280,261),(1289,260),(1298,260),(1307,260),(1316,261),(1317,337.5),
            (1325,262.5),(1334,264),(1343,266),(1352,270),(1360,274),(1367,281),(1371,288),(1373,296),
            (1372,305),(1370,314),(1363,322),(1355,328),(1347,332),(1339,334.5),(1332,335.5),(1325,336.5)
            ]
            for i in range(len(elliptical)):
                SCREEN.blit(GAME_SPRITES['rotator'],elliptical[i])

        SCREEN.blit(modpick,(30,20))
        mods=GAME_SPRITES['gamemod']
        # modesel=0
        SCREEN.blit(mods[0][modhov[0]],(30,77+10))
        SCREEN.blit(mods[1][modhov[1]],(30,136+10))
        SCREEN.blit(mods[2][modhov[2]],(30,195+10))
        SCREEN.blit(mods[3][modhov[3]],(30,254+10))

        SCREEN.blit(colpick,(25,510-8))
        # r_op,y_op,b_op,g_op=0,0,0,0
        SCREEN.blit(redopt[colhov[0]],(35,578))
        SCREEN.blit(yellowopt[colhov[1]],(35,632))
        SCREEN.blit(blueopt[colhov[2]],(175,578))
        SCREEN.blit(greenopt[colhov[3]],(175,632))

        SCREEN.blit(turn,(65,355))
        if(who_turn<=modchoose+1):
            SCREEN.blit(whosturn[who_turn],(30,422))
        
        SCREEN.blit(dice,(1205,50))
        SCREEN.blit(pygame.transform.rotate(diceroller,90),(1150,135))
        
        SCREEN.blit(start_button[starthov],(1230,270))
        if(GAMESTART==1):
            SCREEN.blit(start_button[1],(1230,270))
        
        SCREEN.blit(roll[2],(1160,375))
        if(GAMESTART==0):
            SCREEN.blit(activate[2],(1310,375))
            SCREEN.blit(movpawns[0][2],(1160,445))
            SCREEN.blit(movpawns[1][2],(1310,445))
            SCREEN.blit(movpawns[2][2],(1160,515))
            SCREEN.blit(movpawns[3][2],(1310,515))

        if(playerscol[0]=='red' or playerscol[1]=='red' or playerscol[2]=='red' or playerscol[3]=='red'):
            SCREEN.blit(reds[0],RED_HOME[0])
            SCREEN.blit(reds[1],RED_HOME[1])
            SCREEN.blit(reds[2],RED_HOME[2])
            SCREEN.blit(reds[3],RED_HOME[3])
        if(playerscol[0]=='yellow' or playerscol[1]=='yellow' or playerscol[2]=='yellow' or playerscol[3]=='yellow'):
            SCREEN.blit(yellows[0],YELLOW_HOME[0])
            SCREEN.blit(yellows[1],YELLOW_HOME[1])
            SCREEN.blit(yellows[2],YELLOW_HOME[2])
            SCREEN.blit(yellows[3],YELLOW_HOME[3])
        if(playerscol[0]=='blue' or playerscol[1]=='blue' or playerscol[2]=='blue' or playerscol[3]=='blue'):
            SCREEN.blit(blues[0],BLUE_HOME[0])
            SCREEN.blit(blues[1],BLUE_HOME[1])
            SCREEN.blit(blues[2],BLUE_HOME[2])
            SCREEN.blit(blues[3],BLUE_HOME[3])
        if(playerscol[0]=='green' or playerscol[1]=='green' or playerscol[2]=='green' or playerscol[3]=='green'):
            SCREEN.blit(greens[0],GREEN_HOME[0])
            SCREEN.blit(greens[1],GREEN_HOME[1])
            SCREEN.blit(greens[2],GREEN_HOME[2])
            SCREEN.blit(greens[3],GREEN_HOME[3])

        if(compcol=='red'):
            SCREEN.blit(reds[0],RED_HOME[0])
            SCREEN.blit(reds[1],RED_HOME[1])
            SCREEN.blit(reds[2],RED_HOME[2])
            SCREEN.blit(reds[3],RED_HOME[3])
        elif(compcol=='yellow'):
            SCREEN.blit(yellows[0],YELLOW_HOME[0])
            SCREEN.blit(yellows[1],YELLOW_HOME[1])
            SCREEN.blit(yellows[2],YELLOW_HOME[2])
            SCREEN.blit(yellows[3],YELLOW_HOME[3])
        elif(compcol=='blue'):
            SCREEN.blit(blues[0],BLUE_HOME[0])
            SCREEN.blit(blues[1],BLUE_HOME[1])
            SCREEN.blit(blues[2],BLUE_HOME[2])
            SCREEN.blit(blues[3],BLUE_HOME[3])
        elif(compcol=='green'):
            SCREEN.blit(greens[0],GREEN_HOME[0])
            SCREEN.blit(greens[1],GREEN_HOME[1])
            SCREEN.blit(greens[2],GREEN_HOME[2])
            SCREEN.blit(greens[3],GREEN_HOME[3])
        
        SCREEN.blit(pygame.transform.scale(GAME_SPRITES['ludonote'],(280,170.5)),(1155,591))
        if counter>=30:counter=-1
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def gamestart(gamedet):
    # all variable names are self-explanatory
    WHENEVER_CLICKED=0
    allBoxPositions=(
        (434,370),(477,370),(520,370),(563,370),(606,370),(649,370),
        (692,327-1),(692,284-1),(692,241-1),(692,198-1),(692,155-1),(692,112-1),
        (735+1,112-1),
        (778+1,112-1),(778+1,155-1),(778+1,198-1),(778+1,241-1),(778+1,284-1),(778+1,327-1),
        (821+2,370-1),(864+2,370-1),(907+2,370-1),(950+2,370-1),(993+2,370-1),(1036+2,370-1),
        (1036+2,413),
        (1036+2,456),(993+2,456),(950+2,456),(907+2,456),(864+2,456),(821+2,456),
        (778+1+1,499+1),(778+1+1,542+1),(778+1+1,585+1),(778+1+1,628+1),(778+1+1,671+1),(778+1+1,714+1),
        (735+1,714+1),
        (692+1,714+1),(692+1,671+1),(692+1,628+1),(692+1,585+1),(692+1,542+1),(692+1,499+1),
        (649,456),(606,456),(563,456),(520,456),(477,456),(434,456),
        (434,413)
    ) # 692,283 matches with normalboxpos4 8's 1st position !!
    # (736,111) almost matches with (735,110) <-- normalboxpos4 13's 1st position
    normalboxpos4={
        1: ((433,369),(433+21,369),(433,369+20),(433+21,369+20)),
        3: ((519,369),(519+21,369),(519,369+20),(519+21,369+20)),
        4: ((562,369),(562+21,369),(562,369+20),(562+21,369+20)),
        5: ((605,369),(605+21,369),(605,369+20),(605+21,369+20)),
        6: ((648,369),(648+21,369),(648,369+20),(648+21,369+20)),
        7: ((692,326),(692+21,326),(692,326+20),(692+21,326+20)),
        8: ((692,283),(692+21,283),(692,283+20),(692+21,283+20)),
        9: ((692,240),(692+21,240),(692,240+20),(692+21,240+20)),
        11: ((691+1,-1+154),(691+1+21,-1+154),(691+1,-1+154+20),(691+1+21,-1+154+20)),
        12: ((691+1,-1+111),(691+1+21,-1+111),(691+1,-1+111+20),(691+1+21,-1+111+20)),
        13: ((734+1,-1+111),(734+1+21,-1+111),(734+1,-1+111+20),(734+1+21,-1+111+20)),
        14: ((777+1,-1+111),(777+1+21,-1+111),(777+1,-1+111+20),(777+1+21,-1+111+20)),
        16: ((777+1,-1+197),(777+1+21,-1+197),(777+1,-1+197+20),(777+1+21,-1+197+20)),
        17: ((777+1,-1+240),(777+1+21,-1+240),(777+1,-1+240+20),(777+1+21,-1+240+20)),
        18: ((777+1,-1+283),(777+1+21,-1+283),(777+1,-1+283+20),(777+1+21,-1+283+20)),
        19: ((777+1,-1+326),(777+1+21,-1+326),(777+1,-1+326+20),(777+1+21,-1+326+20)),
        20: ((2+820,369),(2+820+21,369),(2+820,369+20),(2+820+21,369+20)),
        21: ((2+863,369),(2+863+21,369),(2+863,369+20),(2+863+21,369+20)),
        22: ((2+906,369),(2+906+21,369),(2+906,369+20),(2+906+21,369+20)),
        24: ((2+992,369),(2+992+21,369),(2+992,369+20),(2+992+21,369+20)),
        25: ((2+1035,369),(2+1035+21,369),(2+1035,369+20),(2+1035+21,369+20)),
        26: ((2+1035,412),(2+1035+21,412),(2+1035,412+20),(2+1035+21,412+20)),
        27: ((2+1035,455),(2+1035+21,455),(2+1035,455+20),(2+1035+21,455+20)),
        29: ((2+949,455),(2+949+21,455),(2+949,455+20),(2+949+21,455+20)),
        30: ((2+906,455),(2+906+21,455),(2+906,455+20),(2+906+21,455+20)),
        31: ((2+863,455),(2+863+21,455),(2+863,455+20),(2+863+21,455+20)),
        32: ((2+820,455),(2+820+21,455),(2+820,455+20),(2+820+21,455+20)),
        33: ((1+777,498+1),(1+777+21,498+1),(1+777,498+20+1),(1+777+21,498+20+1)),
        34: ((1+777,541+1),(1+777+21,541+1),(1+777,541+20+1),(1+777+21,541+20+1)),
        35: ((1+777,584+1),(1+777+21,584+1),(1+777,584+20+1),(1+777+21,584+20+1)),
        37: ((1+777,670+1),(1+777+21,670+1),(1+777,670+20+1),(1+777+21,670+20+1)),
        38: ((1+777,713+1),(1+777+21,713+1),(1+777,713+20+1),(1+777+21,713+20+1)),
        39: ((1+734,713+1),(1+734+21,713+1),(1+734,713+20+1),(1+734+21,713+20+1)),
        40: ((1+691,713+1),(1+691+21,713+1),(1+691,713+20+1),(1+691+21,713+20+1)),
        42: ((691,627+1),(691+21,627+1),(691,627+20+1),(691+21,627+20+1)),
        43: ((691,584+1),(691+21,584+1),(691,584+20+1),(691+21,584+20+1)),
        44: ((691,541+1),(691+21,541+1),(691,541+20+1),(691+21,541+20+1)),
        45: ((691,498+1),(691+21,498+1),(691,498+20+1),(691+21,498+20+1)),
        46: ((648,455),(648+21,455),(648,455+20),(648+21,455+20)),
        47: ((605,455),(605+21,455),(605,455+20),(605+21,455+20)),
        48: ((562,455),(562+21,455),(562,455+20),(562+21,455+20)),
        50: ((476,455),(476+21,455),(476,455+20),(476+21,455+20)),
        51: ((433,455),(433+21,455),(433,455+20),(433+21,455+20)),
        52: ((433,412),(433+21,412),(433,412+20),(433+21,412+20))
    }
    homecoming={
        'red': ((736,154),(736,197),(736,240),(736,283),(736,326),(736,369)),
        'yellow': ((736,672),(736,629),(736,586),(736,543),(736,500),(736,457)),
        'blue': ((995,413),(952,413),(909,413),(866,413),(823,413),(780,413)),
        'green': ((477,413),(520,413),(563,413),(606,413),(649,413),(692,413))
    }
    homecomingpos4={
        'red': (
        ((735,153),(735+21,153),(735,153+20),(735+21,153+20)),
        ((735,153+43),(735+21,153+43),(735,153+43+20),(735+21,153+43+20)),
        ((735,153+43+43),(735+21,153+43+43),(735,153+43+43+20),(735+21,153+43+43+20)),
        ((735,153+43+43+43),(735+21,153+43+43+43),(735,153+43+43+43+20),(735+21,153+43+43+43+20)),
        ((735,153+43+43+43+43),(735+21,153+43+43+43+43),(735,153+43+43+43+43+20),(735+21,153+43+43+43+43+20)),
        ((736,369),(736,369),(736,369),(736,369))
        ),
        'yellow': (
        ((735,671),(735+21,671),(735,671+20),(735+21,671+20)),
        ((735,671-43),(735+21,671-43),(735,671+20-43),(735+21,671+20-43)),
        ((735,671-43-43),(735+21,671-43-43),(735,671+20-43-43),(735+21,671+20-43-43)),
        ((735,671-43-43-43),(735+21,671-43-43-43),(735,671+20-43-43-43),(735+21,671+20-43-43-43)),
        ((735,671-43-43-43-43),(735+21,671-43-43-43-43),(735,671+20-43-43-43-43),(735+21,671+20-43-43-43-43)),
        ((736,457),(736,457),(736,457),(736,457))
        ),
        'blue': (
        ((994,412),(994+20,412),(994,412+21),(994+20,412+21)),
        ((994-43,412),(994-43+20,412),(994-43,412+21),(994-43+20,412+21)),
        ((994-43-43,412),(994-43-43+20,412),(994-43-43,412+21),(994-43-43+20,412+21)),
        ((994-43-43-43,412),(994-43-43-43+20,412),(994-43-43-43,412+21),(994-43-43-43+20,412+21)),
        ((994-43-43-43-43,412),(994-43-43-43-43+20,412),(994-43-43-43-43,412+21),(994-43-43-43-43+20,412+21)),
        ((780,413),(780,413),(780,413),(780,413))
        ),
        'green': (
        ((476,412),(476+21,412),(476,412+20),(476+21,412+20)),
        ((476+43,412),(476+43+21,412),(476+43,412+20),(476+43+21,412+20)),
        ((476+43+43,412),(476+43+43+21,412),(476+43+43,412+20),(476+43+43+21,412+20)),
        ((476+43+43+43,412),(476+43+43+43+21,412),(476+43+43+43,412+20),(476+43+43+43+21,412+20)),
        ((476+43+43+43+44,412),(476+43+43+43+44+21,412),(476+43+43+43+44,412+20),(476+43+43+43+44+21,412+20)),
        ((692,413),(692,413),(692,413),(692,413))
        )
    }
    startbox={
        'red': 15,
        'yellow': 41,
        'blue': 28,
        'green': 2
    }
    startboxes=(2,15,28,41)
    endboxes=(13,26,39,52)
    endbox={
        'red': 13,
        'yellow': 39,
        'blue': 26,
        'green': 52
    }
    safestarboxes=(2,10,15,23,28,36,41,49)
    SSboxpos4={
        2: ((476,369),(497,369),(476,389),(497,389)),
        10: ((692,196),(692+21,196),(692,196+20),(692+21,196+20)),
        15: ((778,153),(778+21,153),(778,153+20),(778+21,153+20)),
        23: ((951,369),(951+21,369),(951,369+20),(951+21,369+20)),
        28: ((994,455),(994+21,455),(994,455+20),(994+21,455+20)),
        36: ((779,629),(779+21,629),(779,629+20),(779+21,629+20)),
        41: ((692,671),(692+21,671),(692,671+20),(692+21,671+20)),
        49: ((519,455),(519+21,455),(519,455+20),(519+21,455+20))
    }

    bgimg=GAME_SPRITES['background']
    ldname=GAME_SPRITES['ludoname']
    myname=GAME_SPRITES['myname']
    ldboard=GAME_SPRITES['gameboard']

    colpick=GAME_SPRITES['colpick']
    modpick=GAME_SPRITES['modpick']

    redopt=GAME_SPRITES['red_opt']
    yellowopt=GAME_SPRITES['yellow_opt']
    blueopt=GAME_SPRITES['blue_opt']
    greenopt=GAME_SPRITES['green_opt']

    turn=GAME_SPRITES['gameturn']
    whosturn=GAME_SPRITES['whosturn']

    diceroller=GAME_SPRITES['dice_roller']
    dice=GAME_SPRITES['dicelabel']
    dices=GAME_SPRITES['dice']

    diceroll=0

    diceposx=DICEPOS[0][0]
    diceposy=DICEPOS[0][1]

    reds=GAME_SPRITES['redpawn']
    yellows=GAME_SPRITES['yellowpawn']
    blues=GAME_SPRITES['bluepawn']
    greens=GAME_SPRITES['greenpawn']

    start_button=GAME_SPRITES['start']

    roll=GAME_SPRITES['roll']
    activate=GAME_SPRITES['activate']
    movpawns=GAME_SPRITES['movepawns']
    
    playerspos=[[[],[],[],[]]]
    playerspawns=[[0,0,0,0]]
    playersboxtrack=[[0,0,0,0]]

    playerPawnSizes=[[38,38,38,38]]

    someoneCameHome=0
    someoneGotKilled=[]
    killerstop=0
    if gamedet['game mode']!=0:
        for i in range(gamedet['game mode']):
            playerspos.append([[],[],[],[]])
            playerspawns.append([0,0,0,0])
            playersboxtrack.append([0,0,0,0])
            playerPawnSizes.append([38,38,38,38])

    if(gamedet['game mode']==0):
        playerspos.append([[],[],[],[]])
        playerspawns.append([0,0,0,0])
        playersboxtrack.append([0,0,0,0])
        playerPawnSizes.append([38,38,38,38])

    if(gamedet['game mode']==0):
        if(gamedet['chosen colours'][0]=='red'):
            for i in range(4):
                playerspos[0][i].append(RED_HOME[i][0])
                playerspos[0][i].append(RED_HOME[i][1])
                playerspos[1][i].append(YELLOW_HOME[i][0])
                playerspos[1][i].append(YELLOW_HOME[i][1])
        elif(gamedet['chosen colours'][0]=='yellow'):
            for i in range(4):
                playerspos[1][i].append(RED_HOME[i][0])
                playerspos[1][i].append(RED_HOME[i][1])
                playerspos[0][i].append(YELLOW_HOME[i][0])
                playerspos[0][i].append(YELLOW_HOME[i][1])
        elif(gamedet['chosen colours'][0]=='blue'):
            for i in range(4):
                playerspos[0][i].append(BLUE_HOME[i][0])
                playerspos[0][i].append(BLUE_HOME[i][1])
                playerspos[1][i].append(GREEN_HOME[i][0])
                playerspos[1][i].append(GREEN_HOME[i][1])
        elif(gamedet['chosen colours'][0]=='green'):
            for i in range(4):
                playerspos[1][i].append(BLUE_HOME[i][0])
                playerspos[1][i].append(BLUE_HOME[i][1])
                playerspos[0][i].append(GREEN_HOME[i][0])
                playerspos[0][i].append(GREEN_HOME[i][1])
    else:
        for i in range(len(gamedet['chosen colours'])):
            if(gamedet['chosen colours'][i]=='red'):
                for j in range(4):
                    playerspos[i][j].append(RED_HOME[j][0])
                    playerspos[i][j].append(RED_HOME[j][1])
            elif(gamedet['chosen colours'][i]=='yellow'):
                for j in range(4):
                    playerspos[i][j].append(YELLOW_HOME[j][0])
                    playerspos[i][j].append(YELLOW_HOME[j][1])
            if(gamedet['chosen colours'][i]=='blue'):
                for j in range(4):
                    playerspos[i][j].append(BLUE_HOME[j][0])
                    playerspos[i][j].append(BLUE_HOME[j][1])
            if(gamedet['chosen colours'][i]=='green'):
                for j in range(4):
                    playerspos[i][j].append(GREEN_HOME[j][0])
                    playerspos[i][j].append(GREEN_HOME[j][1])

    if gamedet['game mode']==0:
        who_turn=1
    else:
        who_turn=0
    t=-1
    playerpresentbox=[]
    pawnactivated=[-1,-1,-1,-1]
    moveapawn=-10 # represents index of the pawn to move, of who_turn
    nothingHappened=0
    moveOrActivate=0
    computerRolls=0
    inHomeTrack=[
        [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    ]
    playerInHome=[
        [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    ]
    pawnsInSSBox={
        2: [0,0,0,0], 10: [0,0,0,0], 15: [0,0,0,0], 23: [0,0,0,0], 28: [0,0,0,0], 36: [0,0,0,0], 41: [0,0,0,0], 49: [0,0,0,0]
    }
    pawnsInNormalBox={
        1: [0,0,0,0], 3: [0,0,0,0], 4: [0,0,0,0], 5: [0,0,0,0], 6: [0,0,0,0], 7: [0,0,0,0], 8: [0,0,0,0], 9: [0,0,0,0],
        11: [0,0,0,0], 12: [0,0,0,0], 13: [0,0,0,0], 14: [0,0,0,0], 16: [0,0,0,0], 17: [0,0,0,0], 18: [0,0,0,0], 19: [0,0,0,0],
        20: [0,0,0,0], 21: [0,0,0,0], 22: [0,0,0,0], 24: [0,0,0,0], 25: [0,0,0,0], 26: [0,0,0,0], 27: [0,0,0,0], 29: [0,0,0,0],
        30: [0,0,0,0], 31: [0,0,0,0], 32: [0,0,0,0], 33: [0,0,0,0], 34: [0,0,0,0], 35: [0,0,0,0], 37: [0,0,0,0], 38: [0,0,0,0],
        39: [0,0,0,0], 40: [0,0,0,0], 42: [0,0,0,0], 43: [0,0,0,0], 44: [0,0,0,0], 45: [0,0,0,0], 46: [0,0,0,0], 47: [0,0,0,0],
        48: [0,0,0,0], 50: [0,0,0,0], 51: [0,0,0,0], 52: [0,0,0,0]
    }
    pawnsInHomeTrack={
        'red': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        'yellow': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        'blue': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        'green': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    }
    turnForKill=0
    noOfSixes=0
    someoneGonnaDie=0

    whoFirst=[] # when pawn is activated and its starting box is already populated
    valDic=[]
    placeInSSBox,placeInNormalBox=-10,-10
    destinationInSSBox=-10
    destinationInNormalBox=-10
    destinationInHomeTrack=-10
    placeToClearInSSBox,placeToClearInNormalBox=-10,-10
    postDepCheckInSSBox,postDepCheckInNormalBox=1,1
    postDepCheckInHomeTrack=1

    allstartpos={
        'red': RED_STARTPOS,
        'yellow': YELLOW_STARTPOS,
        'blue': BLUE_STARTPOS,
        'green': GREEN_STARTPOS
    }
    allhomepos={
        'red': RED_HOME,
        'yellow': YELLOW_HOME,
        'blue': BLUE_HOME,
        'green': GREEN_HOME,
    }
    winner=-1
    CHECKIFCORRECT=0
    while True:
        SCREEN.blit(bgimg,(0,0))
        SCREEN.blit(ldname,(355,-20))
        SCREEN.blit(myname,(625,20))
        SCREEN.blit(ldboard,(410,87))
        SCREEN.blit(pygame.transform.scale(GAME_SPRITES['ludonote'],(280,170.5)),(1155,591))

        SCREEN.blit(modpick,(30,20))
        mods=GAME_SPRITES['gamemod']
        SCREEN.blit(mods[0][0],(30,77+10))
        SCREEN.blit(mods[1][0],(30,136+10))
        SCREEN.blit(mods[2][0],(30,195+10))
        SCREEN.blit(mods[3][0],(30,254+10))
        
        if gamedet['game mode']==0:
            SCREEN.blit(mods[0][1],(30,77+10))
        elif gamedet['game mode']==1:
            SCREEN.blit(mods[1][1],(30,136+10))
        elif gamedet['game mode']==2:
            SCREEN.blit(mods[2][1],(30,195+10))
        elif gamedet['game mode']==3:
            SCREEN.blit(mods[3][1],(30,254+10))

        SCREEN.blit(colpick,(25,510-8))
        if 'red' in gamedet['chosen colours']:
            SCREEN.blit(redopt[1],(35,578))
        else:
            SCREEN.blit(redopt[2],(35,578))
        if 'yellow' in gamedet['chosen colours']:
            SCREEN.blit(yellowopt[1],(35,632))
        else:
            SCREEN.blit(yellowopt[2],(35,632))
        if 'blue' in gamedet['chosen colours']:
            SCREEN.blit(blueopt[1],(175,578))
        else:
            SCREEN.blit(blueopt[2],(175,578))
        if 'green' in gamedet['chosen colours']:
            SCREEN.blit(greenopt[1],(175,632))
        else:
            SCREEN.blit(greenopt[2],(175,632))

        SCREEN.blit(turn,(65,355))
        if gamedet['game mode']==0:
            SCREEN.blit(whosturn[who_turn],(30,422))
            if who_turn==1:SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][who_turn]],(240,424))
            else: SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][who_turn]],(281,424))
        elif gamedet['game mode']!=0:
            SCREEN.blit(whosturn[1+who_turn],(30,422))
            if who_turn==0:SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][who_turn]],(240,424))
            else: SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][who_turn]],(245,424))

        if gamedet['game mode']==0 and who_turn==0: # in computer's turn, all buttons are shown disabled
            SCREEN.blit(roll[2],(1160,375))
            SCREEN.blit(activate[2],(1310,375))
            SCREEN.blit(movpawns[0][2],(1160,445))
            SCREEN.blit(movpawns[1][2],(1310,445))
            SCREEN.blit(movpawns[2][2],(1160,515))
            SCREEN.blit(movpawns[3][2],(1310,515))
        else:
            if diceroll==0:
                SCREEN.blit(roll[0],(1160,375))
            else:
                SCREEN.blit(roll[1],(1160,375))

            if diceroll==1 and t==5 and diceposx>=DICEPOS[1][0] and playerspawns[who_turn]!=[1,1,1,1]:
                SCREEN.blit(activate[0],(1310,375))
                if moveOrActivate==1 and pawnactivated[who_turn]!=-1:
                    SCREEN.blit(activate[1],(1310,375))
                if moveOrActivate==2:
                    SCREEN.blit(activate[2],(1310,375))
            else:
                SCREEN.blit(activate[2],(1310,375))
            
            SCREEN.blit(movpawns[0][2],(1160,445))
            SCREEN.blit(movpawns[1][2],(1310,445))
            SCREEN.blit(movpawns[2][2],(1160,515))
            SCREEN.blit(movpawns[3][2],(1310,515))

            if(playerspawns[who_turn][0]==1 and diceposx>=DICEPOS[1][0] and diceroll==1):
                if inHomeTrack[who_turn][0]==0 or inHomeTrack[who_turn][0]+t<=5:
                    if moveOrActivate==0:
                        SCREEN.blit(movpawns[0][0],(1160,445))
                    elif moveOrActivate==2 and moveapawn!=0:
                        SCREEN.blit(movpawns[0][2],(1160,445))
                    elif moveOrActivate==2 and moveapawn==0:
                        SCREEN.blit(movpawns[0][1],(1160,445))
            if(playerspawns[who_turn][1]==1 and diceposx>=DICEPOS[1][0] and diceroll==1):
                if inHomeTrack[who_turn][1]==0 or inHomeTrack[who_turn][1]+t<=5:    
                    if moveOrActivate==0:
                        SCREEN.blit(movpawns[1][0],(1310,445))
                    elif moveOrActivate==2 and moveapawn!=1:
                        SCREEN.blit(movpawns[1][2],(1310,445))
                    elif moveOrActivate==2 and moveapawn==1:
                        SCREEN.blit(movpawns[1][1],(1310,445))
            if(playerspawns[who_turn][2]==1 and diceposx>=DICEPOS[1][0] and diceroll==1):
                if inHomeTrack[who_turn][2]==0 or inHomeTrack[who_turn][2]+t<=5:    
                    if moveOrActivate==0:
                        SCREEN.blit(movpawns[2][0],(1160,515))
                    elif moveOrActivate==2 and moveapawn!=2:
                        SCREEN.blit(movpawns[2][2],(1160,515))
                    elif moveOrActivate==2 and moveapawn==2:
                        SCREEN.blit(movpawns[2][1],(1160,515))
            if(playerspawns[who_turn][3]==1 and diceposx>=DICEPOS[1][0] and diceroll==1):
                if inHomeTrack[who_turn][3]==0 or inHomeTrack[who_turn][3]+t<=5:    
                    if moveOrActivate==0:
                        SCREEN.blit(movpawns[3][0],(1310,515))
                    elif moveOrActivate==2 and moveapawn!=3:
                        SCREEN.blit(movpawns[3][2],(1310,515))
                    elif moveOrActivate==2 and moveapawn==3:
                        SCREEN.blit(movpawns[3][1],(1310,515))

        SCREEN.blit(dice,(1205,50))
        SCREEN.blit(start_button[1],(1230,270))

        if gamedet['game mode']==0 and who_turn==0 and diceroll==0:
            valDic.clear()
            for i in range(6):
                ch=1
                for j in range(4):
                    if playerspawns[who_turn][j]==1 and inHomeTrack[who_turn][j]==0 and (playersboxtrack[who_turn][j]>endbox[gamedet['chosen colours'][who_turn]] or (playersboxtrack[who_turn][j]+1+i)<=endbox[gamedet['chosen colours'][who_turn]]) and (playersboxtrack[who_turn][j]+1+i)%52 in startboxes:
                        noOf1=0
                        for k in range(4):
                            if pawnsInSSBox[(playersboxtrack[who_turn][j]+1+i)%52][k]==1:noOf1+=1
                        if noOf1>2:ch=0
                        
                    if playerspawns[who_turn][j]==1 and inHomeTrack[who_turn][j]==0 and (playersboxtrack[who_turn][j]>endbox[gamedet['chosen colours'][who_turn]] or (playersboxtrack[who_turn][j]+1+i)<=endbox[gamedet['chosen colours'][who_turn]]) and (playersboxtrack[who_turn][j]+1+i)%52 in safestarboxes:
                        noOf1=0
                        for k in range(4):
                            if pawnsInSSBox[(playersboxtrack[who_turn][j]+1+i)%52][k]==1:noOf1+=1
                        if noOf1>3:ch=0
                if ch==1:
                    valDic.append(i)
                
            t=valDic[random.randint(0,len(valDic)-1)]
            if 5 in valDic and noOfSixes==2:
                if len(valDic)>1:
                    t=valDic[random.randint(0,len(valDic)-2)]
                noOfSixes=0    
            if t==5:
                noOfSixes+=1
            diceroll=1
            playerpresentbox.clear()
            for i in range(len(playersboxtrack[0])):
                playerpresentbox.append(playersboxtrack[0][i])
        
        if gamedet['game mode']==0 and who_turn==0 and diceroll==1 and t==5 and computerRolls>=90 and moveOrActivate==0 and diceposx>=DICEPOS[1][0]:
            ch=0
            for i in range(4):
                # if computer can send pawn home
                if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playersboxtrack[0][i]==endbox[gamedet['chosen colours'][who_turn]]:
                    ch=1
                    moveOrActivate=2
                    playerpresentbox[i]+=1+t
                    if playerpresentbox[i]>52:
                        playerpresentbox[i]-=52
                    inHomeTrack[0][i]+=1+t
                    moveapawn=i
                    break

            if ch==0:
                for i in range(4):
                    if ch==1:break
                    # if computer can get a kill
                    for j in range(4):
                        if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and ((playerpresentbox[i]<endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[i]+1+t<=endbox[gamedet['chosen colours'][who_turn]]) or playerpresentbox[i]>endbox[gamedet['chosen colours'][who_turn]]) and ((playerpresentbox[i]+1+t)%52)==playersboxtrack[1][j]:
                            ch=1
                            moveOrActivate=2
                            playerpresentbox[i]+=1+t
                            if playerpresentbox[i]>52:
                                playerpresentbox[i]-=52
                            moveapawn=i
                            break

            if ch==0:
                # if computer can activate
                for j in range(4):
                    if playerspawns[0][j]==0:
                        moveOrActivate=1
                        ch=1
                        pawnactivated[who_turn]=j
                        playerspawns[0][j]=1
                        break
            
            if ch==0:
                for i in range(4):
                    # if computer can send a pawn into hometrack
                    if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playersboxtrack[0][i]<=endbox[gamedet['chosen colours'][who_turn]] and playersboxtrack[0][i]+1+t>endbox[gamedet['chosen colours'][who_turn]]:
                        ch=1
                        moveOrActivate=2
                        playerpresentbox[i]+=1+t
                        inHomeTrack[0][i]=playerpresentbox[i]-endbox[gamedet['chosen colours'][who_turn]]
                        if playerpresentbox[i]>52:
                            playerpresentbox[i]-=52
                        moveapawn=i
                        break
            
            if ch==0:
                # if computer can move some pawn out of danger
                minsafedis=[]
                for i in range(4):
                    for j in range(4):
                        if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] not in safestarboxes and playerpresentbox[i]>playersboxtrack[1][j] and 0<(playerpresentbox[i]-playersboxtrack[1][j])<=6:
                            minsafedis.append([playerpresentbox[i]-playersboxtrack[1][j],i])
                        elif playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] not in safestarboxes and 0<(52-playersboxtrack[1][j]+playerpresentbox[i])<=6:
                            minsafedis.append([52-playersboxtrack[1][j]+playerpresentbox[i],i])

                if len(minsafedis)>0:
                    def sortcond(a,b):
                        if a[0]!=b[0]:return a[0]-b[0]
                        else: return a[1]-b[1]
                    
                    minsafedis.sort(key=cmp_to_key(sortcond))
                    
                    ch=1
                    playerpresentbox[minsafedis[0][1]]+=1+t
                    if playerpresentbox[minsafedis[0][1]]>52:
                        playerpresentbox[minsafedis[0][1]]-=52
                    moveOrActivate=2
                    moveapawn=minsafedis[0][1]

            if ch==0:
                # if computer can atleast move some pawn
                for i in range(4):
                    if playerspawns[0][i]==1 and inHomeTrack[0][i]+t<=5:
                        ch=1
                        moveOrActivate=2
                        if playerpresentbox[i]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[i]+1+t>endbox[gamedet['chosen colours'][who_turn]]:
                            inHomeTrack[0][i]=(playerpresentbox[i]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                        elif inHomeTrack[0][i]>0:
                            inHomeTrack[0][i]+=1+t
                        playerpresentbox[i]+=1+t
                        if playerpresentbox[i]>52:
                            playerpresentbox[i]-=52
                        moveapawn=i
                        break
                    if ch==1:break
        elif gamedet['game mode']==0 and who_turn==0 and diceroll==1 and t!=-1 and t!=5 and playerspawns[0]!=[0,0,0,0] and computerRolls>=90 and moveOrActivate==0 and diceposx>=DICEPOS[1][0]:
            ch=0
            for i in range(4):
                # if computer can send pawn home
                if playerspawns[0][i]==1 and 0<inHomeTrack[0][i]<6 and inHomeTrack[0][i]+t==5:
                    ch=1
                    moveOrActivate=2
                    playerpresentbox[i]+=1+t
                    if playerpresentbox[i]>52:
                        playerpresentbox[i]-=52
                    inHomeTrack[0][i]+=1+t
                    moveapawn=i
                    break

            if ch==0:
                for i in range(4):
                    if ch==1:break
                    # if computer can get a kill
                    for j in range(4):
                        if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and ((playerpresentbox[i]<endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[i]+1+t<=endbox[gamedet['chosen colours'][who_turn]]) or playerpresentbox[i]>endbox[gamedet['chosen colours'][who_turn]]) and ((playerpresentbox[i]+1+t)%52)==playersboxtrack[1][j]:
                            ch=1
                            moveOrActivate=2
                            playerpresentbox[i]+=1+t
                            if playerpresentbox[i]>52:
                                playerpresentbox[i]-=52
                            moveapawn=i
                            break

            if ch==0:
                for i in range(4):
                    # if computer can send a pawn into hometrack
                    if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playersboxtrack[0][i]<=endbox[gamedet['chosen colours'][who_turn]] and playersboxtrack[0][i]+1+t>endbox[gamedet['chosen colours'][who_turn]]:
                        ch=1
                        moveOrActivate=2
                        playerpresentbox[i]+=1+t
                        inHomeTrack[0][i]=playerpresentbox[i]-endbox[gamedet['chosen colours'][who_turn]]
                        if playerpresentbox[i]>52:
                            playerpresentbox[i]-=52
                        moveapawn=i
                        break
            
            if ch==0:
                # if computer can move some pawn out of danger
                minsafedis=[]
                for i in range(4):
                    for j in range(4):
                        if playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] not in safestarboxes and playerpresentbox[i]>playersboxtrack[1][j] and 0<(playerpresentbox[i]-playersboxtrack[1][j])<=6:
                            minsafedis.append([playerpresentbox[i]-playersboxtrack[1][j],i])
                        elif playerspawns[0][i]==1 and inHomeTrack[0][i]==0 and playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] not in safestarboxes and 0<(52-playersboxtrack[1][j]+playerpresentbox[i])<=6:
                            minsafedis.append([52-playersboxtrack[1][j]+playerpresentbox[i],i])

                if len(minsafedis)>0:
                    def sortcond(a,b):
                        if a[0]!=b[0]:return a[0]-b[0]
                        else: return a[1]-b[1]
                    
                    minsafedis.sort(key=cmp_to_key(sortcond))
                    
                    ch=1
                    playerpresentbox[minsafedis[0][1]]+=1+t
                    if playerpresentbox[minsafedis[0][1]]>52:
                        playerpresentbox[minsafedis[0][1]]-=52
                    moveOrActivate=2
                    moveapawn=minsafedis[0][1]

            if ch==0:
                # if computer can move a pawn such that it doesn't get into danger
                for i in range(4):
                    if playerspawns[0][i]==1 and inHomeTrack[0][i]+t<=5:
                        if inHomeTrack[0][i]>0:
                            inHomeTrack[0][i]=(playerpresentbox[i]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                            playerpresentbox[i]+=1+t
                            if playerpresentbox[i]>52:
                                playerpresentbox[i]-=52
                            ch=1
                            moveapawn=i
                        elif (playerpresentbox[i]+1+t)%52 in safestarboxes:
                            playerpresentbox[i]=(playerpresentbox[i]+1+t)%52
                            # possibility of it entering hometrack has already been considered above
                            ch=1
                            moveapawn=i
                        elif playerpresentbox[i]+1+t<=52:
                            testit=1
                            for j in range(4):
                                if playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i]<playersboxtrack[1][j]<playerpresentbox[i]+1+t:
                                    testit=0
                                    break
                                if playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] in safestarboxes and playersboxtrack[1][j]==playerpresentbox[i]:
                                    testit=0
                                    break
                            if testit==1:
                                playerpresentbox[i]+=1+t
                                moveapawn=i
                                ch=1
                        else:
                            testit=1
                            for j in range(4):
                                if playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and ((1<=playersboxtrack[1][j]<(playerpresentbox[i]+1+t)%52) or (playerpresentbox[i]<playersboxtrack[1][j]<=52) ):
                                    testit=0
                                    break
                                if playerspawns[1][j]==1 and inHomeTrack[1][j]==0 and playerpresentbox[i] in safestarboxes and playersboxtrack[1][j]==playerpresentbox[i]:
                                    testit=0
                                    break
                            if testit==1:
                                playerpresentbox[i]+=1+t
                                playerpresentbox[i]-=52
                                moveapawn=i
                                ch=1
                    if ch==1:
                        moveOrActivate=2
                        break

            if ch==0:
                # if computer can atleast move some pawn
                randlist=[0,1,2,3]
                random.shuffle(randlist)
                for i in randlist:
                    if playerspawns[0][i]==1 and inHomeTrack[0][i]+t<=5:
                        ch=1
                        moveOrActivate=2
                        if playerpresentbox[i]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[i]+1+t>endbox[gamedet['chosen colours'][who_turn]]:
                            inHomeTrack[0][i]=(playerpresentbox[i]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                        elif inHomeTrack[0][i]>0:
                            inHomeTrack[0][i]+=1+t
                        playerpresentbox[i]+=1+t
                        if playerpresentbox[i]>52:
                            playerpresentbox[i]-=52
                        moveapawn=i
                        break
                    if ch==1:break
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                GAME_SOUNDS['buttonclick'].play()
                pygame.quit()
                sys.exit()
            x,y=pygame.mouse.get_pos()
            clic=pygame.mouse.get_pressed()
            if(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and clic[0] and 1160<=x<=1290 and 375<=y<=422 and diceroll==0 and t==-1:
                GAME_SOUNDS['buttonclick'].play()
                diceroll=1
                valDic.clear()
                for i in range(6):
                    ch=1
                    for j in range(4):
                        '''
                        for regular safestar boxes that are NOT starting boxes, noOf1 can be allowed to be upto <=3,
                        but for starting boxes, noOf1 can be allowed to be only up till <=2, because I want to allow
                        the player of that colour to atleast activate 2 pawns if he does get a sixer, foreign occupancy
                        should not act as a hindrance there
                        '''
                        if playerspawns[who_turn][j]==1 and inHomeTrack[who_turn][j]==0 and (playersboxtrack[who_turn][j]>endbox[gamedet['chosen colours'][who_turn]] or (playersboxtrack[who_turn][j]+1+i)<=endbox[gamedet['chosen colours'][who_turn]]) and (playersboxtrack[who_turn][j]+1+i)%52 in startboxes:
                            noOf1=0
                            for k in range(4):
                                if pawnsInSSBox[(playersboxtrack[who_turn][j]+1+i)%52][k]==1:noOf1+=1
                            if noOf1>2:ch=0
                        
                        if playerspawns[who_turn][j]==1 and inHomeTrack[who_turn][j]==0 and (playersboxtrack[who_turn][j]>endbox[gamedet['chosen colours'][who_turn]] or (playersboxtrack[who_turn][j]+1+i)<=endbox[gamedet['chosen colours'][who_turn]]) and (playersboxtrack[who_turn][j]+1+i)%52 in safestarboxes:
                            noOf1=0
                            for k in range(4):
                                if pawnsInSSBox[(playersboxtrack[who_turn][j]+1+i)%52][k]==1:noOf1+=1
                            if noOf1>3:ch=0
                    
                    if ch==1:
                        valDic.append(i)
                
                t=valDic[random.randint(0,len(valDic)-1)]
                if 5 in valDic and noOfSixes>=2:
                    if len(valDic)>1:
                        t=valDic[random.randint(0,len(valDic)-2)]
                    noOfSixes=0
                
                if t==5:
                    noOfSixes+=1
                '''NEED TO CHECK'''
                # playersboxtrack=[[0,0,0,0]] <-- CAREFUL, appends done here
                playerpresentbox.clear()
                for i in range(len(playersboxtrack[who_turn])):
                    playerpresentbox.append(playersboxtrack[who_turn][i])
            
            if(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and moveOrActivate==0 and clic[0] and diceroll==1 and t==5 and pawnactivated[who_turn]==-1 and 1310<=x<=1440 and 375<=y<=422 and playerspawns[who_turn]!=[1,1,1,1] and diceposx>=DICEPOS[1][0]:
                GAME_SOUNDS['buttonclick'].play()
                for j in range(4):
                    if(playerspawns[who_turn][j]==0):
                        moveOrActivate=1
                        pawnactivated[who_turn]=j
                        break
            
            if(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and moveOrActivate==0 and clic[0] and diceroll==1 and 0<=t<=5 and playerspawns[who_turn][0]==1 and inHomeTrack[who_turn][0]+1+t<=6 and 1160<=x<=1290 and 445<=y<=492 and diceposx>=DICEPOS[1][0]:
                GAME_SOUNDS['buttonclick'].play()
                moveOrActivate=2
                # playerspos=[[ [],[],[],[] ]] <-- CAREFUL, appends done here
                if inHomeTrack[who_turn][0]>0 or (playerpresentbox[0]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[0]+1+t>endbox[gamedet['chosen colours'][who_turn]]):
                    inHomeTrack[who_turn][0]=(playerpresentbox[0]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                    playerpresentbox[0]+=1+t
                else:
                    playerpresentbox[0]+=1+t
                if(playerpresentbox[0]>52):
                    playerpresentbox[0]-=52
            elif(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and moveOrActivate==0 and clic[0] and diceroll==1 and 0<=t<=5 and playerspawns[who_turn][1]==1 and inHomeTrack[who_turn][1]+1+t<=6 and 1310<=x<=1440 and 445<=y<=492 and diceposx>=DICEPOS[1][0]:
                GAME_SOUNDS['buttonclick'].play()
                moveOrActivate=2
                if inHomeTrack[who_turn][1]>0 or (playerpresentbox[1]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[1]+1+t>endbox[gamedet['chosen colours'][who_turn]]):
                    inHomeTrack[who_turn][1]=(playerpresentbox[1]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                    playerpresentbox[1]+=1+t
                else:
                    playerpresentbox[1]+=1+t
                if(playerpresentbox[1]>52):
                    playerpresentbox[1]-=52
            elif(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and moveOrActivate==0 and clic[0] and diceroll==1 and 0<=t<=5 and playerspawns[who_turn][2]==1 and inHomeTrack[who_turn][2]+1+t<=6 and 1160<=x<=1290 and 515<=y<=562 and diceposx>=DICEPOS[1][0]:
                GAME_SOUNDS['buttonclick'].play()
                moveOrActivate=2
                if inHomeTrack[who_turn][2]>0 or (playerpresentbox[2]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[2]+1+t>endbox[gamedet['chosen colours'][who_turn]]):
                    inHomeTrack[who_turn][2]=(playerpresentbox[2]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                    playerpresentbox[2]+=1+t
                else:
                    playerpresentbox[2]+=1+t
                if(playerpresentbox[2]>52):
                    playerpresentbox[2]-=52
            elif(gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and moveOrActivate==0 and clic[0] and diceroll==1 and 0<=t<=5 and playerspawns[who_turn][3]==1 and inHomeTrack[who_turn][3]+1+t<=6 and 1310<=x<=1440 and 515<=y<=562 and diceposx>=DICEPOS[1][0]:
                GAME_SOUNDS['buttonclick'].play()
                moveOrActivate=2
                if inHomeTrack[who_turn][3]>0 or (playerpresentbox[3]<=endbox[gamedet['chosen colours'][who_turn]] and playerpresentbox[3]+1+t>endbox[gamedet['chosen colours'][who_turn]]):
                    inHomeTrack[who_turn][3]=(playerpresentbox[3]+1+t)%endbox[gamedet['chosen colours'][who_turn]]
                    playerpresentbox[3]+=1+t
                else:
                    playerpresentbox[3]+=1+t
                if(playerpresentbox[3]>52):
                    playerpresentbox[3]-=52

            if gamedet['game mode']!=0 or (gamedet['game mode']==0 and who_turn>0):
                if diceroll==1 and clic[0] and 1160<=x<=1290 and 375<=y<=422:
                    SCREEN.blit(roll[1],(1160,375))

                if diceroll==1 and t==5 and (playerspawns[who_turn][0]==0 or playerspawns[who_turn][1]==0 or playerspawns[who_turn][2]==0 or playerspawns[who_turn][3]==0):
                    if clic[0] and 1310<=x<=1440 and 375<=y<=422:
                        SCREEN.blit(activate[1],(1310,375))
            
                if playerspawns[who_turn][0]==1 and inHomeTrack[who_turn][0]+t<=5 and moveOrActivate==0:
                    if diceroll==1 and clic[0] and 1160<=x<=1290 and 445<=y<=492:
                        SCREEN.blit(movpawns[0][1],(1160,445))
                if playerspawns[who_turn][1]==1 and inHomeTrack[who_turn][1]+t<=5 and moveOrActivate==0:
                    if diceroll==1 and clic[0] and 1310<=x<=1440 and 445<=y<=492:
                        SCREEN.blit(movpawns[1][1],(1310,445))
                if playerspawns[who_turn][2]==1 and inHomeTrack[who_turn][2]+t<=5 and moveOrActivate==0:
                    if diceroll==1 and clic[0] and 1160<=x<=1290 and 515<=y<=562:
                        SCREEN.blit(movpawns[2][1],(1160,515))
                if playerspawns[who_turn][3]==1 and inHomeTrack[who_turn][3]+t<=5 and moveOrActivate==0:
                    if diceroll==1 and clic[0] and 1310<=x<=1440 and 515<=y<=562:
                        SCREEN.blit(movpawns[3][1],(1310,515))

        if (gamedet['game mode']>0 or (gamedet['game mode']==0 and who_turn>0)) and diceroll==1 and playerpresentbox!=[] and playerpresentbox!=playersboxtrack[who_turn] and moveapawn==-10 and moveOrActivate==2:
            for i in range(4):
                # if playerpresentbox[i]!=playersboxtrack[who_turn][i] or (inHomeTrack[who_turn][i]!=0 and inHomeTrack[who_turn][i]+t<=5):
                if playerpresentbox[i]!=playersboxtrack[who_turn][i]:
                    moveapawn=i
                    break

        if(t!=-1 and diceroll==1 and diceposx<=DICEPOS[1][0]):
            SCREEN.blit(dices[t],(diceposx,diceposy))
            diceposx+=3
            if gamedet['game mode']==0 and who_turn==0 and computerRolls<=90:
                computerRolls+=1
        elif(t!=-1 and diceroll==1):
            SCREEN.blit(dices[t],(diceposx,diceposy))
            if gamedet['game mode']==0 and who_turn==0 and computerRolls<=90:
                computerRolls+=1

        SCREEN.blit(pygame.transform.rotate(diceroller,90),(1150,135))

        if diceroll==1 and t==5 and diceposx>=DICEPOS[1][0] and pawnactivated[who_turn]!=-1 and moveOrActivate==1:
            # playersboxtrack[who_turn][pawnactivated[who_turn]]=1
            playersboxtrack[who_turn][pawnactivated[who_turn]]=startbox[gamedet['chosen colours'][who_turn]]

            for i in range(4):
                if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]][i]==0:
                    destinationInSSBox=i
                    placeInSSBox=i
                    break
            
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]<38:
                playerPawnSizes[who_turn][pawnactivated[who_turn]]+=2
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and abs(playerPawnSizes[who_turn][pawnactivated[who_turn]]-38)<2:
                playerPawnSizes[who_turn][pawnactivated[who_turn]]=38

            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]!=[0,0,0,0]:
                first=-1
                noOf1=0
                for i in range(4):
                    if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]][i]==1:noOf1+=1
                
                if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[1,0,0,0]:first=0
                if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,1,0,0]:first=1
                if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,1,0]:first=2
                if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,1]:first=3

                if first!=-1:
                    for i in range(1+max(1,gamedet['game mode'])):
                        for j in range(4):
                            if playerspos[i][j][0]==allstartpos[gamedet['chosen colours'][who_turn]][0] and playerspos[i][j][1]==allstartpos[gamedet['chosen colours'][who_turn]][1] and whoFirst==[]:
                                whoFirst.append(i)
                                whoFirst.append(j)
                                break
                        if whoFirst!=[]:break
                    
                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]>19:
                        playerPawnSizes[whoFirst[0]][whoFirst[1]]-=2
                    if whoFirst!=[] and abs(playerPawnSizes[whoFirst[0]][whoFirst[1]]-19)<2:
                        playerPawnSizes[whoFirst[0]][whoFirst[1]]=19

                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and playerspos[whoFirst[0]][whoFirst[1]][0]<SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][0]:
                        playerspos[whoFirst[0]][whoFirst[1]][0]+=3
                    elif whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and playerspos[whoFirst[0]][whoFirst[1]][0]>SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][0]:
                        playerspos[whoFirst[0]][whoFirst[1]][0]-=3
                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and abs(playerspos[whoFirst[0]][whoFirst[1]][0]-SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][0])<3:
                        playerspos[whoFirst[0]][whoFirst[1]][0]=SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][0]
                    
                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and playerspos[whoFirst[0]][whoFirst[1]][1]<SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][1]:
                        playerspos[whoFirst[0]][whoFirst[1]][1]+=3
                    elif whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and playerspos[whoFirst[0]][whoFirst[1]][1]>SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][1]:
                        playerspos[whoFirst[0]][whoFirst[1]][1]-=3
                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and abs(playerspos[whoFirst[0]][whoFirst[1]][1]-SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][1])<3:
                        playerspos[whoFirst[0]][whoFirst[1]][1]=SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][1]
                    
                    if whoFirst!=[] and playerPawnSizes[whoFirst[0]][whoFirst[1]]==19 and playerspos[whoFirst[0]][whoFirst[1]][0]==SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][0] and playerspos[whoFirst[0]][whoFirst[1]][1]==SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][first][1]:
                        first=-1
                        whoFirst.clear()

                if 1<=noOf1<4 and playerPawnSizes[who_turn][pawnactivated[who_turn]]>19:
                    playerPawnSizes[who_turn][pawnactivated[who_turn]]-=2
                if 1<=noOf1<4 and abs(playerPawnSizes[who_turn][pawnactivated[who_turn]]-19)<2:
                    playerPawnSizes[who_turn][pawnactivated[who_turn]]=19

                if playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and playerspos[who_turn][pawnactivated[who_turn]][0]<SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][0]:
                    playerspos[who_turn][pawnactivated[who_turn]][0]+=3
                elif playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and playerspos[who_turn][pawnactivated[who_turn]][0]>SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][0]:
                    playerspos[who_turn][pawnactivated[who_turn]][0]-=3
                if playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and abs(playerspos[who_turn][pawnactivated[who_turn]][0]-SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][0])<3:
                    playerspos[who_turn][pawnactivated[who_turn]][0]=SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][0]

                if playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and playerspos[who_turn][pawnactivated[who_turn]][1]<SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][1]:
                    playerspos[who_turn][pawnactivated[who_turn]][1]+=3
                elif playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and playerspos[who_turn][pawnactivated[who_turn]][1]>SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][1]:
                    playerspos[who_turn][pawnactivated[who_turn]][1]-=3
                if playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and abs(playerspos[who_turn][pawnactivated[who_turn]][1]-SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][1])<3:
                    playerspos[who_turn][pawnactivated[who_turn]][1]=SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][1]

                if playerPawnSizes[who_turn][pawnactivated[who_turn]]==19 and playerspos[who_turn][pawnactivated[who_turn]][0]==SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][0] and playerspos[who_turn][pawnactivated[who_turn]][1]==SSboxpos4[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox][1]:
                    playerspawns[who_turn][pawnactivated[who_turn]]=1
                    pawnactivated[who_turn]=-1
                    pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox]=1
                    placeInSSBox=-10
                    diceroll=2
                    GAME_SOUNDS['stopreached'].play()
                    GAME_SOUNDS['activation'][random.randint(0,-1+len(GAME_SOUNDS['activation']))].play()
                    moveOrActivate=0
            
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and (playerspos[who_turn][pawnactivated[who_turn]][0]<allstartpos[gamedet['chosen colours'][who_turn]][0]):
                playerspos[who_turn][pawnactivated[who_turn]][0]+=3
            elif pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and (playerspos[who_turn][pawnactivated[who_turn]][0]>allstartpos[gamedet['chosen colours'][who_turn]][0]):
                playerspos[who_turn][pawnactivated[who_turn]][0]-=3
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and abs(playerspos[who_turn][pawnactivated[who_turn]][0]-allstartpos[gamedet['chosen colours'][who_turn]][0])<3:
                playerspos[who_turn][pawnactivated[who_turn]][0]=allstartpos[gamedet['chosen colours'][who_turn]][0]

            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and (playerspos[who_turn][pawnactivated[who_turn]][1]<allstartpos[gamedet['chosen colours'][who_turn]][1]):
                playerspos[who_turn][pawnactivated[who_turn]][1]+=3
            elif pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and (playerspos[who_turn][pawnactivated[who_turn]][1]>allstartpos[gamedet['chosen colours'][who_turn]][1]):
                playerspos[who_turn][pawnactivated[who_turn]][1]-=3
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and abs(playerspos[who_turn][pawnactivated[who_turn]][1]-allstartpos[gamedet['chosen colours'][who_turn]][1])<3:
                playerspos[who_turn][pawnactivated[who_turn]][1]=allstartpos[gamedet['chosen colours'][who_turn]][1]
                
            if pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]]==[0,0,0,0] and playerPawnSizes[who_turn][pawnactivated[who_turn]]==38 and (playerspos[who_turn][pawnactivated[who_turn]][0]==allstartpos[gamedet['chosen colours'][who_turn]][0] and playerspos[who_turn][pawnactivated[who_turn]][1]==allstartpos[gamedet['chosen colours'][who_turn]][1]):
                playerspawns[who_turn][pawnactivated[who_turn]]=1
                pawnactivated[who_turn]=-1
                pawnsInSSBox[startbox[gamedet['chosen colours'][who_turn]]][placeInSSBox]=1
                placeInSSBox=-10
                diceroll=2
                GAME_SOUNDS['stopreached'].play()
                GAME_SOUNDS['activation'][random.randint(0,-1+len(GAME_SOUNDS['activation']))].play()
                moveOrActivate=0
        elif diceroll==1 and diceposx>=DICEPOS[1][0] and pawnactivated[who_turn]==-1 and moveapawn==-10:
            if t!=5 and playerspawns[who_turn][0]==0 and playerspawns[who_turn][1]==0 and playerspawns[who_turn][2]==0 and playerspawns[who_turn][3]==0:
                nothingHappened+=1
            else:
                ch=0
                for i in range(4):
                    if playerspawns[who_turn][i]==1 and inHomeTrack[who_turn][i]+t<=5:
                        ch=1
                        break
                if t==5 and (playerspawns[who_turn][0]==0 or playerspawns[who_turn][1]==0 or playerspawns[who_turn][2]==0 or playerspawns[who_turn][3]==0):
                    ch=1
                if ch==0:
                    nothingHappened+=1
        
        # LOT of code editing required here !!
        # playerpresentbox[3]+=(t+1)        
        if diceroll==1 and diceposx>=DICEPOS[1][0] and moveapawn!=-10 and moveOrActivate==2: # try putting diceroll==1 here once 
            # playerspos=[[ [],[],[],[] ]] <-- CAREFUL, appends done here
            # playersboxtrack=[[0,0,0,0]] <-- CAREFUL, appends done here
            # playerpresentbox=[]
            # playerpresentbox.append(playersboxtrack[who_turn][i])

            # I need a post-departure check auditor, to ensure the checks don't happen more times than I want it to
            # and I can set it with 1 at the end of every turn, it will become 0 here, after one check is completely done
            noOf1 = 0
            if playersboxtrack[who_turn][moveapawn] in safestarboxes:
                for i in range(4):
                    if (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and pawnsInSSBox[playersboxtrack[who_turn][moveapawn]][i]==1:
                        noOf1+=1

            noOf1inNormalBox=0
            if playersboxtrack[who_turn][moveapawn] not in safestarboxes:
                for i in range(4):
                    if (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and pawnsInNormalBox[playersboxtrack[who_turn][moveapawn]][i]==1:
                        noOf1inNormalBox+=1
            
            # code that affects where it is coming from
            if postDepCheckInNormalBox==1 and playersboxtrack[who_turn][moveapawn] not in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and noOf1inNormalBox==1:
                pawnsInNormalBox[playersboxtrack[who_turn][moveapawn]]=[0,0,0,0]
                postDepCheckInNormalBox=0
            elif postDepCheckInNormalBox==1 and playersboxtrack[who_turn][moveapawn] not in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and noOf1inNormalBox==2:
                # if gamedet['game mode']==0: # the 'not in safestar boxes' will fail when I am going from one safestar box to another so destination is also in safe star box but what if pawns in source ss box = 2
                for i in range(4):
                    if i!=moveapawn and playersboxtrack[who_turn][i]==playersboxtrack[who_turn][moveapawn] and inHomeTrack[who_turn][i]==0:
                        if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]>allBoxPositions[playersboxtrack[who_turn][i]-1][0]:
                            playerspos[who_turn][i][0]-=3
                        elif playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]<allBoxPositions[playersboxtrack[who_turn][i]-1][0]:
                            playerspos[who_turn][i][0]+=3
                        if playerPawnSizes[who_turn][i]==38 and abs(playerspos[who_turn][i][0]-allBoxPositions[playersboxtrack[who_turn][i]-1][0])<3:
                            playerspos[who_turn][i][0]=allBoxPositions[playersboxtrack[who_turn][i]-1][0]
                            
                        if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][1]>allBoxPositions[playersboxtrack[who_turn][i]-1][1]:
                            playerspos[who_turn][i][1]-=3
                        elif playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][1]<allBoxPositions[playersboxtrack[who_turn][i]-1][1]:
                            playerspos[who_turn][i][1]+=3
                        if playerPawnSizes[who_turn][i]==38 and abs(playerspos[who_turn][i][1]-allBoxPositions[playersboxtrack[who_turn][i]-1][1])<3:
                            playerspos[who_turn][i][1]=allBoxPositions[playersboxtrack[who_turn][i]-1][1]
                            
                        if playerPawnSizes[who_turn][i]<38:
                            playerPawnSizes[who_turn][i]+=3
                        if abs(playerPawnSizes[who_turn][i]-38)<3:
                            playerPawnSizes[who_turn][i]=38 # don't forget to do the same for computer pawns' size too !

                        if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]==allBoxPositions[playersboxtrack[who_turn][i]-1][0] and playerspos[who_turn][i][1]==allBoxPositions[playersboxtrack[who_turn][i]-1][1]:
                            pawnsInNormalBox[playersboxtrack[who_turn][i]]=[1,0,0,0]
                            postDepCheckInNormalBox=0
            elif postDepCheckInNormalBox==1 and playersboxtrack[who_turn][moveapawn] not in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and 2<noOf1inNormalBox<=4:
                # placeInNormalBox=-1 # it would be advisable to reset placeInNormalBox to zero after end of each turn
                placeToClearInNormalBox=-10
                for j in range(4):
                    if playerspos[who_turn][moveapawn][0]==normalboxpos4[playersboxtrack[who_turn][moveapawn]][j][0] and playerspos[who_turn][moveapawn][1]==normalboxpos4[playersboxtrack[who_turn][moveapawn]][j][1]:
                        placeToClearInNormalBox=j
                        break
                if placeToClearInNormalBox!=-10:
                    pawnsInNormalBox[playersboxtrack[who_turn][moveapawn]][placeToClearInNormalBox]=0 # seems right, may be wrong
                    placeToClearInNormalBox=-10
                    postDepCheckInNormalBox=0 # needs to be set to 1 again after end of turn

            if postDepCheckInSSBox==1 and playersboxtrack[who_turn][moveapawn] in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and noOf1==1:
                pawnsInSSBox[playersboxtrack[who_turn][moveapawn]]=[0,0,0,0]
                postDepCheckInSSBox=0
            elif postDepCheckInSSBox==1 and playersboxtrack[who_turn][moveapawn] in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and noOf1==2:
                for i in range(1+max(1,gamedet['game mode'])):
                    for j in range(4):
                        if (i!=who_turn or j!=moveapawn) and playersboxtrack[i][j]==playersboxtrack[who_turn][moveapawn] and inHomeTrack[i][j]==0:
                            if playerPawnSizes[i][j]==38 and playerspos[i][j][0]>allBoxPositions[playersboxtrack[i][j]-1][0]:
                                playerspos[i][j][0]-=3
                            elif playerPawnSizes[i][j]==38 and playerspos[i][j][0]<allBoxPositions[playersboxtrack[i][j]-1][0]:
                                playerspos[i][j][0]+=3
                            if playerPawnSizes[i][j]==38 and abs(playerspos[i][j][0]-allBoxPositions[playersboxtrack[i][j]-1][0])<3:
                                playerspos[i][j][0]=allBoxPositions[playersboxtrack[i][j]-1][0]
                                
                            if playerPawnSizes[i][j]==38 and playerspos[i][j][1]>allBoxPositions[playersboxtrack[i][j]-1][1]:
                                playerspos[i][j][1]-=3
                            elif playerPawnSizes[i][j]==38 and playerspos[i][j][1]<allBoxPositions[playersboxtrack[i][j]-1][1]:
                                playerspos[i][j][1]+=3
                            if playerPawnSizes[i][j]==38 and abs(playerspos[i][j][1]-allBoxPositions[playersboxtrack[i][j]-1][1])<3:
                                playerspos[i][j][1]=allBoxPositions[playersboxtrack[i][j]-1][1] 
                            # reduce the speed of location change to ensure shapeshift happens or just start relocation after shapeshifting is complete, 19 iterations anyway

                            if playerPawnSizes[i][j]<38:
                                playerPawnSizes[i][j]+=3
                            if abs(playerPawnSizes[i][j]-38)<3:
                                playerPawnSizes[i][j]=38

                            if playerPawnSizes[i][j]==38 and playerspos[i][j][0]==allBoxPositions[playersboxtrack[i][j]-1][0] and playerspos[i][j][1]==allBoxPositions[playersboxtrack[i][j]-1][1]:
                                pawnsInSSBox[playersboxtrack[i][j]]=[1,0,0,0]
                                postDepCheckInSSBox=0
            elif postDepCheckInSSBox==1 and playersboxtrack[who_turn][moveapawn] in safestarboxes and playerpresentbox[moveapawn]!=playersboxtrack[who_turn][moveapawn] and (inHomeTrack[who_turn][moveapawn]==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]) and 2<noOf1<=4:
                placeToClearInSSBox=-10
                for j in range(4):
                    if playerspos[who_turn][moveapawn][0]==SSboxpos4[playersboxtrack[who_turn][moveapawn]][j][0] and playerspos[who_turn][moveapawn][1]==SSboxpos4[playersboxtrack[who_turn][moveapawn]][j][1]:
                        placeToClearInSSBox=j # this condition will be valid only once, as after this the pawn will move somewhere else, so position will shift
                        break
                if placeToClearInSSBox!=-10:
                    pawnsInSSBox[playersboxtrack[who_turn][moveapawn]][placeToClearInSSBox]=0 # seems right, may be wrong
                    placeToClearInSSBox=-10
                    postDepCheckInSSBox=0 # needs to be set to 1 again after end of turn
            
            # code that affects where it is going
            if inHomeTrack[who_turn][moveapawn]==0 and playerpresentbox[moveapawn] not in safestarboxes and (postDepCheckInSSBox==0 or postDepCheckInNormalBox==0):
                noOf1inNormalBox=0
                for i in range(4):
                    if pawnsInNormalBox[playerpresentbox[moveapawn]][i]==1:noOf1inNormalBox+=1
                
                checkcount=0
                for j in range(4):
                    if j!=moveapawn and inHomeTrack[who_turn][j]==0 and playersboxtrack[who_turn][j]==playerpresentbox[moveapawn]:checkcount+=1
                if checkcount!=noOf1inNormalBox:someoneGonnaDie=1

                if noOf1inNormalBox==0 or someoneGonnaDie==1:
                    destinationInNormalBox=0
                    if playerPawnSizes[who_turn][moveapawn]<38:playerPawnSizes[who_turn][moveapawn]+=3
                    if abs(playerPawnSizes[who_turn][moveapawn]-38)<3:playerPawnSizes[who_turn][moveapawn]=38

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]<allBoxPositions[playerpresentbox[moveapawn]-1][0]:playerspos[who_turn][moveapawn][0]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]>allBoxPositions[playerpresentbox[moveapawn]-1][0]:playerspos[who_turn][moveapawn][0]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][0]-allBoxPositions[playerpresentbox[moveapawn]-1][0])<2:playerspos[who_turn][moveapawn][0]=allBoxPositions[playerpresentbox[moveapawn]-1][0]

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]<allBoxPositions[playerpresentbox[moveapawn]-1][1]:playerspos[who_turn][moveapawn][1]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]>allBoxPositions[playerpresentbox[moveapawn]-1][1]:playerspos[who_turn][moveapawn][1]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][1]-allBoxPositions[playerpresentbox[moveapawn]-1][1])<2:playerspos[who_turn][moveapawn][1]=allBoxPositions[playerpresentbox[moveapawn]-1][1]

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]==allBoxPositions[playerpresentbox[moveapawn]-1][0] and playerspos[who_turn][moveapawn][1]==allBoxPositions[playerpresentbox[moveapawn]-1][1]:
                        pawnsInNormalBox[playerpresentbox[moveapawn]]=[1,0,0,0]
                elif noOf1inNormalBox==1:
                    destinationInNormalBox=1
                    beginafterthis=0
                    for i in range(4):
                        if i!=moveapawn and playersboxtrack[who_turn][i]==playerpresentbox[moveapawn] and inHomeTrack[who_turn][i]==0:
                            if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]>normalboxpos4[playerpresentbox[moveapawn]][0][0]:
                                playerspos[who_turn][i][0]-=3
                            elif playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]<normalboxpos4[playerpresentbox[moveapawn]][0][0]:
                                playerspos[who_turn][i][0]+=3
                            if playerPawnSizes[who_turn][i]==19 and abs(playerspos[who_turn][i][0]-normalboxpos4[playerpresentbox[moveapawn]][0][0])<3:
                                playerspos[who_turn][i][0]=normalboxpos4[playerpresentbox[moveapawn]][0][0]

                            if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][1]>normalboxpos4[playerpresentbox[moveapawn]][0][1]:
                                playerspos[who_turn][i][1]-=3
                            elif playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][1]<normalboxpos4[playerpresentbox[moveapawn]][0][1]:
                                playerspos[who_turn][i][1]+=3
                            if playerPawnSizes[who_turn][i]==19 and abs(playerspos[who_turn][i][1]-normalboxpos4[playerpresentbox[moveapawn]][0][1])<3:
                                playerspos[who_turn][i][1]=normalboxpos4[playerpresentbox[moveapawn]][0][1]

                            if playerPawnSizes[who_turn][i]>19: # shrinks
                                playerPawnSizes[who_turn][i]-=3
                            if abs(playerPawnSizes[who_turn][i]-19)<3:
                                playerPawnSizes[who_turn][i]=19

                            if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]==normalboxpos4[playerpresentbox[moveapawn]][0][0] and playerspos[who_turn][i][1]==normalboxpos4[playerpresentbox[moveapawn]][0][1]:
                                beginafterthis=1
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]>19:playerPawnSizes[who_turn][moveapawn]-=2
                    if beginafterthis==1 and abs(playerPawnSizes[who_turn][moveapawn]-19)<2:playerPawnSizes[who_turn][moveapawn]=19

                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<normalboxpos4[playerpresentbox[moveapawn]][1][0]:playerspos[who_turn][moveapawn][0]+=2
                    elif beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>normalboxpos4[playerpresentbox[moveapawn]][1][0]:playerspos[who_turn][moveapawn][0]-=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-normalboxpos4[playerpresentbox[moveapawn]][1][0])<2:playerspos[who_turn][moveapawn][0]=normalboxpos4[playerpresentbox[moveapawn]][1][0]

                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<normalboxpos4[playerpresentbox[moveapawn]][1][1]:playerspos[who_turn][moveapawn][1]+=2
                    elif beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>normalboxpos4[playerpresentbox[moveapawn]][1][1]:playerspos[who_turn][moveapawn][1]-=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-normalboxpos4[playerpresentbox[moveapawn]][1][1])<2:playerspos[who_turn][moveapawn][1]=normalboxpos4[playerpresentbox[moveapawn]][1][1]

                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]==normalboxpos4[playerpresentbox[moveapawn]][1][0] and playerspos[who_turn][moveapawn][1]==normalboxpos4[playerpresentbox[moveapawn]][1][1]:
                        pawnsInNormalBox[playerpresentbox[moveapawn]]=[1,1,0,0]
                elif 2<=noOf1inNormalBox<4:
                    placeInNormalBox=-10
                    for j in range(4):
                        if pawnsInNormalBox[playerpresentbox[moveapawn]][j]==0:
                            placeInNormalBox=j
                            destinationInNormalBox=j
                            break
                    if playerPawnSizes[who_turn][moveapawn]>19:playerPawnSizes[who_turn][moveapawn]-=2
                    if abs(playerPawnSizes[who_turn][moveapawn]-19)<2:playerPawnSizes[who_turn][moveapawn]=19

                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][0]:playerspos[who_turn][moveapawn][0]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][0]:playerspos[who_turn][moveapawn][0]-=2
                    if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][0])<2:playerspos[who_turn][moveapawn][0]=normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][0]

                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][1]:playerspos[who_turn][moveapawn][1]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][1]:playerspos[who_turn][moveapawn][1]-=2
                    if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][1])<2:playerspos[who_turn][moveapawn][1]=normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][1]
                    
                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]==normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][0] and playerspos[who_turn][moveapawn][1]==normalboxpos4[playerpresentbox[moveapawn]][placeInNormalBox][1]:
                        pawnsInNormalBox[playerpresentbox[moveapawn]][placeInNormalBox]=1
            elif inHomeTrack[who_turn][moveapawn]==0 and playerpresentbox[moveapawn] in safestarboxes and (postDepCheckInNormalBox==0 or postDepCheckInSSBox==0):
                noOf1=0
                for i in range(4):
                    if pawnsInSSBox[playerpresentbox[moveapawn]][i]==1:noOf1+=1
                # THERE SEEMS TO BE A PROBLEM WITH postDepCheckInNormalBox !!!!
                if noOf1==0:
                    destinationInSSBox=0
                    if playerPawnSizes[who_turn][moveapawn]<38:
                        playerPawnSizes[who_turn][moveapawn]+=2
                    if abs(playerPawnSizes[who_turn][moveapawn]-38)<2:
                        playerPawnSizes[who_turn][moveapawn]=38
                    
                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]<allBoxPositions[playerpresentbox[moveapawn]-1][0]:
                        playerspos[who_turn][moveapawn][0]+=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]>allBoxPositions[playerpresentbox[moveapawn]-1][0]:
                        playerspos[who_turn][moveapawn][0]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][0]-allBoxPositions[playerpresentbox[moveapawn]-1][0])<2:
                        playerspos[who_turn][moveapawn][0]=allBoxPositions[playerpresentbox[moveapawn]-1][0]

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]<allBoxPositions[playerpresentbox[moveapawn]-1][1]:
                        playerspos[who_turn][moveapawn][1]+=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]>allBoxPositions[playerpresentbox[moveapawn]-1][1]:
                        playerspos[who_turn][moveapawn][1]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][1]-allBoxPositions[playerpresentbox[moveapawn]-1][1])<2:
                        playerspos[who_turn][moveapawn][1]=allBoxPositions[playerpresentbox[moveapawn]-1][1]

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]==allBoxPositions[playerpresentbox[moveapawn]-1][0] and playerspos[who_turn][moveapawn][1]==allBoxPositions[playerpresentbox[moveapawn]-1][1]:
                        pawnsInSSBox[playerpresentbox[moveapawn]]=[1,0,0,0]
                elif noOf1==1:
                    destinationInSSBox=1
                    beginafterthis=0
                    for i in range(1+max(1,gamedet['game mode'])):
                        for j in range(4):
                            if (i!=who_turn or j!=moveapawn) and playersboxtrack[i][j]==playerpresentbox[moveapawn] and inHomeTrack[i][j]==0:
                                if playerPawnSizes[i][j]>19:
                                    playerPawnSizes[i][j]-=3
                                if abs(playerPawnSizes[i][j]-19)<3:
                                    playerPawnSizes[i][j]=19
                                
                                if playerPawnSizes[i][j]==19 and playerspos[i][j][0]>SSboxpos4[playersboxtrack[i][j]][0][0]:
                                    playerspos[i][j][0]-=3
                                elif playerPawnSizes[i][j]==19 and playerspos[i][j][0]<SSboxpos4[playersboxtrack[i][j]][0][0]:
                                    playerspos[i][j][0]+=3
                                if playerPawnSizes[i][j]==19 and abs(playerspos[i][j][0]-SSboxpos4[playersboxtrack[i][j]][0][0])<3:
                                    playerspos[i][j][0]=SSboxpos4[playersboxtrack[i][j]][0][0]
                                    
                                if playerPawnSizes[i][j]==19 and playerspos[i][j][1]>SSboxpos4[playersboxtrack[i][j]][0][1]:
                                    playerspos[i][j][1]-=3
                                elif playerPawnSizes[i][j]==19 and playerspos[i][j][1]<SSboxpos4[playersboxtrack[i][j]][0][1]:
                                    playerspos[i][j][1]+=3
                                if playerPawnSizes[i][j]==19 and abs(playerspos[i][j][1]-SSboxpos4[playersboxtrack[i][j]][0][1])<3:
                                    playerspos[i][j][1]=SSboxpos4[playersboxtrack[i][j]][0][1]

                                if playerPawnSizes[i][j]==19 and playerspos[i][j][0]==SSboxpos4[playersboxtrack[i][j]][0][0] and playerspos[i][j][1]==SSboxpos4[playersboxtrack[i][j]][0][1]:
                                    beginafterthis=1
                        
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]>19:playerPawnSizes[who_turn][moveapawn]-=2
                    if beginafterthis==1 and abs(playerPawnSizes[who_turn][moveapawn]-19)<2:playerPawnSizes[who_turn][moveapawn]=19
                        
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<SSboxpos4[playerpresentbox[moveapawn]][1][0]:
                        playerspos[who_turn][moveapawn][0]+=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>SSboxpos4[playerpresentbox[moveapawn]][1][0]:
                        playerspos[who_turn][moveapawn][0]-=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-SSboxpos4[playerpresentbox[moveapawn]][1][0])<2:
                        playerspos[who_turn][moveapawn][0]=SSboxpos4[playerpresentbox[moveapawn]][1][0]
                        
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<SSboxpos4[playerpresentbox[moveapawn]][1][1]:
                        playerspos[who_turn][moveapawn][1]+=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>SSboxpos4[playerpresentbox[moveapawn]][1][1]:
                        playerspos[who_turn][moveapawn][1]-=2
                    if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-SSboxpos4[playerpresentbox[moveapawn]][1][1])<2:
                        playerspos[who_turn][moveapawn][1]=SSboxpos4[playerpresentbox[moveapawn]][1][1]
                    if beginafterthis==1 and playerspos[who_turn][moveapawn][0]==SSboxpos4[playerpresentbox[moveapawn]][1][0] and playerspos[who_turn][moveapawn][1]==SSboxpos4[playerpresentbox[moveapawn]][1][1]:
                        pawnsInSSBox[playerpresentbox[moveapawn]]=[1,1,0,0]
                elif 2<=noOf1<4:
                    placeInSSBox=-10
                    for j in range(4):
                        if pawnsInSSBox[playerpresentbox[moveapawn]][j]==0:
                            placeInSSBox=j
                            destinationInSSBox=j
                            break

                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][0]:
                        playerspos[who_turn][moveapawn][0]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][0]:
                        playerspos[who_turn][moveapawn][0]-=2
                    if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][0])<2:
                        playerspos[who_turn][moveapawn][0]=SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][0]

                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][1]:
                        playerspos[who_turn][moveapawn][1]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][1]:
                        playerspos[who_turn][moveapawn][1]-=2
                    if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][1])<2:
                        playerspos[who_turn][moveapawn][1]=SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][1]

                    if playerPawnSizes[who_turn][moveapawn]>19:
                        playerPawnSizes[who_turn][moveapawn]-=2
                    if abs(playerPawnSizes[who_turn][moveapawn]-19)<2:
                        playerPawnSizes[who_turn][moveapawn]=19

                    if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]==SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][0] and playerspos[who_turn][moveapawn][1]==SSboxpos4[playerpresentbox[moveapawn]][placeInSSBox][1]:
                        pawnsInSSBox[playerpresentbox[moveapawn]][placeInSSBox]=1
            
            if inHomeTrack[who_turn][moveapawn]!=0:
                '''
                it could be that it just entered hometrack from a non-hometrack box so inhomeTrack
                will get updated in that case too, so here regarding where it is coming from, it
                could be already in the hometrack to begin with, or it could be in some standard
                non-hometrack box also
                '''
                # affects where it is coming from, if it was in the home track to begin with
                if playersboxtrack[who_turn][moveapawn]!=playerpresentbox[moveapawn] and 0<playersboxtrack[who_turn][moveapawn]%endbox[gamedet['chosen colours'][who_turn]]<6:
                    noOf1=0
                    for i in range(4):
                        if pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][moveapawn]%endbox[gamedet['chosen colours'][who_turn]]][i]==1:
                            noOf1+=1
                    if postDepCheckInHomeTrack==1 and noOf1==1:
                        pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][moveapawn]%endbox[gamedet['chosen colours'][who_turn]]]=[0,0,0,0]
                        postDepCheckInHomeTrack=0
                    elif postDepCheckInHomeTrack==1 and noOf1==2:
                        for i in range(4):
                            if i!=moveapawn and inHomeTrack[who_turn][i]>0 and playersboxtrack[who_turn][i]==playersboxtrack[who_turn][moveapawn]:
                                if playerPawnSizes[who_turn][i]<38:playerPawnSizes[who_turn][i]+=3
                                if abs(playerPawnSizes[who_turn][i]-38)<3:playerPawnSizes[who_turn][i]=38
                                
                                if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]<homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][0]:
                                    playerspos[who_turn][i][0]+=2
                                elif playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]>homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][0]:
                                    playerspos[who_turn][i][0]-=2
                                if playerPawnSizes[who_turn][i]==38 and abs(playerspos[who_turn][i][0]-homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][0])<2:
                                    playerspos[who_turn][i][0]=homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][0]
                                
                                if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][1]<homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][1]:
                                    playerspos[who_turn][i][1]+=2
                                elif playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][1]>homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][1]:
                                    playerspos[who_turn][i][1]-=2
                                if playerPawnSizes[who_turn][i]==38 and abs(playerspos[who_turn][i][1]-homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][1])<2:
                                    playerspos[who_turn][i][1]=homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][1]

                                if playerPawnSizes[who_turn][i]==38 and playerspos[who_turn][i][0]==homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][0] and playerspos[who_turn][i][1]==homecoming[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][1]:
                                    pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]]=[1,0,0,0]
                                    postDepCheckInHomeTrack=0
                    elif postDepCheckInHomeTrack==1 and 2<noOf1<=4:
                        for i in range(4):
                            if playerspos[who_turn][moveapawn][0]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][i][0] and playerspos[who_turn][moveapawn][1]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][i][1] and pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][i]==1:
                                pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+playersboxtrack[who_turn][i]%endbox[gamedet['chosen colours'][who_turn]]][i]=0
                                postDepCheckInHomeTrack=0
                                break
                
                # code that affects where it is going
                if inHomeTrack[who_turn][moveapawn]==6 and (postDepCheckInHomeTrack==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]):
                    destinationInHomeTrack=0
                    if playerPawnSizes[who_turn][moveapawn]<38:playerPawnSizes[who_turn][moveapawn]+=3
                    if abs(playerPawnSizes[who_turn][moveapawn]-38)<3:playerPawnSizes[who_turn][moveapawn]=38

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]<homecoming[gamedet['chosen colours'][who_turn]][5][0]:playerspos[who_turn][moveapawn][0]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]>homecoming[gamedet['chosen colours'][who_turn]][5][0]:playerspos[who_turn][moveapawn][0]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][0]-homecoming[gamedet['chosen colours'][who_turn]][5][0])<2:playerspos[who_turn][moveapawn][0]=homecoming[gamedet['chosen colours'][who_turn]][5][0]

                    if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]<homecoming[gamedet['chosen colours'][who_turn]][5][1]:playerspos[who_turn][moveapawn][1]+=2
                    elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]>homecoming[gamedet['chosen colours'][who_turn]][5][1]:playerspos[who_turn][moveapawn][1]-=2
                    if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][1]-homecoming[gamedet['chosen colours'][who_turn]][5][1])<2:playerspos[who_turn][moveapawn][1]=homecoming[gamedet['chosen colours'][who_turn]][5][1]
                elif 0<inHomeTrack[who_turn][moveapawn]<6 and (postDepCheckInHomeTrack==0 or -5+endbox[gamedet['chosen colours'][who_turn]]<=playersboxtrack[who_turn][moveapawn]<=endbox[gamedet['chosen colours'][who_turn]]):
                    noOf1=0
                    for i in range(4):
                        if pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][i]==1:noOf1+=1
                    if noOf1==0:
                        destinationInHomeTrack=0
                        if playerPawnSizes[who_turn][moveapawn]<38:playerPawnSizes[who_turn][moveapawn]+=3
                        if abs(playerPawnSizes[who_turn][moveapawn]-38)<3:playerPawnSizes[who_turn][moveapawn]=38

                        if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]<homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0]:
                            playerspos[who_turn][moveapawn][0]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][0]>homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0]:
                            playerspos[who_turn][moveapawn][0]-=2
                        if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][0]-homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0])<2:
                            playerspos[who_turn][moveapawn][0]=homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0]

                        if playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]<homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1]:
                            playerspos[who_turn][moveapawn][1]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==38 and playerspos[who_turn][moveapawn][1]>homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1]:
                            playerspos[who_turn][moveapawn][1]-=2
                        if playerPawnSizes[who_turn][moveapawn]==38 and abs(playerspos[who_turn][moveapawn][1]-homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1])<2:
                            playerspos[who_turn][moveapawn][1]=homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1]
                        
                        if playerspos[who_turn][moveapawn][0]==homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0] and playerspos[who_turn][moveapawn][1]==homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1]:
                            pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]]=[1,0,0,0]
                    elif noOf1==1:
                        destinationInHomeTrack=1
                        beginafterthis=0
                        for i in range(4):
                            if i!=moveapawn and inHomeTrack[who_turn][i]>0 and playersboxtrack[who_turn][i]==playerpresentbox[moveapawn]:
                                if playerPawnSizes[who_turn][i]>19:playerPawnSizes[who_turn][i]-=2
                                if abs(playerPawnSizes[who_turn][i]-19)<2:playerPawnSizes[who_turn][i]=19

                                if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][0]:
                                    playerspos[who_turn][i][0]+=2
                                elif playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][0]:
                                    playerspos[who_turn][i][0]-=2
                                if playerPawnSizes[who_turn][i]==19 and abs(playerspos[who_turn][i][0]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][0])<2:
                                    playerspos[who_turn][i][0]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][0]

                                if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][1]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][1]:
                                    playerspos[who_turn][i][1]+=2
                                elif playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][1]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][1]:
                                    playerspos[who_turn][i][1]-=2
                                if playerPawnSizes[who_turn][i]==19 and abs(playerspos[who_turn][i][1]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][1])<2:
                                    playerspos[who_turn][i][1]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][1]
                                
                                if playerPawnSizes[who_turn][i]==19 and playerspos[who_turn][i][0]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][0] and playerspos[who_turn][i][1]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0][1]:
                                    beginafterthis=1
                        
                        if playerPawnSizes[who_turn][moveapawn]>19:playerPawnSizes[who_turn][moveapawn]-=2
                        if abs(playerPawnSizes[who_turn][moveapawn]-19)<2:playerPawnSizes[who_turn][moveapawn]=19

                        if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]:
                            playerspos[who_turn][moveapawn][0]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]:
                            playerspos[who_turn][moveapawn][0]-=2
                        if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0])<2:
                            playerspos[who_turn][moveapawn][0]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]

                        if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            playerspos[who_turn][moveapawn][1]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            playerspos[who_turn][moveapawn][1]-=2
                        if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1])<2:
                            playerspos[who_turn][moveapawn][1]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]
                        
                        if beginafterthis==1 and playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0] and playerspos[who_turn][moveapawn][1]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]]=[1,1,0,0]
                    elif 2<=noOf1<4:
                        for i in range(4):
                            if pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][i]==0:
                                destinationInHomeTrack=i
                                break
                        if playerPawnSizes[who_turn][moveapawn]>19:playerPawnSizes[who_turn][moveapawn]-=2
                        if abs(playerPawnSizes[who_turn][moveapawn]-19)<2:playerPawnSizes[who_turn][moveapawn]=19

                        if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]:
                            playerspos[who_turn][moveapawn][0]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]:
                            playerspos[who_turn][moveapawn][0]-=2
                        if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][0]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0])<2:
                            playerspos[who_turn][moveapawn][0]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0]

                        if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]<homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            playerspos[who_turn][moveapawn][1]+=2
                        elif playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][1]>homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            playerspos[who_turn][moveapawn][1]-=2
                        if playerPawnSizes[who_turn][moveapawn]==19 and abs(playerspos[who_turn][moveapawn][1]-homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1])<2:
                            playerspos[who_turn][moveapawn][1]=homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]
                        
                        if playerPawnSizes[who_turn][moveapawn]==19 and playerspos[who_turn][moveapawn][0]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0] and playerspos[who_turn][moveapawn][1]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1]:
                            pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack]=1

            if inHomeTrack[who_turn][moveapawn]==0 and someoneGonnaDie==1 and playerspos[who_turn][moveapawn][0]==allBoxPositions[playerpresentbox[moveapawn]-1][0] and playerspos[who_turn][moveapawn][1]==allBoxPositions[playerpresentbox[moveapawn]-1][1] and someoneGotKilled==[]:
                for i in range(1+max(1,gamedet['game mode'])):
                    if i!=who_turn:
                        for j in range(4):
                            if (playersboxtrack[i][j] not in safestarboxes and inHomeTrack[i][j]==0) and playersboxtrack[i][j]==playerpresentbox[moveapawn]:
                                someoneGotKilled.append([i,j])
                                turnForKill=1
                                if killerstop==0:
                                    killerstop=1
                
                if killerstop==1:
                    killerstop=2
                    GAME_SOUNDS['stopreached'].play()

            if someoneGotKilled!=[]:
                checkercount=0
                for j in range(len(someoneGotKilled)):
                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]<38:playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]+=3
                    if abs(playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]-38)<3:playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]=38
                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]<allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][0]:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]+=2
                    elif playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]>allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][0]:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]-=2
                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and abs(playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]-allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][0])<2:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]=allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][0]

                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]<allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][1]:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]+=2
                    elif playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]>allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][1]:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]-=2
                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and abs(playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]-allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][1])<2:
                        playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]=allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][1]

                    if playerPawnSizes[someoneGotKilled[j][0]][someoneGotKilled[j][1]]==38 and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][0]==allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][0] and playerspos[someoneGotKilled[j][0]][someoneGotKilled[j][1]][1]==allhomepos[gamedet['chosen colours'][someoneGotKilled[j][0]]][someoneGotKilled[j][1]][1]:
                        playerspawns[someoneGotKilled[j][0]][someoneGotKilled[j][1]]=0
                        playersboxtrack[someoneGotKilled[j][0]][someoneGotKilled[j][1]]=0
                        inHomeTrack[someoneGotKilled[j][0]][someoneGotKilled[j][1]]=0
                        checkercount+=1
                if checkercount==len(someoneGotKilled):
                    someoneGotKilled.clear()
            
            if inHomeTrack[who_turn][moveapawn]==0 and playerpresentbox[moveapawn] not in safestarboxes and someoneGotKilled==[] and ((destinationInNormalBox==0 and ( (pawnsInNormalBox[playerpresentbox[moveapawn]]==[1,0,0,0] and playerspos[who_turn][moveapawn][0]==allBoxPositions[playerpresentbox[moveapawn]-1][0] and playerspos[who_turn][moveapawn][1]==allBoxPositions[playerpresentbox[moveapawn]-1][1]) or (playerspos[who_turn][moveapawn][0]==normalboxpos4[playerpresentbox[moveapawn]][0][0] and playerspos[who_turn][moveapawn][1]==normalboxpos4[playerpresentbox[moveapawn]][0][1]) )) or (destinationInNormalBox>0 and playerspos[who_turn][moveapawn][0]==normalboxpos4[playerpresentbox[moveapawn]][destinationInNormalBox][0] and playerspos[who_turn][moveapawn][1]==normalboxpos4[playerpresentbox[moveapawn]][destinationInNormalBox][1])):
                for i in range(4):
                    playersboxtrack[who_turn][i]=playerpresentbox[i]
                moveapawn=-10
                moveOrActivate=0
                pawnactivated=[-1,-1,-1,-1]
                postDepCheckInSSBox=1
                postDepCheckInNormalBox=1
                diceroll=2
                destinationInSSBox=-10
                destinationInNormalBox=-10
            elif inHomeTrack[who_turn][moveapawn]==0 and playerpresentbox[moveapawn] in safestarboxes and someoneGotKilled==[] and ((destinationInSSBox==0 and ( (pawnsInSSBox[playerpresentbox[moveapawn]]==[1,0,0,0] and playerspos[who_turn][moveapawn][0]==allBoxPositions[playerpresentbox[moveapawn]-1][0] and playerspos[who_turn][moveapawn][1]==allBoxPositions[playerpresentbox[moveapawn]-1][1]) or (playerspos[who_turn][moveapawn][0]==SSboxpos4[playerpresentbox[moveapawn]][0][0] and playerspos[who_turn][moveapawn][1]==SSboxpos4[playerpresentbox[moveapawn]][0][1]) ) ) or (destinationInSSBox>0 and playerspos[who_turn][moveapawn][0]==SSboxpos4[playerpresentbox[moveapawn]][destinationInSSBox][0] and playerspos[who_turn][moveapawn][1]==SSboxpos4[playerpresentbox[moveapawn]][destinationInSSBox][1])):
                for i in range(4):
                    playersboxtrack[who_turn][i]=playerpresentbox[i]
                moveapawn=-10
                moveOrActivate=0
                pawnactivated=[-1,-1,-1,-1]
                postDepCheckInSSBox=1
                postDepCheckInNormalBox=1
                diceroll=2
                destinationInSSBox=-10
                destinationInNormalBox=-10
            elif 0<inHomeTrack[who_turn][moveapawn]<6 and ((destinationInHomeTrack==0 and pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]]==[1,0,0,0] and playerspos[who_turn][moveapawn][0]==homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][0] and playerspos[who_turn][moveapawn][1]==homecoming[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][1]) or (destinationInHomeTrack>=0 and (destinationInHomeTrack!=0 or pawnsInHomeTrack[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]]!=[1,0,0,0]) and playerspos[who_turn][moveapawn][0]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][0] and playerspos[who_turn][moveapawn][1]==homecomingpos4[gamedet['chosen colours'][who_turn]][-1+inHomeTrack[who_turn][moveapawn]][destinationInHomeTrack][1])):
                for i in range(4):
                    playersboxtrack[who_turn][i]=playerpresentbox[i]
                moveapawn=-10
                moveOrActivate=0
                pawnactivated=[-1,-1,-1,-1]
                destinationInHomeTrack=-10
                postDepCheckInHomeTrack=1
                diceroll=2
            elif inHomeTrack[who_turn][moveapawn]==6 and playerspos[who_turn][moveapawn][0]==homecoming[gamedet['chosen colours'][who_turn]][5][0] and playerspos[who_turn][moveapawn][1]==homecoming[gamedet['chosen colours'][who_turn]][5][1]:
                someoneCameHome=1
                for i in range(4):
                    playersboxtrack[who_turn][i]=playerpresentbox[i]
                moveapawn=-10
                moveOrActivate=0
                pawnactivated=[-1,-1,-1,-1]
                destinationInHomeTrack=-10
                postDepCheckInHomeTrack=1
                diceroll=2
            
        for item in range(len(gamedet['chosen colours'])):
            if(gamedet['chosen colours'][item]=='red'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['red'][5][0] or playerspos[item][i][1]!=homecoming['red'][5][1]:
                            SCREEN.blit(pygame.transform.scale(reds[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
                        else:
                            playerInHome[item][i]=1
            elif(gamedet['chosen colours'][item]=='yellow'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['yellow'][5][0] or playerspos[item][i][1]!=homecoming['yellow'][5][1]:
                            SCREEN.blit(pygame.transform.scale(yellows[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
                        else:
                            playerInHome[item][i]=1
            elif(gamedet['chosen colours'][item]=='blue'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['blue'][5][0] or playerspos[item][i][1]!=homecoming['blue'][5][1]:
                            SCREEN.blit(pygame.transform.scale(blues[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
                        else:
                            playerInHome[item][i]=1
            elif(gamedet['chosen colours'][item]=='green'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['green'][5][0] or playerspos[item][i][1]!=homecoming['green'][5][1]:
                            SCREEN.blit(pygame.transform.scale(greens[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
                        else:
                            playerInHome[item][i]=1
        
        if someoneGotKilled!=[]:
            for i in range(len(someoneGotKilled)):
                if gamedet['chosen colours'][someoneGotKilled[i][0]]=='red':
                    SCREEN.blit(pygame.transform.scale(reds[someoneGotKilled[i][1]],(playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]],playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]])),(playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][0],playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][1]))
                elif gamedet['chosen colours'][someoneGotKilled[i][0]]=='yellow':
                    SCREEN.blit(pygame.transform.scale(yellows[someoneGotKilled[i][1]],(playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]],playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]])),(playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][0],playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][1]))
                elif gamedet['chosen colours'][someoneGotKilled[i][0]]=='blue':
                    SCREEN.blit(pygame.transform.scale(blues[someoneGotKilled[i][1]],(playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]],playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]])),(playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][0],playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][1]))
                elif gamedet['chosen colours'][someoneGotKilled[i][0]]=='green':
                    SCREEN.blit(pygame.transform.scale(greens[someoneGotKilled[i][1]],(playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]],playerPawnSizes[someoneGotKilled[i][0]][someoneGotKilled[i][1]])),(playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][0],playerspos[someoneGotKilled[i][0]][someoneGotKilled[i][1]][1]))

        if moveOrActivate==1 and who_turn>=0 and pawnactivated[who_turn]!=-1:
            if gamedet['chosen colours'][who_turn]=='red':
                SCREEN.blit(pygame.transform.scale(reds[pawnactivated[who_turn]],(playerPawnSizes[who_turn][pawnactivated[who_turn]],playerPawnSizes[who_turn][pawnactivated[who_turn]])),(playerspos[who_turn][pawnactivated[who_turn]][0],playerspos[who_turn][pawnactivated[who_turn]][1]))
            if gamedet['chosen colours'][who_turn]=='yellow':
                SCREEN.blit(pygame.transform.scale(yellows[pawnactivated[who_turn]],(playerPawnSizes[who_turn][pawnactivated[who_turn]],playerPawnSizes[who_turn][pawnactivated[who_turn]])),(playerspos[who_turn][pawnactivated[who_turn]][0],playerspos[who_turn][pawnactivated[who_turn]][1]))
            if gamedet['chosen colours'][who_turn]=='blue':
                SCREEN.blit(pygame.transform.scale(blues[pawnactivated[who_turn]],(playerPawnSizes[who_turn][pawnactivated[who_turn]],playerPawnSizes[who_turn][pawnactivated[who_turn]])),(playerspos[who_turn][pawnactivated[who_turn]][0],playerspos[who_turn][pawnactivated[who_turn]][1]))
            if gamedet['chosen colours'][who_turn]=='green':
                SCREEN.blit(pygame.transform.scale(greens[pawnactivated[who_turn]],(playerPawnSizes[who_turn][pawnactivated[who_turn]],playerPawnSizes[who_turn][pawnactivated[who_turn]])),(playerspos[who_turn][pawnactivated[who_turn]][0],playerspos[who_turn][pawnactivated[who_turn]][1]))
        if moveOrActivate==2 and who_turn>=0 and moveapawn!=-1:
            if gamedet['chosen colours'][who_turn]=='red':
                SCREEN.blit(pygame.transform.scale(reds[moveapawn],(playerPawnSizes[who_turn][moveapawn],playerPawnSizes[who_turn][moveapawn])),(playerspos[who_turn][moveapawn][0],playerspos[who_turn][moveapawn][1]))
            if gamedet['chosen colours'][who_turn]=='yellow':
                SCREEN.blit(pygame.transform.scale(yellows[moveapawn],(playerPawnSizes[who_turn][moveapawn],playerPawnSizes[who_turn][moveapawn])),(playerspos[who_turn][moveapawn][0],playerspos[who_turn][moveapawn][1]))
            if gamedet['chosen colours'][who_turn]=='blue':
                SCREEN.blit(pygame.transform.scale(blues[moveapawn],(playerPawnSizes[who_turn][moveapawn],playerPawnSizes[who_turn][moveapawn])),(playerspos[who_turn][moveapawn][0],playerspos[who_turn][moveapawn][1]))
            if gamedet['chosen colours'][who_turn]=='green':
                SCREEN.blit(pygame.transform.scale(greens[moveapawn],(playerPawnSizes[who_turn][moveapawn],playerPawnSizes[who_turn][moveapawn])),(playerspos[who_turn][moveapawn][0],playerspos[who_turn][moveapawn][1]))
        
        if playerInHome[who_turn]==[1,1,1,1]:
            winner=who_turn
            if gamedet['game mode']==0 and winner==0:
                GAME_SOUNDS['compwins'].play()
            if gamedet['game mode']==0 and winner==1:
                GAME_SOUNDS['playerwins'].play()
            if gamedet['game mode']>0:
                GAME_SOUNDS['playerwins'].play()
            break

        if t!=5 and turnForKill==0 and someoneCameHome==0 and (nothingHappened>=135 or diceroll==2) and CHECKIFCORRECT==0: # <-- conditions to be added here, like pawn kill
            who_turn+=1
            killerstop=0
            if diceroll==2:
                GAME_SOUNDS['stopreached'].play()
            t=-1
            diceposx=DICEPOS[0][0]
            diceposy=DICEPOS[0][1]
            nothingHappened=0
            diceroll=0
            moveOrActivate=0
            computerRolls=0
            if(gamedet['game mode']==0 and who_turn==2):
                who_turn=0
            elif(gamedet['game mode']!=0 and who_turn==1+gamedet['game mode']):
                who_turn=0
        elif (t==5 or someoneCameHome==1 or turnForKill==1) and (nothingHappened>=135 or diceroll==2) and CHECKIFCORRECT==0:
            killerstop=0
            if someoneCameHome==1:
                GAME_SOUNDS['pawnsenthome'][random.randint(0,-1+len(GAME_SOUNDS['pawnsenthome']))].play()
            elif turnForKill==1:
                GAME_SOUNDS['pawnkilled'][random.randint(0,-1+len(GAME_SOUNDS['pawnkilled']))].play()
            elif diceroll==2:
                GAME_SOUNDS['stopreached'].play()
            someoneCameHome=0
            turnForKill=0
            someoneGonnaDie=0
            t=-1
            diceposx=DICEPOS[0][0]
            diceposy=DICEPOS[0][1]
            nothingHappened=0
            diceroll=0
            moveOrActivate=0
            computerRolls=0
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    loopcounter=0
    colourcounter=0
    ludoexitbutton=GAME_SPRITES['ludoexit'][0]
    newgamebutton=GAME_SPRITES['newgame'][0]
    while True:
        loopcounter+=1
        SCREEN.blit(bgimg,(0,0))
        SCREEN.blit(ldname,(355,-20))
        SCREEN.blit(myname,(625,20))
        SCREEN.blit(ldboard,(410,87))
        SCREEN.blit(pygame.transform.scale(GAME_SPRITES['ludonote'],(280,170.5)),(1155,591))

        SCREEN.blit(modpick,(30,20))
        mods=GAME_SPRITES['gamemod']
        SCREEN.blit(mods[0][0],(30,77))
        SCREEN.blit(mods[1][0],(30,136))
        SCREEN.blit(mods[2][0],(30,195))
        SCREEN.blit(mods[3][0],(30,254))
        
        if gamedet['game mode']==0:
            SCREEN.blit(mods[0][1],(30,77))
        elif gamedet['game mode']==1:
            SCREEN.blit(mods[1][1],(30,136))
        elif gamedet['game mode']==2:
            SCREEN.blit(mods[2][1],(30,195))
        elif gamedet['game mode']==3:
            SCREEN.blit(mods[3][1],(30,254))

        SCREEN.blit(colpick,(25,510))
        if 'red' in gamedet['chosen colours']:
            SCREEN.blit(redopt[1],(35,578))
        else:
            SCREEN.blit(redopt[2],(35,578))
        if 'yellow' in gamedet['chosen colours']:
            SCREEN.blit(yellowopt[1],(35,632))
        else:
            SCREEN.blit(yellowopt[2],(35,632))
        if 'blue' in gamedet['chosen colours']:
            SCREEN.blit(blueopt[1],(175,578))
        else:
            SCREEN.blit(blueopt[2],(175,578))
        if 'green' in gamedet['chosen colours']:
            SCREEN.blit(greenopt[1],(175,632))
        else:
            SCREEN.blit(greenopt[2],(175,632))

        SCREEN.blit(turn,(65,355))
        # place winner in place of who_turn
        if gamedet['game mode']==0:
            SCREEN.blit(whosturn[winner],(30,422))
            if winner==1:SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][winner]],(240,424))
            else: SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][winner]],(281,424))
        elif gamedet['game mode']!=0:
            SCREEN.blit(whosturn[1+winner],(30,422))
            if winner==0:SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][winner]],(240,424))
            else: SCREEN.blit(GAME_SPRITES['colturn'][gamedet['chosen colours'][winner]],(245,424))

        if gamedet['game mode']==0 and winner==0: # in computer's turn, all buttons are shown disabled
            SCREEN.blit(roll[2],(1160,375))
            SCREEN.blit(activate[2],(1310,375))
            SCREEN.blit(movpawns[0][2],(1160,445))
            SCREEN.blit(movpawns[1][2],(1310,445))
            SCREEN.blit(movpawns[2][2],(1160,515))
            SCREEN.blit(movpawns[3][2],(1310,515))
        else:
            SCREEN.blit(roll[2],(1160,375))

            SCREEN.blit(activate[2],(1310,375))
            
            SCREEN.blit(movpawns[0][2],(1160,445))
            SCREEN.blit(movpawns[1][2],(1310,445))
            SCREEN.blit(movpawns[2][2],(1160,515))
            SCREEN.blit(movpawns[3][2],(1310,515))

        SCREEN.blit(dice,(1205,50))
        SCREEN.blit(start_button[1],(1230,270))
        SCREEN.blit(pygame.transform.rotate(diceroller,90),(1150,135))

        for item in range(len(gamedet['chosen colours'])):
            if(gamedet['chosen colours'][item]=='red'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['red'][5][0] or playerspos[item][i][1]!=homecoming['red'][5][1]:
                            SCREEN.blit(pygame.transform.scale(reds[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
            elif(gamedet['chosen colours'][item]=='yellow'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['yellow'][5][0] or playerspos[item][i][1]!=homecoming['yellow'][5][1]:
                            SCREEN.blit(pygame.transform.scale(yellows[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
            elif(gamedet['chosen colours'][item]=='blue'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['blue'][5][0] or playerspos[item][i][1]!=homecoming['blue'][5][1]:
                            SCREEN.blit(pygame.transform.scale(blues[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))
            elif(gamedet['chosen colours'][item]=='green'):
                for i in range(4):
                    if inHomeTrack[item][i]<=6:
                        if playerspos[item][i][0]!=homecoming['green'][5][0] or playerspos[item][i][1]!=homecoming['green'][5][1]:
                            SCREEN.blit(pygame.transform.scale(greens[i],(playerPawnSizes[item][i],playerPawnSizes[item][i])),(playerspos[item][i][0],playerspos[item][i][1]))

        if gamedet['game mode']==0 and winner==0:
            SCREEN.blit(GAME_SPRITES['compwin'][colourcounter],(392,185))
        elif gamedet['game mode']==0:
            SCREEN.blit(GAME_SPRITES['player1win'][colourcounter],(392,185))
        elif gamedet['game mode']!=0:
            if winner==0:
                SCREEN.blit(GAME_SPRITES['player1win'][colourcounter],(392,185))
            if winner==1:
                SCREEN.blit(GAME_SPRITES['player2win'][colourcounter],(392,185))
            if winner==2:
                SCREEN.blit(GAME_SPRITES['player3win'][colourcounter],(392,185))
            if winner==3:
                SCREEN.blit(GAME_SPRITES['player4win'][colourcounter],(392,185))

        if loopcounter>=15:
            loopcounter=0
            colourcounter+=1
            if colourcounter==4:colourcounter=0

        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            x,y=pygame.mouse.get_pos()
            clic=pygame.mouse.get_pressed()
            if 627<=x<=877 and 405<=y<=471 and clic[0]:
                GAME_SOUNDS['buttonclick'].play()
                if gamedet['game mode']==0 and winner==0:
                    GAME_SOUNDS['compwins'].stop()
                else:GAME_SOUNDS['playerwins'].stop()
                return 1
            elif 627<=x<=877 and 405<=y<=471:
                newgamebutton=GAME_SPRITES['newgame'][1]
            else:
                newgamebutton=GAME_SPRITES['newgame'][0]
            if 627<=x<=877 and 520<=y<=586 and clic[0]:
                GAME_SOUNDS['buttonclick'].play()
                pygame.quit()
                sys.exit()
            elif 627<=x<=877 and 520<=y<=586:
                ludoexitbutton=GAME_SPRITES['ludoexit'][1]
            else:
                ludoexitbutton=GAME_SPRITES['ludoexit'][0]
        
        SCREEN.blit(newgamebutton,(627,405))
        SCREEN.blit(ludoexitbutton,(627,520))
        pygame.display.update()
        FPSCLOCK.tick(FPS) # game is running at 30 fps

if __name__=='__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('Ludo Game by Neelangshu Roy')
    pygame.display.set_icon(pygame.image.load('ludo_icon.png'))
    GAME_SPRITES['background']=pygame.image.load('Game sprites/ludo background.jpg').convert_alpha()
    GAME_SPRITES['gameboard']=pygame.image.load('Game sprites/Ludo board.png').convert_alpha()
    GAME_SPRITES['dice_roller']=pygame.image.load('Game sprites/dice roller.png').convert_alpha()
    GAME_SPRITES['colpick']=pygame.image.load('Game sprites/colpick.png').convert_alpha()
    GAME_SPRITES['modpick']=pygame.image.load('Game sprites/modpick.png').convert_alpha()
    GAME_SPRITES['rotator']=pygame.image.load('Game sprites/rotator.png').convert_alpha()
    GAME_SPRITES['dice']=(
    pygame.image.load('Game sprites/dice 1.png').convert_alpha(),
    pygame.image.load('Game sprites/dice 2.png').convert_alpha(),
    pygame.image.load('Game sprites/dice 3.png').convert_alpha(),
    pygame.image.load('Game sprites/dice 4.png').convert_alpha(),
    pygame.image.load('Game sprites/dice 5.png').convert_alpha(),
    pygame.image.load('Game sprites/dice 6.png').convert_alpha()       
    )
    GAME_SPRITES['start']=(
        pygame.image.load('Game sprites/start_button.png').convert_alpha(),
        pygame.image.load('Game sprites/start_clicked.png').convert_alpha()
    )
    GAME_SPRITES['red_opt']=(
        pygame.image.load('Game sprites/red_opt.png').convert_alpha(),
        pygame.image.load('Game sprites/red_opt_selected.png').convert_alpha(),
        pygame.image.load('Game sprites/red_opt_disabled.png').convert_alpha()
    )
    GAME_SPRITES['yellow_opt']=(
        pygame.image.load('Game sprites/yellow_opt.png').convert_alpha(),
        pygame.image.load('Game sprites/yellow_opt_selected.png').convert_alpha(),
        pygame.image.load('Game sprites/yellow_opt_disabled.png').convert_alpha()
    )
    GAME_SPRITES['blue_opt']=(
        pygame.image.load('Game sprites/blue_opt.png').convert_alpha(),
        pygame.image.load('Game sprites/blue_opt_selected.png').convert_alpha(),
        pygame.image.load('Game sprites/blue_opt_disabled.png').convert_alpha()
    )
    GAME_SPRITES['green_opt']=(
        pygame.image.load('Game sprites/green_opt.png').convert_alpha(),
        pygame.image.load('Game sprites/green_opt_selected.png').convert_alpha(),
        pygame.image.load('Game sprites/green_opt_disabled.png').convert_alpha()
    )
    GAME_SPRITES['colturn']={
        'red': pygame.image.load('Game sprites/red pawn with turn.png').convert_alpha(),
        'yellow': pygame.image.load('Game sprites/yellow pawn with turn.png').convert_alpha(),
        'blue': pygame.image.load('Game sprites/blue pawn with turn.png').convert_alpha(),
        'green': pygame.image.load('Game sprites/green pawn with turn.png').convert_alpha()
    }

    GAME_SPRITES['redpawn']=(
    pygame.image.load('Game sprites/red pawn 101.png').convert_alpha(),
    pygame.image.load('Game sprites/red pawn 102.png').convert_alpha(),
    pygame.image.load('Game sprites/red pawn 103.png').convert_alpha(),
    pygame.image.load('Game sprites/red pawn 104.png').convert_alpha()
    )
    GAME_SPRITES['yellowpawn']=(
    pygame.image.load('Game sprites/yellow pawn 101.png').convert_alpha(),
    pygame.image.load('Game sprites/yellow pawn 102.png').convert_alpha(),
    pygame.image.load('Game sprites/yellow pawn 103.png').convert_alpha(),
    pygame.image.load('Game sprites/yellow pawn 104.png').convert_alpha()
    )
    GAME_SPRITES['bluepawn']=(
    pygame.image.load('Game sprites/blue pawn 101.png').convert_alpha(),
    pygame.image.load('Game sprites/blue pawn 102.png').convert_alpha(),
    pygame.image.load('Game sprites/blue pawn 103.png').convert_alpha(),
    pygame.image.load('Game sprites/blue pawn 104.png').convert_alpha()
    )
    GAME_SPRITES['greenpawn']=(
    pygame.image.load('Game sprites/green pawn 101.png').convert_alpha(),
    pygame.image.load('Game sprites/green pawn 102.png').convert_alpha(),
    pygame.image.load('Game sprites/green pawn 103.png').convert_alpha(),
    pygame.image.load('Game sprites/green pawn 104.png').convert_alpha()
    )
    GAME_SPRITES['player1win']=(
        pygame.image.load('Game sprites/ludopl1_win_red.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl1_win_yellow.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl1_win_blue.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl1_win_green.png').convert_alpha()
    )
    GAME_SPRITES['player2win']=(
        pygame.image.load('Game sprites/ludopl2_win_red.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl2_win_yellow.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl2_win_blue.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl2_win_green.png').convert_alpha()
    )
    GAME_SPRITES['player3win']=(
        pygame.image.load('Game sprites/ludopl3_win_red.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl3_win_yellow.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl3_win_blue.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl3_win_green.png').convert_alpha()
    )
    GAME_SPRITES['player4win']=(
        pygame.image.load('Game sprites/ludopl4_win_red.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl4_win_yellow.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl4_win_blue.png').convert_alpha(),
        pygame.image.load('Game sprites/ludopl4_win_green.png').convert_alpha()
    )
    GAME_SPRITES['compwin']=(
        pygame.image.load('Game sprites/ludocompwin_red.png').convert_alpha(),
        pygame.image.load('Game sprites/ludocompwin_yellow.png').convert_alpha(),
        pygame.image.load('Game sprites/ludocompwin_blue.png').convert_alpha(),
        pygame.image.load('Game sprites/ludocompwin_green.png').convert_alpha()
    )
    GAME_SPRITES['ludoexit']=(
        pygame.image.load('Game sprites/ludoexit.png').convert_alpha(),
        pygame.image.load('Game sprites/ludoexit_clicked.png').convert_alpha()
    )
    GAME_SPRITES['newgame']=(
        pygame.image.load('Game sprites/ludo_newgame.png').convert_alpha(),
        pygame.image.load('Game sprites/ludo_newgame_clicked.png').convert_alpha()
    )
    GAME_SPRITES['gamemod']=(
    (
        pygame.image.load('Game sprites/gamemod1.png').convert_alpha(),
        pygame.image.load('Game sprites/modesel1.png').convert_alpha()
    ),
    (
        pygame.image.load('Game sprites/gamemod2.png').convert_alpha(),
        pygame.image.load('Game sprites/modesel2.png').convert_alpha()
    ),
    (
        pygame.image.load('Game sprites/gamemod3.png').convert_alpha(),
        pygame.image.load('Game sprites/modesel3.png').convert_alpha()
    ),
    (
        pygame.image.load('Game sprites/gamemod4.png').convert_alpha(),
        pygame.image.load('Game sprites/modesel4.png').convert_alpha()
    )
    )
    GAME_SPRITES['gameturn']=pygame.image.load('Game sprites/gameturn.png').convert_alpha()
    GAME_SPRITES['ludonote']=pygame.image.load('Game sprites/ludonote.png').convert_alpha()
    GAME_SPRITES['whosturn']=(
        pygame.image.load('Game sprites/compturn.png').convert_alpha(),
        pygame.image.load('Game sprites/play1turn.png').convert_alpha(),
        pygame.image.load('Game sprites/play2turn.png').convert_alpha(),
        pygame.image.load('Game sprites/play3turn.png').convert_alpha(),
        pygame.image.load('Game sprites/play4turn.png').convert_alpha()
    )

    GAME_SPRITES['ludoname']=pygame.image.load('Game sprites/ludo name.png').convert_alpha()
    GAME_SPRITES['myname']=pygame.image.load('Game sprites/my_name.png').convert_alpha()
    GAME_SPRITES['dicelabel']=pygame.image.load('Game sprites/dice.png').convert_alpha()
    GAME_SPRITES['roll']=(
        pygame.image.load('Game sprites/roll.png').convert_alpha(),
        pygame.image.load('Game sprites/roll_click.png').convert_alpha(),
        pygame.image.load('Game sprites/roll_disabled.png').convert_alpha()
    )
    GAME_SPRITES['activate']=(
        pygame.image.load('Game sprites/activate.png').convert_alpha(),
        pygame.image.load('Game sprites/activate_click.png').convert_alpha(),
        pygame.image.load('Game sprites/activate_disabled.png').convert_alpha()
    )
    GAME_SPRITES['movepawns']=(
        (
            pygame.image.load('Game sprites/movpawn1.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn1_click.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn1_disabled.png').convert_alpha()
        ),
        (
            pygame.image.load('Game sprites/movpawn2.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn2_click.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn2_disabled.png').convert_alpha()
        ),
        (
            pygame.image.load('Game sprites/movpawn3.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn3_click.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn3_disabled.png').convert_alpha()
        ),
        (
            pygame.image.load('Game sprites/movpawn4.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn4_click.png').convert_alpha(),
            pygame.image.load('Game sprites/movpawn4_disabled.png').convert_alpha()
        )
    )
    GAME_SOUNDS['welcome']=pygame.mixer.Sound('Game sounds/opening sound.mp3')
    GAME_SOUNDS['stopreached']=pygame.mixer.Sound('Game sounds/stopreached.wav')

    GAME_SOUNDS['startbuttonclick']=pygame.mixer.Sound('Game sounds/gamestart buttonclick.wav')
    GAME_SOUNDS['buttonclick']=pygame.mixer.Sound('Game sounds/buttonclick.wav')
    GAME_SOUNDS['clickbaitsound']=pygame.mixer.Sound('Game sounds/clickbaitsound.wav')
    
    GAME_SOUNDS['playerwins']=pygame.mixer.Sound('Game sounds/playerwins.mp3')
    GAME_SOUNDS['compwins']=pygame.mixer.Sound('Game sounds/computerwins.mp3')
    
    GAME_SOUNDS['activation']=[
        pygame.mixer.Sound('Game sounds/activation1.mp3'),
        pygame.mixer.Sound('Game sounds/activation2.mp3'),
        pygame.mixer.Sound('Game sounds/activation3.mp3')
    ]
    GAME_SOUNDS['pawnsenthome']=[
        pygame.mixer.Sound('Game sounds/pawnsenthome1.mp3'),
        pygame.mixer.Sound('Game sounds/pawnsenthome2.mp3')
    ]
    GAME_SOUNDS['pawnkilled']=[
        pygame.mixer.Sound('Game sounds/pawnkilled1.mp3'),
        pygame.mixer.Sound('Game sounds/pawnkilled2.mp3'),
        pygame.mixer.Sound('Game sounds/pawnkilled3.mp3')
    ]
    RED_HOME=[
        [1291-360,138+37],[1248-360,181+37],[1334-360,181+37],[1291-360,225+37]
    ] # 389px differences
    GREEN_HOME=[
        [902-360,138+37],[859-360,181+37],[945-360,181+37],[902-360,225+37]
    ]
    YELLOW_HOME=[
        [902-360,527+37],[859-360,570+37],[945-360,570+37],[902-360,614+37]
    ]
    BLUE_HOME=[
        [1291-360,527+37],[1248-360,570+37],[1334-360,570+37],[1291-360,614+37]
    ]
    GREEN_STARTPOS=[837-360,332+38] # 477,370 -> 837, 369
    RED_STARTPOS=[1140-361,117+37] # 779,154 -> 780,154
    YELLOW_STARTPOS=[1053-360,635+37] # 693,672 -> 693, 672
    BLUE_STARTPOS=[1355-360,419+37] # 995,456 -> 995, 456
    DICEPOS=((1245,143),(1345,143))
    retval=1
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['welcome'],0.85)
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['clickbaitsound'],0.20)
    GAME_SOUNDS['welcome'].play()
    while retval==1:
        gamedet=roll()
        retval=gamestart(gamedet)