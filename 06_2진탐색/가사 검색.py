from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# bisect 모듈을 사용하면, 정렬된 배열에서 특정 데이터의 갯수를 간단히 계산 가능
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

def solution(words, queries):
    # 단어를 새롭게 저장하기 위한 2차원 리스트로 생성
    # 각 행은 단어의 길이를 의미
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    result = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) # 슬라이싱을 사용하여 단어를 뒤집어 저장
    
    # 단어 배열 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for query in queries:
        if query[-1] == '?': # 와일드카드가 접미사로 붙는 경우
            cnt = count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else: # 와일드카드가 접두사로 붙는 경우
            cnt = count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        result.append(cnt)
    
    return result