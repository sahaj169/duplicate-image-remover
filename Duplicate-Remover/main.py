from DuplicateRemover import DuplicateRemover



# Remove Duplicates
# inp = str(input("What do you want to do: \n 1) [Remove duplicate] in a folder \n 2) Find a [similar image] \n (Enter 1 or 2): "))
# if inp.lower() == "1":
dirname = str(input("Enter the folder or directory name you want to find duplicate images in: "))
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# # Find Similar Images
# if inp.lower() == "2":
#     dirname = str(input(
#         "Enter the folder or directory name you want to find duplicate images in: "))
#     dr = DuplicateRemover(dirname)
#     filename = str(input("Enter the file location you want to find duplicate of: "))
    
#     dr.find_similar(filename,70)
