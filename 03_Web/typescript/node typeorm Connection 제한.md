### node typeorm Connection 제한

typeorm 에서 connection limit 때문에 자꾸 서버가 멈추는 현상이 일어난다. 처음엔 connection 을 release 해주는 것으로 문제가 해결 된 줄 알았는데 여러 사람이 사용하다 보니 또 다시 connection limit 때문에 서버가 멈추는 현상이 발생했다. 자고 일어나니 자동으로 connection이 release 되어있어서 원인은 알 수 없었다. 이 문제 관련해서 더 공부를 해봐야 할 것 같다.

