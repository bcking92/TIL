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

   - **Branch**는 



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

- `git config` 명령어는 현재 폴더에서 깃에 저장되어있는 정보들을 확인하거나 정보를 저장할 수 있습니다.

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
- **Push**하기 위해서는 원격저장소의 주소를 저장해주어야 합니다.

```shell
# remote repository(원격저장소) 추가하기
$ git remote add 저장소이름 저장소주소

ex). $ git remote add origin https://gitbub.com/abcd000/first_repository.git
```

- `git init` 과 `git remote add`를 이용하여 원격저장소와 연동할 수 도 있지만 **clone**을 이용하는 방법도 있습니다.

```shell
# Cloning
$ git clone 저장소위치 저장소이름
```

