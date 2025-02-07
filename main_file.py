import os
import pandas as pd
import csv
from pprint import pprint

# Create 'static' directory if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

# Data for ginfo.csv
ginfo_data = {
    'Group ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'Members': [3, 4, 2, 5, 8, 7, 6, 10, 3, 9, 4, 5, 2, 6, 11, 4, 7, 5, 3, 8],
    'Gender': ['Boys', 'Girls', 'Boys', 'Girls', '5 Boys & 3 Girls', 'Girls', 'Boys', '6 Boys & 4 Girls', 'Girls', '4 Boys & 5 Girls', 'Boys', 'Girls', 'Boys', 'Girls', '7 Boys & 4 Girls', 'Boys', '3 Boys & 4 Girls', 'Girls', 'Boys', '5 Boys & 3 Girls']
}

# Create a DataFrame for ginfo.csv
ginfo_df = pd.DataFrame(ginfo_data)

# Save the DataFrame to ginfo.csv in the static folder
ginfo_df.to_csv('static/ginfo.csv', index=False)

# Data for hinfo.csv
hinfo_data = {
    'H_Name': [
        'Boys Hostel A', 'Boys Hostel A', 'Boys Hostel A',
        'Girls Hostel B', 'Girls Hostel B', 'Girls Hostel B',
        'Boys Hostel C', 'Boys Hostel C', 'Boys Hostel C',
        'Girls Hostel D', 'Girls Hostel D', 'Girls Hostel D',
        'Boys Hostel E', 'Boys Hostel E', 'Boys Hostel E',
        'Girls Hostel F', 'Girls Hostel F', 'Girls Hostel F',
        'Boys Hostel G', 'Boys Hostel G', 'Boys Hostel G',
        'Girls Hostel H', 'Girls Hostel H', 'Girls Hostel H',
        'Boys Hostel I', 'Boys Hostel I', 'Boys Hostel I',
        'Girls Hostel J', 'Girls Hostel J', 'Girls Hostel J'
    ],
    'R_no': [
        101, 102, 103,
        201, 202, 203,
        301, 302, 303,
        401, 402, 403,
        501, 502, 503,
        601, 602, 603,
        701, 702, 703,
        801, 802, 803,
        901, 902, 903,
        1001, 1002, 1003
    ],
    'Cap': [
        3, 2, 5,
        3, 2, 4,
        2, 3, 5,
        2, 3, 5,
        4, 3, 2,
        3, 5, 4,
        2, 3, 6,
        2, 3, 2,
        4, 3, 2,
        3, 6, 4
    ],
    'Gender': [
        'Boys', 'Boys', 'Boys',
        'Girls', 'Girls', 'Girls',
        'Boys', 'Boys', 'Boys',
        'Girls', 'Girls', 'Girls',
        'Boys', 'Boys', 'Boys',
        'Girls', 'Girls', 'Girls',
        'Boys', 'Boys', 'Boys',
        'Girls', 'Girls', 'Girls',
        'Boys', 'Boys', 'Boys',
        'Girls', 'Girls', 'Girls'
    ]
}

# Create a DataFrame for hinfo.csv
hinfo_df = pd.DataFrame(hinfo_data)

# Save the DataFrame to hinfo.csv in the static folder
hinfo_df.to_csv('static/hinfo.csv', index=False)

print("ginfo.csv and hinfo.csv created successfully in the static folder.")

rows_group = []
rows_hostel = []
allocated = []
not_allocated = []



#Reading the Group CSV
with open('static/ginfo.csv', mode='r') as data_g:
  csv_data = csv.DictReader(data_g)

  for r in csv_data:
    if len(r["Gender"]) <= 5:
      row_tuple = (r['Group ID'], r["Members"], r['Gender'])
      rows_group.append(row_tuple)

    else:
      lst_temp = r['Gender'].split(' & ')
      cap = ''.join(filter(str.isdigit, lst_temp[0]))
      gen = lst_temp[0][2:]
      row_tuple = (r['Group ID'], cap, gen)
      rows_group.append(row_tuple)

      cap = ''.join(filter(str.isdigit, lst_temp[1]))
      gen = lst_temp[1][2:]
      row_tuple = (r['Group ID'], cap, gen)
      rows_group.append(row_tuple)

#Reading the Hostel CSV
with open('static/hinfo.csv', 'r') as data_h:
  csv_data = csv.DictReader(data_h)
  for r in csv_data:
    row_tuple = (r['H_Name'], r['R_no'], r['Cap'], r['Gender'])
    rows_hostel.append(row_tuple)

def allocate(groups, hostels):
  for hostel in hostels:
    for group in groups:
      if hostel[1] not in allocated:
        if hostel[2] == group[1] and hostel[3] == group[2]:
          allocated.append(hostel)

          print(f"Room no {hostel[1]} allocated to Group {group[0]}")
          break
        elif hostel[2] == group[1] and hostel[3] != group[2]:
          print(f"Room {hostel[1]} Reserved for other gender")
        else:
          print("room already allocated")
  return allocate

allocate(rows_group,rows_hostel)
not_allocated = [row for row in rows_hostel if row not in allocated]
print("\n\n\n")
pprint(allocated)
print(f"Rooms allocated: {len(allocated)}")
print(f"Total rooms: {len(rows_hostel)}")
print(f"Rooms not allocated: {len(rows_hostel)-len(allocated)}")

pprint(not_allocated)
