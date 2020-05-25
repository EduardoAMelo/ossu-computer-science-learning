smallest_one = None
for the_num in [1000, 5000, 500, 100, 600, 10, 1]:
    if smallest_one is None:
        smallest_one = the_num
    elif the_num < smallest_one:
        smallest_one = the_num
    print(smallest_one, the_num)
print("all done!!")
