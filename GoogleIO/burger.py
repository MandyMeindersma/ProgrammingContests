def make_array(even_odd, cases):
    burger_dist=[]
    for item in range(cases):
        burger_dist.append(0)
    if even_odd=="even":
        #even
        mid=cases/2
        for looper in range(mid-1):
            burger_dist[mid+looper]=mid-looper-1
            burger_dist[mid-looper-1]=mid-looper-1
    else:
        #odd
        mid=int(cases/2) # rounds down
        burger_dist[mid]=mid
        for looper in range(1,mid):
            burger_dist[mid-looper]=mid-looper
            burger_dist[mid+looper]=mid-looper
    return burger_dist



file = open("A-large.in", "r").read().splitlines()
num_of_case = int(file[0])
num_case_on = 0
loop = 1
line_type_start=False
for line in file:
    #loop is a num of the line we are on
    if line_type_start:
        #the one number
        num_case_on +=1
        if int(line) %2 == 0:
            #even
            cases = int(line)
            even_odd="even"
        else:
            #odd
            cases = int(line)
            even_odd="odd"
    else:
        if loop != 1:
            #all the numbers
            # make error array
            burger_dist = make_array(even_odd, cases)
            items = line.split()
            error_now=0
            for i in range(cases):
                error_now += (int(items[i])-burger_dist[i])**2
            burger_dist.sort()
            items.sort()
            error_new = 0
            for i in range(cases):
                error_new += (int(items[i])-burger_dist[i])**2
            
            error = error_new
            
            print("Case #"+str(num_case_on)+": "+str(error))

    

    loop +=1
    line_type_start= not line_type_start
