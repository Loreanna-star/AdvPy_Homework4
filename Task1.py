from copy import deepcopy

class FlatIterator():
      
    def __init__(self, my_list):
        self.my_list = deepcopy(my_list)
           
    def __iter__(self):
        self.groups = iter(self.my_list)
        self.group = []  
        return self

    def __next__(self):          
        if not self.group:
            self.group = next(self.groups)
        item = self.group.pop(0) 
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()