def get_val(collection, key, default='git'):
    """

    :param collection: словарь
    :param key: ключ словаря collection значение которого надо вернуть
    :param default: значение, которое возвращается если ключ отсутствует или пустой словарь
    :return: значения словаря по ключу
    """
    if key not in collection.keys():
        return default
    if collection == {}:
        return default
    return collection[key]
