"""
Time Complexity : O(n(k+m)) where n is the no. of queries, k is length of the pattern and m is the avg length of a query 
Space Complexity : O(1) 
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
We iterate through each query and do the 2 pointer approach. Set a boolean to False initially, to start with. Increment the pointer
to the pattern when there is a match and set the boolean to True if we reach end of the pattern. If after that, the query still
has upper case, we set boolean to False and appends it to the result after breaking.
"""

class Solution(object):
    def camelMatch(self, queries, pattern):
        result = []
        for query in queries:
            pointer = 0
            flag = False
            for w in query:
                if pointer < len(pattern) and w == pattern[pointer]:
                    pointer += 1
                    if pointer == len(pattern):
                        flag = True
                elif w.isupper():
                    flag = False
                    break
            result.append(flag)
        return result
        
