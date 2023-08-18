"""
File: bouncing_ball
Name:Jumbo feat.Amelia, Jay
-------------------------
The brick breaking game is divided into user end and code end to execute
"""

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=self.window.width / 2 - self.paddle.width / 2,
                        y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width / 2 - self.ball.width / 2,
                        y=self.window.height / 2 - self.ball.height / 2)

        # 計分表
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.star)

        # Draw bricks
        for x in range(brick_cols):
            for y in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                if y < 2:
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                if 2 <= y < 4:
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                if 4 <= y < 6:
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                if 6 <= y < 8:
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                if 8 <= y < 10:
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=(brick_spacing + brick_width) * x,
                                y=brick_offset + (brick_height + brick_spacing) * y)

        self.total_bricks = brick_cols * brick_rows
        self.brick_height = brick_height
        self.brick_width = brick_width

    def bounce(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def get_ball_dx(self):
        return self.__dx

    def get_ball_dy(self):
        return self.__dy

    def paddle_position(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def star(self, mouse):
        if self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def detect_collision(self):
        # 球的位置和半徑
        x = self.ball.x
        y = self.ball.y
        r = self.ball.width / 2

        # 檢查四角是否碰撞
        top_left = self.window.get_object_at(x, y)
        top_right = self.window.get_object_at(x+2*r, y)
        bottom_left = self.window.get_object_at(x, y+2*r)
        bottom_right = self.window.get_object_at(x+2*r, y+2*r)

        # 檢查碰撞並執行動作
        if top_left is not None:
            self.handle_collision(top_left)
        elif top_right is not None:
            self.handle_collision(top_right)
        elif bottom_left is not None:
            self.handle_collision(bottom_left)
        elif bottom_right is not None:
            self.handle_collision(bottom_right)

    def handle_collision(self, obj):
        if obj == self.paddle:
            # 球與板子碰撞，球反彈
            if self.__dy > 0:
                self.__dy = -self.__dy
        elif obj.width == self.brick_width and obj.height == self.brick_height:
            # 球與磚塊碰撞，球反彈並移除磚塊
            self.__dy = -self.__dy
            self.window.remove(obj)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

    def reset_ball(self):
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2
        self.__dx = 0
        self.__dy = 0






