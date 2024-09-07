import json


def recursive_parser(data, result_data, key):
    for result in result_data.get(key):
        if data.get("id") == result.get("id"):
            data.update(result)
    if key in data.keys():
        new_data = data.get(key)
        cyc_list(new_data, result_data, key)
    else:
        return


def cyc_list(data, result_data, key):
    for test in data:
        recursive_parser(test, result_data, key)


def task3(path1, path2, path3):
    with open(path1, "r") as json_file:
        data1 = json.load(json_file)
    with open(path2, "r") as json_file:
        data2 = json.load(json_file)

    for test in data1.get("tests"):
        recursive_parser(test, data2, "values")

    with open(path3, "w") as json_file:
        json.dump(data1, json_file)


path1 = "tests.json"
path2 = "values.json"
path3 = "report.json"

task3(path1, path2, path3)
