# ProgrammersCodeTest
code of programmers code test (https://programmers.co.kr/learn/challenges)

## 파이썬 정리
- defaultdict에서 lambda까지 사용하면 코드를 더 간략화할 수는 있으나, defaultdict은 보통 dict보다 조금 느리다. (60060 가사검색 문제에서 비교해보니 차이가 조금 남) 
  - 차라리 setdefault를 사용하는것이 좋아보임
    - setdefault를 사용할 시 lambda 사용이 안됨
- reverse할 때 slicing보다 reversed 사용하는게 조금더 좋다고는함.
<br/> <br/> 

## 자바 정리
- 자바 자료구조
  - ![image](https://user-images.githubusercontent.com/54143203/178130283-bcae9837-288b-4d72-8024-4a19570e3328.png)

## 60060_가사검색에서 Python vs C++
- c++에서 nodeDict을 배열[26]으로 해싱 대체해서 해봤는데 c++이 속도가 10배이상 빠르다.
- 근데 파이썬에서 dict이 차지하는 오버헤드가 있는건지하고 dict -> 리스트[26] 해싱으로 바꾸어봤는데 오히려 더 느려짐(수행속도는 아래 사진 참조).
  - ![image](https://user-images.githubusercontent.com/54143203/177346026-be2725a1-c70d-4480-9e1d-53fccb2e5098.png) ![image](https://user-images.githubusercontent.com/54143203/177345934-4df1fdac-ae5f-4f44-bab4-fa0fff102154.png)
  - 좌: dict 사용, 우: 리스트 해싱 사용

- 반대로 c++에서 배열 해싱대신 map 사용했더니 오히려 더 빨라짐(근데 거의 미세함. 서버 오차라 봐야할듯. 수행속도는 아래 사진 참조)
  - ![image](https://user-images.githubusercontent.com/54143203/177345095-95140268-92bd-4e91-bef5-9802609127cf.png) ![image](https://user-images.githubusercontent.com/54143203/177345193-23083b5d-d782-4a83-a9cb-d351327ade43.png)
  - 좌: 배열 해싱, 우: map사용
