#Write your function here
def divisible_by_ten(nums):
  x = 0
  for y in nums:
    if (y % 10 == 0):
      x += 1
  return x

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
