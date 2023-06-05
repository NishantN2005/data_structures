def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)-x-1):
            if arr[y]>arr[y+1]:
                temp=arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=temp
        print(arr)
    return arr
"""Iterates over the array and moves the smaller integers to the front-which pushes the largest int to the end ofthe array. 
This repeats over and over until the array is sorted"""
#time complexity is O(N^2), so not very useful for large data sets

def insertion_sort(arr):
    for x in range(1, len(arr)):
        cur=arr[x] 
        j=x-1
        while j>-1 and cur<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=cur
    return arr
""" Checks if the int at the current index is lower than the previous index. If it is it basically duplicates the value into the current index
and keeps depricating and copying until the value at the previous index is smaller than the current value. Then it goes back up one index and assigns the value there to the current."""
#time complextiy is O(N^2), so not very useful for large data sets

def selection_sort(arr):
    for x in range(len(arr)):
        min_index=x
        for y in range(x+1, len(arr)):
            if arr[y]< arr[min_index]:
                min_index=y
        [arr[min_index], arr[x]]=[arr[x], arr[min_index]]
    return arr
"""Iterates over array and swaps the smallest int with the current index over and over while increasing the current index"""
#time complexity is O(N^2), so not very useful for large data sets

def merge_sort(arr): 
    mid=int(len(arr)/2)

    if len(arr)<2:
        return arr
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    arr=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    arr+=left[i:]
    arr+=right[j:]
    return arr
"""Recursively breaks the arr into two halfs. Then it compares the values and merges it back together"""
#time complexity is O(nlog(n)), which is better than the previous sorting methods

def partition(arr, start, end):
    pivot_index=start
    pivot=arr[pivot_index]
    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start+=1

        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end], arr[start]
    arr[pivot_index], arr[end]=arr[end], arr[pivot_index]
    return end
def quick_sort(arr, start, end):
    if start<end:
        partition_index=partition(arr, start, end)
        quick_sort(arr, start, partition_index-1)
        quick_sort(arr, partition_index+1, end)
    return arr



    
arr=[5,1,9,6,7,2,3,0]
print(quick_sort(arr,0,len(arr)-1))

