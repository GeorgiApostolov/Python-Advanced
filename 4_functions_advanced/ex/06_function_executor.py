def func_executor(*args):
    result = []

    for func, values in args:
        func_result = func(*values)
        result.append(f'{func.__name__} - {func_result}')

    return '\n'.join(result)
