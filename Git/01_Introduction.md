

#	01_Git Introduction

## Terms(용어정리)

1.  **Status**

   - 어떤 file을 **Staging Area**에 올려 놓았을 때, 혹은 기존에 있던 파일이 제거 된 경우, 파일이 수정된 경우 등 git이 관리하는 폴더의 상태를 말합니다.

2.  **Staging Area**

   - **Staging Area**에는 `commit` 을 하기전 `git add`를 통해 staging 된 파일들이 임시로 올라가 있는 곳입니다.  `commit`을 할 때 **Staging Area**에 올라가 있는 파일들은 전부 `commit` 됩니다.

3. **Commit**
- **commit**은 디렉토리에 있는 모든파일(정확히는 **staging area**에 올라와 있는 모든파일)에 대한 스냅샷을 기록해놓은 것입니다. 
   
- **commit**은 폴더를 복사해 다른 공간에 저장하는 것과 기능상으로 유사하지만 훨씬더 유용한 기능입니다. 왜냐하면 `git commit`이 이루어질 때 git은 가능한 **commit**을 가볍게 유지하고자 하기 때문에 **commit**은 디렉토리의 모든 내용을 복사, 저장하는 것이 아니고 어떤 변화가 이루어 졌는지만 기록해 놓습니다. 그러므로 각 커밋에는 디렉토리의 이전 버전과 다음버전의 변경내역을 저장해 놓게 되고 이것은 폴더 전체를 복사해 놓는 것 보다 메모리를 훨씬 효율적으로 사용할 수 있습니다.(linked list 처럼 과거의 커밋과 미래의 커밋이 연결되어 있다.)
   - **commit**은 해시형태로 저장되고 SHA-1 해시를 사용합니다. commit 저장해놓는 폴더 구조도 효율적으로 짜여져 있어(내부는 아직 잘 모릅니다.) 굉장히 빠르게 작동합니다. 
   
4. **Head**

   - **Head**는 현재 작업하고 있는 **commit** 을 말한다.  **Head**는 기본적으로 가장 최신의 **commit**을 가르키고 있다.
   - **Head**를 옮겨 작업할 수 있는데 **Head**를 옮기는 행위를 **Checkout** 이라고 한다.

5. **Push**
- **Push**는 현재 커밋을 원격저장소로 업로드 하는 것을 뜻합니다. 
   
6. **Branch**

   - 



<br>

## Basic(기본 명령어)

#### 시작하기(``Git init`)

- 현재폴더를 깃으로 관리하기 위해서는 command line에서 `Git init` 명령어를 통해 시작을 알려야 합니다.

  ```shell
  # .을 찍는 이유는 현재 폴더를 관리하기 위해서 입니다.
  # 컴퓨터 사이언스에서 .은 대부분 현재위치를 나타냅니다.
  Git init .
  ```

  위의 명령을 실행하면 현재 폴더에 .git이라는 숨김폴더가 생성되고 깃에 대한 정보는 모두 그곳에 저장됩니다.

<br>

#### `Config`

- `git config` 명령어는 현재 폴더에서 깃에 저장되어있는 정보들을 확인하거나 정보를 저장, 수정, 삭제 할 수 있습니다.

```
# git 정보 확인
git config --list
```

```
# github 이메일과 이름 등록하기
$ git config --global user.email "abcd@gmail.com"
$ git config --global user.name "abcd000"
```

```shell
# 어떤 페이지의 정보를 지우고 싶을 때(github.com에 로그인 되어있는 정보를 다 삭제함)
$ git credential reject
$ protocol=https
$ host=github.com
```

<br>

#### `Remote Repository`

- github, gitlab 등 원격저장소에 **commit**을 **Push** 할 수 있습니다.

```shell
# 현재 연결되어 있는 저장소의 이름 확인
$ git remote
```

```shell
# 현재 연결되어 있는 저장소의 이름과 주소 확인
$ git remote -v
```

- 기본적으로는 연결되어있는 저장소의 이름이 없기 때문에 아무것도 나타나지 않습니다.
- **Push**하기 위해서는 원격저장소의 주소를 저장해주어야 합니다. 한 디렉토리에서 원격저장소를 여러개 지정할 수도 있습니다.

```shell
# remote repository(원격저장소) 추가하기
$ git remote add 저장소이름 저장소주소

ex). $ git remote add origin https://gitbub.com/abcd000/first_repository.git
```

- `git init` 과 `git remote add`를 이용하여 원격저장소와 연동할 수 도 있지만 **clone**을 이용하는 방법도 있습니다.

```shell
# Cloning
$ git clone 저장소위치 저장소이름

ex). $ git clone https://github.com/abcd000/first_repository.git new_name
```

- 위의 명령을 실행하면 현재 폴더에 new_name의 폴더를 만들고 그 안에 remote repository의 파일들을 모두 다운받고 깃으로 관리하기 시작합니다.

```shell
# remote repository(원격저장소) 제거하기
$ git remote remove 저장소이름
```



<br>

#### `Add & Commit`

```shell
# Staging area로 해당 파일을 올려놓기
$ git add file_name 

# Staging area로 현재 폴더의 모든 파일 올려놓기
$ git add .
```

- Staging area에 올라간 파일을 내리는 명령도 있습니다.

```shell
# Staging area에 올라가있는 파일 내리기
$ git restore --staged file_name

# Staging area에 올라가있는 모든 파일 내리기
$ git restore --staged .
```

- 위의 명령어에서 파일이 현재폴더에 없는 경우에는 경로를 반드시 작성해주어야 합니다.

```shell
# Staging area에 있는 파일들 commit하기
$ git commit

# message와 함께 commit하기
$ git commit -m "commit message"

# Staging area에 올라와있진 않지만 디렉토리의 변경내용을 자동으로 Staging area에 올려
# 커밋하기
$ git commit -a
```

- commit -m 을 이용하면 commit message를 작성할 수 있습니다. **되도록이면 commit은 메세지와 함께 해야하며 commit message는 대충 입력하지 말고 어떤 변경사항이 적용되었는지 잘 작성해야 합니다. 그래야만 협업에서, 또는 개인 프로젝트의 version control 측면에서 한눈에 알아 보기 쉽습니다.****

<br>

#### `Status & Log`

```shell
# 현재 상태확인(디렉토리의 변경사항)
$ git status
```

```shell
# 지난 commit들을 보여줌(작성자, commit 일시, 이메일, 커밋이름 등 모든정보를 표시)
$ git log

# 커밋의 이름과 해시값만 보고 싶다면
$ git log --oneline

# 브랜치가 어떤식으로 분화되었는지 그림으로 확인하기
$ git log --oneline --graph
```

- log 창에서 나오고 싶을 땐 q를 누르면 나올 수 있다.

<br>

#### `Push & Pull`

- Push와 Pull 은 remote repository(원격저장소)에 현재 폴더의 파일을 업로드하거나 원격저장소에 올라가 있는 파일들을 다운로드하는 것과 비슷합니다.

```shell
# remote repository에 commit을 업로드하기
$ git push -u 저장소이름 브랜치이름

# -u를 설정해 주었으면 그 뒤로는 git push만 해주어도 자동으로 저장소이름과 브랜치이름이 지정됨
$ git push
```

```shell
# remote 저장소의 파일 local로 다운로드하기
$ git pull
```

- 여기서 git pull과 git clone은 차이가 있습니다. 무엇이냐면,
  pull은 이미 git으로 관리되고 있고 원격저장소와 연결이 되어있는 폴더(즉, .git 폴더가 있으면서 `git remote -v`에 주소가 저장되어있는 폴더)에서 원격저장소로 부터 새로운 파일들을 받아올 때 쓰는 명령어이고,
  clone은 git으로 관리되는 폴더가 없는 상태에서 remote repository를 통째로 받아와 local에서 사용하는 개념입니다.

<br>

#### `Checkout`

- Checkout은 Head를 다른 커밋이나 다른 브랜치로 옮기는 것을 말합니다. Checkout은 git의 매우 강력한 version cotrol 기능입니다. Checkout 기능을 이용해 시간을 거스를 수도 있고 또다른 평행세계(브랜치)로 들어갈 수도 있습니다. 

```shell
# 특정 시점의 commit으로 이동
$ git checkout 'commit hash code의 앞 6자리'

# 특정 브랜치로 이동
$ git checkout branch_name

# n단계 이전의 commit으로 이동
$ git checkout HEAD~n
```

- 기본적으로 head는 master branch의 최상단을 가르키고 있습니다. 그러므로 만약에 특정 시점의 commit으로 이동했다가 다시 현재시점으로 복귀하고 싶다면 아래와 같이 마스터 브랜치로 checkout을 해주면 됩니다.

```shell
$ git checkout master
```

