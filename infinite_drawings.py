'''
lab3b.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

# Ex D.1: -->
def update(lsy, s):
    '''
    Generates the next version of the L-system string by applying the
    L-system rules to each character of the string.
    
    Arguments:       lsys: dictionary containing the starting string and rules
                     s:    a L-system string
                     
    Return value:    Final L-system string
    '''
    new_string = ''
    for c in s:
        if c in lsy:
            new_string += lsy[c]
        else:
            new_string += c
    return new_string

            
# Ex D.2: -->
def iterate(lsys, n):
    '''
    Generates the final L-system string resulting from updating n times over
    the starting string for a particular dictionary
    
    Arguments:         lsys: dictionary containing the starting string and rules
                       n:    number of iterations to be performed
                       
    Return value:      Final L-system string
    '''
    result = lsys['start']
    for i in range(n):
        result = update(lsys, result)
    return result

        
# Ex D.3: -->
def lsystemToDrawingCommands(draw, s):
    '''
    Generates a list of drawing commands to draw a figure corresponding to
    the L-system string
    
    Arguments:          draw: dictionary containing characters in the L-system 
                              string and their corresponding commands
                        s:    a L-system string
                        
    Return value:       A list of drawing commands
    '''
    list_comm = []
    for c in s:
        list_comm.append(draw[c])
    return list_comm


# Ex D.4: -->
def nextLocation(x, y, angle, cmd):
    '''
    Generates the new coordinates of the turtle after executing the input 
    command
    
    Arguments:         x, y:  current x and y coordinates
                       angle: angle of the turtle
                       cmd:   command to be executed
                       
    Return value:      new x and y coordinates, along with the angle
    '''
    angle = angle % 360.0
    ang_rad = angle * (math.pi/180.0)
    comd = cmd.split()
    if comd[0] == 'F':
        x += (float(comd[1]) * math.cos(ang_rad))
        y += (float(comd[1]) * math.sin(ang_rad))
    elif comd[0] == 'L':
        angle = (angle + (float(comd[1]))) % 360
    elif comd[0] == 'R':
        angle = (angle - (float(comd[1]))) % 360
    return (x, y, angle)


# Ex D.5: -->        
def bounds(cmds):
    '''
    Computes the bounding coordinates of a drawing resulting from a set of 
    commands
    
    Arguments:       cmds: a list of commands
    
    Return value:    tuple of bounding coordinates- xmin, xmax, ymin, ymax
    '''
    x_max = 0.0
    x_min = 0.0
    y_max = 0.0
    y_min = 0.0
    x_new = 0.0
    y_new = 0.0    
    angle = 0.0
    for i in cmds:
        (x_new, y_new, angle) = nextLocation(x_new, y_new, angle, i)
        if x_new > x_max:
            x_max = x_new
        elif x_new < x_min:
            x_min = x_new
        if y_new > y_max:
            y_max = y_new
        elif y_new < y_min:
            y_min = y_new
    return (x_min, x_max, y_min, y_max)


# Ex D.6: -->
def saveDrawing(filename, bounds, cmds):
    '''
    Writes to a file the bounds, and commands to be executed for a drawing
    
    Arguments:      filename: name of file to be created
                    bounds:   tuple of bounds
                    cmds:     list of commands
                    
    Return value:   a file containing bounds on the first line, and commands on 
                    every subsequent line
    '''
    f = open(filename, 'w')        # Append mode apparently does not work here.
    b = ''
    for i in range(len(bounds)):
        b += str(bounds[i]) + ' '
    f.write(b[:-1] + '\n')
    for i in range(len(cmds)):
        f.write(str(cmds[i]) + '\n')
    f.close()
    
def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

