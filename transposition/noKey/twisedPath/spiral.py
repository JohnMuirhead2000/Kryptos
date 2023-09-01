# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:06:42 2023

Spiral path solver 
@author: bvoc5
"""

#Message encoded as single string 
message = "abcdefghijklmnopqrstuvwxyz"

moves_sequence = []*4
sequence_index = 0  
    
matrix         = [] 
current_row    = 0 
current_col    = 0 

#User input variables
Rows   = 0 
Cols   = 0 
sequence_in = 0 

def main(): 
    
    global Rows, Cols, sequence_in  

    #Obtain numbers of rows and number of columns
    Rows = int(input("Number of Rows: "))
    Cols = int(input("Number of Cols: "))

    print("Sequence: - Starting Pos:  - Moves:") 
    print("0         - (0,0)          - Down, Right, Up, Left")
    print("1         - (Rows-1,0)     - Up, Left, Down, Right")

    #Obtain sequence 
    sequence_in = int(input("Sequence: "))
    
    #Initialize matrix 
    initMatrix() 
    
    #Initialize moves sequence 
    initMovesSequence()  
    
    #Place characters in spiral pattern
    spiralPattern() 
    
    #Print matrix
    for row in range(Rows):
        print(matrix[row])

    return 

#Initialize matrix
def initMatrix():
    
    global matrix     
    for row in range(Rows):
        row_i = [] 
        for col in range(Cols):
            row_i.append(0)
        matrix.append(row_i) 
        
#Initialize moves sequence 
def initMovesSequence(): 
    
    global moves_sequence, current_row
    
    if(sequence_in == 0):
        moves_sequence = ["D", "R", "U", "L"]
    elif(sequence_in == 1):
        moves_sequence = ["U", "R", "D", "L"]
        current_row    = Rows - 1
    else:
        exit(0)
        

#Get the next move by updating sequence index
def getNextMove():
    
    global sequence_index 
    sequence_index  = (sequence_index + 1) % 4 
    current_move    = moves_sequence[sequence_index] 
    
    return current_move

#Update adjacency of current posititon 
def updateAdjacecny(previous_move): 
    
    global current_row, current_col 
    
    if(sequence_in == 0):
    
        if previous_move == "D":
            current_col = current_col + 1 
        elif previous_move == "R": 
            current_row = current_row - 1 
        elif previous_move == "U": 
            current_col = current_col - 1
        elif previous_move == "L":     
            current_row = current_row + 1 
            
    elif(sequence_in == 1): 
    
        if previous_move == "D":
            current_col = current_col - 1 
        elif previous_move == "R": 
            current_row = current_row + 1 
        elif previous_move == "U": 
            current_col = current_col + 1 
        elif previous_move == "L": 
            current_row = current_row - 1       
    else: 
        return 
    

#Place characters in selected spiral pattern 
def spiralPattern(): 
    
    global current_row, current_col 
    
    char_count   = 0 
    current_move = moves_sequence[sequence_index]
        
    for char in message:
        if char_count < (Rows*Cols): 
            if current_move == "D":        
                matrix[current_row][current_col] = char
                if current_row == (Rows - 1) or (matrix[current_row+1][current_col] != 0):
                    current_move = getNextMove()
                    updateAdjacecny("D")  
                else: 
                    current_row = current_row + 1  
            elif current_move == "R": 
                matrix[current_row][current_col] = char
                if current_col == (Cols - 1) or (matrix[current_row][current_col+1] != 0):
                    current_move = getNextMove()
                    updateAdjacecny("R") 
                else:
                    current_col = current_col + 1   
            elif current_move == "U":
                matrix[current_row][current_col] = char
                if (current_row == 0) or (matrix[current_row-1][current_col] != 0):
                    current_move = getNextMove()
                    updateAdjacecny("U")
                else:
                    current_row = current_row - 1   
            elif current_move == "L": 
                matrix[current_row][current_col] = char
                if (current_col == 0) or (matrix[current_row][current_col-1] != 0):
                    current_move = getNextMove()
                    updateAdjacecny("L")
                else:
                    current_col = current_col - 1   
            char_count = char_count + 1
        else:
            break       
    return 
     
#Execute main function 
if __name__ == "__main__":
    main() 




