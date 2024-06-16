# 관통형 프로젝트 (PJT)

## 프로젝트
반응형 웹 페이지 구현

## 목표
1. HTML을 통한 웹 페이지 마크업 이해
2. CSS 라이브러리 이해와 활용
3. Bootstrap 컴포넌트 및 Grid system을 활용한 반응형 레이아웃

## 사용한 개발도구
- Visual Studio Code
- Google Chrome
- Bootstrap
- HTML
- CSS3

## 제공사항
1. 파일: 01_nav.html 역할: 모든 페이지가 공유하는 Navigation Bar
2. 파일: 02_home.html 역할: 메인 영화 페이지
3. 파일: 03_community.html 역할: 커뮤니티 게시판 페이지
4. 파일: 04_footer.html 역할: 모든 페이지가 공유하는 Footer
5. 파일: images/ 역할: 이미지 파일 모음

## 요구사항
### 1. 공통  
- 커뮤니티 웹 서비스 개발을 위한 화면 구성 단계입니다.  
- CSS와 Bootstrap을 적절하게 사용합니다.  
- 명시된 요구사항 이외에는 자유롭게 작성 가능합니다.  
### 2. 01_nav.html  
- Bootstrap Navbar Component로 구성합니다.  
- 화면을 스크롤 하더라도 항상 화면 상단에 고정되어 있습니다.  
- 로고 이미지는 제공된 logo.png를 사용합니다.  
- 내비게이션 메뉴 중 Home, Community는 클릭시 각각 02_home.html, 03_community.html로 이동합니다.  
- 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 출력됩니다.  
- Modal Component 내부에는 HTML form 태그를 사용합니다.  
- 이어지는 결과 출력 예시를 참고하여 요구사항을 충족합니다.  
### 3. 03_home.html  
- 01_nav.html에서 작성한 코드를 적절한 위치에서 활용합니다.  
- 메인 페이지는 Header와 Section 두 부분으로 나뉩니다.  
- Header  
 Bootstrap Carousel Component로 구성합니다.  
 이미지는 최소 3장 이상 사용하며 자동으로 재생됩니다.
- Section  
  내부의 개별 요소들은 Bootstrap Card Component 로 구성합니다.  
  각 Card는 영화 포스터, 제목, 설명을 포함합니다.  
  Card의 높이는 모두 같으며 각 Card는 서로 좌우 일정한 간격을 가집니다.  
- 이어지는 결과 출력 예시를 참고하여 요구사항을 충족합니다.  
### 4. 03_community.html  
- 01_nav.html에서 작성한 코드를 적절한 위치에서 활용합니다.  
- 커뮤니티 페이지는 Aside, Section 그리고 Pagination 세 부분으로 나뉩니다.  
- Aside (게시판 카테고리): HTML aside 태그를 사용합니다, Bootstrap List Group Component로 구성합니다.
- Section (게시판): HTML section 태그를 사용합니다.   
- Aside와 Section은 Viewport width가 992px 미만일 경우와 이상일 경우
전혀 다른 레이아웃을 가집니다.  
- Viewport width 992px 미만  
- Aside와 Section의 width는 Bootstrap의 container 클래스를 사용한 부모 태그의 최대 width 값을 가집니다.  
- Section은 여러 HTML article 태그를 하위 태그로 가집니다.  
- Pagination은 Bootstrap Pagination Component로 구성하며 항상 수평 중앙 정렬 되어있습니다.  
- Viewport width 992px 이상  
- Aside의 width는 부모의 width를 12개로 나누었을 때 2개만큼 차지합니다.  
- Section의 width는 부모의 width를 12개로 나누었을 때 10개만큼 차지합니다.  
- 이때 Section은 Bootstrap Table Content로 구성합니다.  
### 5. 04_footer.html  
- 03_community.html에서 작성한 코드를 그대로 가져와 사용합니다.  
- HTML footer 태그를 사용합니다.  
- 화면을 스크롤 하더라도 항상 화면 하단에 고정되어 있습니다.  
- footer의 텍스트 콘텐츠는 footer 태그 내에서 항상 수직·수평 중앙 정렬되어 있습니다.  
- 작성 완료 후 02_home.html에도 그대로 적용합니다.

## 사용한 Bootstrap 기능  
1. [Breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/)
2. [Containers](https://getbootstrap.com/docs/5.0/layout/containers/)
3. [Grid system](https://getbootstrap.com/docs/5.0/layout/grid/)
4. [Columns](https://getbootstrap.com/docs/5.0/layout/columns/)
5. [Gutters](https://getbootstrap.com/docs/5.0/layout/gutters/)
6. [Images](https://getbootstrap.com/docs/5.0/content/images/)
7. [Tables](https://getbootstrap.com/docs/5.0/content/tables/)
8. [Forms](https://getbootstrap.com/docs/5.0/forms/overview/)
9. [Button group](https://getbootstrap.com/docs/5.0/components/button-group/)
10. [Cards](https://getbootstrap.com/docs/5.0/components/card/)
11. [Carousel](https://getbootstrap.com/docs/5.0/components/carousel/)
12. [List group](https://getbootstrap.com/docs/5.0/components/list-group/)
13. [Modal](https://getbootstrap.com/docs/5.0/components/modal/)
14. [Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
15. [Pagination](https://getbootstrap.com/docs/5.0/components/pagination/)

## 한줄 평
F12 개발자 툴을 애용하고 유용하게 사용하자.  
협업이란, Goat이며 소통이 매우 중요하다.  
조건에 맞게 전반적인 틀을 짜는 것은 쉽지만 아직 깔끔하게 다듬는게 어려운거 같으니 그 부분을 좀 더 보안하고 싶다.