from typing import List

def test_function(nums: List[int], target: int):
    difference_dictionary = {}
    for i in range(0, len(nums), 1):
        print(f'i:{i}')
        difference = target - nums[i]
        print(difference)
        if (difference in difference_dictionary):
            return [difference_dictionary[difference], i]
        else: 
            difference_dictionary[nums[i]] = i
    

def main():
    nums = [-2,7,11,15]
    target = 9

    print (test_function(nums, target))


if __name__ == "__main__":
    main()