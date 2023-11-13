def interleave(iter1, iter2):
    '''accepts two iterables and returns an iterator with each of the given items interleaved'''
    return (x
            for values in zip(iter1, iter2)
            for x in values)

print(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
nums = [1, 2, 3, 4]
print(interleave(nums, (n**2 for n in nums)))
print(list(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
