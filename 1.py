FILE = '1.in'

data = [ _.strip() for _ in open(f'inputs/{FILE}').readlines() ]
digits = (
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine' )
values = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9 }

def fmatch( s: str):
    """Find the first digit or numberword in a string"""
    indices = { digit: 0 for digit in digits }
    for digit in indices:
        indices[digit] = s.find(digit)
    nulls = []
    for digit in indices:
        if indices[digit] == -1:
            nulls.append(digit)
    for _ in nulls:
        indices.pop(_)
    first = min( indices, key = indices.get )
    if first.isnumeric():
        return first
    else:
        return values[first]

def lmatch( s: str):
    """Find the last digit or numberword in a string"""
    indices = { digit[::-1]: 0 for digit in digits }
    for digit in indices:
        indices[digit] = s[::-1].find(digit)
    nulls = []
    for digit in indices:
        if indices[digit] == -1:
            nulls.append(digit)
    for _ in nulls:
        indices.pop(_)
    last = min( indices, key = indices.get )
    if last.isnumeric():
        return last
    else:
        return values[last[::-1]]

calibration_values = []
for _ in data:
    calibration_values.append( int( f'{fmatch( _ )}{lmatch( _ )}' ) )
print( f"Total of calibration values is {sum( calibration_values ) }." )

