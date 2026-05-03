import base64
import sys

with open('snake/snake-min.html', 'r') as file:
    b64 = base64.b64encode(file.read().encode())
    b64_str = f'{b64}'.split("'")[1]
    print(sys.getsizeof(b64_str))
    print(f'data:text/html;base64,{b64_str}')
