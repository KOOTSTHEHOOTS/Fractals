from turtle import *

def koch_curve(level, length):
    """
    
    Parameters
    ----------
    level : int
        complexity of curve, level>=0
    length : length
        length from start to end point

    Returns
    -------
    None.

    """
    # Comment out if you want turtle to draw slower
    speed(0)
    # create koch curve
    def helper(level,length):
        # Fractal is a horizontal line
        if level==0:
            fd(length)
        # Line split into 3, 1/3 of line 
        elif level==1:
            length/=3
            fd(length)
            lt(60)
            fd(length)
            rt(120)
            fd(length)        
            lt(60)
            fd(length)
        else:
            helper(level-1,length/3)
            lt(60)
            helper(level-1,length/3)
            rt(120)
            helper(level-1,length/3)
            lt(60)
            helper(level-1,length/3)
    
    helper(level,length)
    

def koch_snow_flake(level,length):
    koch_curve(level,length)
    rt(120)
    koch_curve(level,length)
    rt(120)
    koch_curve(level,length)