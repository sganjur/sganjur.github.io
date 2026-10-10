import csv
import os

replacements = {
    "Science": "Physical Sciences",
    "Physical & Earth Sciences": "Physical Sciences",
    "Physical Sciences": "Physical Sciences",
    "Life Sciences & Medicine": "Life Sciences",
    "Life Sciences": "Life Sciences",
    "Education": "Social Sciences",
    "Law": "Social Sciences",
    "Social Sciences": "Social Sciences"
}

input_file = "Polymaths.csv"
output_file = "Polymaths.csv.tmp"

with open(input_file, mode='r', encoding='utf-8') as f_in, \
     open(output_file, mode='w', encoding='utf-8', newline='') as f_out:
    
    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        areas = [a.strip() for a in row["Areas of Knowledge"].split(",") if a.strip()]
        new_areas = set()
        for a in areas:
            if a in replacements:
                new_areas.add(replacements[a])
            else:
                new_areas.add(a)
        
        # We need to quote if there are internal commas, but the csv module handles that automatically
        # if we just give it a string.
        row["Areas of Knowledge"] = ", ".join(sorted(list(new_areas)))
        writer.writerow(row)

os.replace(output_file, input_file)
print("CSV cleaned successfully!")
