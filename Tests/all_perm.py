import json

arr1 = [
    ['1','2','3'],
    ["a","b", "c"],
    ["A","B"]
]

# def get_all(arr):
#     combinations = []

#     def combine(terms, accum):
#         last = (len(terms) == 1)
#         n = len(terms[0])
#         for i in range(n):
#             item = accum + terms[0][i]
#             if last:
#                 combinations.append(item)
#             else:
#                 combine(terms[1:], item)
#     combine(arr,"")
#     return combinations


template_map = {
    "el1": "$EL1$",
    "el2": "$EL2$",
    "el3": "$EL3$"
}


possible_values = {
    "el1": [1,2,3,4],
    "el2":["a", "b", "c"],
    "el3":["A", "B"],
    "demo":"A"
}

possible_values2 = {
    "el1": [1,2,3,4]
}


def get_all_dictionaries(template:dict, variations: dict):

    combinations = []

    
    def combine(variations, combined_dict):

        if len(variations.keys()) == 0:
            return


        if len(variations.keys()) == 1:
            key = next(iter(variations))
            for var in variations[key]:
                combined_dict_copy = combined_dict.copy()
                combined_dict_copy[key] = var
                combinations.append(combined_dict_copy)

        key = next(iter(variations))
        for var in variations[key]:
            combined_dict_copy = combined_dict.copy()
            combined_dict_copy[key] = var
            variations_copy = variations.copy()
            del variations_copy[key]
            combine(variations_copy, combined_dict_copy)


    combine(variations, template)

    return combinations



returned_dictionaries = get_all_dictionaries(template_map,possible_values)

# print(returned_dictionaries)

json_dict = json.dumps(returned_dictionaries, indent=4)

# print(json_dict)

dicttionary = {'dict1':
         {'part1':
              {'.wbxml': 'application/vnd.wap.wbxml',
               '.rl': 'application/resource-lists+xml'},
          'part2':
              {'.wsdl': 'application/wsdl+xml',
               '.rs': 'application/rls-services+xml',
               '.xop': 'application/xop+xml',
               '.svg': 'image/svg+xml'}},
     'dict2':
         {'part1':
              {'.dotx': 'application/vnd.openxmlformats-..',
               '.zaz': 'application/vnd.zzazz.deck+xml',
               '.xer': 'application/patch-ops-error+xml'}}}


def demo(dictionary, value):
    mime_type = value
    try:
        key_chain = find_mime_type(dictionary, mime_type)
    except KeyError:
        print ('Could not find this mime type: {0}'.format(mime_type))
        exit()
    print ('Found {0} mime type here: {1}'.format(mime_type, key_chain))
    nested = dictionary
    for key in key_chain:
        nested = nested[key]
    print ('Confirmation lookup: {0}'.format(nested))


def find_mime_type(d, mime_type):
    reverse_linked_q = list()
    reverse_linked_q.append((list(), d))
    while reverse_linked_q:
        this_key_chain, this_v = reverse_linked_q.pop()
        # finish search if found the mime type
        if this_v == mime_type:
            return this_key_chain
        # not found. keep searching
        # queue dicts for checking / ignore anything that's not a dict
        try:
            items = this_v.items()
        except AttributeError:
            continue  # this was not a nested dict. ignore it
        for k, v in items:
            reverse_linked_q.append((this_key_chain + [k], v))
    # if we haven't returned by this point, we've exhausted all the contents
    raise KeyError


if __name__ == '__main__':
    demo(possible_values,"A")

# def find(key, dictionary):
#     for k, v in dictionary.items():
#         if k == key:
#             yield v
#         elif isinstance(v, dict):
#             for result in find(key, v):
#                 yield result
#         elif isinstance(v, list):
#             for d in v:
#                 for result in find(key, d):
#                     yield result

# example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS'}
# example = {
#     "app_url": "",
#     "models": [
#         {
#             "perms": {
#                 "add": True,
#                 "change": True,
#                 "delete": True
#             },
#             "add_url": "/admin/cms/news/add/",
#             "admin_url": "/admin/cms/news/",
#             "name": ""
#         },
#         {
#             "perms": {
#                 "add": True,
#                 "change": True,
#                 "delete": True
#             },
#             "add_url": "/admin/cms/news/add/",
#             "admin_url": "/admin/cms/news/",
#             "name": ""
#         }
#     ],
#     "has_module_perms": True,
#     "name": "CMS"
# }
# print(json.dumps(example, indent=4))

# print(list(find('admin_url', example)))




# if __name__ == '__main__':
#     Main()