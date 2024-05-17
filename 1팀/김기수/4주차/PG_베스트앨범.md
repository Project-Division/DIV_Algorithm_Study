# 프로그래머스 - 베스트앨범

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3)

<br>

- ## 풀이
    - #### 파이썬 딕셔너리와 정렬만을 이용하여 해결할 수 있었음

<br>

- ## 코드
    ```python
    def solution(genres, plays):
        dic = {}
        
        for i in range(len(genres)):
            g = genres[i]
            p = plays[i]
            
            if g in dic:
                dic[g].append((i, p))
            else:
                dic[g] = [(i, p)]
            
        dic_sums = []
        for k in dic.keys():
            dic[k] = sorted(dic[k], key=lambda x: (-x[1], x[0]))
            dic_plays = [i[1] for i in dic[k]]
            dic_sums.append((sum(dic_plays), k))
        dic_sums = sorted(dic_sums, reverse=True)        
        # print(dic, dic_sums)
        
        answer = []
        for _, g in dic_sums:
            for i in range(0, min(2, len(dic[g]))):
                index, p = dic[g][i]
                answer.append(index)
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/ab01bb74-2e3c-47cc-8442-ac7d710e091a)
