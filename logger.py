import csv
import os

# Define the log file path
log_file_path = 'logs/llmresponses.csv'

# Define the header for the CSV file
header = ['Timestamp', 'Prompt', 'LLM Response']

# Check if the log file exists
file_exists = os.path.isfile(log_file_path)

# Function to log info into the CSV file
def log_info(prompt, llmresponse):
    # Get the current timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Open the log file in append mode
    with open(log_file_path, 'a', newline='') as csvfile:
        # Create a csv writer object
        csv_writer = csv.writer(csvfile)
        
        # Write the header if the file is being created
        if not file_exists:
            csv_writer.writerow(header)
        
        # Write the log entry
        csv_writer.writerow([timestamp, prompt, llmresponse])
    
    print(f"Logged: {timestamp} - {prompt} - {llmresponse}")