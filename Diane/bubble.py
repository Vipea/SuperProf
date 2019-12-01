def sorteren(getallen):
    while True:
        flag = 0
        for i in range(len(getallen)-1):
            if getallen[i] > getallen[i+1]:
                flag = 1
                getallen[i], getallen[i+1] = getallen[i+1], getallen[i]

        if flag == 0:
            print(getallen)
            return getallen

getallen = [100,12,8,55,3,2,107,9,34]
gesorteerd = sorteren(getallen)
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

        print(arr)

mergeSort(getallen);
