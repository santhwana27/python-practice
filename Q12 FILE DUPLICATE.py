
src_file = input("Enter the source file name: ")
dest_file = input("Enter the destination file name: ")

with open(src_file, "r") as infile:
    with open(dest_file, "w") as outfile:
        outfile.write(infile.read())

print("File duplicated successfully!")
