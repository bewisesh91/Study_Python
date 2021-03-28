class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def is_square(self):
        dot_list = [self.p1, self.p2, self.p3, self.p4]
        for i in range(len(dot_list)-1) :
            for j in range(len(dot_list)-1) :
                if dot_list[j].x > dot_list[j+1].x :
                    dot_list[j], dot_list[j+1] = dot_list[j+1], dot_list[j]
        for i in range(len(dot_list)-1) :
            for j in range(len(dot_list)-1) :
                if dot_list[j].y > dot_list[j+1].y :
                    dot_list[j], dot_list[j+1] = dot_list[j+1], dot_list[j]
            
        distance1 = ((dot_list[1].x - dot_list[0].x)**2) + ((dot_list[1].y - dot_list[0].y)**2)
        distance2 = ((dot_list[2].x - dot_list[0].x)**2) + ((dot_list[2].y - dot_list[0].y)**2)
        
        x_distance1 = ((dot_list[3].x - dot_list[0].x)**2) + ((dot_list[3].y - dot_list[0].y)**2)
        x_distance2 = ((dot_list[2].x - dot_list[1].x)**2) + ((dot_list[2].y - dot_list[1].y)**2)        
        
        if distance1 == distance2 and x_distance1 == x_distance2 :
            return True
        else :
            return False
