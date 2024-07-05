class HashTable:
    def __init__(self, size=7):
        self.map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set(self, key, value):
        index = self.__hash(key)
        if self.map[index] is None:
          self.map[index] = []
        self.map[index].append([key, value])
    
    def get(self, key):
        index = self.__hash(key)
        if self.map[index] is not None:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index][i][1]

        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.map)):
            if self.map[i] is not None:
                for y in range(len(self.map[i])):
                    keys.append(self.map[i][y][0])
        return keys


        
        
my_hash_table = HashTable()

my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""
