# Brute Force
# In a brute force method we can simply use a for loop to iterate through the entirety of our nums list and then use a nested for loop to Iterate over the remaining
# elements in the list and compare the difference between target and our current iteration and see if it exists anywhere in the list If we do find the difference then
# we can return the current iteration of both for loops. This method will at worst 
# case take O(n^2) but use less space since we are not saving any information. 

def two_sum_brute_force(nums, target):
    for i in range(0, len(nums), 1):
        diff = target - nums[i]
        for j in range(i+1, len(nums), 1):
            if (diff == nums[j]):
                return [i,j]

# Using a dictionary
# To optimize the solution we can do it in one pass. By making use of a dictionary we can save the elements in the array and the index they are located at as we iterate
# through nums. As we iterate through nums we will first check to see if the difference is located in our dictionary, if not, then we save the difference as a key in the
# dictionary and set its value to its index. This allows us to avoid using elements twice.

def two_sum_optimized(nums, target):
    hashmap = {}
    for i in range(0, len(nums), 1):
        print(f'i:{i}')
        print(target - nums[i])
        if (target - nums[i]) in hashmap:
            return [hashmap[target-nums[i]], i]
        hashmap[nums[i]] = i

def main():
    nums = [2,7,11,15]
    target = 9
    # result = two_sum_brute_force(nums, target)
    result = two_sum_optimized(nums, target)
    print(result)


if __name__ == "__main__":
    main()

