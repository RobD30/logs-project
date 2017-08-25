def repeat_separator(num: int = 25, sep: str = '-'):
    print(sep * num)


def format_num(num: int) -> str:
    print(num)
    return "{:,}".format(num)
