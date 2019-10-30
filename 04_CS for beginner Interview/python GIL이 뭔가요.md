#	python GIL이 뭔가요? 

GIL은 Global Interpreter Lock을 말합니다.

Python은 Interpreter가 코드를 읽는 방식으로 작동되는 언어입니다. 그래서 Python 프로그램이 실행되려면 먼저 Interpreter가 메모리에 올라와야 하고 메모리에 올라온 Interpreter는 코드를 실행합니다. 

그런데 이때, Python은 Global Interpreter Lock이 1로 제한 되어있어서 Interpreter를 작동할 수 있는 Thread 사용이 하나로 제한되어 있습니다. 

이렇게 제한이 되어있는 이유는 Python이 thread를 관리하는 방법이 thread-safe 하지 않기 때문입니다. thread-safe 하지 않다는 것은 여러 thread가 동시에 사용될 경우 프로세스에서 공통으로 사용되는 리소스에 여러 thread가 동시에 접근할 수 있다는 말입니다. 동시에 접근하게 되면 변수에 있던 값을 연산할 때 다른 thread의 연산이 씹힐수(?) 있습니다. 그렇게 되면 의도한 계산값이 아닌 다른 계산값이 나오게 됩니다. 이렇게 동시에 여러 thread가 하나의 프로세스 공유 데이터에 접근하는 현상을 race condition이라고 합니다. 

이러한 현상이 문제가 되는 이유는 Python의 메모리 관리 방식과 관련이 있습니다. 파이썬은 객체를 생성하면 그 객체가 얼마나 reference 되었는지를 count 하는 방식으로 메모리를 관리합니다. 그러니까 객체의 reference가 1 이상일 때 공간을 할당하고 0이 되었을 때 가비지 콜렉터에 의해 공간에서 사라집니다. 그런데 만약 동시에 두개의 thread가 하나의 객체의 reference count를 변경한다고 하면 count가 덜되거나 더 되는 일이 발생합니다. 이렇게 되면 메모리에 올라와 있어야할 객체가 없어지거나 메모리에서 지워주어야 하는 객체가 남아있게 됩니다. 이러한 일을 해결하기 위해 모든 객체에 대해 접근을 제한 하는 방법(mutex, mutual exclusive)을 사용할 수 있지만 여러개의 mutex를 사용하는 것은 처리속도 문제가 커질 뿐 아니라 deadlock이 발생활 확률을 높이는 일이 됩니다. 

그래서 Python에서는 아예 Interprete를 작동시키는 thread를 하나로 제한한 것입니다. 이렇게 하면 여러 thread가 동시에 하나의 리소스에 접근하는 일을 원천적으로 차단할 수 있습니다. 

또한 정확하게 말하면 thread 사용이 하나밖에 되지 않는 것이아니고 여러 모듈을 import 해서 여러 thread를 사용할 수 있습니다. 하지만 여전히 interpreter가 실행되는 thread는 1개로 제한 되어있기 때문에 하나의 thread가 CPU를 다 쓰고 나온 뒤에 다른 Thread가 CPU를 사용할 수 있습니다. 사실상 multi threading이 가지는 이점을 이용한다 라고 보기는 어려운 것입니다. 

그렇다고 Python에서의 multi threading이 완전히 의미 없는 것은 아닙니다. 만약에 I/O 작업(입출력 작업, 커널을 통해서 외부기기와 연결된 입출력을 처리하는 일. I/O 작업에서는 CPU가 거의 사용되지 않습니다.)이 빡세게 일어나는 프로그램에서는 I/O 작업이 이루어 지는 동안 다른 thread가 CPU를 사용할 수 있기 때문에 성능의 개선이 일어날 수 있습니다. 

multi threading을 할 수 없다고 해서 병렬처리가 되지 않는 것은 아닙니다. mulit processing을 통해 병렬처리를 구현 할 수 있습니다. mulit threading과 마찬가지로  multiprocessing  모듈을 import 해서 병렬 처리를 구현할 수 있습니다. 다만 mulit processing은 mulit threading에 비해 메모리 사용량이 훨씬 많다는 단점이 있습니다. 또 프로세스를 2개이상 사용하는 작업이기 때문에 프로세스간 데이터 교환을 시켜주어야 합니다.

그런데 공유해야 하는 데이터가 많아지면 프로세스간 데이터 교환에 엄청난 코스트를 쓰게 됩니다. 그러므로 python이 아닌 C++ 같은 언어를 사용할 때에는 프로세스간 공통으로 사용하는 리소스들이 많은 작업에는 mulit threading을 통해 병렬처리를, 프로세스간 공통으로 사용하는 리소스들이 적고 많은 연산량을 필요로 하는 작업에서는 mulit processing을 통해 분산처리 프로그래밍을 구현하는 것이 효과적입니다.