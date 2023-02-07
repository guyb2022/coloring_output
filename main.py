import re
"""
Color powershell output as in the code editor
"""

# conditional
conditionals = ['if', 'elif', 'else', 'while', 'for','return']
# functional
function = ['def', 'class']
# Parameter
params = ['int', 'float', 'str', 'list', 'tuple', 'set', 'dict',
            'bool', 'bytes', 'bytearray', 'complex', 'frozenset', 'range']
# Symbols
symbols = ['+', '-', '*', '/', '//', '%', '**', '=', '==', '!=', '<', '>',
            '<=', '>=', '(', ')', '[', ']', '{', '}', '.', ',', ':', ';',
            '@', '#', '+=', '-=', '*=', '/=', '%=', '**=', " "]


def split_func_declaration(word):
    results =  re.findall(r'\b\w+\b|\+|-|\*|/|//|%|\**|=|==|!=|<|>|<=|>=|\(|\)|[|]|{|}|.|,|:|;|@|#|\+=|-=|\*=|/=|%=|\**=|" "', word)
    return  [x for x in results if x != '']

def convert_to_list(lines):
    return lines.split('\n')

def color_code(text):
    colored_text = ''
    # breaking the text into list
    words = convert_to_list(text)
    for word in words:
        # Iterating over each line and parse it
        results = split_func_declaration(word)
        for i, part in enumerate(results):
            # for catching function names
            if i < (len(results)-2) and results[i+1] == '(':
                colored_text += "\033[33m" + part + "\033[0m"
            elif part in conditionals:
                colored_text += "\033[35m" + part + "\033[0m"
            elif part in symbols:
                colored_text += "\033[33m" + part + "\033[0m"
            elif part in function:
                colored_text += "\033[36m" + part + "\033[0m"
            else:
                colored_text += "\033[36;1m" + part + "\033[0m"
        colored_text += '\n'
    return colored_text

words = ["def number_to_bits(number):\n","if number:\n","bits = []\n",
         "while number:\n","number, remainder = divmod(number, 2)\n",
         "bits.insert(0, remainder)\n","return bits\n","else:\n","return [0]"]

text = "def number_to_bits(number):\nif number:\nbits = []\n\
while number:\nnumber, remainder = divmod(number, 2)\n\
bits.insert(0, remainder)\nreturn bits\nelse:\n\
return [0]"

if __name__ == '__main__':
    print(color_code(text))