'''
Problem # 10

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time


def scheduler(f, n):
    time.sleep(n/1000)
    f()


def function():
    print('hello world')
