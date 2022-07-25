# 처음 상태              내 위치
Linked List = ["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]

# 1번 이동                           내 위치
Linked List = ["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]

# 2번 이동                                      내 위치
Linked List = ["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]

# 3번 이동                                                 내 위치
Linked List = ["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]

# 4번 이동                                                             내 위치
Linked List = ["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]


# 추가
["node 1"] -> ["node 2"] -> ["node 3"] -> ["node 4"] -> ["node 5"]
                              ["New node "] 을 중간에 넣어야 합니다

# 1. node 3 의 Pointer를 New node 으로 연결하고,
["node 3"] -> ["New node "]
["node 4"] -> ["node 5"]

# 2. New node 으로 Pointer를 node 4 으로 연결합니다.
["node 3"] -> ["New node "] -> ["node 4"] -> ["node 5"]



# 삭제
["node 1"] -> ["node 2"] -> ["node 3"] -> ["New node "] -> ["node 4"] -> ["node 5"]
                                              ["node 4"] 을 버려야 합니다

# New node 의 Pointer를 떼서, node 5 으로 연결하면 됩니다!
["New node "]     ->      ["node 5"]
        ["node 4"]