class Solution:
  def sortByBits(self, arr):
    return sorted(arr, key=lambda v: (bin(v).count('1'), v))   
