#read through the file prog.log

with open('prog.log') as f:
    lines = f.readlines()
    #Find the second feild in each li
    for line in lines:
        
        #count how many times a line is repeated in a dictionary
        number_of_times = {}
        for line in lines:
            if line in number_of_times:
                number_of_times[line] += 1
            else:
                number_of_times[line] = 1
        
        #create a new file called prog2.log that shows the items in the dictionary and then the number of times they are repeated
        
                
        with open('prog2.log', 'w') as f:
            for line in number_of_times:
                #f.write(f'{str(number_of_times[line])} {line}')
                
                chunks = line.split(', ')
                f.write(f'{chunks[0]}, {chunks[1]}, {str(number_of_times[line])}x{chunks[2]}, {chunks[3]}')  
            #print(str(number_of_times[line]))
            
