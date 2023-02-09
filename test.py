from collections import OrderedDict
with open('def_working.txt','r') as data:
    lines=data.readlines()




posdic={}

for line in lines:
    splited=line.split()
    cell_name=splited[2]
    pos_y=splited[-4]
    pos_x=splited[-5]


    if cell_name=='BITIE_T8_11T_DG16LLHG':
        if not pos_y in posdic.keys():
            posdic[pos_y]=[]
            posdic[pos_y].append(pos_x)
        else:
            posdic[pos_y].append(pos_x)


myKeys = list(posdic.keys())
myKeys.sort()
sorted_dict = {i: posdic[i] for i in myKeys}
 

prevKey=myKeys[0]

bottom_cordinates=[]
top_cordinates=[]

for key in myKeys[1:]:
    
    for new_pos_x in sorted_dict[key]:
        for old_pos_x in sorted_dict[prevKey]:
            if int(old_pos_x)-3000<int(new_pos_x)<int(old_pos_x)+3000:
                # print("bottom coordinate",(old_pos_x,prevKey))
                # print("top coordinate",(new_pos_x,key))
                bottom_cordinates.append((old_pos_x,prevKey))
                top_cordinates.append((new_pos_x,key))
    prevKey=key
    
# print(bottom_cordinates)
# print(top_cordinates)


modified_lines=[]
for line in lines:
    splited=line.split()
    cell_name=splited[2]
    pos_y=splited[-4]
    pos_x=splited[-5]

    co_ordinate=(pos_x,pos_y)
    # print(co_ordinate)
    if co_ordinate in top_cordinates:
        splited[2]='FILL_T8_11T_DG16LLHG'
        # print(splited)
        test_str=' '.join(splited)
        modified_lines.append(test_str)
        # print(test_str)
    else:
        # print(splited)
        test_str=' '.join(splited)
        # print(test_str)
        modified_lines.append(test_str)


with open('output.txt','w') as f:
    for line in modified_lines:
            f.write(line)
            f.write('\n')

f.close()