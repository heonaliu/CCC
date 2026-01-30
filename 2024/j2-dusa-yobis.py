path = "2024/j2-dusa-yobis-input.txt" 

with open(path, 'r') as file:
    lines_list = file.readlines()
    
start = int(lines_list[0].strip())
toBreak = False
index = 1

while (not toBreak):
    num = int(lines_list[index].strip())
    if (start > num):
        start += num
        index+=1
        
    else:
        toBreak = True
        print(start)
