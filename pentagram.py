import turtle


def draw_pentagram(size):
    """
     绘制五角星
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def pentagram(size):
    """
    迭代绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

    # 五角星绘制完成，更新参数
    size += 10
    if size <= 100:
        pentagram(size)


def main():
    turtle.color('blue')
    size = 50
    pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
