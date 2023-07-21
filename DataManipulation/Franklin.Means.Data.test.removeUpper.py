output_file = open('Data.test.removeUpper.txt', 'w')
word = []
'''Opens and reads the input file'''
with open('us-counties.2.txt') as file:
  for line in file:
    '''checks for uppercase words and skips them'''
    if line.isupper():
      '''Adds all CAPS words to an array'''
      word.append(line)
      '''Writes the array to the file'''
      output_file.write(line)
    else:
      pass
output_file.close()
'''Shows an output so you know the code ran successfully'''
print("Complete")