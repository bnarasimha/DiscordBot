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
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(log_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        if not file_exists:
            csv_writer.writerow(header)
        
        csv_writer.writerow([timestamp, prompt, llmresponse])
    
    print(f"Logged: {timestamp} - {prompt} - {llmresponse}")

def logUserFeedback(prompt, feedback):
    if (prompt != None):
        with open(log_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        updated = False
        for row in rows:
            if row["Prompt"] == prompt:
                row["User_Feedback"] = feedback
                updated = True
                break

        if updated:
            with open(log_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print(f"Updated entry")
        else:
            print(f"No entry found")





        # with open(log_file_path, 'r') as readFile,  open(log_file_path, 'a') as writeFile:
        #     for row in readFile:
        #         if row["Prompt"] == prompt:
        #             writeFile.writerow([row["Timestamp"], row["Prompt"], row["LLM_Response"], feedback])
        #             print(f"User feedback has been updated")
        

