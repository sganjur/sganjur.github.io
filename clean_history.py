import csv
import os

replacements = {
    "History": "History & Geography"
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
        
        row["Areas of Knowledge"] = ", ".join(sorted(list(new_areas)))
        writer.writerow(row)

os.replace(output_file, input_file)
print("CSV cleaned successfully (History -> History & Geography)!")
