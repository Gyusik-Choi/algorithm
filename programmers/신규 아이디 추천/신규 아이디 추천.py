import re


def change_upper_to_lower(new_id):
    return new_id.lower()


def sub_all_except_allowed_string(new_id):
    # filtered_id = re.compile('[^a-z0-9\-\_\.]')
    # return filtered_id.sub('', new_id)
    # 위와 아래는 같은 기능
    return re.sub('[^a-z0-9\-\_\.]', '', new_id)


def sub_consecutive_period(new_id):
    # return re.sub('\.+', '.', new_id)
    # 위와 아래는 같은 기능
    return re.sub('\.{1,}', '.', new_id)


def sub_first_and_last(new_id):
    # new_id = re.sub('^[.]', '', new_id)
    # new_id = re.sub('[.]$', '', new_id)
    # 위와 아래는 같은 기능
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    return new_id


def sub_is_empty(new_id):
    if not len(new_id):
        return "a"
    return new_id


def sub_over_length(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        return re.sub('\.$', '', new_id)
    return new_id


def sub_short_length(new_id):
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]
        return sub_short_length(new_id)
    return new_id


def solution(new_id):
    new_id = change_upper_to_lower(new_id)
    new_id = sub_all_except_allowed_string(new_id)
    new_id = sub_consecutive_period(new_id)
    new_id = sub_first_and_last(new_id)
    new_id = sub_is_empty(new_id)
    new_id = sub_over_length(new_id)
    new_id = sub_short_length(new_id)
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))

# 참고
# https://codingspooning.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D%EC%9C%BC%EB%A1%9C-%ED%95%9C%EA%B8%80-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0-%EB%AC%B8%EC%9E%90%EC%97%B4-text-%EC%A0%84%EC%B2%98%EB%A6%AC
# https://jjuha-dev.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-resub%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%B9%98%ED%99%98%ED%95%98%EA%B8%B0
# https://whitewing4139.tistory.com/167
