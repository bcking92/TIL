# Git

- Git은 코드를 관리하는 시스템으로 고안되었지만 여러 기능으로 사용됩니다.
  - SCM(Source Code Manager)
  - VCS(Version Control System)
  - 원격저장소, Remote Repository
    - Github, Gitlab, Bitbucket 등
  - 협업도구
    - Git은 브랜치와 머지를 이용해 강력한 협업 툴로서 기능을 합니다.
    - 협업의 방식에는 크게 3가지가 있지만 주로 Branch and PR 방법을 사용합니다.
      - Push and Pull
        -  협업자들이 차례로 Push와 Pull을 진행하는 방법. 동시에 작업하는 것이 아님.
      - Fork and PR(Pull Request)
        - 관리자의 Repository를 Fork 해와서 수정 후 pull request를 보내는 방식
      - Branch and PR(Pull Request)
        - 하나의 Repository에서 Branch를 따로 까서 pull request를 보내는 방식

<br>

## How to use git & git hub

- ###	[깃 기초](01_Introduction.md)



개발협력을 할땐 대장을 정해야댐



Leader가 관리를함 

프로젝트 생성은 항상 Leader

공동의 마크다운 문서 

README라는 마크다운 생성



git status 에 빨간파일이 있으면 pull 안댐



git 협업이 비효율적으로 보이지만 변화를 트래킹하기에 아주 유리함(코드가 길어지면 깃이 걍 최고)



깃협업의 원칙

1.(아주 높은 수준의 팀웍이 아니고서는) 협업할때 같은 파일을 건드리지말자!!!(특히 동시간대에 동일파일 건드리면 최악)

2.소통을 많이하자



conflict = change 2개가 충돌하는 상황 : 정리해주어야 한다.

협업시나리오 (동시에 작업하지만 않으면된다 = 리더는 일을 분배시켜야됨)ㅐㅔ

1. 시간을 분리하거나
2. 파일을 분리하거나