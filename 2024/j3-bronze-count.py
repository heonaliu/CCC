path = "/Users/heonaliu/Desktop/Projects/CCC/2024/j3-bronze-count-input.txt"

with open(path, 'r') as file:
    lines_list = file.readlines()

lines_list = [int(i.strip()) for i in lines_list]
num = lines_list[0]
print(lines_list)

lines_list.remove(num)
lines_list.sort()
max = lines_list[-1]
silver = 0
silver_index = 0
bronze = 0
print(lines_list)
for i in range(num-1, -1, -1):
    if (lines_list[i] != max):
        #first silver occurrence
        silver = lines_list[i]
        silver_index = i
        break

print(lines_list)
#returns a new list with last being silver
del lines_list[silver_index+1:]
print(lines_list)

for i in range(len(lines_list)-1, -1, -1):
    if (lines_list[i] != silver):
        #first silver occurrence
        bronze = lines_list[i]
        break
print(bronze)
bronze_count = 0
for i in range(len(lines_list)):
    if (lines_list[i] == bronze):
        bronze_count += 1

print(bronze, bronze_count)