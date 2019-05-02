# Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID (Blackboard username): bpshah
#
# CSE 101, Fall 2018
# Assignment 3-2 (List Manipulation) starter code

# Complete the functions below for this assignment

def magicSquare(n):
    num = 2
    row = 0
    col = 0
    currRow = 0
    currCol = (n//2)
    if n % 2 == 0 or n <= 0:
        return None
    else:
        square = [-1]*n

        for i in range(len(square)):
            square[i] = [-1]*n

        square[currRow][currCol] = 1

        for i in range((n*n) - 1):
            row = currRow
            col = currCol
            if row == 0:
                row = (n-1)
            else:
                row = row - 1

            if col == 0:
                col = (n-1)
            else:
                col = col - 1

            if square[row][col] == -1:
                currRow = row
                currCol = col
                square[currRow][currCol] = num
            else:
                currRow = currRow + 1
                square[currRow][currCol] = num
                
            num += 1
                
        return square


def checkCourses(required, filename):
    transcript = {}
    notTaken = []
    
    for line in open(filename):
        line = line.strip()
        space = line.index(" ")
        course = line[:space]
        grade = int(line[space:])
        transcript[course] = grade

    for i in required:
        if i in transcript and transcript[i] >= 75:
            pass
        else:
            notTaken.append(i)
    if len(notTaken) == 0:
        return True
    else:
        return notTaken


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Test of Part 1
    print("Creating a magic square with n = -3:")
    s = magicSquare(-3)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 5:")
    s = magicSquare(5)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 7:")
    s = magicSquare(7)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 4:")
    s = magicSquare(4)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    # Add your own tests here

    print("Creating a magic square with n = 3:")
    s = magicSquare(3)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    # Test of Part 2
    requiredCourses = ["CSE114", "CSE214", "CSE215", "CSE216", "CSE220", "CSE300", "CSE303", "CSE310", "CSE312", "CSE316", "CSE320", "CSE373", "CSE416"]

    print("Result of calling checkCourses() with file 'transcript1.txt':", checkCourses(requiredCourses, "transcript1.txt"))
    print()

    print("Result of calling checkCourses() with file 'transcript2.txt':", checkCourses(requiredCourses, "transcript2.txt"))
    print()

    print("Result of calling checkCourses() with file 'transcript3.txt':", checkCourses(requiredCourses, "transcript3.txt"))
    print()

    # Add your own tests here

    print()
    

