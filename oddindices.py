#Write your function here
def odd_indices(lst):
  list_new=[]
  for x in range(1, len(lst), 2):
  	list_new.append(lst[x])
  return (list_new)

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
