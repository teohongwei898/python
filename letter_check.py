def letter_check (word,letter):
  x = 0
  for y in word:
    if y == letter:
      return True
    else:
      x+=1
  return False
