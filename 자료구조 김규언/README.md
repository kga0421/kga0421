#김규언 202630203
## 9월10일 (2주차 강의)



# html의 h1부터 h6까지의 표현 
# h1 크기
## h2 크기
### h3 크기
#### h4 크기
##### h5 크기

*이텔릭체*


**볼드**

----
1. 사과
2. 배
3. 감

*사과
  *깍은 사과
  *맛있는  사과
*배
*감

# This program prints Hello, world!
print('Hello, world!')
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}

https://www.google.com/

# 큐 초기화 함수
def init_queue(size):
    global test_queue, front, rear  # queue 대신 test_queue 사용
    test_queue = [None] * size
    front = -1  # 1이 아니라 -1로 설정해야 0번 위치부터 차례대로 데이터가 들어갑니다.
    rear = -1
    return print("큐 초기화 완료되었습니다. 큐 크기는 " + str(size) + "입니다.")


def is_queue_full():
    global rear
    if rear == len(test_queue) - 1:
        return True
    else:
        return False


def is_queue_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global rear
    if is_queue_full():
        print("큐가 가득 찼습니다.")
        return
    rear += 1
    test_queue[rear] = data


def dequeue():
    global front
    if is_queue_empty():
        print("큐가 비어 있습니다.")
        return None
    front += 1
    data = test_queue[front]
    test_queue[front] = None
    return data


def queue_print():
    print("===큐 상태 ===")
    for i in range(len(test_queue)):
        print(test_queue[i])
    print("============")
    print("front:", front)
    print("rear:", rear)
    print("============")


# 실행
init_queue(5)

enqueue("커피")
enqueue("녹차")
enqueue("꿀물")
enqueue("꿀물")
enqueue("꿀물")
enqueue("꿀물")  # 6번째는 꽉 차서 "큐가 가득 찼습니다." 출력됨
queue_print()
