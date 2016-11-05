def sorting():
    filename = ("food.txt")
    file_handle = open(filename, "r")
    words = []
    for line in file_handle:
        words += line.split()
        print (line)
    file_handle.close()
    print (sorted(words))


sorting()

#def quick_sort(array):
