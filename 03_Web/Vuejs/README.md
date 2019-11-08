# PJT 09

- 목표
  - Vue.js의 Component를 이용해 영화 정보 페이지 만들기
    - 각 component에 맞는 기능 구현하기
      - App.vue
        - 서버로부터 데이터를 받아온다.
      - MovieList.vue
        - 받아온 데이터를 리스트로 나열한다.
        - 장르를 선택했을 때 알맞은 데이터만 골라낸다.
      - MovieListItem.vue
        - 영화별로 표시할 내용을 div에 담는다.
      - MovieListItemModal
        - 영화별로 상세보기 버튼을 클릭 했을 때 modal을 띄운다.
    - 컴포넌트 계층구조를 이용하기

- 까다로웠던 점
  - node.js module 설치되있지 않아 run serve가 되지 않던 과정에서 원인 파악이 어려웠다.
    - npm install을 통해 package.json에 명시된 module을 설치 할 수 있다는 것을 배웠다.
  - 부모 컴포넌트에서 자식컴포넌트로 데이터를 넘겨주는 과정을 이해하기 어려웠다.
    - 부모는 component custom element에 바인딩 attribute 을 통해 데이터를 넘겨주고, 자식은 props를 통해 부모의 데이터를 받아 사용한다는 것을 확실히 인지했다.
  - 부모 컴포넌트로 부터 물려받은 데이터와 해당 컴포넌트에서 정의한 데이터 사이에 혼동이 있었다.
    - 처음에 부모 컴포넌트로 물려받을 데이터를 다시한번 data로 정의해야 되는 줄알았지만 별개로 작동한다는 것을 알았다.
  - axios.get을 통해 얻은 데이터가 바로 사용되지 않는 점이 이해하기 어려웠다.
    - axios.get 은 비동기 함수이기 때문에 axios.get이 완전히 처리되기 전에 데이터를 사용하려고 해서 의도와 다른 결과가 다른 것이었다는 것을 배웠다.
  - arrow function과 그냥 function의 this binding 방법이 이해가 가지 않았다.





#### 실행결과

