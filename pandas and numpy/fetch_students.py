import json
import urllib.request
import csv

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
with urllib.request.urlopen(url) as response:
    data = json.load(response)

if isinstance(data, dict) and "students" in data:
    data = data["students"]

if not isinstance(data, list):
    raise ValueError("Expected JSON data to be a list of students")

sorted_data = sorted(data, key=lambda x: x.get("marks", 0), reverse=True)
print(sorted_data)

if sorted_data:
    fieldnames = list(sorted_data[0].keys())
    with open("sorted_student_data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

print("Sorted data has been saved to 'sorted_student_data.csv'")
