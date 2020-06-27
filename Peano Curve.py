from turtle import *


def peano(level, length):
    """
    draws a peano curve of complexity defined by level, the distance between the 
    start and end point if it took a direct path is defined by distance

    Parameters
    ----------
    level : int
        complexity of curve, level>=0
        level 0 is a straight line
    length : int
        length between start to end point

    Returns
    -------
    None. - prints fractal

    """
    # Comment out if you want turtle to draw slower
    speed(0)
    rt(45)
    
    def helper(level,length):
        length/=3
        
        def move_square(length,direction,level):
            direction_dict={"r":rt, "l":lt}
            if level==1:
                for i in range(2):
                    fd(length)
                    direction_dict[direction](90)
                fd(length)
            else:
                for i in range(2):
                    helper(level-1,length)
                    direction_dict[direction](90)
                helper(level-1,length)
               
        if level==1:
            fd(length)
            rt(90)
            move_square(length,"l",level)
            lt(90)
            fd(length)
            rt(90)
            move_square(length,"r",level)
            lt(90)
            fd(length)        
        else:
            helper(level-1,length)
            rt(90)
            move_square(length,"l",level)
            lt(90)
            helper(level-1,length)
            rt(90)
            move_square(length,"r",level)
            lt(90)
            helper(level-1,length)
            
    helper(level,length)