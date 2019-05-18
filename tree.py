"""
利用递归函数绘制分形树
"""
import turtle


def draw_branch(length, size):
    """
     绘制分形树
    """
    turtle.pensize(size)
    # 绘制右侧树枝
    if length >= 5:
        if length <= 20:
            turtle.color('green')
        else:
            turtle.color('brown')
        turtle.forward(length)
        print('向前 ', length)
        turtle.right(20)
        print('右转 20°')
        draw_branch(length - 15, size - 1)
        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40°')
        draw_branch(length - 15, size - 1)
        # 返回之前的树枝
        turtle.right(20)
        print('右转 20°')
        turtle.backward(length)
        print('后退 ', length)


def main():
    turtle.color('brown')
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    length = 100
    size = 8
    draw_branch(length, size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
