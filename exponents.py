#Write your function here
def exponents(bases, powers):
  new_lst = []
  for x in bases:
    for y in powers:
      new_lst.append(x ** y)
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
