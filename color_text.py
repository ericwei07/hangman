import os
if os.name == 'nt':
    os.system('color')


def colored(text, custom_color, bold=False, underline=False, wholeline=False):
    color = {
        'GREY': '\033[90m',
        'GRAY': '\033[90m',
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
    }
    if bold:
        text = color['BOLD'] + text
    if underline:
        text = color['UNDERLINE'] + text
    custom_color = str(custom_color).upper()
    if custom_color in color:
        text = color[custom_color] + text
    elif str(custom_color).isdigit():
        text = '\033[' + custom_color + 'm' + text
    if wholeline:
        return text
    return text + color['ENDC']


if __name__ == '__main__':
    for x in range(90,107):
        print(colored("hello, world" + " " + str(x), x, True, True, True))
        print(colored("hello, world" + " " + str(x), x, True, False, True))
        print(colored("hello, world" + " " + str(x), x, False, True, True))
        print(colored("hello, world" + " " + str(x), x, False, False, True))
