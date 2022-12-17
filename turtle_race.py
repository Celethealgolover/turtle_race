from turtle import Turtle,Screen
from random import randint
t=Turtle()
s=Screen()
r=Screen()
t.color("yellow")
s.setup(1500,900)
p=s.textinput(title="Pe care pariezi?",prompt="Alege culoarea:")
colors=["red","yellow","blue","orange","purple","green"]
y_pos=[-360,-220,-80,60,200,340]
ls=[]
for x in range(6):
    nt=Turtle(shape="turtle")
    nt.color(colors[x])
    nt.penup()
    nt.speed(20)
    nt.goto(-700,y_pos[x])
    ls.append(nt)
def roen(s):
    if s=="rosu":
        return "red"
    elif s=="galben":
        return "yellow"
    elif s=="albastru":
        return "blue"
    elif s=="portocaliu":
        return "orange"
    elif s=="mov":
        return "purple"
    elif s=="verde":
        return "green"
def enro(s):
    if s=="red":
        return "rosu"
    elif s=="yellow":
        return "galben"
    elif s=="blue":
        return "albastru"
    elif s=="orange":
        return "portocaliu"
    elif s=="purple":
        return "mov"
    elif s=="green":
        return "verde"
def rrace():
  race=True
  while race==True:
      for x in ls:
        if x.xcor()>700:
            race=False
            winner=x.color()
            if winner[0]==roen(p):
                r.textinput(title="Felicitari!", prompt=f"{enro(winner[0])} a castigat!")
            else:
                r.textinput(title="Din pacate ai pierdut!", prompt=f"{enro(winner[0])} a castigat!")
        n=randint(0,20)
        x.forward(n)
s.listen()
s.onkey(rrace,"space")
s.exitonclick()