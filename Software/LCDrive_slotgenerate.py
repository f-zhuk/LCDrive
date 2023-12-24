from math import sin, cos, pi
import time
import svgwrite
import tkinter as tk
import tksvg

#
window = tk.Tk()
#svg_image = tksvg.SvgImage( file = '/ABCDEF.svg' )
dwg = svgwrite.Drawing('C:/Users/Fedor/Documents/GitHub/LCDrive/Software/slot.svg', profile='tiny')
points = [(200 + i * cos(i / 10), 200 + i * sin(i / 10)) for i in range(100)]
dwg.add(dwg.polyline(points, stroke='blue', fill='none'))
dwg.save()

svg_image = tksvg.SvgImage( file = 'C:/Users/Fedor/Documents/GitHub/LCDrive/Software/slot.svg', scaletoheight = 200 )

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
