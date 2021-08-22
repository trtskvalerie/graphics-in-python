import graphics as gr


def main():
    win = gr.GraphWin('very wholesome', 1280, 720)
    draw_image(win)
    win.getMouse()
    win.close()


def draw_image(win):
    house_x, house_y = win.width//2, win.height*2//3
    house_h = win.width//3
    house_w = house_h*4//3

    draw_bg(win)
    draw_house(win, house_x, house_y, house_w, house_h)


def draw_bg(win):
    ground = gr.Rectangle(gr.Point(0, win.height//2), gr.Point(win.width-1, win.height-1))
    ground.setOutline(gr.color_rgb(0, 102, 0))
    ground.setFill(gr.color_rgb(0, 102, 0))
    ground.draw(win)

    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(win.width, win.height//2))
    sky.setOutline(gr.color_rgb(0, 128, 255))
    sky.setFill(gr.color_rgb(0, 128, 255))
    sky.draw(win)


def draw_house(win, x, y, w, h):
    walls_w, walls_h = w, h*3//4
    roof_w, roof_h = w, h-walls_h
    walls_x, walls_y = x, y
    roof_x, roof_y = x, y-walls_h

    draw_walls(win, walls_x, walls_y, walls_w, walls_h)
    draw_roof(win, roof_x, roof_y, roof_w, roof_h)


def draw_walls(win, x, y, w, h):
    walls = gr.Rectangle(gr.Point(x-w//2, y), gr.Point(x+w//2, y-h))
    walls.setOutline(gr.color_rgb(224, 244, 224))
    walls.setFill(gr.color_rgb(224, 244, 224))
    walls.draw(win)

    door_x, door_y = x, y
    door_w, door_h = w//6, h//3
    window_x, window_y = x+w//4, y-h//2
    window_w, window_h = w//5, h//3

    draw_door(win, door_x, door_y, door_w, door_h)
    draw_window(win, window_x, window_y, window_w, window_h)


def draw_roof(win, x, y, w, h):
    roof = gr.Polygon(gr.Point(x-w//2-25, y), gr.Point(x+w//2+25, y), gr.Point(x, y-h))
    roof.setOutline(gr.color_rgb(102, 51, 0))
    roof.setFill(gr.color_rgb(102, 51, 0))
    roof.draw(win)


def draw_door(win, x, y, w, h):
    door = gr.Rectangle(gr.Point(x-w//2, y), gr.Point(x+w//2, y-h))
    door.setOutline(gr.color_rgb(51, 25, 0))
    door.setFill(gr.color_rgb(51, 25, 0))
    door.draw(win)


def draw_window(win, x, y, w, h):
    window = gr.Rectangle(gr.Point(x-w//2, y), gr.Point(x+w//2, y-h))
    window.setOutline(gr.color_rgb(51, 25, 0))
    window.setFill(gr.color_rgb(51, 25, 0))
    window.draw(win)

    glass_x, glass_y = x, y-10
    glass_w, glass_h = w-20, h-20

    draw_glass_in_window(win, glass_x, glass_y, glass_w, glass_h)


def draw_glass_in_window(win, x, y, w, h):
    glass = gr.Rectangle(gr.Point(x-w//2, y), gr.Point(x+w//2, y-h))
    glass.setOutline(gr.color_rgb(153, 255, 255))
    glass.setFill(gr.color_rgb(153, 255, 255))
    glass.draw(win)


if __name__ == "__main__": main()