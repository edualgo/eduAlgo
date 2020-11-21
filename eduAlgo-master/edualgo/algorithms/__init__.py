def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'_{"_" * (width + indent * 2)}_\n'  # upper_border
    if title:
        box += f'_{space}{title:<{width}}{space}_\n'  # title
        box += f'_{space}{"-" * len(title):<{width}}{space}_\n'  # underscore
    box += ''.join([f'_{space}{line:<{width}}{space}_\n' for line in lines])
    box += f'_{"_" * (width + indent * 2)}_'  # lower_border
    print(box)



