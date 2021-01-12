# 136.Single Number

[TOC]

---

* Link: https://leetcode.com/problems/single-number/



## Question

Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**

```
Input: [2,2,1]
Output: 1
```

**Example 2:**

```
Input: [4,1,2,1,2]
Output: 4
```



## Solutions

### Solution 0

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(nums) <= 1:
                return nums[0]
            
            check_num = nums.pop(0)
            if check_num in nums:
                nums.remove(check_num)
                continue
            else:
                return check_num
```



### Solution 1: List operation

**Algorithm**

1. Iterate over all the elements in `nums`
2. If some number in `nums` is new to array, append it
3. If some number is already in the array, remove it

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
```

**Complexity Analysis**

- Time complexity : $O(n^2)$. We iterate through `nums`, taking $O(n)$ time. We search the whole list to find whether there is duplicate number, taking $O(n)$ time. Because search is in the `for` loop, so we have to multiply both time complexities which is $O(n^2)$.
- Space complexity : $O(n)$. We need a list of size $n$ to contain elements in `nums`.

### Solution 2: Hash Table

**Algorithm**

We use hash table to avoid the $O(n)$ time required for searching the elements.

1. Iterate through all elements in `nums` and set up key/value pair.
2. Return the element which appeared only once.

```python
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
```

**Complexity Analysis**

- Time complexity : $O(n \cdot 1) =O(n)$. Time complexity of `for` loop is $O(n)$. Time complexity of hash table (dictionary in python) operation `pop` is $O(1)$.
- Space complexity : $O(n)$. The space required by `hash_table` is equal to the number of elements in `nums`.

### Solution 3: Math

**Concept**

$2 * (a+b+c) - (2a+2b+c) = c$

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
```

**Complexity Analysis**

- Time complexity : $O(n + n) = O(n)$. `sum` will call `next` to iterate through `nums`. We can see it as `sum(list(i, for i in nums))` which means the time complexity is $O(n)$ because of the number of elements($n$) in `nums`.
- Space complexity : $O(n + n) = O(n)$. `set` needs space for the elements in `nums`.

### Solution 4: Bit Manipulation

**Concept**

- If we take XOR of zero and some bit, it will return that bit
    - $a \oplus 0 = a$
- If we take XOR of two same bits, it will return 0
    - $a \oplus a = 0$
- $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$

So we can XOR all bits together to find the unique number.

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```

**Complexity Analysis**

- Time complexity : $O(n)$. We only iterate through `nums`, so the time complexity is the number of elements in `nums`.
- Space complexity : $O(1)$.