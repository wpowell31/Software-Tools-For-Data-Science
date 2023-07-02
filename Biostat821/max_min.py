#Max and min utilities

def max(a: int, b: int, c: int) -> int | str:
    '''Return maximum of a, b, and c'''
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
     return c

print(max(30, 4, 5))
