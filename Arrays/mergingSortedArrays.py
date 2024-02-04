def mergingSortedArrays(arr1, arr2):

    mergedArray = []
    i = 0
    j = 0        
    item_arr1 = arr1[0]
    item_arr2 = arr2[0]

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    while(item_arr1 or item_arr2):
        if( item_arr2 == None or (item_arr1 >= item_arr2)):
            mergedArray.append(item_arr2)
            item_arr2 = arr2[i]
            i = i+1
        else:
            mergedArray.append(item_arr1)
            item_arr1 = arr1[j]
            j = j+1

    return MER

print(mergingSortedArrays([0,3,4,31], [4,6,30]))

# def mergingSortedArrays(arr1, arr2):
#     mergedArray = []
#     i = 0
#     j = 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             mergedArray.append(arr1[i])
#             i += 1
#         else:
#             mergedArray.append(arr2[j])
#             j += 1
    
#     # Append remaining elements from arr1 and arr2, if any
#     while i < len(arr1):
#         mergedArray.append(arr1[i])
#         i += 1

#     while j < len(arr2):
#         mergedArray.append(arr2[j])
#         j += 1
    
#     return mergedArray

# result = mergingSortedArrays([0, 3, 4, 31], [4, 6, 30])
# print(result)
