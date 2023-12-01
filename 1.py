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
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9' }

def match_nums( s: str ) -> tuple:
    """Find the first and last digit or numberword in a string"""
    indices = { digit: s.find(digit) for digit in digits if s.find( digit ) != -1 }
    first = min( indices, key = indices.get, default = None )
    last = max( indices, key = indices.get, default = None )
    if any( _ is None for _ in ( first, last ) ):
        raise ValueError( f'Input string did not have a match: {s}' )
    if first.isalpha():
        first=values[first]
    if last.isalpha():
        last=values[last]
    return ( int(first), int(last) )

calibration_values = [ 10 * first + last for (first, last) in ( match_nums(_) for _ in data ) ]
print( f"Total of calibration values is {sum( calibration_values ) }." )

