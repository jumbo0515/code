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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
switch = False


def main():
    global switch
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    lives_label = GLabel('lives: ' + str(lives))
    graphics.window.add(lives_label, x=graphics.window.width - lives_label.width, y=lives_label.height)
    total_bricks = graphics.total_bricks
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        ball_dx = graphics.get_ball_dx()
        ball_dy = graphics.get_ball_dy()
        graphics.ball.move(ball_dx, ball_dy)
        graphics.bounce()
        graphics.detect_collision()
        if graphics.ball.y > graphics.window.height - graphics.ball.height:
            graphics.reset_ball()
            lives -= 1
            lives_label.text = 'Lives: ' + str(lives)
        if lives == 0 or graphics.score == total_bricks:
            break


if __name__ == '__main__':
    main()
