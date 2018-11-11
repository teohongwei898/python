#Write your function here
def remove_middle(lst,start,end):
  first_half = lst[0:start]
  last_half = lst[end+1:]
  return first_half + last_half

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
