import json
import os

folder = os.getcwd()


def item_stats(size_1, size_2, dir_name):
    file_quantity = 0
    file_ext = []
    for item in os.listdir(dir_name):
        if os.path.isfile(item):
            file_size = os.stat(item).st_size
            if size_1 < file_size < size_2:
                file_quantity += 1
                ext = item.rsplit('.', maxsplit=1)[-1].lower()
                if ext not in file_ext:
                    file_ext.append(ext)
    return file_quantity, file_ext


sizes = {
    100: (item_stats(0, 100, folder)),
    1000: (item_stats(100, 1000, folder)),
    10000: (item_stats(1000, 10000, folder)),
    100000: (item_stats(10000, 100000, folder))
}

print(sizes)

with open('sizes_summary.json', 'w', encoding='utf-8') as sizes_file:
    data = json.dumps(sizes)
    sizes_file.write(data)
