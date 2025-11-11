from dequeu import deque

def palindrome_checker(word):
    main_word = word
    reverse = ""
    is_palindrome = True
    
    for x in main_word[::-1]:
        reverse += x

    if main_word == reverse:
        is_palindrome = True
    else:
        is_palindrome = False

    return f"{is_palindrome} "


p = "radar"
print(palindrome_checker(p))


# Using deque class 

def palindrome_checker(word):
    d = deque()
    
    # Add each character to rear
    for char in word:
        d.add_front(char)
    
    # Compare front and rear until middle
    while d.size() > 1:
        if d.peek_front() != d.peek_rear():
            return False
        d.remove_front()
        d.remove_rear()
    
    return True
g = "radar"
print(palindrome_checker(g))  # Is a palindrome  