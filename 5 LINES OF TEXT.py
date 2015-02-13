#GEORGE WEST
#13/02/15
#5 LINES OF TEXT

with open("text.txt", mode = "w", encoding = "utf-8") as my_file:
    for count in range(5):
        text = input("Please enter a line: ")
        my_file.write(text)
        my_file.write("\n")
        
with open("text.txt", mode = "r", encoding = "utf-8") as my_file:
    for line in my_file:
        print(line,end="")
