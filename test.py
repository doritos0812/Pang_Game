relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import chain, combinations


# 전체의 부분 집합 구하는 함수 combination을 사용한다.
def get_all_subset(iterable):
    s = list(iterable)

    # 결과는 tuple로 나오므로 이를 전체 연결하기 위한 itertools.chain()으로 연결한다.
    d = chain.from_iterable(combinations(iterable,r) for r in range(len(iterable) + 1))
    return d

def solution(relation):
    answer_list = []
    subset_list = get_all_subset(list(range(0, len(relation[0]))))
    unique_list = []

    # 유일성을 만족하는 부분집합 구하기


    for subset in subset_list:
        unique = True
        row_set = set() # 중복을 허용하지 않는 집합
        for row in range(len(relation)):
            data = ''
            for column in subset:
                data += relation[row][column] + '.'

            # row_set에서 중복이 되는 원소가 있는 지 검사합니다.
            if data in row_set: # 중복이 된다면 유일성을 만족하지 않습니다.
                unique = False
                break
            row_set.add(data)

        #print(row_set)
        if unique: # 유일성을 만족한다면 추가합니다.
            unique_list.append(subset)

    # 유일성을 만족하는 column을 정렬합니다.
    unique_list = sorted(unique_list, key = lambda x:len(x))
    #print(unique_list)

    # 최소성을 만족하지 검사합니다.
    for subset in unique_list:
        subset = set(subset)
        check = True
        # 부분 집합인지 검사합니다.
        for j in answer_list:
            if j.issubset(subset): # set(A).issubset(B) # A가 B의 부분 집합인지 검사
                check = False
        if check == True:
            answer_list.append(subset)

    # 최종적으로 유일성과 최소성을 만족하는 column의 개수를 반환
    return len(answer_list)

print(solution(relation))