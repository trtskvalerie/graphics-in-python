import graphics as gr


def main():
    win = gr.GraphWin('nudes', 310, 180)
    draw_message(win)
    win.getMouse()
    win.close()


def draw_message(win):
    send_x, send_y = 40, 10
    nudes_x, nudes_y = 10, 100

    draw_send(win, send_x, send_y)
    draw_nudes(win, nudes_x, nudes_y)


def draw_send(win, x, y):
    draw_s(win, x, y)
    x = get_next_x(x)
    draw_e(win, x, y)
    x = get_next_x(x)
    draw_n(win, x, y)
    x = get_next_x(x)
    draw_d(win, x, y)


def draw_nudes(win, x, y):
    draw_n(win, x, y)
    x = get_next_x(x)
    draw_u(win, x, y)
    x = get_next_x(x)
    draw_d(win, x, y)
    x = get_next_x(x)
    draw_e(win, x, y)
    x = get_next_x(x)
    draw_s(win, x, y)


def draw_s(win, x, y):
    stroke_1 = gr.Rectangle(gr.Point(x, y), gr.Point(x+50, y+10))
    stroke_2 = gr.Rectangle(gr.Point(x, y+30), gr.Point(x+50, y+40))
    stroke_3 = gr.Rectangle(gr.Point(x, y+60), gr.Point(x+50, y+70))
    stroke_4 = gr.Rectangle(gr.Point(x, y), gr.Point(x+20, y+40))
    stroke_5 = gr.Rectangle(gr.Point(x+30, y+30), gr.Point(x+50, y+70))
    stroke_6 = gr.Rectangle(gr.Point(x+30, y), gr.Point(x+50, y+20))
    stroke_7 = gr.Rectangle(gr.Point(x, y+50), gr.Point(x+20, y+70))

    stroke_1.setFill('black')
    stroke_2.setFill('black')
    stroke_3.setFill('black')
    stroke_4.setFill('black')
    stroke_5.setFill('black')
    stroke_6.setFill('black')
    stroke_7.setFill('black')

    stroke_1.draw(win)
    stroke_2.draw(win)
    stroke_3.draw(win)
    stroke_4.draw(win)
    stroke_5.draw(win)
    stroke_6.draw(win)
    stroke_7.draw(win)


def draw_e(win, x, y):
    stroke_1 = gr.Rectangle(gr.Point(x, y), gr.Point(x+50, y+10))
    stroke_2 = gr.Rectangle(gr.Point(x, y+30), gr.Point(x+50, y+40))
    stroke_3 = gr.Rectangle(gr.Point(x, y+60), gr.Point(x+50, y+70))
    stroke_4 = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))

    stroke_1.setFill('black')
    stroke_2.setFill('black')
    stroke_3.setFill('black')
    stroke_4.setFill('black')

    stroke_1.draw(win)
    stroke_2.draw(win)
    stroke_3.draw(win)
    stroke_4.draw(win)


def draw_n(win, x, y):
    stroke_1 = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))
    stroke_2 = gr.Rectangle(gr.Point(x+40, y), gr.Point(x+50, y+70))
    stroke_3 = gr.Polygon(gr.Point(x+10, y), gr.Point(x+10, y+20), gr.Point(x+40, y+70), gr.Point(x+40, y+50))

    stroke_1.setFill('black')
    stroke_2.setFill('black')
    stroke_3.setFill('black')

    stroke_1.draw(win)
    stroke_2.draw(win)
    stroke_3.draw(win)


def draw_d(win, x, y):
    stroke_1 = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))
    stroke_2 = gr.Rectangle(gr.Point(x, y), gr.Point(x+40, y+10))
    stroke_3 = gr.Rectangle(gr.Point(x, y+60), gr.Point(x+40, y+70))
    stroke_4 = gr.Rectangle(gr.Point(x+40, y+10), gr.Point(x+50, y+60))

    stroke_1.setFill('black')
    stroke_2.setFill('black')
    stroke_3.setFill('black')
    stroke_4.setFill('black')

    stroke_1.draw(win)
    stroke_2.draw(win)
    stroke_3.draw(win)
    stroke_4.draw(win)


def draw_u(win, x, y):
    stroke_1 = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))
    stroke_2 = gr.Rectangle(gr.Point(x+40, y), gr.Point(x+50, y+70))
    stroke_3 = gr.Rectangle(gr.Point(x, y+60), gr.Point(x+50, y+70))

    stroke_1.setFill('black')
    stroke_2.setFill('black')
    stroke_3.setFill('black')

    stroke_1.draw(win)
    stroke_2.draw(win)
    stroke_3.draw(win)


def get_next_x(x): return x + 60


if __name__ == "__main__": main()