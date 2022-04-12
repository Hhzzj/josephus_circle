import random

CHARS1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHARS2 = "abcdefghijklmnopqrstuvwxyz"


class Person(object):
    def __init__(self, last_name, first_name, id):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def __str__(self):
        return "姓:%s 名:%s 编号:%s" %(self.last_name, self.first_name, self.id)

    def get_name(CHARS):
        assert CHARS != ''
        name = ''
        for i in range(2):
            name += random.choice(CHARS)
        return name

    def get_id(pos):
        assert type(pos) == int
        id = pos + 1
        return id

    def get_people_list(people_nums):
        assert type(people_nums)==int 
        assert people_nums > 0
        people_list = []
        for i in range(people_nums):
            last_name = Person.get_name(CHARS1)  
            first_name = Person.get_name(CHARS2) 
            id = Person.get_id(i)  
            people_list.append(Person(last_name, first_name, id))
        return people_list


class JosephusCircle():
    def  __init__(self,people_list,interval,start_person_id):
        assert type(people_list)==list  and type(interval)==int and type(start_person_id)==int
        assert 0 < start_person_id <= len(people_list)
        self.people_list = people_list
        self.interval = interval
        self.start_person_id = start_person_id
        self.start_pos = [ person.id for person in self.people_list ].index(self.start_person_id)

    def __iter__(self):
        return self 

    def __next__(self):
        if len(self.people_list)>0:
            out_pos = (self.start_pos+self.interval-1) % len(self.people_list)
            out_person = self.people_list.pop(out_pos)
            self.start_pos = out_pos
            return out_person
        else:
            raise StopIteration


if __name__ == '__main__':
    people_list = Person.get_people_list(11)
    josephus_circle = JosephusCircle(people_list, 3, 4)

    for person in josephus_circle:
        print(person.__str__())
