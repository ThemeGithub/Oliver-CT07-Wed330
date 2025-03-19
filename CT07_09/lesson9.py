guess = int(input("Who will win? "))

import turtle as t
import random as r


# Main turtle stuff

window = t.Screen()
window.setup(width = 600, height = 600)
window.bgcolor("forestgreen")

drawer = t.Turtle()
drawer.fillcolor("orange")
drawer.shape("square")

# end line
drawer.up()
drawer.goto(-300, 250)
for i in range(25):
    drawer.stamp()
    drawer.forward(25)

# start line
drawer.goto(-300, -250)
drawer.pencolor("yellow")
drawer.seth(0)
drawer.down()
drawer.forward(600)
drawer.hideturtle()

# players
P1 = t.Turtle()
P2 = t.Turtle()
P3 = t.Turtle()
turtles = [P1, P2, P3]
colors = ["red", "lime", "cyan"]
names = ["P1", "P2", "P3"]
index = 0
for i in turtles:
    i.seth(90)
    i.up()
    i.shape("turtle")
    i.fillcolor(colors[index])
    i.pencolor(colors[index])
    i.goto(index * 200 - 200, -250)
    i.write(names[index], align = "center", font = ("Arial", 20))
    index = index + 1
    i.down()
winner = ""
index = 0
while True:
    for i in turtles:
        i.seth(r.randint(75, 115))
        i.forward(r.randint(5, 15))
        if i.ycor() > 250:
            winner = index + 1
        index = index + 1
    index = 0
    if winner != "":
        break
print(str(winner) + " won")
if winner == guess:
    print("u were correct")
else:
    print("u were dum")
    
window.mainloop()