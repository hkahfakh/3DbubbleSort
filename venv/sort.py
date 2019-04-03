from turtle import *
from random import *
import time


def bubble_sort(rectangle_list):
    for passnum in range(0, 10 - 1):
        for i in range(0, 10 - passnum - 1, 1):
            if rectangle_list[i].num > rectangle_list[i + 1].num:
                rectangle_list[i].replace(rectangle_list[i + 1])
                time.sleep(0.5)  # 休眠1秒



class Cube():
    def __init__(self, x, y, num, leng=10):
        self.x = x
        self.y = y
        self.num = num
        self.side_len = leng
        self.create_cube()

    def create_side(self):
        fillcolor("#639CD3")
        begin_fill()
        left(170)
        forward(self.side_len)

        right(80)
        forward(20 * self.num)

        right(100)
        forward(self.side_len)

        right(80)
        forward(20 * self.num)
        end_fill()

        setheading(0)  # 恢复向右默认

    def create_top(self):
        fillcolor("#95CEFF")

        penup()
        goto(self.x, self.y + 20 * self.num)
        pendown()

        begin_fill()

        forward(20)

        left(170)
        forward(self.side_len)

        left(10)
        forward(20)

        left(170)
        forward(self.side_len)
        end_fill()
        setheading(0)  # 恢复向右默认

    def create_rectangle(self):
        color("#639CD3")

        penup()
        goto(self.x, self.y)
        pendown()

        fillcolor("#7CB5E6")
        begin_fill()
        for x in range(1, 5):
            if x % 2 == 1:
                n = 20
            else:
                n = 20 * self.num
            forward(n)
            left(90)
        end_fill()

    def create_cube(self):
        tracer(False)
        self.create_rectangle()
        self.create_side()
        self.create_top()
        tracer(True)

    def erase_rectangle(self):
        setheading(0)
        color("white")

        penup()
        goto(self.x, self.y)
        pendown()

        fillcolor("white")
        begin_fill()
        for x in range(1, 5):
            if x % 2 == 1:
                n = 20
            else:
                n = 20 * self.num
            forward(n)
            left(90)
        end_fill()

    def erase_side(self):
        fillcolor("white")
        begin_fill()
        left(170)
        forward(self.side_len)

        right(80)
        forward(20 * self.num)

        right(100)
        forward(self.side_len)

        right(80)
        forward(20 * self.num)
        end_fill()

        setheading(0)  # 恢复向右默认

    def erase_top(self):
        fillcolor("white")

        penup()
        goto(self.x, self.y + 20 * self.num)
        pendown()

        begin_fill()
        forward(20)

        left(170)
        forward(self.side_len)

        left(10)
        forward(20)

        left(170)
        forward(self.side_len)
        end_fill()
        setheading(0)  # 恢复向右默认

    def erase_cube(self):
        tracer(False)
        self.erase_rectangle()
        self.erase_side()
        self.erase_top()
        tracer(True)

    def replace(self, n):
        self.erase_cube()
        n.erase_cube()
        self.num, n.num = n.num, self.num
        self.create_cube()
        n.create_cube()


if __name__ == '__main__':

    hideturtle()

    # Cube(35 * 1, 0, randint(1, 10))

    var = list()
    for i in range(0, 10):
        var.append(Cube(35 * i, 0, randint(1, 10)))

    bubble_sort(var)

    done()
