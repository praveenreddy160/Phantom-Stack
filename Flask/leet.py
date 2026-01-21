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


