def find_ceo(array_of_ppl):
    highest=array_of_ppl[0]
    for i in range(highest, 0, -1):
        try:
            array_of_ppl.pop(i)
        except:
            pass
    if highest != 0:
        array_of_ppl.pop(0)
    return len(array_of_ppl) + highest



file = open("B-small-attempt0.in", "r").read().splitlines()
num_of_case = int(file[0])
num_case_on = 0
loop = 1
line_type="num of lines"
for line in file:
    #loop is a num of the line we are on
    if loop != 1:
        if line_type == "num of lines":
            num_of_lines=int(line)
            line_type = "counting"
            array_of_ppl=[]
            num_case_on +=1
            num_of_lines_done=1
        elif line_type == "counting":
            # make an array
            line = line.split()
            for i in range(int(line[0])):
                array_of_ppl.append(int(line[1]))
            if num_of_lines_done == num_of_lines:
                line_type = "num of lines"
                array_of_ppl.sort(reverse=True)
                ceo_num = find_ceo(array_of_ppl)
                print("Case #"+str(num_case_on)+": "+str(ceo_num))
            num_of_lines_done += 1




 
            

    loop +=1