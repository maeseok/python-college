data =[2, 45, 33, 12, 67, 80, 59, 75, 93, 38, 54, 27, 98, 1, 71, 52, 86, 41, 64, 36]
'''dic={}

for i in range(len(data)):
    res = '''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.cnt=0
    def hash_function(self, key):
        return (key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        ori_index=index
        i=1
        while self.table[index] is not None:
            index = (ori_index + i**2) % self.size  # 다음 위치로 이동
            i+=1
            self.cnt+=1
        self.table[index] = key

    def display(self):
        print("해시 테이블:", self.table)
        return self.cnt

# 예시 사용
hash_table = HashTable(23)

keys = data
for i in range(len(keys)):
    hash_table.insert(keys[i])

print(hash_table.display())

