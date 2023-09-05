
class DataStorage:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:

    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]

    def modulo(self, key):
        if type(key) == int:
            return key % self.size
        else:
            ascii_sum = 0
            for i in key:
                ascii_sum += ord(i)
            return ascii_sum % self.size

    def solve_collision(self, data, key):
        for i in range(self.size):
            key_value = (data + self.c1 * i + self.c2 * i ** 2) % self.size
            if self.tab[key_value] is None:
                return key_value
            elif self.tab[key_value] is not None:
                if self.tab[key_value].key == key:
                    return key_value
            else:
                return None

    def search(self, key):
        key_val = self.modulo(key)
        if key <= len(self.tab):
            return self.tab[key_val].data
        else:
            return None

    def insert(self, data, key):
        temp = DataStorage(key, data)
        key_value = self.modulo(temp.key)
        if self.tab[key_value] is not None:
            if self.tab[key_value].key != key:
                key_value = self.solve_collision(key_value, key)
        if key_value is None:
            print("Brak miejsca")
            return None
        self.tab[key_value] = temp

    def remove(self, key):
        if key <= len(self.tab):
            self.tab[key] = None
        else:
            print('brak danej o podanym kluczu')

    def __str__(self):
        temp_str = '{'
        for i in self.tab:
            if i is not None:
                temp_str = temp_str + str(i.key) + ':' + str(i.data)
            else:
                temp_str += str(None)
            temp_str = temp_str + ','
        temp_str = temp_str[:-1]
        temp_str = temp_str + '}'
        return temp_str



print('1.utowrzenie tablicy o rozmiarze 13 i dodanie do niej wartości:')
tab = HashTable(13)
tab.insert('A', 0)
tab.insert('B', 1)
tab.insert('C', 2)
tab.insert('D', 3)
tab.insert('E', 4)
tab.insert('F', 5)
tab.insert('G', 18)
tab.insert('H', 31)
tab.insert('I', 8)
tab.insert('J', 9)
tab.insert('K', 10)
tab.insert('L', 11)
tab.insert('M', 12)
print(tab)
print('2.Dana o kluczu 5:')
print(tab.search(5))
print('3.Dana o kluczu 14:')
print(tab.search(14))
tab.insert('Z', 5)
print('4.Nadpisanie oraz wypisanie danej o kluczu 5:')
print(tab.search(5))
print('5.Usunięcie danej o kluczu 5 i wypisanie tablicy:')
tab.remove(5)
print(tab.__str__())
print('6.Dana o kluczu 31:')
print(tab.search(31))
tab.insert('W', 'test')
print('tablica z wielokrotnosciami 13stki:')

# druga tablica
tab_2 = HashTable(13)
tab_2.insert('A', 13)
tab_2.insert('B', 26)
tab_2.insert('C', 39)
tab_2.insert('D', 52)
tab_2.insert('E', 65)
tab_2.insert('F', 78)
tab_2.insert('G', 91)
tab_2.insert('H', 104)
tab_2.insert('I', 117)
tab_2.insert('J', 130)
tab_2.insert('K', 143)
tab_2.insert('L', 156)
tab_2.insert('M', 169)
print(tab_2)

tab_3 = HashTable(13, 0, 1)
tab_3.insert('A', 13)
tab_3.insert('B', 26)
tab_3.insert('C', 39)
tab_3.insert('D', 52)
tab_3.insert('E', 65)
tab_3.insert('F', 78)
tab_3.insert('G', 91)
tab_3.insert('H', 104)
tab_3.insert('I', 117)
tab_3.insert('J', 130)
tab_3.insert('K', 143)
tab_3.insert('L', 156)
tab_3.insert('M', 169)
print(tab_3)

print('1.utowrzenie tablicy o rozmiarze 13 i dodanie do niej wartości:')
tab_4 = HashTable(13, 0, 1)
tab_4.insert('A', 0)
tab_4.insert('B', 1)
tab_4.insert('C', 2)
tab_4.insert('D', 3)
tab_4.insert('E', 4)
tab_4.insert('F', 5)
tab_4.insert('G', 18)
tab_4.insert('H', 31)
tab_4.insert('I', 8)
tab_4.insert('J', 9)
tab_4.insert('K', 10)
tab_4.insert('L', 11)
tab_4.insert('M', 12)
print(tab_4)
print('2.Dana o kluczu 5:')
print(tab_4.search(5))
print('3.Dana o kluczu 14:')
print(tab_4.search(14))
tab_4.insert('Z', 5)
print('4.Nadpisanie oraz wypisanie danej o kluczu 5:')
print(tab_4.search(5))
print('5.Usunięcie danej o kluczu 5 i wypisanie tablicy:')
tab_4.remove(5)
print(tab_4.__str__())
print('6.Dana o kluczu 31:')
print(tab_4.search(31))
tab_4.insert('W', 'test')