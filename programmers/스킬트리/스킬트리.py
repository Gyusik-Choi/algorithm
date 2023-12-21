def solution(skill, skill_trees):
    def is_possible_to_learn(skills):
        if len(skills) == 1:
            return True

        skill_degree = dict()
        skill_priorities = dict()

        for s in skill:
            skill_degree[s] = 0
            skill_priorities[s] = []

        for i in range(len(skill) - 1):
            for j in range(i + 1, len(skill)):
                skill_degree[skill[j]] += 1
                skill_priorities[skill[i]].append(skill[j])

        for s in skills:
            if s not in skill_priorities:
                continue

            if skill_degree[s]:
                return False

            for followed_skill in skill_priorities[s]:
                skill_degree[followed_skill] -= 1

        return True

    cnt = 0
    for tree in skill_trees:
        if is_possible_to_learn(tree):
            cnt += 1

    return cnt


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# 참고
# https://m.blog.naver.com/ndb796/221236874984
