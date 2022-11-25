nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

def flat_generator(my_list):
    for group in my_list:
        for item in group:
            yield item

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
	    print(item)