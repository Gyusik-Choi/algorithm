def solution(data, ext, val_ext, sort_by):
    data_obj = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    filter_lst = list(filter(lambda x: x[data_obj[ext]] < val_ext, data))
    return sorted(filter_lst, key=lambda x: x[data_obj[sort_by]])


print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
