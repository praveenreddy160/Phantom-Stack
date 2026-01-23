# def read_massive_log_file(file_path):
#     """
#     Generator function to read a large file one line at a time.
#     It yields a line, pauses execution, and waits for the next call.
#     """
#     # 'with' ensures the file is closed properly even if we crash
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line

# # --- Usage in the Interview ---

# # 1. Create the generator object (This executes nothing yet!)
# log_generator = read_massive_log_file("waymo_drive_logs.txt")

# # 2. Iterate through it (This pulls lines one by one)
# error_count = 0
# for log_line in log_generator:
#     if "ERROR" in log_line:
#         error_count += 1
#         # (Optional) Process the error here

# print(f"Found {error_count} errors.")

def sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return[]

print(sum([2,7,11,15], 9))


def subarraySum(nums, k):
    # 1. Initialize variables
    count = 0
    current_sum = 0
    
    prefix_sums = {0: 1}
    
    # 3. Walk through the array
    for num in nums:
        # Update running total
        current_sum += num
        
       
        needed_past_sum = current_sum - k
        
        if needed_past_sum in prefix_sums:
            # Add the number of times we saw that past sum
            count += prefix_sums[needed_past_sum]
        
    
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
    return count

# --- Test Case ---
# You can copy-paste this to test it
nums = [3, 4, 7, -7]
k = 7
print(f"Input: {nums}, Target: {k}")
print(f"Result: {subarraySum(nums, k)}")