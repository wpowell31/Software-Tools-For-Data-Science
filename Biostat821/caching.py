'''Demonstrate caching.'''

cache: dict[int, int] = dict()

def add5(x: int) -> int:
    '''Add 5 to x.'''
    if x not in cache:
        cache[x] = x+5
    return cache[x]
    

if __name__ == '__main__':
    print(f'3 plus 5 is {add5(3)}')
    print(f'4 plus 5 is {add5(4)}')
    print(f'3 plus 5 is {add5(3)}')
    print(f'2 plus 5 is {add5(2)}')
