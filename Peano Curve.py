def peano(level, length):
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