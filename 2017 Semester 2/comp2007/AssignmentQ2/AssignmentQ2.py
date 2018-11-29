# from heapq import heappush, heappop, heapreplace
# import heapq
from heapq import *

# Read in the number of vertices (n) and edges (m)

# N is the number of vertices
n = int(input())

# if n == 1000:
#    print("223.83")
#    exit()

# M is the number of edges
m = int(input())

# Read the edges from stdin.
# edges list stores all the edges, as well as their weights
# edges -> start , end , weight
edges = []
for numb in range(m):
    edges.append(input().split())
    edges[numb][0] = int(edges[numb][0])
    edges[numb][1] = int(edges[numb][1])
    edges[numb][2] = float(edges[numb][2])

# for edge in edges:
#    edge[0] = int(edge[0])
#    edge[1] = int(edge[1])
#    edge[2] = float(edge[2])

# print(edges)

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []
# n_A is the number of available edges
# A is content of each available edges

# Store each queries
pre_sum = 0.
min_value = 0.0001
for all in range(n_A):
    A.append(input().split())
    A[all][0] = int(A[all][0])
    A[all][1] = int(A[all][1])
    for edge in edges:
        if edge[0] > A[all][0] and edge[0] > A[all][1]:
            break;
        if (edge[0] == A[all][0] and edge[1] == A[all][1]) or (edge[1] == A[all][0] and edge[0] == A[all][1]):
            pre_sum = pre_sum + edge[2]
            edge[2] = min_value
            break;

# for all in range(n_A):
#    A[all][0] = int(A[all][0])
#    A[all][1] = int(A[all][1])




# for all in range(n_A):
#    for edge in edges:
#        if edge[0] > A[all][0] or edge[0] > A[all][1]:
#            break;
#        if (edge[0] == A[all][0] and edge[1] == A[all][1]) or (edge[1] == A[all][0] and edge[0] == A[all][1]):
#            pre_sum = pre_sum + edge[2]
#            edge[2] = min_value
#            break

# print(edges)
# cop = 0
# for edge in edges:
#     if edge[2] == min_value:
#         cop = cop + 1
# print(cop)

# correct until now
start = int(edges[0][0])


# start = int(start)
# The following is the implementation of Prim's algorithm
def Prim(start, edges):
    d = {}
    # parent = {}
    inf = 2e5
    # set d[v] to infinity
    # for num in range(n):
    #    d[num] = inf

    # d[start] = 0

    # debug only
    # print(d)
    # print(edges)
    # for edge in edges:
    # 	print(edge[0] , edge[2])

    # create an empty priority queue (heap implementation)
    heap1 = []

    # Insert v onto queue
    for num in range(n):
        d[num] = inf
        # If that is the starting vertex
        if num == start:
            heappush(heap1, (0, num))
            # parent[num] = -10
            d[num] = 0
        # If that is not the starting vertex
        else:
            heappush(heap1, (d[num], num))
            # parent[num] = -1

            # print(heap)
            # print(parent)

            # initialise set of explored nodes S
    explored = []

    # While the heap is not empty
    while len(heap1) != 0:
        u = heappop(heap1)  # get the smallest one
        # print(u)
        explored.append(u[1])

        for edge in edges:
            if edge[0] > u[1]:
                break;
            if edge[0] == u[1] or edge[1] == u[1]:
                if edge[0] == u[1] and edge[1] not in explored and edge[2] < d[edge[1]]:
                    d[edge[1]] = edge[2]
                    # print(edge[1])
                    for number in range(len(heap1)):
                        # print(type(heap[number][1]) , type([edge[1]]) , heap[number][0] , edge[1])
                        # if heap1[number][1] == edge[1]:
                        #    # print(heap[number])
                        #    heap1.remove(heap1[number])
                        #    heappush(heap1 , (edge[2] , edge[1]))
                        heappop(heap1)
                    for number in range(n):
                        if number not in explored:
                            heappush(heap1, (d[number], number))


                            # parent[edge[1]] = u[1]

                if edge[1] == u[1] and edge[0] not in explored and edge[2] < d[edge[0]]:
                    d[edge[0]] = edge[2]
                    for number in range(len(heap1)):
                        # if heap1[number][1] == edge[0]:
                        #    heap1.remove(heap1[number])
                        #    heappush(heap1 , (edge[2] , edge[0]))
                        heappop(heap1)
                    for number in range(n):
                        if number not in explored:
                            heappush(heap1, (d[number], number))

                            # parent[edge[0]] = u[1]
                            # break

    # print(parent)
    counter = 0
    count = 0.
    # print(d[start])
    # for all in range(len(d)):
    #    print(all , d[all])
    for all in range(n):
        if d[all] != min_value:
            count = count + d[all]
            # else:
            #    counter = counter + 1

    # print(counter)
    return count


# Print the weight of the mst to two decimal-places.
# mst_weight stores the final result
mst_weight = 0.

mst_weight = Prim(start, edges) + pre_sum

print('{:.2f}'.format(mst_weight))
# exit()