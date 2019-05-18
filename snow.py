"""
    绘制雪花
"""
import turtle


def koch(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def snow(size, n):
    for i in range(3):
        koch(size, n)
        turtle.right(120)


def main():
    size, n = eval(input('请输入雪花的大小和阶数'))
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(3)
    snow(200, 3)
    turtle.hideturtle()
    turtle.exitonclick()


if __name__ == '__main__':
    main()
