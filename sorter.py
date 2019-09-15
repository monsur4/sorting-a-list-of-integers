vals= [2, 3, 2, 4, 4, 5, 1, 6, 6, 1, 4, 7, 6, 4, 5, 6, 5, 5, 1, 6]
# first: sort the list
vals.sort()

# second: create two new array
# one as a set of the elements in the array
# the other as a list of the corresponding frequency
n = 0
first_index = 0
last_index = first_index
freq_list = []
element_list = []
while last_index < len(vals):
    if vals[first_index] == vals[last_index]:
        last_index = last_index + 1
        n = n + 1
    else:
        element_list.append(vals[first_index])
        first_index = last_index
        freq_list.append(n)
        n = 0

element_list.append(vals[first_index])
freq_list.append(n)
print("element list = " + str(element_list))
print("frequency list = " + str(freq_list))

# create an intermediate list sorting the frequency of the elements
# this is where the sorting occurs
intermediate_list = freq_list.copy()
intermediate_list.sort(reverse = True)
print("intermediate list = " + str(intermediate_list))

# find the index of the elements in the intermediate list in the frequency list
final_list = []
for i in intermediate_list:
    item_index = freq_list.index(i)
    item = element_list[item_index]
    item_list = []
    item_list.append(item)
    # print the item based on its frequency of occurence
    final_list.extend(item_list * i)
    #remove the items already listed
    freq_list.remove(i)
    element_list.remove(element_list[item_index])

print("final list = " + str(final_list))


