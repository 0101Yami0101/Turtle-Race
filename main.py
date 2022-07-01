#The Turtle race
from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make Your Bet", prompt= "Which one will win.. Pick a color: ")
# print(user_bet)

colors = ["violet","indigo", "blue", "green", "yellow", "orange", "red"]
defx = -200
defy = -100
all_turtles = []
race_on = False


for turtle_index in range(0,7):
    newTurt = Turtle('turtle')
    newTurt.penup()
    newTurt.color(colors[turtle_index])
    newTurt.goto(defx, defy)
    all_turtles.append(newTurt)
    defy +=30

        
if user_bet:
    race_on = True
        
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 235:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won. The winner was {winner} ")
            else:
                print(f"You lost. The winner was {winner} ")

        rand_distance = random.randint(0,20)
        turtle.forward(rand_distance)


screen.exitonclick()

