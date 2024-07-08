def perm(k, num):  # 순열 조합
    if k == L:
        if is_valid(tmp):  # 올바른 문자열인지 확인
            print(''.join(tmp))
        return

    for i in range(num, C):
        if new_list[i] not in tmp[:k]:
            tmp[k] = new_list[i]
            perm(k + 1, i + 1)
            tmp[k] = 'A'


def is_valid(password): # 모음이 존재하는지 확인
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2  # 1개 이상의 모음 존재하는 단어 + 2개 이상의 자음


L, C = map(int, input().split())
char = list(map(str, input().split()))
new_list = sorted(char)
vowels = {'a', 'e', 'i', 'o', 'u'}  # 모음 모음집
tmp = ['A'] * L

perm(0, 0)
