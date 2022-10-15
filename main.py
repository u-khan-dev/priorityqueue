from priorityqueue import PriorityQueue
from person import Person


def main():
    pq = PriorityQueue()
    pq.insert(Person(12, 'Stan'))
    pq.insert(Person(1, 'Jake'))
    pq.insert(Person(14, 'Nadia'))
    pq.insert(Person(2, 'Penny'))
    pq.insert(Person(10, 'Luke'))
    pq.insert(Person(3, 'Adam'))
    pq.insert(Person(25, 'Ruth'))

    print(pq)

    while not pq.isEmpty():
        print(pq.pop_and_delete())


if __name__ == '__main__':
    main()
