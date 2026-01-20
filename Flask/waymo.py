def parse_log_line(log_line):
    log_line = log_line.strip()
    
    timestamp_end = log_line.find("]")
    timestamp = log_line[1:timestamp_end]
    
    parts = log_line.split(" ")
    
    severity = parts[2].replace("[", "").replace("]", "")
    
    return {
        "time": timestamp,
        "level": severity,
        "message": " ".join(parts[3:])
    }

if __name__ == "__main__":
    sample_data = "[2025-01-18 14:00:00] [CRITICAL] Sensor:Lidar_Front disconnected"
    
    result = parse_log_line(sample_data)
    print(result)



import re

file_content = """
[Log] System started
[Log] ERROR: Disk full
[Log] User logged in
[Log] ERROR: Network timeout
"""

matches = re.findall("ERROR", file_content)

print(matches)
# Output: ['ERROR', 'ERROR']
