# Reading lines from a file
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
