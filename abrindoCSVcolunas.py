f = open("D:/Users/Roberson/Google Drive/Python/diversos/payments.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
print(full_data)

# ou use o print(len(full_data)

count = 0
for row in full_data:
    count += 1
print(count)