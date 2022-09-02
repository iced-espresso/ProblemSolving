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

- ### Singleton 
  - 싱글톤 패턴이란 "최초 한번만 메모리를 할당하고(Static) 그 메모리에 객체를 만들어 사용하는 디자인 패턴"이다.
    - 일반적으로 getInstance() 라는 메소드를 통해 Singleton 클래스를 가져와 사용한다.
  - 간단한 형태의 Singleton 구현은 아래와 같다. 
    - ```java
      class Singleton {
          private static Singleton instance = new Singleton();
      
          //생성자가 private이므로 외부에서 호출 new로 생성 못함.
          private Singleton() {}
      
          public static Singleton getInstance() {
              return instance;
          }
      }
      ```
  - 위와 같이 구현하였을 때, 클래스의 로딩 시점에 static 인스턴스가 생성되므로 아래와 같이 lazy init을 할수 있다.
    - ```java
      class Singleton {
          private static Singleton instance;
      
          private Singleton() {}
      
          public static Singleton getInstance() {
              if(instance == null){
                  instance = new Singleton();
              }
              return instance;
          }
      }
      ```
    - 하지만 위와 같은 방식도 문제가 있는데, 바로 멀티 쓰레드 환경에서 instance가 여러개 생길 수 있다는 것이다.
    - Thread-safe를 고려하기위해 synchrosized를 사용하여도 되지만 이러면 성능이 저하된다.
  - Lazy Init & Thread-safe한 좋은 방법으로 아래와 같이 Holder를 사용하는 방식이 있다.
    - ```java
      class Singleton {
          private Singleton() {}
      
          public static Singleton getInstance() {
              return InstanceHolder.instance
          }
      
          private static class InstanceHolder{
              private static final Singleton instance = new Singleton();
          }
      }
      ```
  - 추가적으로 effective java에 나와 있는 enum을 통한 Singleton 구현 방법도 있다. 
    - ```java
      enum Singleton {
          INSTANCE;
      
          private Singleton() {
          }
          public static Singleton getInstance() {
              return Singleton.INSTANCE;
          }
      }
      ```
    - 해당 방식으로 구현하게 될 시 Serialization 문제와 Reflection 문제를 간단히 해결 할 수 있다.
    - enum을 사용할 시 클래스로딩 시점에 만들어지니 lazy init은 아니지만, 사실상 해당 enum을 클래스로딩만 하고 구체적인 타입을 쓰지 않는 경우는 거의 없으므로 이 점은 크게 고민하지 않아도 된다고 한다.
  - 좋은글
    - https://velog.io/@skyepodium/%ED%81%B4%EB%9E%98%EC%8A%A4%EB%8A%94-%EC%96%B8%EC%A0%9C-%EB%A1%9C%EB%94%A9%EB%90%98%EA%B3%A0-%EC%B4%88%EA%B8%B0%ED%99%94%EB%90%98%EB%8A%94%EA%B0%80

- ### class loading 관점에서 static 멤버 접근 vs static final 멤버 접근, 
  - ```java
     public class Main {
         public static void main(String[] args) {
             System.out.println(ClassA.staticMember);
             System.out.println(ClassB.staticFinalMember);
             System.out.println(ClassB.staticFinalClassC);
         }
     }
      
     class ClassA {
         static {
             System.out.println("ClassA Loading");
         }
      
         public static String staticMember = "ClassA static member";
     }
      
     class ClassB {
         static {
             System.out.println("ClassB Loading");
         }
      
         public static final String staticFinalMember = "ClassB static final member";
         public static final ClassC staticFinalClassC = new ClassC();
     }
      
     class ClassC {
         static {
             System.out.println("ClassC Loading");
         }
     }
     ```
  - 위와 같은 코드가 있다 하면 실행 결과는 다음과 같다.
    - ![image](image_실행결과.png)
    - static final primitive type 멤버에 대한 접근으로는 class loading이 되지 않는다.
    - static primitive type 멤버에 대한 접근으로는 class loading이 된다.
    - static final reference type 멤버에 대한 접근으로는 class loading이 된다. (ClassA, ClassC 모두 Loading됨)

  

## Spring

- ### JPA Entity는 non-private 기본생성자가 필요하다.

  - JPA의 Entity는 반드시 기본 생성자(NoArgsConstructor)를 지녀야 한다.
    - 이유 : JPA는 DB 값을 객체 필드에 주입할 때 기본 생성자로 객체를 생성한 후 Reflection API를 사용하기 때문이다.
    
  - Entity의 기본 생성자는 public, protected 이어야하고 private 으로 선언해서는 안된다.
    - 이유 : 이는 JPA의 지연로딩과 관련이 있다.
      - JPA의 지연로딩(Lazy Loading)이란? &rarr;  https://velog.io/@nyong_i/JPA-%EC%A7%80%EC%97%B0%EB%A1%9C%EB%94%A9LAZY-LOADING
      
    - 지연로딩으로 인해 Proxy 객체를 사용하게 되는 경우, 원본 Entity를 상속하게 된다.
    
    - 그 후 실제로 사용되는 시점에 Entity 정보를 조회하여 Proxy Entity가 원본 Entity를 참조하도록 한다. 
    
    - private 기본생성자를 사용하게 된다면 상속이 불가능해지기에 protected나 public 생성자를 사용해야한다.
    
      

- ### @Bean과 @Component 의 차이

  - @Bean의 경우 개발자가 컨트롤 불가능한 **외부 라이브러리**들을 Bean으로 등록시키고 싶을 때 사용한다.

  -  @Bean의 경우 주로 @Configuration이 붙은 클래스 내의 메소드에 사용된다.

  -  @Component의 경우 **개발자가 컨트롤 가능한 Class**에 붙여 사용한다.

  -  @Component는 @Service, @Controller, @Repository에 포함되어 있다.

    

- ### Servlet 동작과정

  1. client가 HTTP Request를 Servlet Container에 보낸다.

  2. Servlet Container는 HttpServletRequest, HttpServletResponse 두 객체를 생성한다.

  3. Client의 HTTP 요청을 분석하여 어느 Servlet에 대한 요청인지 찾는다.

  4. 해당하는 Servlet의 service() 메소드를 호출 및 doGet() doPost() 등을 호출
     - 2에서 생성된 HttpServletRequest, HttpServletResponse가 인자로 전달됨.
     - 이 과정에서 해당 Servlet이 없다면 생성하고 init()을 먼저 호출한다.

  5. doGet()/doPost() 에서 생성된 동적 웹 페이지 결과물이 HttpServletResponse 객체에 담긴다.

  6. Servlet Container는 HttpServletResponse 객체를 HTTP 형태로 바꾸어 응답한다.

  7. 이 후 HttpServletRequest, HttpServletResponse 객체의 메모리를 소멸 시킨다.

     

- ### DispatcherServlet

  - ![image-20220831051914472](D:\git_repos\ProblemSolving\DispatcherServlet.png)

  - DispatcherServlet이란 HTTP 프로토콜을 통해 들어오는 모든 요청을 가장 먼저 받아 중앙집중식으로 처리하는 프론트 컨트롤러이다.

  - DispatcherServlet의 동작과정은 다음과 같다.

    1. Client의 HTTP요청을 DispatcherServlet이 받는다.

    2. HandlerMapping을 통해 HTTP 요청에 해당하는 Controller를 찾는다.

       - HandlerMapping의 구현체 중 RequestMappingHandlerMapping은 @Controller로 작성된 모든 컨트롤러 Bean을 파싱하여 HashMap으로 관리한다.

    3. 해당하는 Controller에 요청을 위임할 핸들러 어댑터를 찾아 전달한다.

       - 어댑터를 사용하는 이유는 Controller의 구현 방식이 다양하기 때문이다.
       - 즉 어댑터 패턴을 적용하므로써 Controller의 구현 방식에 상관없이 요청을 위임할 수 있다.

    4. HandlerAdapter가 Controller로 요청을 위임한다.

    5. Controller를 통해 비즈니스 로직이 처리된다.

    6. Controller가 요청을 처리한 뒤 반환한다.

    7. HandlerAdapter가 반환값을 처리한다.

       1. 만약 Controller가 View 이름을 반환하면 ViewResolver를 통해 렌더링 후 View를 반환하게 된다.
       2. 만약 객체를 반환하였다면(@RestController) ViewResolver 대신 HttpMessageConverter가 동작해서 객체를 JSON으로 Serialize하여 반환한다. 


- ### Session 방식 vs. Token(JWT) 방식

  - HTTP는 stateless 프로토콜이다. 따라서 이전에 누가 요청을 했는지, 인증된 client인 지 알 수가 없다.

  - 이를 해결하는 방법으로 세션 방식과 jwt token 방식이 있는데 그 차이점을 알아보자.

  - ##### 세션 방식

    - #### ![image-20220831030656766](C:\Users\csu20\AppData\Roaming\Typora\typora-user-images\image-20220831030656766.png) 

    - 세션 방식은 Server측에 Client의 접속 상태를 저장하는 방식이다.

      1. 웹 서버 or 별도의 세션 스토리지에 세션을 저장해놓고, 클라이언트에게 해당 Session Id를 반환해준다.
      2. 이 후 client 측에서는 해당 Session Id를 쿠키에 저장해두고 다음 요청시에 해당 값을 같이 보낸다.
      3. 서버 측에서는 해당 Session Id를 통해 Client의  검증할 수 있다.

    - 장점

      1. 구현이 상당히 명확하고 실제 서버에서 로그인 상태 확인이 굉장히 유용하다.
      2. client측의 쿠키가 설사 노출되더라도 session id는 유의미한 값을 갖고 있지 않아 보안성이 강하다.

    - 단점

      1. 서버에서 추가적인 세션 저장공간이 필요하다.
      2. 서버의 확장성이 떨어진다. (Scale-out이 힘들다.)

  - ##### 토큰(JWT) 방식

    - ![image-20220831032016940](C:\Users\csu20\AppData\Roaming\Typora\typora-user-images\image-20220831032016940.png)
    - 토큰은 사용자 인증을 위한 정보를 서명한 것이며, JWT(JSON Web Token) 은 현재 토큰 인증에서 가장 많이 사용되는 표준이다.
      1. 사용자가 로그인하면 서버측에서 secret key를 이용하여 acess token을 발급한다.
      2. Client 측은 해당 acess token을 로컬 스토리지/쿠키 등에 저장하고, 이후 HTTP 요청 시 같이 보낸다.
      3. 서버는 JWT Signature를 검증하고, Payload로부터 사용자 정보를 확인하고 서비스를 처리한다.
    - 장점
      1. 세션처럼 서버 측에서 정보를 저장하고 있지 않고, 단순히 전달받은 토큰의 데이터와 서명을 검증하는 것으로 인증이 가능하다. 즉 메모리가 따로 들지 않는다.
      2. Scale out이 용이하다.
      3. 멀티플랫폼/멀티서비스에서 사용하기 용이하다.
      4. 트래픽에 대한 부담이 낮다.
    - 단점
      1. 토큰에는 사용자 정보가 담겨 있으므로 jwt 토큰이 노출될 시 중요한 정보가 노출된다.
      2. 일반적으로 토큰에는 데이터가 담겨있으므로 단순 Session Id만 담겨있는 것보다 사이즈가 크다.

  - 이미지 출처 : https://blog.lgcns.com/2687

  - JWT는 공개 키 암호 방식을 사용한다. 자세히 알고 싶다면 아래 링크 참조

    - https://meetup.toast.com/posts/239


- ### @Controller vs. @RestController

  - TBD

## 네트워크       

- ### OSI 7계층 간단 정리

  1. Physical Layer : 디지털 데이터 <-> 아날로그 신호로 변환 해주는 모듈
  2. Data-link Layer: **같은 네트워크** 상에 있는 **컴퓨터들**이 **데이터**를 주고 받을 수 있게 해주는 모듈. 
     - 이더넷 프로토콜이 사용된다.
     - framing
     - mac 주소 기반으로 동작한다.
     - 허브, L2 스위치가 해당계층에서 사용되는 장비다. 
  3. Network Layer(Internet Layer) : **서로 다른 네트워크**에 있는 **컴퓨터들**끼리 **통신**할 수 있게 해주는 모듈
     - IP 주소를 이용해서 최적의 길을 찾고(라우팅), 자신 다음의 라우터에게 데이터를 넘겨주는 것(포워딩)
     - 라우터가 라우팅 테이블 관리. 캐시도 사용
     - IP 주소 기반으로 동작한다.
     - ARP 프로토콜 : IP 주소를 MAC 주소로 변환시켜주는 프로토콜
  4. Transport Layer : **어플리케이션(프로세스)** 간 **신뢰**할 수 있는 데이터 통신이 가능하도록 하는 모듈
     - 포트 번호를 통해 컴퓨터 내 응용 프로세스를 구분가능케 한다.
     - 연결지향형 통신: 신뢰성/정확성이 우선인 통신이라서 여러 번 확인하고 보내는, 상대편과 확인해가며 통신하는 방식
     - 비연결형 통신 : 효율성을 우선으로 하여, 확인 절차 없이 데이터를 전달하는 통신방식
     - 연결지향형 통신 : TCP, 비연결형 통신: UDP
     - 3계층까지가 하드웨어 통신을 주로 다룬다면, 4계층부터는 소프트웨어 통신을 많이 다룬다.
  5. Session Layer : 데이터가 통신하기 위한 논리적인 연결을 해주는 모듈
     - 통신을 하기 위한 세션을 확립/유지/중단(운영체제가 해줌)
  6. Presentation Layer : 여러 다른 시스템들이 저마다 다른 데이터 표현 방식을 사용하는데, 이를 하나의 통일된 구문 형식으로 변환시키는 기능을 수행하는 모듈.
  7. Application Layer : 실 서비스(네트워크 어플리케이션)을 제공하기 위해  인터넷 상 컴퓨터들 간 다양한 데이터(메세지, 명령)를 주고 받게 해주는 모듈.
     - HTTP/FTP/SSH/Telnet 등의 프로토콜
     - 클라이언트 - 서버 모델, P2P 모델 2가지 모델이 존재
     - 클라이언트 - 서버 모델 : 클라이언트는 서버에게 서비스 요청. 서비스는 요청에 대한 처리와 응답. 웹 서비스 등. 주로 TCP 이용
     - P2P 모델 : 개인과 개인이 연결되어 통신되는 구조. 

## 디자인 패턴

- ### Strategy Pattern(전략 패턴)

  - 특정 행위(알고리즘이나 로직)을 다른 클래스로 위임하여, 동적으로 행위를 자유롭게 바꿀 수 있게 해주는 패턴
  - ![image-20220905010656836](C:\Users\csu20\AppData\Roaming\Typora\typora-user-images\image-20220905010656836.png)

- ### Observer Pattern

  - ![image-20220905010915149](C:\Users\csu20\AppData\Roaming\Typora\typora-user-images\image-20220905010915149.png)
  - 한 객체의 상태가 바뀌면 그 객체에 의존하는 다른 객체에게 연락이 가고 자동으로 내용이 갱신되는 방식으로 일대다 의존성을 정의하는 패턴.

## 60060_가사검색에서 Python vs C++

- c++로 동일로직 짜봤는데 10배~20배나 빠르다.
  - ![image](https://user-images.githubusercontent.com/54143203/177346026-be2725a1-c70d-4480-9e1d-53fccb2e5098.png) ![image](https://user-images.githubusercontent.com/54143203/177345095-95140268-92bd-4e91-bef5-9802609127cf.png)
  - 좌: 파이썬, 우: c++
