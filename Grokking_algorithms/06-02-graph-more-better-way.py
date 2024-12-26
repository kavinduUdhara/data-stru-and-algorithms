from collections import deque

class Person:
    def __init__(self, name: str, isSeller: bool):
        self.name = name
        self.isSeller = isSeller
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def get_friends(self):
        return self.friends

class SocialNetwork:
    def __init__(self):
        self.people = {}
    
    def add_person(self, name: str, isSeller: bool):
        if name not in self.people:
            self.people[name] = Person(name, isSeller)
    
    def add_friendship(self, name1: str, following: list):
        if name1 in self.people:
            for i in following:
                if i in self.people:
                    self.people[name1].add_friend(i)
    def display_network(self):
        for person in self.people.values():
            friends_names = [friend for friend in person.get_friends()]
            print(f"{person.name} follows: {', '.join(friends_names)}")
    def find_sellers(self, person: str):
        if person in self.people:
            search_queue = deque()
            search_queue += self.people[person].get_friends()
            searched = set()
            print(search_queue)
            while search_queue:
                friend = search_queue.popleft()
                if friend not in searched:
                    if self.people[friend].isSeller:
                        print(f"{friend} is a seller")
                        return True
                    else:
                        search_queue += self.people[friend].get_friends()
                        searched.add(friend)
            return False



net = SocialNetwork()
net.add_person("me", False)
net.add_person("alice", False)
net.add_person("bob", False)
net.add_person("claire", False)
net.add_person("peggy", False)
net.add_person("anuj", False)
net.add_person("jonny", False)
net.add_person("thom", True)

net.add_friendship("me", ["alice", "bob", "claire"])
net.add_friendship("bob", ["anuj", "peggy"])
net.add_friendship("alice", ["peggy"])
net.add_friendship("claire", ["thom", "jonny"])

net.display_network()

net.find_sellers("me")