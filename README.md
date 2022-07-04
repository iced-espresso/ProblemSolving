# ProgrammersCodeTest
code of programmers code test (https://programmers.co.kr/learn/challenges)

# 파이썬 정리
- defaultdict에서 lambda까지 사용하면 코드를 더 간략화할 수는 있으나, defaultdict은 보통 dict보다 조금 느리다. (60060 가사검색 문제에서 비교해보니 차이가 조금 남) 
  - 차라리 setdefault를 사용하는것이 좋아보임
    - setdefault를 사용할 시 lambda 사용이 안됨
- reverse할 때 slicing보다 reversed 사용하는게 조금더 좋다고는함.