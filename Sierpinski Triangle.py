from turtle import *

def sierpinski(level, length):
    """
    draws a Sierpinski curve of complexity defined by level, 
    the length of one side of the equilateral triangle

    Parameters
    ----------
    level : int
        complexity of curve, level>0
        level 1 is an equilateral triangle
    length : int
        length of one side of the equilateral triangle 

    Returns
    -------
    None. - prints fractal

    """
    # Comment out if you want turtle to draw slower
    speed(0)
    lt(60)
    def helper(level,length):
        if level==1:
            for i in range(3):
                fd(length)
                rt(120)
        else:
            helper(level-1,length/2)
            fd(length/2)
            helper(level-1,length/2)
            rt(120)
            fd(length/2)
            lt(120)
            helper(level-1,length/2)
            lt(120)
            fd(length/2)
            rt(120)
            
            
    helper(level,length)