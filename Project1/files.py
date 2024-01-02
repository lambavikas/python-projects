# Always Open a File and Specify Mode Read, Write, Append
file = open("main.py", "r")

# Check if file is Readable
print(file.readable())
# Print some attribute about the file like file name
print(file.name)
# Read the first line of the file
print(file.readline())
print("-------------------------------------------------------------------")
# Read the entire file in a single shot from the current position i.e. Line 2
print(file.read())
# close the file
file.close()
print("-------------------------------------------------------------------")
# Always Open a File and Specify Mode Read, Write, Append
file = open("main.py", "r")
# Another way to read the whole file but line by line
for line in file.readlines():
    print(line)
print("-------------------------------------------------------------------")
# close the file
file.close()
