with open('examples/Common Data Formats/nginx_logs/nginx_logs', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        result = []
        line = line.split()
        result.append(line[0])
        result.append(line[5].lstrip('"'))
        result.append(line[6])
        final = tuple(result)
        print(final)
