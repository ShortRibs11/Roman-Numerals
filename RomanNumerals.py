#===========================================
# Roman Numerals Program
#===========================================
# Reads a file containing roman numerals and
# converts them into arabic numerals
#===========================================
# Author: Jacob "ShortRibs" Hake
#===========================================

# The file we will read roman numerals from
FILENAME = "roman.txt"

#===========================================
# getArabicNumeral(r) function
# Converts a number (r) in roman numerals into Arabic numerals
# NOTE: Does not support roman numeral subtraction notation
#   (For example, 4 must be written as IIII, not IV)
#===========================================
def getArabicNumeral(r):
    # To hold the value of the number
    value = 0

    # Iterate through all the letters and add up their values
    for s in r:
        if (s == 'I'):
            value += 1
        elif (s == 'V'):
            value += 5
        elif (s == 'X'):
            value += 10
        elif (s == 'L'):
            value += 50
        elif (s == 'C'):
            value += 100
        elif (s == 'D'):
            value += 500
        else:
            value += 1000

    # Return the cumulative total value of the symbols
    return value

#===========================================
# Main Program
#===========================================

# Open the file into a variable called infile
infile = open(FILENAME, "r")

# Read the first line of the file
line = infile.readline()

# Print out a header for the data display
print(format("Roman:", "<14") + " | Arabic:\n"+
      "----------------------------------")

# For every line in the file
while (line != ''):
    # Get rid of the endline
    line = line.strip('\n')

    # Print the roman and arabic numerals for the number into the table
    print(format(line, "<14") + " | " + format(getArabicNumeral(line), "<14"))

    # Read the next line from the file
    line = infile.readline()

# Close the file when we are done with it
infile.close()

#===========================================
# End of Program
#===========================================
