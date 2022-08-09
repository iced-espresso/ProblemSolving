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


- ### Anoymous 객체
  
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


- ### Java Sort에 관하여 
  
  1. **java에서 Arrays.sort()와 Collections.sort()의 내부 구현이 다르다**.
      
      - | Type                            | Method                                | 구현 Alogirhm      | 시간 복잡도                                             |
        | ------------------------------- | ------------------------------------- | ------------------ | ------------------------------------------------------- |
        | Primitive Array                 | Arrays.sort()                         | DualPivotQuicksort | Best:O(NlogN)<br />Average:O(NlogN)<br />Worst:O(N^2)   |
        | 1. Object형 Array<br />2. Collections | Arrays.sort()<br />Collections.sort() | Timsort(stable)    | Best:O(NlogN)<br />Average:O(NlogN)<br />Worst:O(NlogN) |
      
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
        
     2) Comparable 이용
        - 개인적으로는 제일 자주쓰고 편한방법
        - Comparable implements 하여 compareTo 구현
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
            ```
- ### Java HashMap
  - java의 HashMap은 이름 그대로 hash code를 이용해 key:value 매핑을 해주는 자료구조이다.
  - 내부적으로 버킷(table) 배열을 가지고 있다.
  - Separate Chaining으로 해시충돌을 해결한다고 하며, 버킷 내에서는 RBT(Red BlacK Tree)를 사용하여 효율적으로 충돌을 관리한다.
    - 버킷의 Size가 8미만일 경우 그냥 Linear Chain으로 둔다고 한다. 8이상이 되면 RBT로 전환.
  - 일반적인 경우에선 HashMap 조회/삽입에 대한 시간복잡도는 O(1)로 봐도 되겠지만 Worst Case에서는 O(logN)이 될수도 있다. (많은 충돌이 있을경우) 
  - 또한 HashMap에서는 데이터의 개수가 내부 Threshold에 이를 때 마다 해시 버킷 사이즈를 2배씩 하는데(초기 default값은 16), 이 과정에서 오버헤드가 굉장히 클 수 있으므로 저장될 데이터의 개수가 어느정도 예측이 된다면 버킷 사이즈를 생성자로 미리 지정하는 것이 바람직하다.
    - 만약 데이터 개수를 예상할 수 없다면 항상 O(logN)을 보장하는 TreeMap을 사용하는 것이 오히려 좋은 performance를 보이는 case도 있을 수 있다.
  - HashMap은 데이터 삽입에 대한 순서가 보장되지 않으므로, 순서가 보장되어야 한다면 LinkedHashMap을 사용하고 정렬이 필요하다면 TreeMap을 사용하자.
- ### transient 키워드
  - 자바의 transient 키워드는 class의 필드 중 직렬화하지 않을 것들을 지정하기 위해 사용된다.
  - 즉, 객체가 바이트 스트림으로 serialize될 때 transient 키워드가 붙은 필드는 제외되고, deserialize 시에는 해당 필드의 타입별 기본 값이 할당된다고 한다. 
            

## 60060_가사검색에서 Python vs C++
- c++로 동일로직 짜봤는데 10배~20배나 빠르다.
  - ![image](https://user-images.githubusercontent.com/54143203/177346026-be2725a1-c70d-4480-9e1d-53fccb2e5098.png) ![image](https://user-images.githubusercontent.com/54143203/177345095-95140268-92bd-4e91-bef5-9802609127cf.png)
  - 좌: 파이썬, 우: c++
