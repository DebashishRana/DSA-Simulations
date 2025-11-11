from dequeu import deque

front = deque()
back = deque()


front.add_front("google.com")
front.add_front("facebook.com")
print(f"Front Deque {front}")
print(f"Back Deque {back}")

print("Operations:")

back.add_front(front.peek_front())
front.remove_front()
print(f"Front Deque {front}")
print(f"Back Deque {back}")


