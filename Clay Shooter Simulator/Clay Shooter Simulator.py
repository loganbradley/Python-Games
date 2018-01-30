from math import *
from graphics import *
from time import sleep
from random import randint, choice
import os
# project3.py
# Team: Ariya Lau, Yunshu Cai, and Logan Bradley-Trietsch
# Description: This program can allow the user to change certain values that,
#   in turn, affect a function that animates circles. The round number and
#   score are displayed. Top scores are saved to top_scores.txt.
# Purpose: This program simulates a clay shooter. The user can adjust the
#   difficulty of the game by adjusting the parameters. Features were
#   added to improve the functionality and fun of the game.
# Function: This program utilizes several functions in order to have clean,
#   easily-readable code, and also to facilitate the utility of the program.


# Display scores text
def score_display(win,num_names_displayed,start_rank,high_scores_txt):
    try:
        if high_scores_txt!=None:
            if num_names_displayed==2:
                high_scores_txt.undraw()
            else:
                for i in high_scores_txt:
                    i.undraw()
    except:
        pass
    # Open top scores file and store contents in a list
    high_scores_file=open("top_scores.txt","r")
    high_scores=high_scores_file.readlines()
    # Remove '\n'
    i=0
    while i<(len(high_scores)):
        if high_scores[i]=="\n":
            high_scores=high_scores.remove("\n")
        high_scores[i]=high_scores[i].replace("\n",'')
        i+=1
    high_scores_txt_lst=[]
    # Convert highscores into text objects and draw them on window
    try:
        if num_names_displayed==1:
            high_scores_txt_lst=Text(Point(160,470),high_scores[2])
            high_scores_txt_lst.draw(win)
        elif num_names_displayed<3:
            for i in range(2,num_names_displayed+2):
                high_scores_txt=Text(Point(160,450+(i-2)*20),high_scores[i])
                high_scores_txt.draw(win)
                high_scores_txt_lst.append(high_scores_txt)
        elif len(high_scores)<5:
            for i in range(len(high_scores)-2):
                high_scores_txt=Text(Point(160,430+(i)*20),high_scores[i+2])
                high_scores_txt.draw(win)
                high_scores_txt_lst.append(high_scores_txt)            
        else:
            for i in range(3):
                high_scores_txt=Text(Point(160,430+(i)*20),high_scores[start_rank+1+i])
                high_scores_txt.draw(win)
                high_scores_txt_lst.append(high_scores_txt)
    except IndexError:
        pass  
    return high_scores_txt_lst,len(high_scores)

# Scroll arrow movement
def move_scroll(win,msg_up,msg_down,start_rank,num_names_displayed,
                len_highscores):
    # Check if messages up or down button clicked
    points=[Point(365.0, 445.0), Point(365.0, 465.0),
            Point(355.0, 465.0), Point(372.5, 480.0), Point(390.0, 465.0),
            Point(380.0, 465.0), Point(380.0, 445.0)]
    arrow_down_points=msg_down.getPoints()
    # if the scroll reaches the bottom of the list and the there are 3 highscore records 
    if start_rank==len_highscores-4 and len_highscores==6:
        # move the up scroll arrow down to illustrate to the user that the
        #  scroll display reached the bottom
        msg_up.undraw()
        msg_up=Polygon(Point(365,440),Point(365,420),Point(355,420),Point(372.5,405),Point(390,420),Point(380,420),Point(380,440))
        msg_up.move(0,15)
        msg_up.draw(win)
        msg_up.setFill('black')
        msg_down.undraw()
        msg_down=Polygon(Point(365,460),Point(365,480),Point(355,480),Point(372.5,495),Point(390,480),Point(380,480),Point(380,460))
        msg_down.setFill("black")
        msg_down.draw(win)
    # if the scroll reaches the bottom of the list 
    elif start_rank==len_highscores-4:
        # move the up scroll arrow down to illustrate to the user that the
        #  scroll display reached the bottom
        msg_up.undraw()
        msg_up=Polygon(Point(365,440),Point(365,420),Point(355,420),Point(372.5,405),Point(390,420),Point(380,420),Point(380,440))
        msg_up.move(0,15)
        msg_up.draw(win)
        msg_up.setFill('black')
    # if there are less than 3 records displayed 
    elif num_names_displayed==2:
        # move the down arrow up to illustrate to the user that the they
        #  cannot scroll up
        msg_down.move(0,-15)
    # if there are less than 3 records displayed 
    elif start_rank==1:
        # move the down arrow up to illustrate to the user that the they
        #  cannot scroll up
        msg_down.undraw()
        msg_down=Polygon(Point(365,460),Point(365,480),Point(355,480),Point(372.5,495),Point(390,480),Point(380,480),Point(380,460))
        msg_down.setFill("black")
        msg_down.move(0,-15)
        msg_down.draw(win)
        msg_up.undraw()
        msg_up=Polygon(Point(365,440),Point(365,420),Point(355,420),Point(372.5,405),Point(390,420),Point(380,420),Point(380,440))
        msg_up.draw(win)
        msg_up.setFill('black')
    # arrows are in default position if there are 3 records on display
    elif num_names_displayed<3:
        pass
    else:
        msg_up.undraw()
        msg_down.undraw()
        msg_up=Polygon(Point(365,440),Point(365,420),Point(355,420),Point(372.5,405),Point(390,420),Point(380,420),Point(380,440))
        msg_down=Polygon(Point(365,460),Point(365,480),Point(355,480),Point(372.5,495),Point(390,480),Point(380,480),Point(380,460))
        msg_up.setFill("black")
        msg_down.setFill("black")
        msg_up.draw(win)
        msg_down.draw(win)
    # return the up and down arrows
    return msg_up,msg_down

 # Create Clay Target Control Panel       
def control_panel():
    lst=[]
    win=GraphWin('Clay Target Control Panel', 400, 515)
    win.setBackground('white')
    # Draw Game Panel
    game_panel=Text(Point(200, 10), 'GAME PANEL')
    game_panel.setStyle('bold')
    game_panel.setSize(9)
    game_panel.draw(win)
    game_panel_box=Rectangle(Point(10, 20), Point(390, 170))
    game_panel_box.draw(win)
    # New game button and text
    new_game_button=Rectangle(Point(20, 50), Point(130, 85))
    new_game_button.setFill('gray')
    new_game_button.draw(win)
    new_game_text=Text(Point(75, 68), 'NEW GAME')
    new_game_text.setSize(9)
    new_game_text.draw(win)
    # Creative Part 2- set day/night button and text
    day_button=Rectangle(Point(145, 50), Point(200, 85))
    day_button.setFill('yellow')
    day_button.draw(win)
    day_text=Text(Point(172, 68), 'DAY')
    day_text.setSize(9)
    day_text.draw(win)
    night_button=Rectangle(Point(200, 50), Point(255, 85))
    night_button.setFill('blue')
    night_button.draw(win)
    night_text=Text(Point(227, 68), 'NIGHT')
    night_text.setSize(9)
    night_text.draw(win)
    # Quit button and text
    quit_button=Rectangle(Point(275, 50), Point(385, 85))
    quit_button.setFill('red')
    quit_button.draw(win)
    quit_text=Text(Point(330, 68), 'QUIT')
    quit_text.setSize(9)
    quit_text.draw(win)
    # Player entry box and text            
    player_text=Text(Point(75, 100), 'Player')
    player_text.setSize(9)
    player_text.draw(win)
    player_box=Rectangle(Point(20, 110), Point(130, 145))
    player_box.draw(win)
    player_entry=Entry(Point(75, 125), 11)
    player_entry.setFill('white')
    player_entry.draw(win)
    # Round display, text, and box
    round_text=Text(Point(200, 100), 'Round')
    round_text.setSize(9)
    round_text.draw(win)
    round_box=Rectangle(Point(175, 110), Point(225, 145))
    round_box.draw(win)
    round_number=Text(Point(200, 127), '1')
    round_number.draw(win)
    # Score display, text, and box
    score_text=Text(Point(330, 100), 'Score')
    score_text.setSize(9)
    score_text.draw(win)
    score_box=Rectangle(Point(305, 110), Point(355, 145))
    score_box.draw(win)
    score_number=Text(Point(330, 127), '0')
    score_number.draw(win)
    # Draw Target Panel
    target_panel=Text(Point(200, 200), 'TARGET PANEL')
    target_panel.setStyle('bold')
    target_panel.setSize(9)
    target_panel.draw(win)
    target_box=Rectangle(Point(10, 215), Point(390, 375))
    target_box.draw(win)
    # Angle entry, box, buttons, and text
    angle_text=Text(Point(75, 230), 'Angle')
    angle_text.setSize(9)
    angle_text.draw(win)
    angle_box=Rectangle(Point(50, 240), Point(100, 275))
    angle_box.draw(win)
    angle_top_button=Circle(Point(112, 245), 8)
    angle_top_button.draw(win)
    angle_top_button.setFill('red')
    angle_bottom_button=Circle(Point(112, 265), 8)
    angle_bottom_button.draw(win)
    angle_bottom_button.setFill('red')
    angle_entry=Entry(Point(75, 257), 3)
    angle_entry.setText('45')
    angle_entry.setFill('white')
    angle_entry.draw(win)
    angle_top_line=Line(Point(112, 236), Point(112, 252))
    angle_top_line.draw(win)
    angle_top_line.setArrow('first')
    angle_bot_line=Line(Point(112, 259), Point(112, 273))
    angle_bot_line.draw(win)
    angle_bot_line.setArrow('last')
    # Power entry, box, buttons, and text
    power_text=Text(Point(200, 230), 'Power')
    power_text.setSize(9)
    power_text.draw(win)
    power_box=Rectangle(Point(175, 240), Point(225, 275))
    power_box.draw(win)
    power_top_button=Circle(Point(236, 245), 8)
    power_top_button.draw(win)
    power_top_button.setFill('red')
    power_bottom_button=Circle(Point(236, 265), 8)
    power_bottom_button.draw(win)
    power_bottom_button.setFill('red')
    power_entry=Entry(Point(200, 257), 3)
    power_entry.setText('10')
    power_entry.setFill('white')
    power_entry.draw(win)
    power_top_line=Line(Point(236, 236), Point(236, 252))
    power_top_line.draw(win)
    power_top_line.setArrow('first')
    power_bot_line=Line(Point(236, 259), Point(236, 273))
    power_bot_line.draw(win)
    power_bot_line.setArrow('last')
    # Gravity, text, box, entry, buttons
    gravity_text=Text(Point(330, 230), 'Gravity')
    gravity_text.setSize(9)
    gravity_text.draw(win)
    gravity_box=Rectangle(Point(305, 240), Point(355, 275))
    gravity_box.draw(win)
    gravity_top_button=Circle(Point(366, 245), 8)
    gravity_top_button.draw(win)
    gravity_top_button.setFill('red')
    gravity_bottom_button=Circle(Point(366, 265), 8)
    gravity_bottom_button.draw(win)
    gravity_bottom_button.setFill('red')
    gravity_entry=Entry(Point(330, 256), '3')
    gravity_entry.setFill('white')
    gravity_entry.setText('5')
    gravity_entry.draw(win)
    gravity_top_line=Line(Point(366, 236), Point(366, 252))
    gravity_top_line.draw(win)
    gravity_top_line.setArrow('first')
    gravity_top_line=Line(Point(366, 259), Point(366, 273))
    gravity_top_line.draw(win)
    gravity_top_line.setArrow('last')
    ## create buttons
    # Move pull double button to make room
    # for pull double button
    pull=Rectangle(Point(210,308),Point(310,348))
    pull.setFill("deep pink")
    pull.setWidth(1.5)
    pull.draw(win)
    # Create a new pull button "pull single"
    pull1=Rectangle(Point(90,308),Point(190,348))
    pull1.setFill("deep pink")
    pull1.setWidth(1.5)
    pull1.draw(win)
    # label buttons
    # Original pull button now pull double
    # move pull double button to make room for pull single button
    pull_txt= Text(Point(260,328),"PULL DOUBLE")
    pull_txt.setSize(10)
    pull_txt.setStyle("bold")
    pull_txt.draw(win)
    # Create a new pull button "pull single"
    pull1_txt= Text(Point(140,328),"PULL SINGLE")
    pull1_txt.setSize(10)
    pull1_txt.setStyle("bold")
    pull1_txt.draw(win)
    # Create a messages text display
    msg_header=Text(Point(170,390),("Rank            Username                   Score                 Rounds"))
    msg_header.setSize(8)
    msg_header.setStyle("bold")
    msg_header.draw(win)
    msg_display=Rectangle(Point(15,405),Point(390,495))
    msg_display.setWidth(1.5)
    msg_display.setFill('white')
    msg_display.draw(win)
    scroll_area=Line(Point(355,405),Point(355,495))
    scroll_area.setWidth(1.5)
    scroll_area.draw(win)
    msg_up=Polygon(Point(365,440),Point(365,420),Point(355,420),Point(372.5,405),Point(390,420),Point(380,420),Point(380,440))
    msg_down=Polygon(Point(365,460),Point(365,480),Point(355,480),Point(372.5,495),Point(390,480),Point(380,480),Point(380,460))
    msg_up.setFill("black")
    msg_down.setFill("black")
    msg_up.draw(win)
    msg_down.draw(win)
    # Create top_scores.txt
    try:
        hs_file=open('top_scores.txt', 'r')
        high_score_list=hs_file.readlines()
        high_score_list=high_score_list[2:]
        if high_score_list==None:
            high_score_list=[]
        # Set default messages text display
        display,len_highscores=score_display(win,1,1,None)
    except FileNotFoundError:
        hs_file=open('top_scores.txt', 'w')
        print('Rank\tUsername\tScore\tRounds', file=hs_file)
        print('====================================', file=hs_file)
        high_score_list=[]
        hs_file.close()
        display,len_highscores=0,0
    # Create scores dict
    high_score_list2=[]
    score_dict={}
    if high_score_list!=[]:
        for i in high_score_list:
            line=i.split('\t')
            line[3]=line[3].replace('\n', '')
            high_score_list2.append(line)
        for i in high_score_list2:
            score_dict[i[1]]=float(i[2])/100*int(i[3])
    top_scores_dict={}
    # Create round dict
    round_dict={}
    if high_score_list!=[]:
        for i in high_score_list2:
            round_dict[i[1]]=int(i[3])
    # Append items to lst and return
    power=int(power_entry.getText())
    angle=int(angle_entry.getText())
    gravity=int(gravity_entry.getText())
    # Create lst to easily pass objects between functions
    lst=[new_game_button, day_button, quit_button, player_entry,
         round_number, score_number, angle_entry, angle_top_button,
         angle_bottom_button, power_entry, power_top_button,
         power_bottom_button, gravity_entry, gravity_top_button,
         gravity_bottom_button, pull, power, angle, gravity,
         high_score_list, win, score_dict, round_dict, pull1,msg_header,
         msg_display,scroll_area,msg_up,msg_down, display,
         len_highscores,night_button, top_scores_dict]
    return win, lst

# Define game_window function
def game_window():
    game_win=GraphWin('Game Window', 600, 600)
    game_win.setBackground('light blue')
    # Creative Part 2- Day/Night Background
    # Description: This feature adds 2 distinct, vibrant backgrounds: day and
    #  night. Day features a large, yellow sun, while night features a
    #  waning moon and twinkling stars.
    # Purpose: The team thought that a visually stimulating creative figure
    #  needed to be added. After all, everyone likes seeing a new vista.
    # Draw Day
    grass=Rectangle(Point(0, 450), Point(600, 600))
    grass.setFill('light green')
    grass.draw(game_win)
    sun = Circle(Point(125,165) , 45)
    sun.setFill('yellow1')
    sun.setOutline('yellow1')
    sun.draw(game_win)
    sunshine1 = Polygon(Point(120,30),Point(125,115),Point(140,20))
    sunshine1.setFill('yellow1')
    sunshine1.setOutline('yellow1')
    sunshine1.draw(game_win)
    sunshine2 = Polygon(Point(173,135),Point(212,53),Point(247,54))
    sunshine2.setFill('yellow1')
    sunshine2.setOutline('yellow1')
    sunshine2.draw(game_win)
    sunshine3 = Polygon(Point(174,183),Point(263,188),Point(273,148))
    sunshine3.setFill('yellow1')
    sunshine3.setOutline('yellow1')
    sunshine3.draw(game_win)
    sunshine4 = Polygon(Point(150,217),Point(173,301),Point(196,281))
    sunshine4.setFill('yellow1')
    sunshine4.setOutline('yellow1')
    sunshine4.draw(game_win)
    sunshine5 = Polygon(Point(108,216),Point(80,272),Point(111,275))
    sunshine5.setFill('yellow1')
    sunshine5.setOutline('yellow1')
    sunshine5.draw(game_win)
    sunshine6 = Polygon(Point(10,207),Point(14,234),Point(79,187))
    sunshine6.setFill('yellow1')
    sunshine6.setOutline('yellow1')
    sunshine6.draw(game_win)
    sunshine7 = Polygon(Point(77,140),Point(24,91),Point(42,76))
    sunshine7.setFill('yellow1')
    sunshine7.setOutline('yellow1')
    sunshine7.draw(game_win)
    # Creative Part 1- Limiting the User's Number of Shots
    # Description: The user will only have 5 shots (clicks) that will register.
    #  After those 5 shots have been used, the user's shots (clicks) will
    #  no longer register. The number of shots the user has is displayed in
    #  the top left of the game window. Green means that the user has that shot,
    #  and red means the user has used that shot. Shots are reloaded after each
    #  round.
    # Purpose: Limiting the number of shots the user has prevents the user from clicking
    #  simply clicking a lot and making the game very easy. This new feature
    #  makes the game more realistic and fun.
    # p3 part 6 limiting number of shots, display to user how
    #  many shots they have (green=loaded, red=unloaded)
    # create a list of bullets
    bullets=[]
    bullet=Rectangle(Point(10,20),Point(20,40))
    for i in range(5):
        bullet2=bullet.clone()
        bullet2.move(15,0)
        bullet2.setFill('red')
        bullet2.draw(game_win)
        bullets.append(bullet2)
        bullet=bullet2
    return game_win, bullets

# Distance function that will be used to determine if the user clicks
#  an object
def dist(clickPoint, circle_center):
    click_x=clickPoint.getX()
    click_y=clickPoint.getY()
    circle_x=circle_center.getX()
    circle_y=circle_center.getY()
    dist1=((click_x-circle_x)**2+(click_y-circle_y)**2)**(1/2)
    return dist1

# Define control_panel_functionality (p is power and a is angle)
def control_panel_functionality(lst, game_win, win, bullets):
    # Set scroll variables
    start_rank=1
    num_names_displayed=1
    up_click=0
    msg_display=lst[25]
    msg_header=lst[24]
    scroll_area=lst[26]
    msg_up=lst[27]
    msg_down=lst[28]
    display=lst[29]
    len_highscores=lst[30]
    animation="off"
    a=0
    b=0
    while a!=1:
        clickPoint=win.checkMouse()
        if clickPoint!=None:
            # Initialize power, angle, and gravity
            power, angle, gravity=lst[16], lst[17], lst[18]
            # check clickPoint
            click_x=clickPoint.getX()
            click_y=clickPoint.getY()
            # Check if messages up or down button clicked
            point_lst=msg_up.getPoints()
            point2_lst=msg_down.getPoints()
            # Check if msg up clicked
            if click_y> point_lst[3].getY()and click_y<point_lst[-1].getY() and click_x>point_lst[2].getX() and click_x<point_lst[4].getX():
                # If there are 3 names displayed on the screen increase the
                #  starting rank 
                if num_names_displayed>3 and start_rank<(len_highscores-4):
                    start_rank+=1
                # If num_names_displayed<3:
                num_names_displayed+=1
                if start_rank<int(round(len_highscores/2,0)):
                    msg_up,msg_down=move_scroll(win,msg_up,msg_down,start_rank,num_names_displayed,len_highscores)
                elif start_rank==int(round(len_highscores/2,0)) and up_click!=1:
                    msg_up,msg_down=move_scroll(win,msg_up,msg_down,start_rank,num_names_displayed,len_highscores)
                    up_click+=1
                display,len_highscores=score_display(win,num_names_displayed,start_rank,display)
            # Check if msg down clicked
            elif click_y< point2_lst[3].getY()and click_y>point2_lst[-1].getY() and click_x>point2_lst[2].getX() and click_x<point2_lst[4].getX():
                up_click=0
                if start_rank>1:
                    start_rank-=1
                    display,len_highscores=score_display(win,num_names_displayed,start_rank,display)   
                    msg_up,msg_down=move_scroll(win,msg_up,msg_down,start_rank,num_names_displayed,len_highscores)
            # Get centers of the circle buttons
            angle_top_button_center=lst[7].getCenter()
            angle_bottom_button_center=lst[8].getCenter()
            power_top_button_center=lst[10].getCenter()
            power_bottom_button_center=lst[11].getCenter()
            gravity_top_button_center=lst[13].getCenter()
            gravity_bottom_button_center=lst[14].getCenter()
            # Get distance from click to circular buttons
            dist_atb=dist(clickPoint, angle_top_button_center)
            dist_abb=dist(clickPoint, angle_bottom_button_center)
            dist_ptb=dist(clickPoint, power_top_button_center)
            dist_pbb=dist(clickPoint, power_bottom_button_center)
            dist_gtb=dist(clickPoint, gravity_top_button_center)
            dist_gbb=dist(clickPoint, gravity_bottom_button_center)
            # Check new game button
            player_entry=lst[3]
            player_name=player_entry.getText()
            if player_name!='' and b==0:
                new_game_button=lst[0]
                new_game_button.setFill('green')
                if click_x>=20 and click_x<=130 and click_y>=50 and click_y<=85 and player_name!='' :
                    angle_entry=lst[6]
                    angle_entry.setText('45')
                    power_entry=lst[9]
                    power_entry.setText('10')
                    gravity_entry=lst[12]
                    gravity_entry.setText('5')
                    player_entry=lst[3]
                    player_entry.setText('')
                    lst[15].setFill('yellow')
                    lst[23].setFill('yellow')
            # Check pull button
            angle_entry, power_entry, gravity_entry=lst[6], lst[9], lst[12]
            if player_name!='' and int(angle_entry.getText())>=30 and int(angle_entry.getText())<=60 and int(power_entry.getText())>=5 and int(power_entry.getText())<=50 and int(gravity_entry.getText())>=3 and int(gravity_entry.getText())<=25:
                lst[15].setFill('yellow')
                lst[23].setFill('yellow')
             # Check if pull double clicked
            if click_y>308 and click_y<348 and click_x>210 and click_x<310 and int(angle_entry.getText())>=30 and int(angle_entry.getText())<=60 and int(power_entry.getText())>=5 and int(power_entry.getText())<=50 and int(gravity_entry.getText())>=3 and int(gravity_entry.getText())<=25:             
                b=1
                lst[0].setFill('grey')
                lst[7].setFill('light grey')
                lst[8].setFill('light grey')
                lst[10].setFill('light grey')
                lst[11].setFill('light grey')
                lst[13].setFill('light grey')
                lst[14].setFill('light grey')
                lst[15].setFill('deeppink')
                lst[23].setFill('deeppink')
                # Set pull_type to pull double
                pull_type='double'
                # Make pull button inactive
                lst[15].setFill("deeppink")
                pull_status="inactive"
                # Make pull single button inactive
                lst[23].setFill("deeppink")
                # Pause for 2 seconds
                sleep(2)
                # Call animate function with game window passed through and 
                # Part 6 - Pass in list of bullets
                animate(game_win,lst,pull_type,bullets)
                # p3 part 3 set clickPoint to clicks made while animation in progress
                clickPoint=win.checkMouse()
                # set clickPoint to zero so that any clicks made during are null
                clickPoint=0
                # Pull button active again after animation
                lst[15].setFill("yellow")
                # Make pull single button active
                lst[23].setFill("yellow")
                lst[7].setFill('red')
                lst[8].setFill('red')
                lst[10].setFill('red')
                lst[11].setFill('red')
                lst[13].setFill('red')
                lst[14].setFill('red')
                lst[15].setFill('yellow')
                lst[23].setFill('yellow')
                b=0
            # Check if pull single clicked
            if click_y>308 and click_y<348 and click_x>90 and click_x<190 and int(angle_entry.getText())>=30 and int(angle_entry.getText())<=60 and int(power_entry.getText())>=5 and int(power_entry.getText())<=50 and int(gravity_entry.getText())>=3 and int(gravity_entry.getText())<=25:
                b=1
                lst[0].setFill('grey')
                lst[7].setFill('light grey')
                lst[8].setFill('light grey')
                lst[10].setFill('light grey')
                lst[11].setFill('light grey')
                lst[13].setFill('light grey')
                lst[14].setFill('light grey')
                lst[15].setFill('deeppink')
                lst[23].setFill('deeppink')
                # Set pull type
                pull_type='single'
                # Make pull button inactive
                lst[15].setFill("deeppink")
                # Make pull single button inactive
                lst[23].setFill("deeppink")
                # Pause for 2 seconds
                sleep(2)
                # Call animate function with game window passed through
                # Pass in list of bullets
                animate(game_win,lst,pull_type,bullets)
                # Set clickPoint to clicks made while animation in progress
                clickPoint=win.checkMouse()
                # set clickPoint to zero so that any clicks made during are null
                clickPoint=0
                # Pull buttons active again after animation
                lst[23].setFill("yellow")
                lst[15].setFill("yellow")
                # Game over pull buttons becomes inactive
                lst[15].setFill("deeppink")
                lst[23].setFill("deeppink")
                lst[7].setFill('red')
                lst[8].setFill('red')
                lst[10].setFill('red')
                lst[11].setFill('red')
                lst[13].setFill('red')
                lst[14].setFill('red')
                lst[15].setFill('yellow')
                lst[23].setFill('yellow')
                b=0
            # Check if click in quit button
            if click_x>=275 and click_x<=385 and click_y>=50 and click_y<=85:
                # If user clicked in the control panel during the animation,
                #  animation is turned off by the click
                win.close()
                game_win.close()
                break
            # Check if click in circular buttons
            if dist_atb<=8:
                n=lst[6]
                n=n.getText()
                n=int(n)
                n+=1
                if n>=30 and n<=60:
                    n=str(n)
                    lst[6].setText(n)
            elif dist_abb<=8:
                n=lst[6]
                n=n.getText()
                n=int(n)
                n=n-1
                if n>=30 and n<=60:
                    n=str(n)
                    lst[6].setText(n)
            elif dist_ptb<=8:
                n=lst[9]
                n=n.getText()
                n=int(n)
                n=n+1
                if n>=5 and n<=50:
                    n=str(n)
                    lst[9].setText(n)
            elif dist_pbb<=8:
                n=lst[9]
                n=n.getText()
                n=int(n)
                n=n-1
                if n>=5 and n<=50:
                    n=str(n)
                    lst[9].setText(n)
            elif dist_gtb<=8:
                n=lst[12]
                n=n.getText()
                n=int(n)
                n=n+1
                if n>=3 and n<=25:
                    n=str(n)
                    lst[12].setText(n)
            elif dist_gbb<=8:
                n=lst[12]
                n=n.getText()
                n=int(n)
                n=n-1
                if n>=3 and n<=25:
                    n=str(n)
                    lst[12].setText(n)
            # Creative part 2- Check if user clicks on day/night button
            if click_x>=145 and click_x<=200 and click_y>=50 and click_y<=85:
                # Set background to day
                game_win.setBackground('light blue')
                grass=Rectangle(Point(0, 450), Point(600, 600))
                grass.setFill('light green')
                grass.draw(game_win)
                cover1 = Rectangle(Point(0,41),Point(600,450))
                cover1.setFill('light blue')
                cover1.setOutline('light blue')
                cover1.draw(game_win)
                cover1_plus = Rectangle(Point(119,0),Point(600,41))
                cover1_plus.setFill('light blue')
                cover1_plus.setOutline('light blue')
                cover1_plus.draw(game_win)
                sun = Circle(Point(125,165) , 45)
                sun.setFill('yellow1')
                sun.setOutline('yellow1')
                sun.draw(game_win)
                sunshine1 = Polygon(Point(120,30),Point(125,115),Point(140,20))
                sunshine1.setFill('yellow1')
                sunshine1.setOutline('yellow1')
                sunshine1.draw(game_win)
                sunshine2 = Polygon(Point(173,135),Point(212,53),Point(247,54))
                sunshine2.setFill('yellow1')
                sunshine2.setOutline('yellow1')
                sunshine2.draw(game_win)
                sunshine3 = Polygon(Point(174,183),Point(263,188),Point(273,148))
                sunshine3.setFill('yellow1')
                sunshine3.setOutline('yellow1')
                sunshine3.draw(game_win)
                sunshine4 = Polygon(Point(150,217),Point(173,301),Point(196,281))
                sunshine4.setFill('yellow1')
                sunshine4.setOutline('yellow1')
                sunshine4.draw(game_win)
                sunshine5 = Polygon(Point(108,216),Point(80,272),Point(111,275))
                sunshine5.setFill('yellow1')
                sunshine5.setOutline('yellow1')
                sunshine5.draw(game_win)
                sunshine6 = Polygon(Point(10,207),Point(14,234),Point(79,187))
                sunshine6.setFill('yellow1')
                sunshine6.setOutline('yellow1')
                sunshine6.draw(game_win)
                sunshine7 = Polygon(Point(77,140),Point(24,91),Point(42,76))
                sunshine7.setFill('yellow1')
                sunshine7.setOutline('yellow1')
                sunshine7.draw(game_win)
            # Creative Part 2- Check if user clicked in night button
            if click_x>=200 and click_x<=255 and click_y>=50 and click_y<=85:
                # Creative Part 2- Set background to night
                game_win.setBackground('dark blue')
                grass=Rectangle(Point(0, 450), Point(600, 600))
                grass.setFill('dark green')
                grass.draw(game_win)
                cover2 = Rectangle(Point(0,41),Point(600,450))
                cover2.setFill('dark blue')
                cover2.setOutline('dark blue')
                cover2.draw(game_win)
                cover2_plus = Rectangle(Point(119,0),Point(600,41))
                cover2_plus.setFill('dark blue')
                cover2_plus.setOutline('dark blue')
                cover2_plus.draw(game_win)
                moon = Circle(Point(125,165),50)
                moon.setFill('light yellow')
                moon.setOutline('light yellow')
                moon.draw(game_win)
                shadow = Circle(Point(170,140),45)
                shadow.setFill('dark blue')
                shadow.setOutline('dark blue')
                shadow.draw(game_win)
                # Creative part 2- Draw stars in random places
                for i in range(15):
                    star = Circle(Point(choice(range(180,590)),choice(range(50,400))),choice(range(1,3)))             
                    star.setFill('white')
                    star.setOutline('white')
                    star.draw(game_win)
                for i in range(5):
                    star = Circle(Point(choice(range(40,180)),choice(range(225,400))),choice(range(1,3)))                   
                    star.setFill('white')
                    star.setOutline('white')
                    star.draw(game_win)
                
# Create new function that animates a single target
def animate_single(target1,target1_x_pos,APG,win,ctrl_win,score,score_txt,
                   bullets,shots):
    # Set variables
    angle=float(APG[0].getText())
    power=float(APG[1].getText())
    gravity=float(APG[2].getText())
    dx= abs(power*(cos(radians(angle))))
    dy= abs(power*(sin(radians(angle))))
    dx_r=abs(power)
    initial_dy=dy
    time=0
    # Choose if rabbits or clay targets
        #   0 means clay targets
        #   1 means rabbits
        #   2 means sparrow (Creative Part 3)
        #   3 means froggy (Creative Part 4)
    number=randint(0, 3)
    # Animate clay pigeons
    if number==0:
        # Draw target
        target1.draw(win)
        target1_Y=target1.getCenter().getY()
        # Animate target
        while target1!=None:
            time+=.02
            # Check for mouse click
            click= win.checkMouse()
            if click:
                # Creative Part 1- limiting number of shots,
                #  increment shots taken
                shots+=1
                # Change color of bullets to red to indicate that the shot
                #  has been used
                if shots<=5:
                    bullets[shots-1].setFill('red')
                # Check if targets are clicked on
                # Limiting number of shots, do not allow user to
                #  shoot if they used up 5 shots
                if dist(click,target1.getCenter())<target1.getRadius() and shots<=5:
                    target1.undraw()
                    # if undrawn, center value y does not exist
                    target1_Y=0
                    # increase score
                    score+=.5
                    # update score text
                    score_str=str(score)
                    # make score 2 decimal places
                    if len(score_str[score_str.find("."):])==2:
                        score_str+="0"    
                    score_txt.setText(score)
            # check to make sure clay target 1 above grass
            if target1_Y<=451:
                # if target 1 starts on the left dx is positive else dx
                #  is negative
                if target1_x_pos==0:
                    target1.move(.5*dx,.5*dy)
                    sleep(.045)
                else:
                    target1.move(-.5*dx,.5*dy)
                    sleep(.045)
            # undraw target if below grass
            if target1_Y>=451:
                target1.undraw()
                # if undrawn center value y does not exist
                target1_Y=0
            # if clay targets reach far side or both are undrawn break loop
            if target1.getCenter().getX()>601 or target1.getCenter().getX()<1 or target1_Y==0:
                target1.undraw()
                sleep(.5)
                break
            target1_Y=target1.getCenter().getY()
            dy=gravity*time-initial_dy-1
    # Animate rabbits
    if number==1:
        target1= Circle(Point(target1_x_pos,450),8)
        target1.setFill("darkgrey")
        # draw target
        target1.draw(win)
        target1_Y=target1.getCenter().getY()
        while target1!=None:
             # check for mouse click
            click= win.checkMouse()

            if click:
                # Creative Part 1- limiting number of shots, increment shots taken
                shots+=1
                # change color of bullets to red to indicate that the shot
                #  has been used
                if shots<=5:
                    bullets[shots-1].setFill('red')
                # Creative Part 1- limiting number of shots, do not allow user to
                #   shoot if they used up 5 shots
                # check if targets are clicked on
                if dist(click,target1.getCenter())<target1.getRadius() and shots<=5:
                    target1.undraw()
                    # increase score
                    score+=.5
                    # update score text
                    score_str=str(score)
                    # make score 2 decimal places
                    if len(score_str[score_str.find("."):])==2:
                        score_str+="0"
                    score_txt.setText(score)
                    sleep(.5)
                    break
            if target1_x_pos==0:
                target1.move(.55*dx_r,0)
                sleep(.045)
            else:
                target1.move(-.55*dx_r,0)
                sleep(.045)
                # if undrawn center value y does not exist
                target1_Y=0
            # if clay targets reach far side or both are undrawn break loop
            if target1.getCenter().getX()>601 or target1.getCenter().getX()<1:
                target1.undraw()
                sleep(.5)
                break
            target1_Y=target1.getCenter().getY()
    # Creative Part 3- Animate Sparrow Targets
    # Description: This new type of target will move in an oscillating manner,
    #  similar to a sine wave. All other aspects like score, round,
    #  etc. will be tracked normally. The team even incorporated a separate
    #  creative part into this one, i.e., the shot number restriction.
    # Purpose: This new target type will provide more variety and a new
    #  type of challenge for the user.
    # Animate Sparrow Targets
    if number==2:
        # Initalize variables
        time=0
        target1= Circle(Point(target1_x_pos,randint(150, 250)),8)
        target1.setFill("brown")
        # Draw target
        target1.draw(win)
        target1_Y=target1.getCenter().getY()
        # Animate target
        while target1!=None:
            time+=10
            # Check for mouse click
            click= win.checkMouse()
            if click:
                # Creative Part 1- limiting number of shots, increment shots taken
                shots+=1
                # change color of bullets to red to indicate that the shot has
                #  been used
                if shots<=5:
                    bullets[shots-1].setFill('red')
                # check if targets are clicked on
                # Creative Part 1- limiting number of shots, do not allow user to
                #  shoot if they used up 5 shots
                if dist(click,target1.getCenter())<target1.getRadius() and shots<=5:
                    target1.undraw()
                    # if undrawn, center value y does not exist
                    target1_Y=0
                    # increase score
                    score+=.5
                    # update score text
                    score_str=str(score)
                    # make score 2 decimal places
                    if len(score_str[score_str.find("."):])==2:
                        score_str+="0"    
                    score_txt.setText(score)
            # Sparrow Targets- The team split the dy into a dy_1 and dy_2 to
            #  give the sparrows an asymmetric pattern
            dy_1=.4*power*sin(radians(time))
            dy_2=.4*power*cos(radians(time))
            # Check to make sure clay target 1 above grass
            if target1_Y<=451:
                # If target 1 starts on the left dx is positive else dx is negative
                if target1_x_pos==0:
                    target1.move(.75*dx,dy_1)
                    sleep(.045)
                else:
                    target1.move(-.75*dx,dy_2)
                    sleep(.045)
            # Undraw target if below grass
            if target1_Y>=451:
                target1.undraw()
                # If undrawn center value y does not exist
                target1_Y=0
            # If clay targets reach far side or both are undrawn break loop
            if target1.getCenter().getX()>601 or target1.getCenter().getX()<1 or target1_Y==0:
                target1.undraw()
                sleep(.5)
                break
            target1_Y=target1.getCenter().getY()
    #Creative Part 4- Animate Froggy Targets
    # Description: This new type of target will move in a manner similar to
    #  a hopping frog. First, the frog will start out hopping towards the
    #  opposite end of the screen. When it lands, it will rest for a brief
    #  moment before hopping again. The player is intended to hit the frog
    #  when it lands, as the frog's jump path is quick and difficult to hit.
    #  All other aspects like score, round, etc. will be tracked normally.
    #  The team even incorporated a separate creative part into this one, i.e.,
    #  the shot number restriction.
    # Purpose: This new target type will provide more variety and a new type of challenge
    #  for the player.
    # Animate Froggy
    if number==3:
        # Initialize variables
        time=0
        target1= Circle(Point(target1_x_pos,450),8)
        target1.setFill("green")
        # Draw target
        target1.draw(win)
        target1_Y=target1.getCenter().getY()
        # Animate target
        while target1!=None:
            time+=.02
            # Check for mouse click
            click= win.checkMouse()
            if click:
                # p3 part 6 limiting number of shots, increment shots taken
                shots+=1
                # change color of bullets to red to indicate that the shot has been used
                if shots<=5:
                    bullets[shots-1].setFill('red')
                # check if targets are clicked on
                # p3 part 6 limiting number of shots, do not allow user to shoot if they used up 5 shots
                if dist(click,target1.getCenter())<target1.getRadius() and shots<=5:
                    target1.undraw()
                    # if undrawn, center value y does not exist
                    target1_Y=0
                    # increase score
                    score+=.5
                    # update score text
                    score_str=str(score)
                    # make score 2 decimal places
                    if len(score_str[score_str.find("."):])==2:
                        score_str+="0"    
                    score_txt.setText(score)
                    sleep(.5)
                    break
            # Undraw Froggy if off the screen
            if target1.getCenter().getX()>600 or target1.getCenter().getX()<0 and target1!=None:
                target1.undraw()
                target1=None
                sleep(.5)
                break
            # Froggy hop is as follows: when a froggy touches the grass
            #  (y_value>=450), then it stops (sleep), and jumps (time=0)
            # Make Froggy Hop
            if target1.getCenter().getY()>=450 and target1!=None:
                sleep(.5)
                time=0
            # Increment dy
            dy=gravity**3*time**2-initial_dy-35
            # if target 1 starts on the left dx is positive else dx is negative
            if target1_x_pos==0:
                target1.move(.25*dx,.01*dy)
                sleep(.005)
            else:
                target1.move(-.25*dx,.01*dy)
                sleep(.005)
            target1_Y=target1.getCenter().getY()
    return score,score_txt,shots          
                
# Define animate function                    
def animate(game_win, lst, pull_type,bullets):
    # Initialize variables
    lst[0].setFill('grey')
    score=0
    power, angle, gravity=lst[16], lst[17], lst[18]
    a=2
    dx=abs(power*cos(radians(angle)))
    dy=abs(power*sin(radians(angle)))
    dx_r=abs(power)
    initial_dy=dy
    time=0
    d=0
    dist1, dist2=None, None
    ctrl_win=lst[20]
    # Creative part 1- limiting number of shots, keep track of how many shots are taken 
    shots=0
    # Creative part 1- let user know gun is reloading by displaying a reloading
    #  text
    reload_txt=Text(Point(60,60),"reloading")
    reload_txt.draw(game_win)
    dot=Text(Point(90,60),".")
    dots=[]
    for i in range(4):
        dot2=dot.clone()
        dot2.move(5*i,0)
        dots.append(dot2)
    for i in dots:
        i.draw(game_win)
        sleep(.1)
    for i in dots:
        i.undraw()
    for i in dots:
        i.draw(game_win)
        sleep(.1)
    for i in dots:
        i.undraw()
    for i in dots:
        i.draw(game_win)
        sleep(.1)
    for i in dots:
        i.undraw()
    reload_txt.undraw()
    # Creative Part 1- setFill bullets to green to indicate
    #  that shots are available
    for i in bullets:
        i.setFill('lightgreen')
    if pull_type=='double':
        # Choose if rabbits or clay targets
        #   0 means clay targets
        #   1 means rabbits
        #   2 means sparrows (Creative Part 3)
        #   3 means froggy (Creative Part 4)
        number=randint(0, 3)
        # Animate clay targets
        if number==0:
            # This loop counts the number of sets of 2 disks thrown
            while d<1:
                # Initialize and draw disks
                power=int(lst[9].getText())
                angle=int(lst[6].getText())
                gravity=int(lst[12].getText())
                disk1_initial_y=randint(350, 450)
                disk1=Circle(Point(0, disk1_initial_y), 8)
                disk1.setFill('dark grey')
                disk2_initial_y=randint(350, 450)
                disk2=Circle(Point(600, disk2_initial_y), 8)
                disk2.setFill('dark grey')
                disk1.draw(game_win)
                disk2.draw(game_win)
                clickPoint=None
                clickPoint1=None
                while a!=0:
                    # Check disk coordinates
                    if disk1!=None:
                        disk1_center=disk1.getCenter()
                        disk1_x=disk1_center.getX()
                        disk1_y=disk1_center.getY()
                    if disk2!=None:
                        disk2_center=disk2.getCenter()
                        disk2_x=disk2_center.getX()
                        disk2_y=disk2_center.getY()
                    # Check if user clicks a disk
                    if clickPoint==None:
                        clickPoint=game_win.checkMouse()
                        if clickPoint:
                            # p3 part 6 limiting number of shots, increment shots taken
                            shots+=1
                            # change color of bullets to red to indicate that the shot has been used
                            if shots<=5:
                                bullets[shots-1].setFill('red')
                    # Creative part 1- limiting number of shots, do not allow user to shoot if they used up 5 shots
                    if clickPoint!=None and disk1!=None and shots<=5:
                        dist1=dist(clickPoint, disk1_center)
                        if dist1<=8 and disk1!=None:
                            disk1.undraw()
                            disk1=None
                            a=a-1
                            # Add score of .5
                            score+=.5
                    # Creative Part 1- Limiting number of shots, do not allow user to shoot if they used up 5 shots    
                    if clickPoint!=None and disk2!=None and shots<=5:
                        dist2=dist(clickPoint, disk2_center)
                        if dist2<=8 and disk2!=None:
                            disk2.undraw()
                            a=a-1
                            disk2=None
                            # Add score of .5
                            score+=.5
                    dist1, dist2=0, 0
                    # Increment time
                    time+=.02
                    # Undraw disks if they are in the grass or off the screen
                    if (disk1_x>600 or disk1_y>450 or disk1_x<0) and disk1!=None:
                        disk1.undraw()
                        a=a-1
                        disk1=None
                    if (disk2_x<0 or disk2_y>450 or disk2_x>600) and disk2!=None:
                        disk2.undraw()
                        a=a-1
                        disk2=None
                    # Increment dy
                    dy=gravity*time-initial_dy-1
                    # Animate disks
                    if disk1!=None:
                        disk1.move(.5*dx, .5*dy)
                    if disk2!=None:
                        disk2.move(-.5*dx, .5*dy)
                    # Reset clickpoint and sleep
                    clickPoint=None
                    sleep(.045)
                d+=1
                a=2
                time=0
                sleep(.5)
                clickPoint=None
            lst[0].setFill('green')
        #Animate rabbits
        if number==1:
            # This loop counts the number of sets of 2 disks thrown
            while d<1:
                # Initialize and draw disks
                power=int(lst[9].getText())
                angle=int(lst[6].getText())
                gravity=int(lst[12].getText())
                disk1_initial_y=450
                disk1=Circle(Point(0, disk1_initial_y), 8)
                disk1.setFill('dark grey')
                disk2_initial_y=450
                disk2=Circle(Point(600, disk2_initial_y), 8)
                disk2.setFill('dark grey')
                disk1.draw(game_win)
                disk2.draw(game_win)
                clickPoint=None
                clickPoint1=None
                while a!=0:
                    # Check disk coordinates
                    if disk1!=None:
                        disk1_center=disk1.getCenter()
                        disk1_x=disk1_center.getX()
                        disk1_y=disk1_center.getY()
                    if disk2!=None:
                        disk2_center=disk2.getCenter()
                        disk2_x=disk2_center.getX()
                        disk2_y=disk2_center.getY()
                    # Check if user clicks a disk
                    if clickPoint==None:
                        clickPoint=game_win.checkMouse()
                        if clickPoint:
                        # Creative Part 1- limiting number of shots, increment shots
                        #  taken
                            shots+=1
                        # change color of bullets to red to indicate that the shot has been used
                            if shots<=5:
                                bullets[shots-1].setFill('red')
                     # Creative Part 1- Limiting number of shots, do not allow user to shoot if they used up 5 shots    
                    if clickPoint!=None and disk1!=None and shots<=5:
                        dist1=dist(clickPoint, disk1_center)
                        if dist1<=8 and disk1!=None:
                            disk1.undraw()
                            disk1=None
                            a=a-1
                            # Add score of .5
                            score+=.5
                     # Creative Part 1- Limiting number of shots, do not allow user to shoot if they used up 5 shots    
                    if clickPoint!=None and disk2!=None and shots<=5:
                        dist2=dist(clickPoint, disk2_center)
                        if dist2<=8 and disk2!=None:
                            disk2.undraw()
                            a=a-1
                            disk2=None
                            # Add score of .5
                            score+=.5
                    dist1, dist2=0, 0
                    # Increment time
                    time+=.05
                    # Undraw disks if they are in the grass or off the screen
                    if (disk1_x>600 or disk1_x<0) and disk1!=None:
                        disk1.undraw()
                        a=a-1
                        disk1=None
                    if (disk2_x<0 or disk2_x>600) and disk2!=None:
                        disk2.undraw()
                        a=a-1
                        disk2=None
                    # Animate disks
                    if disk1!=None:
                        disk1.move(.55*dx_r, 0)
                    if disk2!=None:
                        disk2.move(-.55*dx_r, 0)
                    # Reset clickpoint and sleep
                    clickPoint=None
                    sleep(.045)
                d+=1
                a=2
                time=0
                sleep(.5)
                clickPoint=None
            lst[0].setFill('green')
        # Creative Part 3- Animate Sparrow Targets
        # Description: This new type of target will move in an oscillating manner, similar to a sine wave.
        #  All other aspects like score, round, etc. will be tracked normally. The team even incorporated
        #  a separate creative part into this one, i.e., the shot number restriction.
        # Purpose: This new target type will provide more variety and a new type of challenge for the user.
        if number==2:
            # This loop counts the number of sets of 2 disks thrown
            while d<1:
                # Initialize and draw sparrows
                power=int(lst[9].getText())
                angle=int(lst[6].getText())
                gravity=int(lst[12].getText())
                disk1_initial_y=randint(150, 250)
                disk1=Circle(Point(0, disk1_initial_y), 8)
                disk1.setFill('brown')
                disk2_initial_y=randint(200, 300)
                disk2=Circle(Point(600, disk2_initial_y), 8)
                disk2.setFill('brown')
                disk1.draw(game_win)
                disk2.draw(game_win)
                clickPoint=None
                clickPoint1=None
                # The team decided to set a lower dx. The reason for this decision was to make an oscillating
                #  target easier to hit.
                dx=.3*dx
                while a!=0:
                    # Check sparrow coordinates
                    if disk1!=None:
                        disk1_center=disk1.getCenter()
                        disk1_x=disk1_center.getX()
                        disk1_y=disk1_center.getY()
                    if disk2!=None:
                        disk2_center=disk2.getCenter()
                        disk2_x=disk2_center.getX()
                        disk2_y=disk2_center.getY()
                    # Check if user clicks a sparrow
                    if clickPoint==None:
                        clickPoint=game_win.checkMouse()
                        if clickPoint:
                            # Creative Part 1- Limiting number of shots,
                            #  increment shots taken
                            shots+=1
                            # change color of bullets to red to indicate that the shot has been used
                            if shots<=5:
                                bullets[shots-1].setFill('red')
                    # Creative Part 1- Limiting number of shots, do not allow
                    #  user to shoot if they used up 5 shots
                    if clickPoint!=None and disk1!=None and shots<=5:
                        dist1=dist(clickPoint, disk1_center)
                        if dist1<=8 and disk1!=None:
                            disk1.undraw()
                            disk1=None
                            a=a-1
                            # Add score of .5
                            score+=.5
                    # Creative Part 1- Limiting number of shots, do not allow
                    #  user to shoot if they used up 5 shots    
                    if clickPoint!=None and disk2!=None and shots<=5:
                        dist2=dist(clickPoint, disk2_center)
                        if dist2<=8 and disk2!=None:
                            disk2.undraw()
                            a=a-1
                            disk2=None
                            # Add score of .5
                            score+=.5
                    dist1, dist2=0, 0
                    # Increment time. The reasons for the higher time value is
                    #  to make
                    #  the period of the trig function shorter.
                    time+=10
                    # Undraw disks if they are in the grass or off the screen
                    if (disk1_x>600 or disk1_y>450 or disk1_x<0) and disk1!=None:
                        disk1.undraw()
                        a=a-1
                        disk1=None
                    if (disk2_x<0 or disk2_y>450 or disk2_x>600) and disk2!=None:
                        disk2.undraw()
                        a=a-1
                        disk2=None
                    # Increment dy_1 and dy_2. The team decided to split the dy value into
                    #  2 in order to give the sparrows asymmetric flight paths.
                    dy_1=.4*power*sin(radians(time))
                    dy_2=.4*power*cos(radians(time))
                    # Animate disks
                    if disk1!=None:
                        disk1.move(.75*dx, dy_1)
                    if disk2!=None:
                        disk2.move(-.75*dx, dy_2)
                    # Reset clickpoint and sleep
                    clickPoint=None
                    sleep(.045)
                d+=1
                a=2
                time=0
                sleep(.5)
                clickPoint=None
            lst[0].setFill('green')
        # Creative Part- Animate Froggy Targets
        # Description: This new type of target will move in a manner similar to a hopping frog.
        #  First, the frog will start out hopping towards the opposite end of the screen. When
        #  it lands, it will rest for a brief moment before hopping again. The player is
        #  intended to hit the frog when it lands, as the frog's jump path is quick and
        #  difficult to hit. All other aspects like score, round, etc. will be tracked
        #  normally. The team even incorporated a separate creative part into this one, i.e.,
        #  the shot number restriction.
        # Purpose: This new target type will provide more variety and a new type of challenge
        #  for the player. Plus, froggies are cute!
        # Animate Froggy
        if number==3:
            # Initialize and draw disks
            power=int(lst[9].getText())
            angle=int(lst[6].getText())
            gravity=int(lst[12].getText())
            disk1_initial_y=450
            disk1=Circle(Point(0, disk1_initial_y), 8)
            disk1.setFill('green')
            disk2_initial_y=450
            disk2=Circle(Point(600, disk2_initial_y), 8)
            disk2.setFill('green')
            disk1.draw(game_win)
            disk2.draw(game_win)
            clickPoint=None
            clickPoint1=None
            while a!=0:
                # Check disk coordinates
                if disk1!=None:
                    disk1_center=disk1.getCenter()
                    disk1_x=disk1_center.getX()
                    disk1_y=disk1_center.getY()
                if disk2!=None:
                    disk2_center=disk2.getCenter()
                    disk2_x=disk2_center.getX()
                    disk2_y=disk2_center.getY()
                # Check if user clicks a disk
                if clickPoint==None:
                    clickPoint=game_win.checkMouse()
                    if clickPoint:
                        # Creative Part 1- Limiting number of shots, increment
                        #  shots taken
                        shots+=1
                        # change color of bullets to red to indicate that the shot has been used
                        if shots<=5:
                            bullets[shots-1].setFill('red')
                # Creative Part 1- Limiting number of shots, do not allow user
                #  to shoot if they used up 5 shots
                if clickPoint!=None and disk1!=None and shots<=5:
                    dist1=dist(clickPoint, disk1_center)
                    if dist1<=8 and disk1!=None:
                        disk1.undraw()
                        disk1=None
                        a=a-1
                        # Add score of .5
                        score+=.5
                # Creative Part 1- Limiting number of shots, do not allow user
                #  to shoot if they used up 5 shots    
                if clickPoint!=None and disk2!=None and shots<=5:
                    dist2=dist(clickPoint, disk2_center)
                    if dist2<=8 and disk2!=None:
                        disk2.undraw()
                        a=a-1
                        disk2=None
                        # Add score of .5
                        score+=.5
                dist1, dist2=0, 0
                # Increment time
                time+=.02
                # Undraw Froggy if off the screen
                if (disk1_x>600 or disk1_x<0) and disk1!=None:
                    disk1.undraw()
                    a=a-1
                    disk1=None
                if (disk2_x<0 or disk2_x>600) and disk2!=None:
                    disk2.undraw()
                    a=a-1
                    disk2=None
                # Make Froggy Hop
                #  The team used a conditional that checked whether the froggy
                #  was touching the grass and if it existed. 
                if disk1_y>=450 and disk2_y>=450 and disk1!=None:
                    sleep(.5)
                    time=0
                elif disk1_y>=450 and disk1!=None:
                    sleep(.5)
                    time=0
                elif disk2_y>=450 and disk2!=None:
                    sleep(.5)
                    time=0
                # Increment dy
                dy=gravity**3*time**2-initial_dy-35
                # Animate disks
                if disk1!=None:
                    disk1.move(.25*dx, .01*dy)
                if disk2!=None:
                    disk2.move(-.25*dx, .01*dy)
                
                # Reset clickpoint and sleep
                clickPoint=None
                sleep(.005)
            d+=1
            a=2
            time=0
            sleep(.5)
            clickPoint=None
            lst[0].setFill('green')
    # If pull_type is single animate one target at a time 
    elif pull_type=='single':
        # Creative Part 1- Limiting number of shots, keep track of how many
        #  shots are taken 
        shots=0
        APG=[lst[6],lst[9],lst[12]]
        # first clay target x value chosen at random
        target1_x_pos=choice((0,600))
        target1= Circle(Point(target1_x_pos,randint(350,450)),8)
        target1.setFill("darkgrey")
        # target 2 starts at the opposite side of target 1
        if target1_x_pos==600:
            target2_x_pos=0
        else:
            target2_x_pos=600
        # create target 2
        target2= Circle(Point(target2_x_pos,randint(350,450)),8)
        target2.setFill("darkgrey")
        score,lst[5],shots=animate_single(target1,target1_x_pos,APG,game_win,lst[20],score,lst[5],bullets,shots)
        score,lst[5],shots=animate_single(target2,target2_x_pos,APG,game_win,lst[20],score,lst[5],bullets,shots)
    # Update scores and round number
    round_number=int(lst[4].getText())
    score_dict, round_dict=lst[21], lst[22]
    lst[5].setText(score)
    p_name=lst[3].getText()
    intermediate_score=float(lst[5].getText())
    try:
        p_score=score_dict[p_name]
    except KeyError:
        p_score=0
    p_score+=intermediate_score
    score_dict[p_name]=p_score
    lst[21]=score_dict
    try:
        round_dict[p_name]=round_dict[p_name]+1
    except KeyError:
        round_dict[p_name]=1
    lst[22]=round_dict
    update_high_score(lst)
    # Creative Part 5- Check score, determine what audio function to call
    #   If hit zero, call corresponding function
    if intermediate_score==0:
        # Call function
        audio_hit0()
    #   If hit one, call corresponding function
    if intermediate_score==0.5:
        # Call function
        audio_hit1()
    #   If hit two, call corresponding function
    if intermediate_score==1:
        # Call function
        audio_hit2()
    score_number=0
    p_name, p_score, p_lst='', 0, []
    round_number+=1
    lst[4].setText(round_number)
    # Update top scores dictionary
    top_scores_dict=lst[32]
                   
# Define score sorting key function
def s_scores(one_score):
    score1=float(one_score[1])
    return score1

# Define score dict sorting function
def dict_sort(mydict):
    items=list(mydict.items())
    items=sorted(items, key=s_scores, reverse=True)
    mydict1={}
    for i in items:
        name=i[0]
        mydict1[name]=i[1]
    return mydict1

# define main function
def main():
    game_win,bullets=game_window()
    win, lst=control_panel()
    control_panel_functionality(lst, game_win, win,bullets)

# Define update_high_score function
def update_high_score(lst):
    # Initialize variables
    score_dict, round_dict, top_scores_dict=lst[21], lst[22], lst[32]
    hs_file=open('top_scores.txt', 'w')
    print('Rank\tUsername\tScore\tRounds', file=hs_file)
    print('====================================', file=hs_file)
    score_dict=dict_sort(score_dict)
    lst[21]=score_dict
    intermediate_list=[]
    # Write top scores to file if more that 10 different players
    if len(score_dict)>10:
        for i in range(10):
            name=list(score_dict.keys())[i]
            real_score=float(score_dict[name])/int(round_dict[name])*100
            real_score=round(real_score, 2)
            period_index=str(real_score).find('.')
            after_decimal=str(real_score)[period_index+1:]
            if len(after_decimal)<2:
                after_decimal=after_decimal+'0'
            real_score=str(real_score)[:period_index]+'.'+str(after_decimal)
            top_scores_dict[name]=real_score
        top_scores_dict=dict_sort(top_scores_dict)
        for i in range(10):
            name=list(top_scores_dict.keys())[i]
            intermediate_list.append([i+1, name, top_scores_dict[name],
                                     round_dict[name]])
        for i in range(len(intermediate_list)-1):
            if float(intermediate_list[i][2])==float(intermediate_list[i+1][2]):
                if int(intermediate_list[i][3])>=int(intermediate_list[i+1][3]):
                    pass
                else:
                    intermediate_list[i][0], intermediate_list[i+1][0]=intermediate_list[i+1][0], intermediate_list[i][0]
                    intermediate_list[i], intermediate_list[i+1]=intermediate_list[i+1], intermediate_list[i]
        for i in intermediate_list:
            print(i[0], i[1], i[2], i[3], sep='\t', file=hs_file)
    # Write scores to file if 10 players or less
    else:
        for i in range(len(score_dict)):
            name=list(score_dict.keys())[i]
            real_score=float(score_dict[name])/int(round_dict[name])*100
            real_score=round(real_score, 2)
            period_index=str(real_score).find('.')
            after_decimal=str(real_score)[period_index+1:]
            if len(after_decimal)<2:
                after_decimal=after_decimal+'0'
            real_score=str(real_score)[:period_index]+"."+str(after_decimal)
            top_scores_dict[name]=real_score
        top_scores_dict=dict_sort(top_scores_dict)
        for i in range(len(score_dict)):
            name=list(top_scores_dict.keys())[i]
            intermediate_list.append([i+1, name, top_scores_dict[name],
                                     round_dict[name]])
        for i in range(len(intermediate_list)-1):
            if float(intermediate_list[i][2])==float(intermediate_list[i+1][2]):
                if int(intermediate_list[i][3])>=int(intermediate_list[i+1][3]):
                    pass
                else:
                    intermediate_list[i][0], intermediate_list[i+1][0]=intermediate_list[i+1][0], intermediate_list[i][0]
                    intermediate_list[i], intermediate_list[i+1]=intermediate_list[i+1], intermediate_list[i]
        for i in intermediate_list:
            print(i[0], i[1], i[2], i[3], sep='\t', file=hs_file)
    hs_file.close()   

# Creative Part 5- Play Audio Files
# Description: The audio files will provide positive or negative
#  feedback to the player based on the number of targets hit.
# Purpose: The team believed that more feedback would make the game more
#  engaging. The random selection from multiple files prevents the files
#  from becoming old and adds replay value to the game.

# Creative Part 5- Define audio function 1
#   Description: This function will play an audio clip randomly selected from
#    one of 5 audio files if the player fails to hit any targets. These
#    files correspond to how well the user performed. In this case, the
#    user will be humorously teased by the Simpsons characters.
def audio_hit0():
    # Randomly select a number from 0 to 4
    i=randint(0, 4)
    # Play corresponding .wav file
    if i==0:
        os.system('eat_my_short.wav')
    if i==1:
        os.system('laughing_stock1.wav')
    if i==2:
        os.system('sucks.wav')
    if i==3:
        os.system('what_is_this.wav')
    if i==4:
        os.system('alert.wav')
    # Display text as well. This part is for people who are deaf or users who
    #  use Macs.
    win1=GraphWin('Score Text Result', 300, 300)
    text1=Text(Point(150, 150), 'With that score, you will be the\nlaughing stock of the whole town!')
    text1.setStyle('bold')
    text1.setFill('brown')
    text1.draw(win1)
    sleep(3)
    win1.close()
    
# Creative Part 5- Define audio function 2
#   Description: This function will play an audio clip if the player
#    hits exactly one target. These files correspond to how well the user
#    performed. In this case, the user will be told that their performance "looks good."
def audio_hit1():
    # Play corresponding .wav file
    os.system('carvey_bush_looks_good.wav')
    # Display text as well. This part is for people who are deaf or users who
    #  use Macs.
    win1=GraphWin('Score Text Result', 300, 300)
    text1=Text(Point(150, 150), 'That score looks good.\nIt is not bad!')
    text1.setStyle('bold')
    text1.setFill('green')
    text1.draw(win1)
    sleep(3)
    win1.close()

# Creative Part 5- Define audio function 3
#   Description: This function will play an audio clip randomly selected
#    from one of 6 audio files if the player hits both targets. These
#    files correspond to how well the user performed. In this case, the
#    user will hear Robin exclaim, "Holy" something or Rosie O'Donnell's
#    approbation.
def audio_hit2():
    # Randomly select a number from 1 to 6
    i=randint(0,6)
    # Play corresponding .wav file
    if i==0:
        os.system('holy_alphabet.wav')
    if i ==1:
        os.system('holy_ball_and_chain.wav')
    if i==2:
        os.system('holy_fruit_salad.wav')
    if i==3:
        os.system('holy_heart_failure.wav')
    if i==4:
        os.system('holy_mashed_potatoes')
    if i==5:
        os.system('holy_nightmare.wav')
    if i==6:
        os.system('odonell_you_go_girl.wav')
    # Display text as well. This part is for people who are deaf or users who
    #  use Macs.
    win1=GraphWin('Score Text Result', 300, 300)
    text1=Text(Point(150, 150), 'Holy Beefaroni, Batman!\nThat is an amazing score!')
    text1.setStyle('bold')
    text1.setFill('deeppink')
    text1.draw(win1)
    sleep(3)
    win1.close()

   
main()
