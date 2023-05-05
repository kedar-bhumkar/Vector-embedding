ints = [1,2,3,4,5,6,7,8,9,10]
chunk_size = 4
for i in range(0, len(ints), chunk_size):
    chunk = ints[i:i+chunk_size]
    print('chunk -' , chunk)


