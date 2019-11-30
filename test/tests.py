# import time
# import requests
#
#
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print(start)
#         result = func(*args, **kwargs)
#         print(func.__name__, 'cost', time.time() - start)
#         print(func)
#         return result
#
#     return wrapper
#
#
# @time_it
# def fetch_page():
#     print('aa')
#     requests.get("https://www.souhu.com")
#
#
# fetch_page()
import cProfile


def loop(count):
    result = []
    for i in range(count):
        result.append(i)
cProfile.run('loop(10000)')
