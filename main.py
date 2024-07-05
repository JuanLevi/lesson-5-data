


def MergeSort(list):

    if len(list)>1:
        mid=len(list)//2
        l=list[0:mid]
        r=list[mid:len(list)]

        print(l)
        print(r)

        MergeSort(l)
        MergeSort(r)

        i=0
        j=0
        k=0

        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                list[k]=l[i]
                i+=1
            elif l[i]<r[j]:
                list[k]=r[j]
                j+=1
            k+=1
        
        while i<len(l):
            list[k]=l[i]
            i+=1
            k+=1

        while j<len(r):
            list[k]=r[j]
            j+=1
            k+=1
        
        print(list)








    

list1=[-2,5,2,8,9,1,13,245,-12,1251,8556,56858,-23,12]

MergeSort(list1)

















