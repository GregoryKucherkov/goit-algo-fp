import turtle
import math


def draw_pythagoras_tree(t, order, size):
    if order == 0:
        return
        
    else:
        t.forward(size / math.sqrt(2))
        t.left(45)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.right(90)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.left(45)
        t.backward(size / math.sqrt(2))

def pythagoras_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    #t.goto(-size / 2, size / 2)
    t.goto(-size / 2 , -size / 2 - 50) 
    t.left(90)
    t.pendown()
    draw_pythagoras_tree(t, order, size)
    window.mainloop()


def main():
    order = int(input('Enter the integer to determine the recursion depth: '))
    pythagoras_tree(order)

if __name__ == "__main__":
    main()

