import json

def GetJsonFromFile(filePath):
    contents = ""
    fh = open(filePath)
    for line in fh:
        cleanedLine = line.split("//", 1)[0]
        if len(cleanedLine) > 0 and line.endswith("\n") and "\n" not in cleanedLine:
            cleanedLine += "\n"
        contents += cleanedLine
    fh.close
    while "/*" in contents:
        preComment, postComment = contents.split("/*", 1)
        contents = preComment + postComment.split("*/", 1)[1]
    dict_pairs = {}
    json_file = json.loads(contents)
    if "columns" in json_file:
        for i in json_file["columns"]:
            dict_pairs.update(i)
        return dict_pairs
    else:
        {}

def read_json_file(json_file):
    json_file = json.loads(json_file)
    dict_pairs = {}
    if "columns" in json_file:
        for i in json_file["columns"]:
            dict_pairs.update(i)
        return dict_pairs

