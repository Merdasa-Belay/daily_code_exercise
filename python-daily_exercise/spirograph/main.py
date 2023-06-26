import turtle as t
import random
eyob = t.Turtle()
t.colormode(255)



def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  color = (r, g, b)

  return color

eyob.speed("fastest")
for _ in range(100):
  eyob.color(random_color())
  eyob.circle(90)
  eyob.right(6)
  eyob.forward(1)







screen = t.Screen()
screen.exitonclick()