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
    #   ...Find the first element to add by looping through outter loop and use an inner for loop to
    #  loop through the second element to add(that is next to the first added element)
    # Also, check if the sum of those equal to target. If it is, then return the index of those 2 element in an array.
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.#(nums[i]<nums[j]) and 
    for i in range(len(nums)-1):
        for j in range (i+1, len(nums)):
            if ((nums[i]+nums[j])==target):
                return([i,j])
        


    


def max_profit(prices):
    # Outline:
    #   ...Create 2 for loop, one for moving through each element and other for moving through the element that is next  to the 
    #element that we are checking right now. inside of the second loop, substract the first element from the second element and 
    # store that substraction in some variable. Then check if that substraction is bigger or lessthan next substraction. If the it's 
    # bigger than every substraction, then print that substraction.
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    #i:int=0
    large_sub:int=0
 
    for i in range(len(prices)-1):
        for j in  range(i+1,len(prices)):
            current_sub:int=prices[j]-prices[i]
            if(current_sub>large_sub):
                large_sub=current_sub
    return large_sub
            




def max_subarray(nums):
    # Outline:Create a outer for loop to increase the j value,
    # for example after finding the sum of whole thing[inner loop] on first round it increases j to go to the next level(num[1]).
    # And create inner loop to calculate sum in different level.(nums[1]+nums[2],nums[1]+nums[2]+nums[3]...). Also we need to set 1st 
    # value in element as the bigger sum firstly beacuse we don't know which sum is bigger yet. Then, chech if the previous sum is less than current sum,
    #  if it is set the final sum to current sum. If not move on to the next sum.and the inner loop start from second element beacuse we are adding other
    #  element with first element.
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    final_sum:int=nums[0]
    for i in range(len(nums)-1):
        bigger_sum=nums[i]
        for j in range(i+1,len(nums)):
            bigger_sum+=nums[j]
            if bigger_sum>final_sum:
                final_sum=bigger_sum
        

    return final_sum
       

    pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([1, 2]) == 1


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    
    print(two_sum([3, 2, 4], 6) )  # [1, 2]
    print(max_profit([7, 6, 4, 3, 1]) )# returns 0
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    
    test_two_sum()
    test_max_profit()
    test_max_subarray()







    


if __name__ == "__main__":
    main()
