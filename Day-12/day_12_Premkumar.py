def linearSearch(n, k, arr):
  """
  This function takes k as the key value and linear search 
  for it if the value is found it returns the index of the key 
  value else it will return -1 
  Example:-
    n, k = 4, 5
    arr = [2, 4, 5, 8]
    returns 2
  """
  for i in range(n):
    if arr[i] == k:
      return i
  else:
    return -1

if __name__ == "__main__":
  n = int(input("Enter number of elements you want \n"))
  arr = [float(num) for num in input("Enter space seperated {} numbers for array \n".format(n)).split()]
  k = float(input("Enter the search key \n"))
  print("index of the search key is {}".format(linearSearch(n, k, arr)))