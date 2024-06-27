# 1038. Binary Search Tree to Greater Sum Tree
original node value plus the sum of all node value greater than the original node value in BST (.sum)
use .sum += node.val so we have sum value.  then node.val = .sum. we can get GST
And .sum should be equal to current node value plus the sum of all node value greater than the current node value
we need to determine all other node value and the current node value. so need traverse. 
BST have left node right node and root. think about order about it. how to read each node value? we can use recursion

# 91. Decode Ways
first, if not 1-26 or is 0, should return 0. because 0 means nothing
x = len, len is message
how to divide?



# 1382. Balance a Binary Search Tree


# 117. Populating Next Right Pointers in Each Node II



# 1791. Find Center of Star Graph
there is only one center.
so find the same number in each edge.
but just need to compare the first two edge is enough. because each edge have center number
compare edge[0, 0],to edge[1, 0] and edge [1, 1].
we can use if ...or ...    else...

# 128. Longest Consecutive Sequence
we need to create a empty array. use Hashmap
we have an unsorted array of integers nums. so first we need to order it.
we need to use a for loop and while loop to determine that the adjacent numbers in the array differ only by 1 for whole nums. nums and nums - 1
and store the numbers in an empty array. Until the adjacent numbers do not differ by 1.
so we will have many new array. we need to choose the biggest one. 



