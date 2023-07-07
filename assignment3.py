q1>def threeSumClosest(nums, target):
    nums.sort()  # Sort the array to enable the two-pointer approach
    closest_sum = float('inf')  # Initialize the closest sum to a large value

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return current_sum  # Found an exact match, return the sum

            # Update the closest_sum if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1  # Move the left pointer to increase the sum
            else:
                right -= 1  # Move the right pointer to decrease the sum

    return closest_sum  # Return the closest sum found

# Example usage
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)
q2>def fourSum(nums, target):
    nums.sort()  # Sort the array to enable the two-pointer approach
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the first element

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicates for the second element

            left = j + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the fourth element

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

    return result

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)
q3>def nextPermutation(nums):
    # Find the first pair of adjacent elements where nums[i-1] < nums[i]
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i == 0:
        # Array is in descending order, reverse it to get the lowest possible order
        nums.reverse()
    else:
        # Find the smallest number in the suffix that is larger than nums[i-1]
        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1

        # Swap nums[i-1] with the smallest number found in the suffix
        nums[i-1], nums[j] = nums[j], nums[i-1]

        # Reverse the suffix to obtain the next lexicographically greater permutation
        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

# Example usage
nums = [1, 2, 3]
result = nextPermutation(nums)
print(result)
q4>def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Target value not found, return the index for insertion

# Example usage
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)
q5>def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    # If we reach this point, all digits were 9
    return [1] + digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)
q6>def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)
q7>def findMissingRanges(nums, lower, upper):
    ranges = []
    prev = lower - 1

    for num in nums + [upper + 1]:
        if num > prev + 1:
            ranges.append(getRange(prev + 1, num - 1))
        prev = num

    return ranges

def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + '->' + str(end)

# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
q8>def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort the intervals based on the start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False  # Overlapping intervals found

    return True  # No overlapping intervals found, person can attend all meetings

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)
