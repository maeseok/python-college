class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.cnt=0
    def hash_function(self, key):
        return key % self.size

    def second_hash_function(self, key):
        # 두 번째 해시 함수는 간단한 예시로 key를 7로 나눈 나머지를 사용합니다.
        return 1+ (key % 11)

    def double_hashing(self, key, i):
        return (self.hash_function(key) + i * self.second_hash_function(key)) % self.size

    def insert(self, key):
        i = 0
        index = self.hash_function(key)

        while self.table[index] is not None:
            i += 1
            index = self.double_hashing(key, i)
            self.cnt+=1
        self.table[index] = key

    def display(self):
        print("해시 테이블:", self.table)
        return self.cnt


# 예시 사용
hash_table_double_hashing = HashTableDoubleHashing(23)

keys =[2, 45, 33, 12, 67, 80, 59, 75, 93, 38, 54, 27, 98, 1, 71, 52, 86, 41, 64, 36]
for key in keys:
    hash_table_double_hashing.insert(key)

print(hash_table_double_hashing.display())