nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
    [333333],
]

class FlatIterator():
      
    def __init__(self, my_list):
        self.my_list = my_list
           
    def __iter__(self):
        self.groups = iter(self.my_list)
        self.group = []  
        return self

    def __next__(self):          
        if not self.group:
            self.group = next(self.groups)
        item = self.group.pop(0) 

        return item

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
	    print(item)
	
    #flat_list = [elem for elem in FlatIterator(nested_list)]	
    #print(flat_list)