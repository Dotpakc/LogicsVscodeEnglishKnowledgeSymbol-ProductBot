#paginator


def paginator(data_list, page=0, per_page=5):
    start = (page ) * per_page
    end = start + per_page
    print("paginator", start, end)
    print("paginator", data_list)# [ (key, value), (key, value)]
    return data_list[start:end]