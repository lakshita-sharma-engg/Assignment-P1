data = [[15, 25], [35, 45], [55, 65]]
print(data)

updated_data = list(data)
print(updated_data)

updated_data[1][1] = 99

print("Original data:", data)
print("Updated data:", updated_data)