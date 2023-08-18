"""
File: bouncing_ball
Name:Jumbo feat.Amelia
-------------------------
Write down the ball landing and bouncing process, and add a switch and limit the number of bouncing completions
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # 球的水平速度
DELAY = 10  # 動畫暫停
GRAVITY = 1  # 重力加速度
SIZE = 20  # 球的大小
REDUCE = 0.9  # 每一次反彈時，在垂直速度所剩之比例
START_X = 30  # 球的起始 x 座標
START_Y = 40  # 球的起始 y 座標

window = GWindow(width=800, height=500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)

switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch
    ball.filled = True
    ball.fill_color = 'blue'
    window.add(ball)
    onmouseclicked(event)
    vy = 0  # 垂直速度
    bounce_count = 0  # 碰撞次數

    while True:
        pause(DELAY)
        if switch:
            while True:
                vy += GRAVITY   # 更新垂直速度
                if ball.y + SIZE > window.height:   # 與地板碰撞
                    ball.y = window.height - SIZE   # 球碰到地板
                    vy = -vy * REDUCE                # 反彈,垂直速度取負值
                if ball.x > window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    vy = 0
                    bounce_count += 1
                    switch = False
                    break
                if bounce_count >= 3:
                    ball.x = START_X
                    ball.y = START_Y
                    vy = 0
                    switch = False
                    break
                ball.move(VX, vy)
                pause(DELAY)


def event(mouse):
    global ball, switch
    switch = True


if __name__ == "__main__":
    main()
