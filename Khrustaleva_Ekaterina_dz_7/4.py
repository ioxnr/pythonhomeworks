import os

folder = os.getcwd()

sizes = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}

for item in os.scandir(folder):
    if os.path.isfile(item):
        file_size = os.stat(item).st_size
        if file_size <= 100:
            sizes[100] += 1
        elif 100 < file_size <= 1000:
            sizes[1000] += 1
        elif 1000 < file_size <= 10000:
            sizes[10000] += 1
        elif 10000 < file_size <= 100000:
            sizes[100000] += 1

print(sizes)
