p = "(()())()"

def check(p, u, v):
    if p == '':
        return ''
    else:
        sum = 0
        for i in range(len(p)):
            if p[i] == '(':
                sum += 1
            elif p[i] == ')':
                sum -= 1
            if sum == 0:
                index = i
                break
        u += p[:index + 1]
        v += p[index + 1:]
        for i in u:
            if i == '(':
                sum += 1
            elif i == ')':
                sum -= 1
            if sum < 0:
                str = '(' + check(v, '', '') + ')'
                temp = ''
                for i in u:
                    if i == '(':
                        temp += ')'
                    else:
                        temp += '('
                str += temp[1:-1]
                return str
        str = u + check(v, '', '')
        return str

def solution(p):
    answer = check(p, '', '')
    return answer

print(solution(p))