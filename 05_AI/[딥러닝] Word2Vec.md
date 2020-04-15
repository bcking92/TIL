# [딥러닝] Word2Vec

### Encoding?

딥러닝 모델에 text를 input으로 넣을 순 없다. 그 때 encoding을 한다.
encoding은 text를 number로 바꿔주는 것이다.

### One Hot Encoding

단어의 개수만큼의 차수의 벡터를 만들고 각각 대응하는 단어의 벡터에 1 나머지에는 0을 주는 방식

| unique word | encoding  |
| ----------- | --------- |
| thank       | [1, 0, 0] |
| you         | [0, 1, 0] |
| love        | [0, 0, 1] |

One Hot Encoding은 유사도가 없다. 단어사이의 관계를 표시할 수 없다. 왜냐하면 각각의 단어사이의 거리가 모두 같고 코사인 유사도(Cosine similarity)가 모두 0이 된다.(모든 단어 사이의 각도가 90도)

그래서 **Embedding**이 필요하다.

### Embedding

Embedding은 One Hot Encoding 보다 일반적으로 저차원의 벡터로 구성되며 유사도를 갖는다.

| unique word | encoding     | embedding |
| ----------- | ------------ | --------- |
| king        | [1, 0, 0, 0] | [1, 2]    |
| man         | [0, 1, 0, 0] | [1, 3]    |
| queen       | [0, 0, 1, 0] | [5, 1]    |
| woman       | [0, 0 ,0 ,0] | [5, 3]    |

### Word2Vec

Word2Vec은 embedding 중의 하나이며 유사도는 인접한 단어(이웃, Neighbor)들로부터 얻게 된다. 







