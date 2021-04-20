find_smallest_int = lambda arr: min(arr)

def find_smallest_int(arr):
  return min(arr)

def find_smallest_int(arr):
  min = arr[0]
  for num in arr:
    if num < min:
      min = num
  return min
