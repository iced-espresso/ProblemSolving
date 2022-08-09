# ProgrammersCodeTest
code of programmers code test (https://programmers.co.kr/learn/challenges)





## 파이썬 정리

- defaultdict에서 lambda까지 사용하면 코드를 더 간략화할 수는 있으나, defaultdict은 보통 dict보다 조금 느리다. (60060 가사검색 문제에서 비교해보니 차이가 조금 남) 
  - dict이 더 빠르긴 하나 defaultdict이 가독성이 너무 좋다.
- reverse할 때 slicing보다 reversed 사용하는게 조금더 좋다고는함.
<br/> <br/> 

## 자바 정리
- ### 자바 collections
  
  - ![image](https://user-images.githubusercontent.com/54143203/178130283-bcae9837-288b-4d72-8024-4a19570e3328.png)


- #### Anoymous 객체
  
  - 이름이 없는 클래스.
  - 재사용 목적이 아닌 1번만 사용하려고 할때 사용함.
  - ex) UI 이벤트처리, 스레드 객체, comparator 등
  - 예시코드
    ```java
    import java.util.Comparator;
    
    public class AnonymousTest {
    
        public static void main(String args[]){
            Person person_age1 = new Person(1);
            Person person_age10 = new Person(10);
    
            Comparator<Person> ageComparator = new Comparator<Person>() {
                @Override
                public int compare(Person o1, Person o2) {
                    return o1.getAge() - o2.getAge();
                }
            };
    
            System.out.println(ageComparator.compare(person_age1, person_age10));
        }
    }
    
    class Person{
        private int age;
        Person(int age){
            this.age = age;
        }
        public int getAge(){
            return age;
        }
    }


- #### Java Sort에 관하여 
  
  1. **java에서 Arrays.sort()와 Collections.sort()의 내부 구현이 다르다**.
      
      - | Type                            | Method                                | 구현 Alogirhm      | 시간 복잡도                                             |
        | ------------------------------- | ------------------------------------- | ------------------ | ------------------------------------------------------- |
        | Primitive Array                 | Arrays.sort()                         | DualPivotQuicksort | Best:O(NlogN)<br />Average:O(NlogN)<br />Worst:O(N^2)   |
        | Object형 Array<br />Collections | Arrays.sort()<br />Collections.sort() | Timsort(stable)    | Best:O(NlogN)<br />Average:O(NlogN)<br />Worst:O(NlogN) |
      
      - 생각해보면 primitive형 정렬에는 stable 정렬이 의미가 없을테니 quick sort를 응용한 방식을 쓴 것 같고, Object에 대한 정렬에서는 stable 정렬이 필요하다 생각하여 TimSort를 사용한 것 같다.
      
      - 참고로 TimSort의 경우 merge sort and insertion sort의 hybrid버전이라고 한다.
  2) **Object에 대한 다양한 sort 방법**
     
     1) Comparator 이용
        1) Comparator Class 구현
        2) Anonymous 객체 이용
           - [Anoymous 객체](#anoymous-객체) 참조
        3) 람다식 이용
           - ```java
             Collections.sort(personList, (a,b)-> a.getAge() - b.getAge());
             ```
        
     2) Comparable implements 하여 compareTo 구현
        - 개인적으로는 제일 자주쓰고 편한방법
        - ```java
          class Person implements Comparable<Person>{

                private int age;
                private String name;

                Person(int age, String name){
                    this.age = age;
                    this.name = name;
                }

                public int getAge(){
                    return age;
                }

                public String getName(){
                    return name;
                }

                public String toString(){
                    return "(" + name + "," + Integer.toString(age) + ")";
                }
            
                @Override
                public int compareTo(Person target){
                    if(this.name.equals(target.name)){
                        return this.age - target.age;
                    }
                    else {
                        return this.name.compareTo(target.name);
                    }
                }
                
            }
            

## 60060_가사검색에서 Python vs C++
- c++로 동일로직 짜봤는데 10배~20배나 빠르다.
  - ![image](https://user-images.githubusercontent.com/54143203/177346026-be2725a1-c70d-4480-9e1d-53fccb2e5098.png) ![image](https://user-images.githubusercontent.com/54143203/177345095-95140268-92bd-4e91-bef5-9802609127cf.png)
  - 좌: 파이썬, 우: c++
