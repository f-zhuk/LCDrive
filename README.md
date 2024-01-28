# LCDrive
This project shows what happens if you take an ordinary cycloidal reducer and unfold it into a straight line
Well, not so straight actually

The actuator is made out of four plates, two of which are guiding plates for alignment and two are pushing sliders.
In this device, sliders travel in circles with a radius of 1mm relative to the alignment plate. Sliders are 180 degrees out of phase.
Travel trajectory is defined by eccentrics mounted on shafts of two motors that run synchronously.
All plates have slots. Sliders have cycloidal cutouts, alignments have linear path cutouts. 

Now let’s add the carriage. All cutouts have a width equal to pin's diameter. The pin is ideally an integral part of the carriage and it engages with the edges of the cutouts. Cutouts in all plates define the exact position of the pin at every moment in time.

Pin and carriage respectively are pushed along the axis with the motors rotation.

In total one full rotation gives 2π (6.28) millimeters of travel or 10 mm of useful travel corresponds to 1.59 revolutions. In full step mode it takes 32 steps for one revolution of the internal shaft and 64*63.68395~4076 steps for the main shaft. This means that ideally it takes around 6487 steps to cover the whole 10 mm range or in other words, it is 1.54 micron movement per step in an ideal world.

Since I am not satisfied with current situation with parametric curves and offset tools in FreeCAD I wrote a small Python script to generate SVGs for import. Extruded pads I have prototyped with FDM which took me a couple of iterations. Then I milled my parts with a 1mm endmill out of 2mm aluminum strip. Using FreeCAD as a CAM has its drawbacks and at this point I think it might be reasonable to generate G-code in the same Python script skipping the FreeCAD part.

Advantages: 

1. No screw drive
2. Slim design
3. Great step distance

Disadvantages:

1. Large backlash
2. High resistance resulting in low pushing force

Possible improvements:

1. Add one more phase to get a 120-degree difference between moving slides
2. Add miniature bearings
3. Motor synchronization and feedback
