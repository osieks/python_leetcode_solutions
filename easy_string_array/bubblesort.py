def bubble_sort(data):
    for i in range(len(data)):
        #print("i=",i)
        for j in range(len(data[:-1-i])):
            #print("j=",j)
            if data[j]>data[j+1]:
                #print("swap ",data[j]," i ",data[j+1])
                tmp = data[j]
                data[j]=data[j+1]
                data[j+1]=tmp
            #print("don't swap ",data[j]," i ",data[j+1])
    #print ("sorted")
    return data