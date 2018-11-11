#Write your function here
def middle_element(lst):
  length = len(lst)
  if length % 2 == 1:
    return (lst[length//2])
  else:
    a = lst[length//2]
    b = lst[length//2-1]
    avg= (a+b)/2
  return avg

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
