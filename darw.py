from Focus_Roots import *

def change():
    set_background(color_sky_blue)
    draw_circle(x=0, y=0, radius=100, width=0, color=color_yellow)
    draw_rect(top=0, left=400, width=500, height=200, draw_width=0, color=color_emeraldgreen)
    draw_rect(top=50, left=150, width=300, height=250, draw_width=0, color=color_firebrick)
    draw_rect(top=25, left=110, width=350, height=40, draw_width=0, color=color_brown)
    draw_rect(top=50, left=80, width=300, height=40, draw_width=0, color=color_brown)
    draw_rect(top=150, left=250, width=100, height=150, draw_width=0, color=color_chocolate)
    draw_circle(x=235, y=340, radius=10, width=0, color=color_yellow)
    write_text("A House",200,50,50,color=color_white)

    #draw_circle(220,300,10,0,color=color_aqua)

draw(change)