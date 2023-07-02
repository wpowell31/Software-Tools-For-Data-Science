header = ['a', 'b', 'c']
data = [2, 4, 5]


def lookup(header, data, col) -> int:
    '''function to lookup.'''
    return dict(zip(header, data))[col]

def lookup2(header, data, col) -> int:
    '''Lookup alternate version.'''
    for i in range(len(header)):
        if header[i] == col:
            return data[i]
    return None

print(lookup(header, data, 'b'))