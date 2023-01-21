import json

filename = 'YourFile.json'  # file name we want to compress
newname = filename.replace('.json', '.min.json')  # Output file name

with open(filename, encoding="utf8") as fp:
    print("Compressing file: " + filename)
    print('Compressing...')

    jload = json.load(fp)
    newfile = json.dumps(jload, indent=None, separators=(',', ':'), ensure_ascii=False)
    newfile = newfile.encode('latin1').decode('utf-8') # remove this
    print(newfile)
    with open(newname, 'w', encoding="utf8") as f:  # add encoding="utf8"
        f.write(newfile)

print('Compression complete!')