#PRACA SKOŃCZONA

class Elements:

    def __init__(self, elements):
        self.elements = elements
        self.next = None


class List:
    # inaczej metoda create:
    def __init__(self):
        self.head = None
        self.num_elem = 0

    def destroy(self):
        self.head = None

    def add(self, new_elem):
        if self.head is None:
            elem = Elements(new_elem)
            self.head = elem
            # zwieksz liczbe elem
        else:
            elem = Elements(new_elem)
            elem.next = self.head
            self.head = elem
            # zwieksz liczbe elem
        self.num_elem += 1

    def remove(self):
        if self.num_elem == 1:
            self.head = None
        else:
            self.head = self.head.next
        self.num_elem -= 1

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        self.num_elem += 1
        return self.num_elem

    def get(self):
        return  self.head.elements

    def print_list(self):
        elem = self.head
        for i in range(self.num_elem):
            print(elem.elements)
            elem = elem.next

    def add_bottom(self, new_elem):
        elem = self.head
        for i in range(self.num_elem):
            # print("wartosc przed przypisaniem:", elem.elements)
            elem = elem.next
            # print("wartosc po przypisaniu:", elem.elements)
            if i == self.num_elem-2:
                # print("Nowy element")
                elem.next = Elements(new_elem)
                self.num_elem += 1
                break

    def remove_bottom(self):
        elem = self.head
        for i in range(self.num_elem):
            # print("wartosc przed przypisaniem:", elem.elements)
            elem = elem.next
            # print("wartosc po przypisaniu:", elem.elements)
            if i == self.num_elem-3:
                elem.next = None
                self.num_elem -= 1
                break

    def take(self, n):

        if n >= self.num_elem:
            n = self.num_elem
        temp = n
        last_elem = self.head
        new_List = List()
        for i in range(n):
            for i in range(temp):
                if temp == 1:
                    temp = temp - 1
                    new_List.add(self.head.elements)
                    break
                last_elem = last_elem.next
                if i == temp-2:
                    temp = temp - 1
                    new_List.add(last_elem.elements)
                    last_elem = self.head
                    break
        return new_List

    def drop(self, n):
        if n >= self.num_elem:
            return None
        temp = self.num_elem
        last_elem = self.head
        new_List = List()
        for i in range(self.num_elem-n):
            for j in range(temp):
                if j == temp:
                    break
                last_elem = last_elem.next
                if j == temp-2:
                    temp = temp - 1
                    new_List.add(last_elem.elements)
                    last_elem = self.head
                    break
        return new_List

uczelnie = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

list = List()

for i in uczelnie:
    list.add(i)

print("\nDodanie elementow do listy:")
list.print_list()
print("\nUzycie remove:")
list.remove()
list.print_list()
print("\nWynik uzycia is_empty: ", list.is_empty())
print("\nWynik uzycia get:", list.get())
list.add_bottom(('PG', 'Gdańsk', 1945))
print("\nWynik uzycia add_bottm:")
list.print_list()
print("\nWynik uzycia remove_bottom:")
list.remove_bottom()
list.print_list()
print("\nWynik uzycia take:")
lista_nowa = list.take(3)
lista_nowa.print_list()
print("\nWynik uzycia drop:")
lista_nowa = list.drop(3)
lista_nowa.print_list()
print("\nWynik uzycia destroy:")
print("brak wyniku świadczy o poprawyn działaniu metody destory")