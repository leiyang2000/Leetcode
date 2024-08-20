### 1) 1038. Binary Search Tree to Greater Sum Tree
original node value plus the sum of all node value greater than the original node value in BST (.sum) <br>
use .sum += node.val so we have sum value.  then node.val = .sum. we can get GST <br>
And .sum should be equal to current node value plus the sum of all node value greater than the current node value <br>
we need to determine all other node value and the current node value. so need traverse. <br>
BST have left node right node and root. think about order about it. how to read each node value? we can use recursion <br>
<br><br>

### 2) 91. Decode Ways
first, if not 1-26 or is 0, should return 0. because 0 means nothing <br>
x = len, len is message <br>
how to divide? <br>
<br><br>

### 3) 1382. Balance a Binary Search Tree


### 4) 117. Populating Next Right Pointers in Each Node II



### 5) 1791. Find Center of Star Graph
there is only one center. <br>
so find the same number in each edge. <br>
but just need to compare the first two edge is enough. because each edge have center number <br>
compare edge[0, 0],to edge[1, 0] and edge [1, 1]. <br>
we can use if ...or ...    else... <br>
if 0 0 == 1 0 or 0 0 == 1 1 means 0 0 is center. return 0 0 <br>
else means 0 1 is center so return 0 1
<br><br>

### 6) 128. Longest Consecutive Sequence
First, create a hash table, the empty dictionary. <br>
Update the lengths corresponding to num previous and next, that is, num-1 and num+1.<br>
d[num-1] and d[num+1] correspond to x and y, the consecutive lengths before and after the current number.<br>
At this point, the length is x + y + the length of the current number, which is x + 1 + y.<br>
We have a string of consecutive numbers. We want to update the lengths represented by the first and last digits of this string, that is, update to x+1+y.<br>
The first number is the current number minus the length represented by the previous number (num-x) and the last number is (num+y). At this point, the lengths of d[num-x] and d[num+y] are the lengths of the entire string of digits x+1+y.<br>
Setting a res = 0, we update res to indicate the longest consecutive length. If x+1+y is greater than res, then res=x+1+y. then use a for loop.<br>
Finally return res.<br>
<br><br>

### 7) 2285. Maximum Total Importance of Roads
first, traverse all country. determine which country connect the most roads. <br>
store it in an empty array. and order it(roads number). then give the biggest importance to the country have the most roads. <br>
now we have an ordered array (1,2,2,3,3). this is roads. <br>
and we distribute importance. it is (1,2,3,4,5). then we use roads times importanve. <br>
finally, add these 5 number which is the biggest importance <br>
<br><br>

### 8) 141. Linked List Cycle
use a Hash map. create an empty array <br>
use head as current node. we can use while current:    array.add(current) <br>
then read next node. keep adding. so empty array will add a lot of node <br>
when the node is the end. currenr.next will the pos. if the pos in this hash set. return true <br>
else return false. <br>
* double pointer work, question!? <br>
<br><br>

### 9) 2192. All Ancestors of a Node in a Directed Acyclic Graph
it is like leetcode 1791, but not find center <br>
reserve traverse all node. deternmine whether each node has a superior(end). if not, return [] <br>
if there are any superiors, determine how many superiors and names each node has <br>
<br><br>

### 10) 166. Fraction to Recurring Decimal
First, we can determine whether the numerator and denominator are 0. If the numerator is 0, 0 is returned directly. If the denominator is 0, it is meaningless. <br>
then calculate // and %, respectively, the integer part and the remainder part. <br>
<br><br>

### 11) 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
*?*


### 12) 169. Majority Element
sort the nums, and return the mid, becuz mid is the majority element <br>



### 13) 1550. Three Consecutive Odds
use % to determine num in arr is even or odds. if num % 2 =0 is even, = 1 is odds <br>
use for loop to traverse arr. <br>
<br>

### 14) 177. Nth Highest Salary
*?*

### 15) 350. Intersection of Two Arrays II
use hash map<br>
create an empty array to store same number <br>
we can sort two nums array <br>


### 16) 179. Largest Number
because it is int number, we need to arrange these numbers together. so we should change int to string <br>
and we need to compare the first digit size of a number <br>
if there is a 0 in string type, just put it in the end <br>
then reverse sort them <br>


### 17) 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
if there are 4 number, we can just return 0. because we can replace all number<br>
if more than 4 numbers, first, we need to use nums.sort() to sort all int in nums. <br>


### 18) 185. Department Top Three Salaries
*?*

### 19) 2181. Merge Nodes in Between Zeros
define a val = 0, then we use val += sum, sum == val. between two 0 <br>


### 20）192. Word Frequency


### 21）1518. Water Bottles
numofbottle // numofexchanges = 0 ？ <br>
total bottle + numofbottle // numofexchanges <br>
numofbottle % numofexchanges + numofbottle // numofexchanges <br>

### 22) 194. Transpose File


### 23) 2418. Sort the People
Match the name with the height <br>
rank the height from largest to smallest, use reverse or decend <br>
return the name <br>

### 24) 199. Binary Tree Right Side View
Traverse every level of tree <br>
create a empty result arr [] <br>
if not root, there no result, so return this empty arr <br>
create a new arr to store every level node val. from left to right <br>
then we put the right node val to result<br>
return result <br>

### 25) 88. Merge Sorted Array
add nums 2 in nums 1, becuz nums1 has enough space <br>
first, we can call sort func<br>
we also can use two pointers in each nums arr <br>


### 26) 214. Shortest Palindrome




### 27) 26. Remove Duplicates from Sorted Array
i = 0，then if nums i != nums i+1, that is a new number<br>
so i += 1, return i, i is the length <br>


### 28) 218. The Skyline Problem



### 29) 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance



### 30) 233. Number of Digit One
*?*


### 31) 40. Combination Sum II
use dfs <br>
if target == 0, a combination that satisfies the condition is found and added to the result list. <br>
if target < 0: indicates that the current combination is invalid and is directly returned. <br>


### 32) 239. Sliding Window Maximum
Initializes an empty list res to store the result <br>
we can use left and right pointer <br>


### 33) 2134. Minimum Swaps to Group All 1's Together II
[0] is next to [-1] <br>
count number of 1 <br>


### 34) 240. Search a 2D Matrix II
it is a 2D array, matrix[i][j] <br>
we can start from the left botton <br>


### 35) 


### 36)




















