"""
File: babygraphics.py
Name: Jumbo feat. Amelia and jay
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    each_x = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS) - 1
    x_coord = GRAPH_MARGIN_SIZE + each_x * year_index
    return x_coord


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE
                       , width=LINE_WIDTH, fill='black')   # 第一條左右的線
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')  # 第二條左右的線
    for year_index in range(len(YEARS)):    # 上下的線
        x_coord = get_x_coordinate(CANVAS_WIDTH, year_index)
        year = YEARS[year_index]
        canvas.create_text(x_coord + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=year,  anchor=tkinter.NW)
        canvas.create_line(x_coord, GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE, x_coord, CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_order = 0  # 從0開始,四個顏色重複循環
    for name in lookup_names:
        color = COLORS[color_order]  # COLORS list中放入0,1,2,3的編碼
        for i in range(len(YEARS) - 1):  # 兩點連成一線,最後一點沒有人跟他接,所以做到YEARS-1
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)
            y_dish = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000     # 前1000名  在高度的y軸中分成1000格
            if str(YEARS[i]) in name_data[name]:    # 年在名字內(排名在1000內)
                y1 = int(name_data[name][str(YEARS[i])]) * y_dish  # 獲取名字name在年份YEARS[i]的排名,用int將排名轉換為整數原本是list
                s1 = int(name_data[name][str(YEARS[i])])
            else:  # 排名超過1000
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2
                s1 = ' *'
            if str(YEARS[i+1]) in name_data[name]:  # 第二個點
                y2 = int(name_data[name][str(YEARS[i+1])]) * y_dish  # y_dish 是為了讓取得的數字在正確的排序,不加的話高度只有600
            else:  # 排名超過1000
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2

            canvas.create_text(x1+TEXT_DX, y1 + GRAPH_MARGIN_SIZE, text=name+' '+str(s1), anchor=tkinter.SW, fill=color)
            canvas.create_line(x1, y1+GRAPH_MARGIN_SIZE, x2, y2+GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)
        canvas.create_text(x2 + TEXT_DX, y2 + GRAPH_MARGIN_SIZE, text=name + ' ' + str(s1), anchor=tkinter.SW,
                           fill=color)   # 製造最後一個點的文字
        if color_order < len(COLORS)-1:   # 0,1,2 (因為顏色是四個形成一個循環,所以不能超過3,不然3+1=4,要讓4回到0
            color_order += 1
        else:  # 3
            color_order = 0  # 第4個數歸零


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
