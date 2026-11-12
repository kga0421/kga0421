# Node 클래스 정의
class Node():
    def __init__(self):  # 오타 수정: __int__ -> __init__
        self.data = None
        self.link = None

# 첫 번째 노드 생성
node1 = Node()
node1.data = "다현0"

# 두 번째 노드 생성 및 연결
node2 = Node()
node2.data = "다현1"
node1.link = node2

# 세 번째 노드 생성 및 연결
node3 = Node()
node3.data = "다현2"
node2.link = node3

# 네 번째 노드 생성 및 연결
node4 = Node()
node4.data = "다현3"
node3.link = node4

# 다섯 번째 노드 생성 및 연결
node5 = Node()
node5.data = "다현4"
node4.link = node5

# 데이터 모두 출력
current = node1
print(current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")
print()  # 줄바꿈

# 데이터 삽입 ("다현1"과 "다현2" 사이에 "솔라" 삽입)
newNode = Node()
newNode.data = "솔라"
newNode.link = node2.link
node2.link = newNode

# 삽입 후 전체 데이터 다시 출력
current = node1
print(current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")
print()  