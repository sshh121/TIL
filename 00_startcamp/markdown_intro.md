# 마크다운 기본

> `>` 파이프라인으로 '인용문이나 부연설명 등을 작성할 때 사용'
>
> `#` 하나는 대제목 heading 1이라는 의미

## heading 2

### heading 3

#### heading 4

##### heading 5

###### heading 6

---

> `---` 은 구분선

## 리스트

### 순서가 있는 리스트

1. 리스트 만들어진다.
2. 엔터치면 자동으로 다음 숫자 만들어진다.
   1. 탭`tab`  누르면 그 세부사항도 만들 수 있다. 
3. `shift+tab`은 다시 밖으로 나갈 수 있다.
4. 완전히 나가고자 한다면 가장 밖에 있는 리스트에서 한 번 더 들여쓰기



### 순서가 없는 리스트

- `-`
- 얘도 순서가 있는 리스트와 같다.
  - 들여쓰기 된다.
    1. 순서가 없는 리스트와 순서가 있는 리스트 섞어서 쓸 수도 있다. 

---

## 코드와 관련된 기능

### code block

>  `색 넣어주는 기능 아님` <- 코드 블럭 생성 (백틱 ``이용)
>
> 문장을 쓰던 도중에 print() 라는 코드를 써야 한다면, 코드의 가독성을 늘리기 위해 사용한다.
>
> 문장을 쓰던 도중에 `print()` 라는 코드를 써야 한다면, 코드의 가독성을 늘리기 위해 사용한다.



### code snippet

> 백틱 ` 3개를 한 번에
>
> 그 뒤에 쓰고자 하는 언어(python,....)

```python
print('hello')
```

---

### 텍스트 관리

**중요한 내용** -> `ctrl+b` bold체로 변경 가능

**숫자 8 특수문자 2개 사이** `** **`

~~취소선~~ -> `~~` 물결 2개 사이



### 링크

> `[링크 이름](링크url)`

[노출될 링크 이름](https://www.naver.com/) -> 절대경로

[노출될 링크 이름](www.naver.com/) -> 상대경로



### 이미지

>  주의점 : 반드시 .md파일을 내가 관리하고자 하는 곳에 **먼저 저장**
>
>  먼저 저장안하면 절대경로(C드라이브)에 저장됨, 저장한 후에는 상대경로 설정되고 폴더 생성
>
>  => github에 올릴 때 폴더 + markdown 같이 올리기



+) `ctrl+t` : 표 삽입, `ctrl+1, 2, 3...` : 헤딩 번호 변경 가능

`ctrl+/` : 코드 원본 볼 수 있음








