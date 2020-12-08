import heapq as heap 

def solution(A,B):

    count = 0
    value = 0
    
    difference = sum(A) - sum(B)

    if difference == 0:
        return 0
    elif difference < 0:
        min_heap, max_heap = A,B
    else:
        min_heap, max_heap = B,A
    
    difference = abs(difference)

    heap.heapify(min_heap)
    max_heap = [-i for i in max_heap]
    heap.heapify(max_heap)

    count = 0
    value = 0

    while value < difference:

        max_heap_value = abs(max_heap[0])
        min_heap_value = min_heap[0]
        
        if min_heap_value == 6 and max_heap_value == 1:
            return -1

        min_difference = 6-min_heap_value 
        max_difference = max_heap_value-1 

        count+=1
        value+= max(min_difference, max_difference)

        if min_difference>max_difference:
            heap.heappop(min_heap)
            heap.heappush(min_heap,6)
        else:
            heap.heappop(max_heap)
            heap.heappush(max_heap,-1)
    
    return count