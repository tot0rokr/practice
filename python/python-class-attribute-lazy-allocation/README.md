Child 클래스가 정의되기 전에 Child class attribute를 사용하는 Parent class의 staic method를 호출하는
경우, __init_subclass__를 사용하면 해결할 수 있다.

다음과 같은 디자인을 하기 위해 많은 노력을 기울였다. ChatGPT도 해결해주지 못하던 디자인을 드디어
Copilot의 도움을 받아 해결했다. 프롬프트는 다음과 같다.

```
Base class에서 handler라는 list인 class field를 사용하는 데코레이터 함수가 있고, BaseClass를 상속받는
ConcreteClass마다 handler를 재정의(override)하는데, ConcreteClass에서 메소드에 BaseClass의
데코레이터를 사용하면 handler에 해당 메소드를 추가하고싶어. 그런데 ConcreteClass가 여러개인 경우
클래스마다 각각 handler가 독립적이어서 본인의 메서드만 포함하고 싶어. 이럴 때 어떻게 설계할 수
있을까?
```
