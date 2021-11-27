from merge import merge_sort
from insertion import insertion_sort
from selection import selection_sort
from bogosort import bogo_sort

def bogo_test():
    assert bogo_sort([12,51, 124, 23, 5, 2]) == [2,5,12,23,51,124]

# If no error appears, it has passed the tests
def insertion_test():
    assert insertion_sort([1,24,23,14,2]) == [1,2,14,23,24]

def merge_test():
    assert merge_sort([1,4,512,25,2], 0, [1,4,512,25,2]) == [1,2,4,25,512]

def selection_test():
    assert selection_sort([1,4,512,25,2]) == [1,2,4,25,512]

bogo_test()
merge_test()
insertion_test()
selection_test()