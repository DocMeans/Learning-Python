# Franklin Means, 07/20/2023
# This program open a file of numnbers. Puts them in an array
# Then calculates the lowest, highest and avaerage values and counts the numbers per range
# Once the program has finished it writes the results to a new file.
'''Imported Statistics to use the mean function'''
import statistics

''' Define ranges'''
ranges = [(00000, 9999), (10000, 19999), (20000, 29999), 
          (30000, 39999), (40000, 49999), (50000, 59999),
          (60000, 69999), (70000, 79999), (80000, 89999),
          (90000, 99999)]
counts = [0] * len(ranges) 
numbers = []

''' Read .txt file'''
with open('large.file.of.numbers.txt') as my_input_file_handle:
#with open('1to9.txt') as my_input_file_handle:
  for line in my_input_file_handle:
    number = int(line)
    numbers.append(number)
    
    ''' Count in ranges'''
    for index, range in enumerate(ranges):
      if range[0] <= number <= range[1]:
        counts[index] += 1
        ''' Calculate statistics'''     
min_number = min(numbers)
max_number = max(numbers)
average = statistics.mean(numbers)
my_input_file_handle.close()

''' Write output file'''
with open('file.analysis.txt', 'w') as my_output_file:
#with open('file.analysis2.txt', 'w') as my_output_file:

  my_output_file.write('--------Results--------\n')
  my_output_file.write(f'Count: {len(numbers)}\n')
  my_output_file.write(f'Minimum: {min_number}\n')
  my_output_file.write(f'Maximum: {max_number}\n')
  my_output_file.write(f'Average: {round(average, 2)}\n')
  
  '''Write range counts'''
  for index, count in enumerate(counts):
    range = ranges[index]
    ''' formats a string with the range and count.'''
    my_output_file.write(f'Count {range[0]}-{range[1]}: {count}\n')
my_output_file.close()
print("Complete")
