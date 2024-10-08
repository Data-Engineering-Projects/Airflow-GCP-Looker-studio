import json

def schema_and_data_transform(line):
    values = line.rstrip('\n').split(',')
    obj = {
        'rank': values[0],
        'name': values[1],
        'country': values[2]
    }

    # Convert the dictionary to a JSON string
    json_string = json.dumps(obj)

    return json_string
