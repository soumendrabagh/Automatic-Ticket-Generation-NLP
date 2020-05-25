# Data Preprocessing Util


def removeString(data, regex):
    return data.str.lower().str.replace(regex.lower(), ' ')


def getRegexList():
    """
     Adding regex list as per the given data set to flush off the unnecessary text
    :return:
    """
    regex_list = []
    regex_list += ['From:(.*)\r\n']  # from line
    regex_list += ['Sent:(.*)\r\n']  # sent to line
    regex_list += ['received from:(.*)\r\n']  # received data line
    regex_list += ['received']  # received data line
    regex_list += ['To:(.*)\r\n']  # to line
    regex_list += ['CC:(.*)\r\n']  # cc line
    regex_list += ['https?:[^\]\n\r]+']  # https & http
    regex_list += ['[\w\d\-\_\.]+@[\w\d\-\_\.]+']  # emails are not required
    regex_list += ['[0-9][\-0–90-9 ]+']  # phones are not required
    regex_list += ['[0-9]']  # numbers not needed
    regex_list += ['[^a-zA-z 0-9]+']  # anything that is not a letter
    regex_list += ['[\r\n]']  # \r\n
    regex_list += [' [a-zA-Z] ']  # single letters makes no sense
    regex_list += [' [a-zA-Z][a-zA-Z] ']  # two-letter words makes no sense
    regex_list += ["  "]  # double spaces

    regex_list += ['^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$']
    regex_list += ['[\w\d\-\_\.]+ @ [\w\d\-\_\.]+']
    regex_list += ['Subject:']
    regex_list += ['[^a-zA-Z]']

    return regex_list


def cleanDataset(dataset, column, regex_list):
    for regex in regex_list:
        dataset[column] = removeString(dataset[column], regex)
    return dataset
