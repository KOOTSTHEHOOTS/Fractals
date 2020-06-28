from turtle import *

def upside_arrowhead(level, length):
    """
    

    Parameters
    ----------
    level : int
        complexity of curve, level>0.
    length : int
        length of one side of the equilateral triangle 

    Returns
    -------
    None - prints fractal

    """
    # Comment out if you want turtle to draw slower
    speed(0)
    
    # odd level start with outward arrow head
    # turn left
    if level%2!=0:
        lt(60)
    
    
    def basic_movement(level,length,direction):
        direction_dict={"l":lt, "r":rt}
        length/=2
        for i in range(2):
            fd(length)
            direction_dict[direction](60)
        fd(length)
           
    # Draws an outward curve
    def helper_A(level,length):
        direction="r"
        
        if level==1:
            basic_movement(level,length,direction)
            
        else:
            helper_B(level-1,length/2)
            rt(60)
            helper_A(level-1,length/2)
            rt(60)
            helper_B(level-1,length/2)
            
    # Draws an inward curve
    def helper_B(level,length):
        direction="l"
        if level==1:
            basic_movement(level,length,direction)
        else:
            helper_A(level-1,length/2)
            lt(60)
            helper_B(level-1,length/2)
            lt(60)
            helper_A(level-1,length/2) 
        
    helper_A(level,length)