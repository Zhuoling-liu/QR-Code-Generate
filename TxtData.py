import copy
from helper import *
class TxtData:
    '''
    >>> my_list_simple = [[2,1,3],[4,5,6]]
    >>> my_txt_simple = TxtData(my_list_simple)
    >>> my_txt_simple.rows
    2
    >>> my_txt_simple.cols
    3
    >>> my_list = get_data("big_data.txt")
    >>> my_txt = TxtData(my_list)
    >>> my_txt.cols
    2
    >>> my_txt.rows
    2
    >>> my_txt.data
    '''
    def __init__(self,data):
        self.data = copy.deepcopy(data)
        self.rows = len(data)
        self.cols = len(data[0])
        
    def __str__(self):
        '''
        >>> my_list_simple = [[2,1,3],[4,5,6]]
        >>> my_txt_simple=TxtData(my_list_simple)
        >>> print(my_txt_simple)
        This TxtData object has 2 rows and 3 columns
        '''
        return 'This TxtData object has '+ str(self.rows)\
        + ' rows and '+str(self.cols) +' columns'
    
    def get_pixels(self):
        '''
        >>> my_list_simple = [[2,1,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_pixels()
        6
        '''
        return self.rows * self.cols
    
    def get_data_at(self,row,col):
        if row >= self.rows or col >= self.cols:
            raise ValueError("Index out of bound!")
        return self.data[row][col]
    
    def pretty_save(self,file_name):
        fobj = open(file_name, 'w')
        for row in self.data:
            txt_content =''
            for col in row:
                if col == 1:
                    txt_content+= "\u2588" * 2
                else:
                    txt_content += '  '
            fobj.write(txt_content+ '\n')
        fobj.close()

    def equals(self,another_data):
        '''
        >>> m1 = [[1,2],[2,3]]
        >>> m2 = TxtData(m1)
        >>> m3 = txtdata(m1)
        >>> m3 = TxtData(m1)
        >>> m2.equals(m3)
        True
        '''
        if self.rows != another_data.rows or \
           self.cols != another_data.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != another_data.data[i][j]:
                    return False
        return True

    def approximately_equals(self,another_data,precision):
        '''
        >>> s1=[[1,2,3],[4,5,6]]
        >>> s2=[[1,2,3],[7,8,9]]
        >>> t1=TxtData(s1)
        >>> t2=TxtData(s2)
        >>> t1.equals(t2)
        False
        >>> t1.approximately_equals(t2,0.5)
        True
        >>>  my_list=get_data("small_error.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_list2 = get_data("small_error copy.txt")
        >>> my_txt2 = TxtData(my_list2)
        >>> my_txt.approximately_equals(my_txt2)
        >>> my_txt.approximately_equals(my_txt2,0.5)
        True
        '''
        if self.rows != another_data.rows or \
           self.cols != another_data.cols:
            return False
        diff_num = 0
        total_num = self.get_pixels()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != another_data.data[i][j]:
                    diff_num += 1
                
        inconsistent_rate = diff_num / total_num
        return inconsistent_rate <= precision
        
        

                    
                    
                    
        