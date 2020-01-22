## Express with typescript

### Typescript

- typescript는 interpreted 언어가 아니고 compile 언어임 = compiler, compile option설정필요

### Express 시작하기

```shell
npm init
```

- dependencies

```shell
npm i express
```

- devDependencies

```shell
npm i -D typescript
```

```shell
# @types : 해당 모듈을 typescript로 변환해주는 모듈
# https://microsoft.github.io/TypeSearch/
# 여기서 변환 가능한 모듈인지 검색 가능
npm i -D @types/node @types/express
```

- tsconfig.json 파일 생성

```shell
npx tsc -init
```





- TSLint 적용

```shell
npm i -D tslint tslint-config-standard
```

