#Write your function here
def combine_sort(lst1, lst2):
  a = lst1 + lst2
  b = sorted(a)
  return b

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))