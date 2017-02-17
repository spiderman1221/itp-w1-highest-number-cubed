"""This is the entry point of the program."""
#highest cubable number still less than argument

def highest_number_cubed(limit):
    y=0
    for i in range(limit):
        while (y**3) <= limit:
            y += 1
    return (y -1)        
        
    
    
