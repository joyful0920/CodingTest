s = "aabbaccc"

def solution(s):
    # 각각 단위(1, 2, 3... len(s))로 자른 문자열 길이를 저장할 리스트
    results = []

    # 1부터 s의 길이까지 반복하면서
    for i in range(1, len(s) + 1):
        # 문자열 자르기
        sliced = [] # 자른 문자열 파트를 담을 리스트
        for j in range(0, len(s), i):
            sliced.append(s[j:j + i])
            # i == 1 -> s[0:1], s[1:2], s[2:3]... sliced = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']
            # i == 2 -> s[0:2], s[2:4], s[4:6]... sliced = ['aa', 'bb', 'ac', 'cc']
            

        # 자른 문자열들을 서로 비교하며 문자열 압축
        parts = [] # 중복된 문자열을 제거한 파트를 담을 리스트
        nums = [] # 반복되는 파트를 카운트한 숫자를 담을 리스트
        cnt = 1
        # 자른 문자열 파트를 앞뒤로 비교
        # sliced = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']
        for j in range(1, len(sliced)):
            if sliced[j] == sliced[j - 1]:
                cnt += 1
            else:
                parts.append(sliced[j - 1])
                if cnt == 1:
                    cnt = ''
                nums.append(str(cnt))
                cnt = 1
        
        # 앞선 반복문에서 누락된 마지막 문자열 파트에 대한 처리
        parts.append(sliced[-1])
        if cnt == 1:
            cnt = ''
        nums.append(str(cnt))

        # sliced = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']
        # parts = ['a', 'b', 'a', 'c']
        # nums = [2, 2, '', 2]

        # 문자열 압축 결과를 result 변수에 저장
        result = ''
        for j in range(len(nums)):
            result += (nums[j] + parts[j]) # 2a + 2b + a + 2c -> 2a2ba2c
        
        # results 리스트에 각각 단위로 잘라서 압축한 문자열의 길이를 저장
        results.append(len(result))

    return min(results)

print(solution(s))