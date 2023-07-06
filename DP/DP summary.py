"""
There are 5 patterns:
1. Minimum (Maximum) Path to Reach a Target
2. Distinct Ways
3. Merging Intervals
4. DP on Strings
5.
"""

"""
1. Minimum (Maximum) Path to Reach a Target:
Statement: given a target find minimum or maximum cost/ path/ sum to reach the target
Approach: choose minimum (maximum) path among all possible path before the current state
          then add values for the current state
routes[i] = min(routes[i - 1], route[i - 2], ..., routes[i - k]) + cost[i]
"""
# Top Down:
for i in range(len(ways_size)):
    result = min(result, top_down(target - ways[i]) + cost/ path/ some_sum)

# Bottom Up:
for i in range(len(target)):
    for j in range(len(ways_size)):
        if ways[j] <= i:
            table[i] = min(table[i], table[i - ways[j]] + cost/ path/ some_sum)

"""
2. Distinct Ways
Statement: given a target find a number of distinct ways to reach the target
Approach: sum all possible ways to reach the current state.
routes[i] = routes[i - 1] + routes[i - 2], ..., + routes[i - k]
"""

# Top Down:
for i in range(len(ways_size)):
    result += top_down(target - ways[i])

# Bottom Up:
for i in range(len(target)):
    for j in range(len(ways_size)):
        if ways[j] <= i:
            table[i] += table[i - ways[j]]

"""
3. Merging Intervals
Statement: given a set of numbers find an optimal solution for a problem considering the current number 
and the best right sides
Approach: find an optimal solutions for every interval and return the best possible answer.
dp[i][j] = dp[i][k] + result[k] + dp[k + 1][j]
"""

# Top Down:
for k in range(i, j):
    result = max(result, top_down(nums, i, k - 1) + result[k] + top_down(nums, k + 1, j))

# Bottom Up:
for I in range(1, n):
    for i in range(n - 1):
        j = i + I
        for k in range(i, j):
            dp[i][j] = max(dp[i][j], dp[i][k] + result[k] + dp[k + 1][j])

"""
4. DP on Strings
Statement: most of time you are given two string where lengths of those strings are not big 
Approach: most of the problems on this pattern requires a solution that can be accepted in O(n ** 2)
"""
for i in range(1, n + 1):  # i - indexing string s1
    for j in range(1, m + 1):  # j - indexing string s2
        if dq[i - 1] == s2[j - 1]:
            dp[i][j] = /*code*/
        else:
            dp[i][j] = /*code*/

"""
5. Decision Making
Statement: given a set of values find an answer with an option to choose or ignore the current value
Approach: if you decide to choose the current value, use the previous result where the value was ignored, 
vice-verse, if you decide to ignore the current value, use previous result where value was used.
"""
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j] + array[i], dp[i - 1][j - 1])
        dp[i][j - 1] = max(dp[i][j - 1], dp[i - 1][j - 1] + array[i], array[i])
