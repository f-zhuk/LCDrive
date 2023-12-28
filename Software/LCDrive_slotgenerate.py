from math import sin, cos, pi
import time
import svgwrite
from svgwrite import cm, mm
import tkinter as tk
import tksvg

length_total=100
height_total=30
travel=10
axle_border=7
ecc_radius=1
pin_radius=1
sectors=18

def slot_line(svgdwg, x_center, y_center, length):
    #dy= (y_end-y_center)/(x_end-x_center)
    points=[(x_center-length/2, y_center+pin_radius)]
    for i in range(sectors+1, 3*sectors, 1):
        points.append((x_center-length/2+cos(i/2/sectors*pi)*pin_radius, y_center+sin(i/2/sectors*pi)*pin_radius))
    
    for i in range(-sectors, sectors, 1):
        points.append((x_center+length/2+cos(i/2/sectors*pi)*pin_radius, y_center+sin(i/2/sectors*pi)*pin_radius))

    #point = (x_center, y_center)
    #points = [point]
    #point = (x_end, y_end)
    #points.append(point)
    #svgdwg.polyline(points, stroke='black', stroke_width=0.1, fill='none')
    return svgdwg.polygon(points, stroke='black', stroke_width=0.1, fill='none')

def slot_cycl(svgdwg, x_center, y_center):
    #center cap
    points=[(x_center-pin_radius, y_center-pin_radius)]
    for i in range(2*sectors+1, 4*sectors, 1):
        points.append((x_center+cos(i/2/sectors*pi)*pin_radius, y_center-ecc_radius+sin(i/2/sectors*pi)*pin_radius))
    #inner right
    inner_ecc_radius=1-pin_radius/pi
    for i in range(1, 4*sectors, 1):
        points.append((x_center+pin_radius+inner_ecc_radius*(i/2/sectors*pi-sin(i/2/sectors*pi)), y_center-ecc_radius+(ecc_radius-pin_radius/2)*(1-cos(i/2/sectors*pi))))
    #right cap
    for i in range(2*sectors+1, 4*sectors, 1):
        points.append((x_center+ecc_radius*2*pi+cos(i/2/sectors*pi)*pin_radius, y_center-ecc_radius+sin(i/2/sectors*pi)*pin_radius))
    #outer right
    outer_ecc_radius=1+pin_radius/pi
    intersection=8
    for i in range(4*sectors-1, 0, -1):
        if x_center-pin_radius+outer_ecc_radius*(i/2/sectors*pi-sin(i/2/sectors*pi)) > x_center :
            intersection=i
            points.append((x_center-pin_radius+outer_ecc_radius*(i/2/sectors*pi-sin(i/2/sectors*pi)), y_center-ecc_radius+(ecc_radius+pin_radius/2)*(1-cos(i/2/sectors*pi))))
    #outer left   
    for i in range(intersection, 4*sectors-1, 1):
        points.append((x_center+pin_radius-outer_ecc_radius*(i/2/sectors*pi-sin(i/2/sectors*pi)), y_center-ecc_radius+(ecc_radius+pin_radius/2)*(1-cos(i/2/sectors*pi))))
    #left cap
    for i in range(2*sectors+1, 4*sectors, 1):
        points.append((x_center-ecc_radius*2*pi+cos(i/2/sectors*pi)*pin_radius, y_center-ecc_radius+sin(i/2/sectors*pi)*pin_radius))        
    #inner left
    for i in range(4*sectors-1, 0, -1):
        points.append((x_center-pin_radius-inner_ecc_radius*(i/2/sectors*pi-sin(i/2/sectors*pi)), y_center-ecc_radius+(ecc_radius-pin_radius/2)*(1-cos(i/2/sectors*pi))))

    return svgdwg.polygon(points, stroke='black', stroke_width=0.1, fill='none')

#
window = tk.Tk()
#Base
dwg = svgwrite.Drawing('/home/fedorzhuk/Documents/GitHub/LCDrive/Software/base.svg', size=('100mm', '30mm'), viewBox=('0 0 100 30'), profile='tiny')

outline=dwg.rect((0, 0), (length_total, height_total), stroke='black', stroke_width=0.1, fill='none')
left_axle=dwg.circle(center=(axle_border, height_total/2), r=2.5,  stroke='black', stroke_width=0.1, fill='none')
right_axle=dwg.circle(center=(length_total-axle_border, height_total/2), r=2.5,  stroke='black', stroke_width=0.1, fill='none')

dwg.add(outline)
dwg.add(left_axle)
dwg.add(right_axle)
dwg.add(slot_line(dwg, length_total/2-10, height_total/2-10, travel))
dwg.add(slot_line(dwg, length_total/2+10, height_total/2-10, travel))
dwg.add(slot_line(dwg, length_total/2-10, height_total/2+10, travel))
dwg.add(slot_line(dwg, length_total/2+10, height_total/2+10, travel))
dwg.save()
#Slot
dwg = svgwrite.Drawing('/home/fedorzhuk/Documents/GitHub/LCDrive/Software/slot.svg', size=('100mm', '30mm'), viewBox=('0 0 100 30'), profile='tiny')
outline=dwg.rect((0, 0), (length_total-2*ecc_radius, height_total), stroke='black', stroke_width=0.1, fill='none')
left_axle=dwg.circle(center=(axle_border-ecc_radius, height_total/2), r=5,  stroke='black', stroke_width=0.1, fill='none')
right_axle=dwg.circle(center=(length_total-axle_border-ecc_radius, height_total/2), r=5,  stroke='black', stroke_width=0.1, fill='none')

dwg.add(outline)
dwg.add(left_axle)
dwg.add(right_axle)
dwg.add(slot_cycl(dwg, length_total/2-10-ecc_radius*pi/2, height_total/2-10))
dwg.add(slot_cycl(dwg, length_total/2+10-ecc_radius*pi/2, height_total/2-10))
dwg.add(slot_cycl(dwg, length_total/2-10-ecc_radius*pi/2, height_total/2+10))
dwg.add(slot_cycl(dwg, length_total/2+10-ecc_radius*pi/2, height_total/2+10))
dwg.save()

svg_image = tksvg.SvgImage( file = '/home/fedorzhuk/Documents/GitHub/LCDrive/Software/slot.svg', scaletoheight = 200 )

tk.Label( image = svg_image ).pack()
window.title("LCDrive_slotgenerate")
window.geometry('1000x600')
window.configure(background="white")
text = tk.StringVar()
text.set("LCDrive.svg")
greeting = tk.Label(window, bg="white", textvariable=text, font=("Montserrat Light", 20))
#greeting.place(relx = 0.5, rely = 0.5, anchor = 'center')

greeting.pack()
window.update()

new_frame = None
while True:
    #print
    window.update()
    time.sleep(0.1)

#window.mainloop() 
