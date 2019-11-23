def data(*args, **kwargs):
    print(*args)
    print(type(args))
    print(kwargs)
    print(kwargs.get('name'))


if __name__ == '__main__':
    data(1, 2, 3, 4, 5, name='jiayawu', id=123)
