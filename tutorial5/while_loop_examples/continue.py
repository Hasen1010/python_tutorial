print("Please enter a positive integer")
required_count = int(input())
count = 1

print("Start counting")
while count <= required_count:  # The following runs as long as this condition is true
    if count % 2 == 1:
        count += 1
        continue
    print("Count: {0}".format(count))
    count += 1