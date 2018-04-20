def filterArrayByKey(array, key, value):
    return reverseArrayOrder(
        list(
            filter(
                lambda member: compare(member, key, value),
                array
            )
        )
    )


def compare(object, key, value):
    return object[key] == value


def kebabCase(name):
    return (
        name.lower()
        .replace('"', '')
        .replace('...', '')
        .replace('.', '')
        .replace('(', '')
        .replace(')', '')
        .replace('!', '')
        .replace('?', '')
        .replace(':', '')
        .replace(';','')
        .replace(',', '')
        .replace('  ', ' ')
        .strip()
        .replace(' ', '-')
    )


def reverseArrayOrder(array):
    return array[::-1]
