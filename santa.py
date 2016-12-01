import random

names = ['Alice','Bob', 'Cameron', 'Diana', 'Eric', 'Fred']
original = list(names)

#make sure we get a derangement of names
de = 0
while de == 0:
  names = list(original)
  for i in range(len(names)): 
    j = random.randint(i, (len(names) - 1))
    tmp = names[i]
    names[i] = names[j]
    names[j] = tmp
    if names[i] == original[i]:
      de = 0
      break
    else:
      de = 1

for i in range(len(names)):
  if original[i] == names[i]:
   de = 0

if de == 0:
  print('not deranged')
else:
  print('derangement!')
#just double check for double sureness	  

for i in range(len(names)):
  f = open("{}.txt".format(original[i]), "w")
  f.write("{} gives to {}".format(original[i], names[i]))
  f.close()
#write the files, send the appropriate named text file to each person.
#each file contains a name of the person to which they are giving to.
