def solution(files):
    def split_file(file):
        # head, number, tail, file
        new_file = ['', '', '', '']
        head = ''
        number = ''
        tail = ''

        last_digit_idx = 0

        for idx, char in enumerate(file):
            if char.isdigit():
                if not number:
                    last_digit_idx = idx - 1

                if idx - last_digit_idx <= 1:
                    number += char
                    last_digit_idx = idx
                else:
                    tail += char

                if not head:
                    head += ''.join(map(lambda x: x.lower(), ''.join(file[:idx])))
            else:
                if head:
                    tail += char

        new_file[0] = head
        new_file[1] = number
        new_file[2] = tail
        new_file[3] = file
        return new_file

    new_files = []

    for f in files:
        new_files.append(split_file(f))

    return list(map(lambda x: x[3], sorted(new_files, key=lambda x: (x[0], int(x[1])))))


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
