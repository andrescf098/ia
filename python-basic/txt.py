with open("curso-platzi-python/files/Little Red Riding Hood.txt", "r") as file:
    tota_lines = 0
    for line in file:
        tota_lines += 1
        print(line.strip())
    print(tota_lines)

""" with open("curso-platzi-python/files/Little Red Riding Hood.txt", "r") as file:
    lines = file.readlines()
    print(lines)
 """
""" with open("curso-platzi-python/files/Little Red Riding Hood.txt", "a") as file:
    file.write("\n\nHola mundo") """