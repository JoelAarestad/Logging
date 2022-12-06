import csv

# read the input.csv file
with open('input.csv', 'r') as input_file:
  reader = csv.reader(input_file)
  # skip the first row containing the column headers
  next(reader)

  # create a dictionary to store the counts of sets for each exercise
  sets_counts = {}

  # iterate over the rows in the input file
  for row in reader:
    exercise = row[0]
    weight = row[1]
    reps = row[2]
    date = row[3]

    # increment the count of sets for this exercise
    if exercise not in sets_counts:
      sets_counts[exercise] = 1
    else:
      sets_counts[exercise] += 1

  # write the output.csv file
  with open('output.csv', 'w') as output_file:
    writer = csv.writer(output_file)
    # write the column headers
    writer.writerow(['Exercise', 'Weight', 'Sets', 'Reps', 'Date'])

    # write one row for each exercise
    for exercise, sets_count in sets_counts.items():
      writer.writerow([exercise, weight, sets_count, reps, date])
