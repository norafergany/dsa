from collections import deque

graph = {"you": ["claire", "alice", "bob"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "jonny": [], "thom": [], "peggy": []}


def find_seller(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(name):
                print(name + " is a mango seller")
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False


def is_seller(name):
    return name[-1] == "m"
