### 1038. Binary Search Tree to Greater Sum Tree
original node value plus the sum of all node value greater than the original node value in BST (.sum) <br>
use .sum += node.val so we have sum value.  then node.val = .sum. we can get GST <br>
And .sum should be equal to current node value plus the sum of all node value greater than the current node value <br>
we need to determine all other node value and the current node value. so need traverse. <br>
BST have left node right node and root. think about order about it. how to read each node value? we can use recursion <br>
<br><br>

### 91. Decode Ways
first, if not 1-26 or is 0, should return 0. because 0 means nothing <br>
x = len, len is message <br>
how to divide? <br>
<br><br>

### 1382. Balance a Binary Search Tree


### 117. Populating Next Right Pointers in Each Node II



### 1791. Find Center of Star Graph
there is only one center. <br>
so find the same number in each edge. <br>
but just need to compare the first two edge is enough. because each edge have center number <br>
compare edge[0, 0],to edge[1, 0] and edge [1, 1]. <br>
we can use if ...or ...    else... <br>
if 0 0 == 1 0 or 0 0 == 1 1 means 0 0 is center. return 0 0 <br>
else means 0 1 is center so return 0 1
<br><br>

### 128. Longest Consecutive Sequence
we need to create a empty array. use Hashmap <br>
we have an unsorted array of integers nums. so first we need to order it. <br>
we need to use a for loop and while loop to determine that the adjacent numbers in the array differ only by 1 for whole nums. nums and nums - 1 <br>
for i in len(nums) <br>
and store the numbers in an empty array. Until the adjacent numbers do not differ by 1. <br>
so we will have many new array. we need to choose the biggest one. <br>
<br><br>

### 2285. Maximum Total Importance of Roads
first, traverse all country. determine which country connect the most roads. <br>
store it in an empty array. and order it(roads number). then give the biggest importance to the country have the most roads. <br>
now we have an ordered array (1,2,2,3,3). this is roads. <br>
and we distribute importance. it is (1,2,3,4,5). then we use roads times importanve. <br>
finally, add these 5 number which is the biggest importance <br>
<br><br>

### 141 Linked List Cycle
use a Hash map. create an empty array <br>
use head as currenr node. we can use while current:    array.add(current) <br>
then read next node. keep adding. so empty array will add a lot of node <br>
when the node is the end. currenr.next will the pos. if the pos in this hash set. return true <br>
else return false. <br>
* double pointer work, question!? <br>
<br><br>





