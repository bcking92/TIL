#### sslforfree에서 무료 SSL 보안 인증서 발급받아 Nginx에 적용하기

1. [SSL for free](https://www.sslforfree.com/)에 들어가서 도메인의 주소를 입력하고 Create Free SSL Certificate버튼을 클릭한다.

2. 인증서를 서버에 직접 업로드해서 사용할 것이므로 Manual Verification(수동 인증)을 클릭한다.(DNS 말고)

3. 인증을하려면 80번 포트가 열려있어야 댄다. 뭐 이런 이야기가 나온다. Manually Verify Domain(수동으로 도메인 인증하기) 버튼을 누른다.

4. 버튼을 누르면 1번부터 7번항목 까지 순서가 나오는데 1번에서 verification file(인증 파일)을 다운로드 받는다.

5. 다운로드 받은 파일을 서버에 올리고 `http://host/.well-known/acme-challenge/인증파일` 주소로 접근 했을 때 인증파일에 접근할 수 있도록 만들어 주면 된다.

   우리는 Nginx를 사용하고 있으므로 서버 설정으로 들어가 위의 루트를 추가해 준다.

   ```
   server {
   ...
   	location /.well-known {
   		root 인증 파일이 저장된 경로
   	}
   ...
   }
   ```

   이렇게 추가해 주면 된다. 이 때 주의할 점은 파일 저장 경로를 시크릿 폴더로 만들면 안된다는 것. 이 것 때문에 자꾸 안되서 고생했다.

6. Nginx를 restart 해주고 위의 주소로 접근 했을 때 인증파일에 접근할 수 있는지 확인해 본다.

7. 접근이 잘 되면 Download SSL Certification 버튼을 눌러 인증서를 다운받는다.

8. 인증서는 압축파일로 되어있고 압축을 풀면 3개의 파일이 나온다.

   - ca_bundle.crt
   - certificate.crt
   - private.key

   IIS 사용자라면 인증서를 pfx파일로, Tomcat 사용자라면 인증서를 jks파일로 변환 해주어야 하지만 우리 서버는 Nginx이므로 그냥 사용해도 된다. 파일 3개 전부를 서버에 올려주고 적당한 폴더를 만들어 집어넣는다. (예시. /certs/)

9. 이제 Nginx 설정에서 인증서를 등록하면 끝이다.

   ```nginx
   server {
   	listen 80;
   	listen 443 ssl; # 443 포트를 열어준다
       
       server_name host;
       
       ssl_certificate /certs/certificate.crt;	# 인증서 파일과
       ssl_certificate_key /certs/private.key; # 비공개키 정보를 설정한다.
       ...
   }
   ```

   끝.

   이긴 한데 이렇게하면 우리의 사이트에 유저들이 http로 들어올 수 도 있고 https로 들어올 수도 있다. http로 들어오는 친구들의 정보를 보호하기 위해 친절하게 https로 redirect 시켜버리자. redirect를 위해 server 뭉치를 분리한다.

   ```nginx
   server {
   	listen 80;
   	server_name host;
   	location / {
   		return 301 https://$host$request_uri;
           # return 301을 이용해 redirect 시켜주는데
           # $host = server_name 이고
           # $request_uri = host 하위의 uri이다. 
   	}
   }
   
   server {
       listen 443 ssl;
       server_name host;
       
       ssl_certificate /certs/certificate.crt;
       ssl_certificate_key /certs/private.key;
       
       location / {
           ...
       }
       ...
   }
   ```

   이런 식으로 하면 http로 들어오는 친구들도 https로 리다이렉트 시킬 수 있다.

   

10. Let's Encrypt의 무료 인증서는 3개월마다 갱신해야 한다.

<br>

#### Express에 SSL 적용하기

Client Server에 SSL을 적용했으면 REST API Server에도 SSL을 적용시켜야 한다. (위험하다고 post, put, delete 요청이 안보내짐, get은 되긴하는데 경고 메세지를 띄운다.)

Express에 SSL을 적용하는 것은 매우 간단하다. typescript 문법으로 하면

```typescript
...
// 라이브러리 두개를 불러와 주고
import * as fs from 'fs';
import * as https from 'https';
...

// express app을 실행시킬 때 https를 통해 실행시킨다.
// + https에 인증서 정보를 설정한다.
https.createServer({
    ca: fs.readFileSync('/certs/ca_bundle.crt'),
    cert: fs.readFileSync('/certs/certificate.crt'),
    key: fs.readFileSync('/certs/private.key')
}, app).listen(3000, () => {
    console.log('hosting on https://localhost:3000!!')
})
```

위의 코드를 추가해주면 끝이다.

 <br>

#### 이 사이트의 보안연결은 완벽하지 않습니다.

Client서버와 REST API 서버 모두 HTTPS를 적용했는데 이런 경고 메세지가 떴다. 로그인 페이지에선 이 메세지가 뜨지 않고 로그인을 한 뒤 부터 이 메세지가 뜨는데 콘솔창에 경고메세지와 함께 어떤 파일이 위험한지 알려주고 있었다. 

![mixedContents](./mixedContents.jpg)

눌러서 자세히 보니 S3에서 이미지를 가져올 때 http요청으로 가지고 오고 있다고 경고를 하고 있었다. 

이러한 경고가 뜨는 것은 서비스에서 매우 불리하다. 구글 SEO(검색엔진최적화, search Engine Optimization)에서 보안이 확실하지 않은 사이트는 우선순위에서 밀리게 한다고 하기 때문이다. 그래서 이 문제를 해결해야 하는데 방법은

- S3에서 이미지를 받아올 때
- CDN을 사용할 때
- 외부 사이트의 이미지 링크를 불러올 때
- 각종 요청을 보낼 때

등등 모두 https 요청으로 바꾸면 되것다.

