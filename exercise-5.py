"""Exercise 5: Stop on Exception"""

def swap(list, i, j):
    """Swap 2 items of a list in-place."""
    list[i], list[j] = list[j], list[i]

def bubble_sort(list_of_nums):
    """Sorts the list in-place using the Bubble Sort algorithm."""
    for iteration in range(len(list_of_nums)): # Do n times
        for i in range(len(list_of_nums) - 1):
            if list_of_nums[i] > list_of_nums[i+1]:
                swap(list_of_nums, i, i+1)


if __name__ == '__main__':
    nums = [12, 6, 2, 4, 3, 7]
    bubble_sort(nums)
    print(nums)
