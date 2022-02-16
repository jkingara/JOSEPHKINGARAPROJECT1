import arcade

def main():
    arcade.open_window(1250, 700, "Yes We Can")
    arcade.set_background_color(arcade.color.RED)
    polygon = arcade.create_polygon([(20, 150), (20, 400), (150, 100)], arcade.color.RED)
    rectangle = arcade.create_rectangle(100, 550, 180, 180, arcade.color.WHITE)
    square = arcade.create_rectangle(500, 550, 290, 160, arcade.color.YELLOW_ROSE)
    ellipse = arcade.create_ellipse_filled(280, 280, 200, 200, arcade.color.AIR_FORCE_BLUE)
    ellipse2 = arcade.create_ellipse_filled(550, 270, 270, 200, arcade.color.FAWN)
    line = arcade.create_line(700, 700, 700, 20, arcade.color.ALMOND)
    text = arcade.draw_text("SHAPES AND SIZES", 730, 600, arcade.color.ANTIQUE_BRONZE, 20)



    rectangle.draw()
    square.draw()
    ellipse.draw()
    ellipse2.draw()
    line.draw()
    polygon.draw()
    arcade.run()



main()
