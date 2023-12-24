import re


def solution(files):
    def split_file(file):
        head = re.split('[0-9]', file.lower())[0]
        number = re.findall('[0-9]+', file)[0]
        tail = re.split('[0-9]', file)[1]
        return [head, number, tail, file]

    sorted_files = sorted(map(lambda f: split_file(f), files), key=lambda x: (x[0], int(x[1])))
    return list(map(lambda x: x[3], sorted_files))


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# 참고
# https://school.programmers.co.kr/learn/courses/30/lessons/17686/solution_groups?language=python3
# https://velog.io/@geonhwi/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-2
# https://velog.io/@seob/regex-is-easy
