import sys
def show_size(x, level=0):
#    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if level == 0:
        summ_ = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                summ_ += show_size(key, level + 1) + show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                summ_ += show_size(item, level + 1)
        return summ_
    else:
        return sys.getsizeof(x)

