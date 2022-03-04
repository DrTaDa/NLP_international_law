import json

country_list = json.load(open("countries.json", "r"))

countries_plurinames = {}  

for country in country_list:
    if "en_short_name" in country:
        countries_plurinames[country["en_short_name"]] = [country["en_short_name"].split(' ')]
        for key in ["en_short_name1", "en_short_name2"]:
            if key in country:
                countries_plurinames[country["en_short_name"]].append(country[key].split(' '))


def find_sequence_in_tokens(sequence, tokens):

    if isinstance(sequence, str):
        sequence_formatted = [sequence.lower()]
    else:
        sequence_formatted = [w.lower() for w in sequence]

    indexes_start = []

    for index in range(len(tokens) - len(sequence_formatted) + 1):
        if tokens[index:index + len(sequence_formatted)] == sequence_formatted:
            indexes_start.append(index)

    return indexes_start


def find_countries_in_tokens(tokens, offset_indexes=0, search_bracket=False):

    countries = []
    countries_index = []

    for country in countries_plurinames:

        idxs = []
        for name in countries_plurinames[country]:

            if search_bracket:
                mod_name = name + [')']
                idxs += find_sequence_in_tokens(mod_name, tokens)
                mod_name[-1] = name[-1] + ')'
                idxs += find_sequence_in_tokens(mod_name, tokens)
            else:
                idxs += find_sequence_in_tokens(name, tokens)

        if idxs:
            countries.append(country)
            countries_index.append([idx + offset_indexes for idx in idxs])

    # Clean congo, Korea, guinea
    to_remove = []
    for i, (c1, idxs1) in enumerate(zip(countries, countries_index)):
        
        if c1 not in ["Republic Congo", "Republic Korea", "Guinea"]:
            continue

        for j, (c2, idxs2) in enumerate(zip(countries, countries_index)):

            if c1 == "Republic Congo" and "Democratic Republic Congo" == c2:
                for idx1 in idxs1:
                    for idx2 in idxs2:
                        if idx1 - 1 == idx2:
                            to_remove.append([i, idx1])

            elif c1 == "Republic Korea" and c2 == "Democratic People Republic Korea":
                for idx1 in idxs1:
                    for idx2 in idxs2:
                        if idx1 - 2 == idx2:
                            to_remove.append([i, idx1])

            elif c1 == "Guinea" and c2 == "Guinea-Bissau":
                for idx1 in idxs1:
                    for idx2 in idxs2:
                        if idx1 == idx2:
                            to_remove.append([i, idx1])

            elif c1 == "Guinea" and c2 == "Papua New Guinea":
                for idx1 in idxs1:
                    for idx2 in idxs2:
                        if idx1 - 2 == idx2:
                            to_remove.append([i, idx1])

            elif c1 == "Guinea" and c2 == "Equatorial Guinea":
                for idx1 in idxs1:
                    for idx2 in idxs2:
                        if idx1 - 1 == idx2:
                            to_remove.append([i, idx1])
    
    idxs_len0 = []
    for idxs in to_remove:
        countries_index[idxs[0]].remove(idxs[1])
        if len(countries_index[idxs[0]]) == 0:
            idxs_len0.append(idxs[0])
    
    countries = [c for i, c in enumerate(countries) if i not in idxs_len0]
    countries_index = [c for i, c in enumerate(countries_index) if i not in idxs_len0]

    return countries, countries_index


def find_keyword_in_tokens(tokens, keyword):
    
    if "-" in keyword:
        idxs_keyword = find_sequence_in_tokens(keyword.replace("-", ""), tokens) + \
                       find_sequence_in_tokens(keyword.split("-"), tokens)
    else:
        idxs_keyword = find_sequence_in_tokens(keyword, tokens)

    return idxs_keyword
