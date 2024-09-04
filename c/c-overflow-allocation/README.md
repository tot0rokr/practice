# C overflow allocation for structure

`struct` 내부의 배열 필드를 가변적으로 할당받기 위한 테크닉.
C언어는 배열의 index 체크를 하지 않고, struct의 크기를 고려하지 않고, 포인터를 통해 무제한 접근이
가능한 점을 이용한다.
