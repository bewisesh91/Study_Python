class Calculator:
    def __init__(self):
        self.start = '0'

    def digit(self, num):
        self.num = num
        self.start = str(self.start) + str(self.num)
        return self.start
                
    def plus(self):
        if self.start[-1] == '-' or self.start[-1] == '+'  :
            self.start = self.start[:-1]
        self.start = str(self.start) + '+'
            
    def minus(self):
        if self.start[-1] == '-' or self.start[-1] == '+'  :
            self.start = self.start[:-1]
        self.start = str(self.start) + '-'
    
    def clear(self):
        self.start = '0'
        
    def equal(self):
        num_list = []
        cal_num = 0
        temp = ''
        ex_temp = ''
        for i in range(len(self.start)) :
            if self.start[i] == '+' :
                temp = int(self.start[cal_num:i])
                cal_num = i + 1
                num_list.append(temp)
                num_list.append(self.start[i])
            elif self.start[i] == '-' :
                temp = int(self.start[cal_num:i])
                cal_num = i + 1
                num_list.append(temp)
                num_list.append(self.start[i])
            else :
                if cal_num == 0 :
                    ex_temp = ex_temp + self.start[i]
                else :
                    ex_temp = ''
                    ex_temp = ex_temp + self.start[cal_num:]
        num_list.append(int(ex_temp))
        
        result = num_list[0]        
        for i in range(1, len(num_list)) :
            if num_list[i-1] == '+' :
                result += num_list[i]
            elif num_list[i-1] == '-' :
                result -= num_list[i]
                                    
        return result
