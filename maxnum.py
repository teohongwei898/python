#Write your function here
def max_num(nums):
  maximum = nums[0]
  for x in nums:
    if x > maximum:
      maximum = x
    else:
      maximum = maximum
  return (maximum)
