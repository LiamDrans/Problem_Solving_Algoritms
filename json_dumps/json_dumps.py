"""Program to perform the function of json.dumps on dictionary objects featuring recursive logic"""

def json_dumps(dictionary):
    """Takes the dictionary to be converted to json format"""

    json_string = ""
    dict_counter = 0

    for key in dictionary:

        dict_counter += 1
        json_key = key_to_json(key)

        if isinstance(dictionary[key], dict):

            json_string = json_dict(
                json_key, dictionary[key], dict_counter, len(dictionary), json_string
            )

        elif isinstance(dictionary[key], (list, tuple)):

            json_string = json_list(json_key, dictionary[key], json_string)

        else:
            json_key = key_to_json(key)
            json_value = value_to_json(dictionary[key])

            json_string = json_element(
                json_key, json_value, dict_counter, len(dictionary), json_string
            )

    return json_string

def key_to_json(key):

    """Converts the key of the json into what is expected in the json format - i.e. bool True -> true"""

    return [str(key).lower() if isinstance(key, bool) else key][0]

def value_to_json(value):

    """Converts the key of the json into what is expected in the json format - i.e. ..."""

    return [
                (
                    f'"{value}"'
                    if isinstance(value, str)
                    else (
                        str(value).lower()
                        if isinstance(value, bool)
                        else value
                    )
                )
            ][0]


def json_dict(key, value, counter, length, json_string):

    """Contains the string logic for converting a dictionary object into json format"""

    if json_string == "" and length == 1:
        json_string += f'\u007b"{key}": {json_dumps(value)}\u007d'
    elif length == counter:
        json_string += f'"{key}": {json_dumps(value)}\u007d'
    elif counter == 1:
        json_string += f'\u007b"{key}": {json_dumps(value)}, '
    else:
        json_string += f'"{key}": {json_dumps(value)}, '

    return json_string


def json_list(key, value, json_string):

    """Contains the string logic for converting a list or tuple object into json format"""

    new_list = []
    sub_list_string = ""

    for item in value:

        if isinstance(item, dict):

            sub_list_string += json_dumps(item)
        
        else:
            
            new_item = value_to_json(item)
            new_list.append(new_item)

    if sub_list_string == "":
        sub_list_string = ", ".join(map(str, new_list))
    elif len(new_list) > 0:
        sub_list_string += f', {", ".join(map(str, new_list))}'

    json_string += f'\u007b"{key}": [{sub_list_string}]\u007d'

    return json_string

def json_element(key, value, counter, length, json_string):
    
    """Contains the string logic for converting all other elements (str, int, bool) into json format"""

    if length == 1:
        json_string += f'\u007b"{key}": {value}\u007d'
    elif json_string == "" and length > 1:
        json_string += f'\u007b"{key}": {value}, '
    elif counter == length:
        json_string += f'"{key}": {value}\u007d'
    else:
        json_string += f'"{key}": {value}, '

    return json_string