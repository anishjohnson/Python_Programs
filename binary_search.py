# Functioning of binary search
# list = [1, 2, 3, 4, 5] (if not ordered in asscending order then do it first)
# target = 2
# step1: It will divide the dataand get the mid value.
# step2: It will compare if the target is less than or greater than the target.
# step3: Since 2 is less than 3 it will consider the values left to 3.
# step4: It will now again divide the list and get the mid value.
# Now the mid value is the target, hence we have found the required value.



def binary_search(_list, target, low=None, high=None):
  if low == None and high == None:
    low, high = 0, len(_list) - 1
  
  mid = (low + high)//2
  
  while low < high:

    if target == l[mid]:
      return mid
    
    elif target < l[mid]:
      return binary_search(_list, target, low = low, high = mid - 1)

    else:
      return binary_search(_list, target, low = mid + 1, high = high)
  
  return 'Target not present in the list.'


if __name__ == '__main__':
  l  = [1, 2, 3, 4, 5, 9, 20]
  target = 4
  print(binary_search(l,target))

'''
# Logic

l = [1, 2, 3, 4, 5, 9, 20]
target = 4
low = 0 
high = len(l)-1 = 6

midpoint = 0+6//2 = 3

4 > 3 >> low = midpoint+1, high = high 
new l = [4, 5, 9, 20] # only including the values after midpoint
low = midpoint + 1 = 3+1 = 4
high = len(l)-1 = 6
new midpoint = 4+6//2 = 5

4 < 5 >> low = low, high = midpoint-1
low = 4
high = midpoint - 1 = 5-1 = 4
new l = [4]

now target = midpoint

'''
