# Franklin Means 07/20/2023
# This program reads from a file and reformats the contents of the file
# Stanton, KY formatted to KY: Stanton
# Also ignores all capital words

'''Sets the output file name'''
manipulated_file = open('Counties.Manipulated.txt', 'w')

'''Opens and reads the input file'''
with open('us-counties.2.txt') as file:
  for line in file:
    '''checks for uppercase words and skips them'''
    if line.isupper():
      pass
    else:
      '''Rearanges the line by stripping whitepaces and separating the to words
         by the comma into two new variables'''
      if ',' in line:
        city, state = line.split(',')
        city = city.strip()
        state = state.strip()
        '''Reformats the new lines'''
        manipulated_file.write(f"{state}: {city}\n")
manipulated_file.close()
'''Shows an output so you know the code ran successfully'''
print("Complete")