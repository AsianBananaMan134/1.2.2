# a122_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

wn = trtl.Screen()
wn.bgcolor("aquamarine2")

#-----leaderboard variables-----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----manages the leaderboard for top 5 scorers-----
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----others-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
spot.speed(0)
score_writer.speed(0)

#-----start game function-----
game_start = False
start = trtl.Turtle()
start.shape("circle")
start.shapesize(5)
start.color("lime")

def start_game(x,y):
  global game_start
  game_start = True
  start.hideturtle()
start.onclick(start_game)

while not game_start:
  spot.hideturtle()
spot.showturtle()

#-----lists-----
color_list = ["red", "blue", "yellow", "DarkGreen","DarkOrange","black","azure","DarkOrchid1","DeepPink3","DarkSlateGray4"]
size_list = [0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle() 
counter.speed(0)
# -----game configuration----
spot_shape = "triangle"
spot_color = "blue"
spot_fill_color = "blue"
score = 0 

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-250,250)
score_writer.pendown()

font_setup = ("Arial", "20", "normal")

# -----initialize turtle-----
spot.shape(spot_shape)
spot.color(spot_color)
spot.fillcolor(spot_fill_color)

def change_color():
  spot.color(rand.choice(color_list))
  spot.stamp()
  spot.color("blue")

def change_size():
  spot.shapesize(rand.choice(size_list))

def spot_clicked(x, y):
  global timer 
  if timer_up == False:
    updated_score()
    change_color()
    change_size()
    change_position()

def updated_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font = font_setup)

def change_position():
  spot.penup()
  new_xpos = rand.randint(-150,150)
  new_ypos = rand.randint(-200,200)
  spot.goto(new_xpos, new_ypos)

#-----make rectange for timer-----
t = trtl.Turtle()
#-----make a rectangle box for the score-----
t.penup()
t.goto(-300,250)
t.pendown()

def make_timer():
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.hideturtle()
  
def make_big_rectangle():
  counter.forward(150)
  counter.left(90)
  counter.forward(50)
  counter.left(90)
  counter.forward(150)
  counter.left(90)
  counter.forward(50)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    spot.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# -----make the timer box-----
counter =  trtl.Turtle() 
t.penup() 
t.pendown()
make_timer()
counter.penup()
counter.goto(200,250)
counter.pendown()
make_big_rectangle()
t.hideturtle()
counter.hideturtle()
countdown()

# -----events----------------
spot.onclick(spot_clicked)

wn.mainloop()
wn.ontimer(countdown, counter_interval)
