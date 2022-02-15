def reverse_string(string: str) -> str:
    if type(string) != str:
        raise TypeError(f'Type is not str, but {type(string)}')
    return string[::-1]

