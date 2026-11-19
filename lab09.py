# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # Step 1: Find two numbers in the list that add up to the target and return their positions
    # Step 2: Practice example: [2, 7, 11, 15]. Target = 9 -> 2 and 7 from the list add up to 9, and their positions in the list are [0, 1].
    # Step 3: The plan is to go through 1 number at a time. For each number, ask what number is needed to reach the target and if its in the list. If its seen it, return both positions. If not, remember this number and keep going. 
    
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #       to `target`. Assume there is exactly one answer.
    seen = {}                                   # keeps track of the numbers looked at so far
    for j, num in enumerate(nums):
        compliment = target - num               # compliment is the number needed to reach the target
        if compliment in seen:
            return [seen[compliment], j]
        seen[num] = j                           # if I haven't found a match yet, save the number for later


def max_profit(prices):
    # Outline:
    # Step 1: The code should buy on day one, and sell on a later day to maximize profit. If there's no profit, return 0.
    # Step 2: Example: [7, 1, 5, 3, 6, 4], buy at 1, sell at 6, profit 5!
    # Step 3: Plan: run through the prices (list) one at a time, and keep track of the lowest price seen SO FAR. For each price, check what the profit would be if I sold today, and to remember that price!
    
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #       buying on one day and selling on a LATER day. If no profit is possible, return 0.
    
    # no prices means no trades, so no profit
    if not prices:
        return 0

    lowest = prices[0]  # the lowest price seen so far
    max_profit = 0       # the maximum profit seen so far

    for price in prices:
        # checks if this price is the lowest seen so far
        if price < lowest:
            lowest = price
        else:
            # calculates the profit if we sold today
            profit = price - lowest
            # checks if this is the best profit seen so far
            if profit > max_profit:
                max_profit = profit
            
    return max_profit                                  # returns the maximum profit


def max_subarray(nums):
    # Outline:
    # 1. Look to find the number that creates the largest sum when added to the numbers to the left and right of it.
    # 2. Example: [5, 4, -1, 7, 8]. Add all these numbers to get 23
    # 3. The plan: Run through the list one number at a time, but keep a running sum going. If the running sum is negative, reset it to 0. Keep track of the largest sum seen so far and return that at the end. If the running sum ever drops to 0, start over from the current number. 
    
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #       `nums`. The list has at least one number.
    
    current = nums[0]                                      # The current sum of the subarray
    best = nums[0]                                         # The highest sum I've gotten so far. Starts at the first number
                                                           # Not 0, because the answer can be negative
    for num in nums[1:]: 
        if current < 0:                                        # If the current sum is negative, reset it to 0 and start over
            current = num
        else:
            current = current + num                                  # Adds the current number to the current sum

        if current > best:                                    # If the current sum is greater than the best sum I have, update the best sum
            best = current

    return best                                                # Returns the best sum found




def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Step 1: Need to check that each bracket is closed by the right type, and in the right order.
    # Step 2: For example: "([)])", ) shows up while [ is still open, so this doesn't work
    # Step 3: Plan: Run through the string. When I see a closing bracket, I know it has to match the top of the pile. If it doesn't, it's not balanced. The end result should be an empty pile. 
    
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #       order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    
    stack = []                             # Keeps track of opening brackets that haven't been closed yet.
    piles = {")": "(", "]": "[", "}": "{"}      # A dictionary that maps closing brackets to their corresponding opening brackets

    for ch in s:
        if ch in "([{":                       # If the character is an opening bracket, add it to the stack
            stack.append(ch)
        elif ch in ")]}":                     # If a character is a closing bracket, check if it matches the top of the stack
            if len(stack) == 0 or stack[-1] != piles[ch]:  # If the stack is empty or the top of the stack doesn't match the closing bracket, it's not balanced
                return False
            stack.pop()                      # If it matches, remove the opening bracket from the stack

    return len(stack) == 0                  # If the stack is empty at the end, all brackets were matched correctly

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
