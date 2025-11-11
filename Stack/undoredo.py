#importing modules 
import sys
from stack import stack

def undo_redo(arvuemnt,action) -> str:
    #intiatin variables
    placeholder1 = stack()
    undo = stack()
    redo = stack()
    # safe case
    if not isinstance(action,str):
        newstr = str(action)
    else:
        pass
    
    #main loop 
    while True:
        for x in arvuemnt:
            placeholder1.push(x)
            #return arvuemnt works 
        if action.lower() == 'undo':
            unduin = placeholder1.pop()
            redo.push(unduin)
            return placeholder1
        
        if action.lower == 'redo':
            if  redo.is_empty():
                return f"Not possible no actions done prior"
                
            
            placeholder1.push(unduin)
            a =redo.pop()
            undo.push(a)
            return placeholder1

stack1 = ['a','b','c','d','e','f']
action1 = "undo"
action2 = "redo"
print(undo_redo(stack1,action1))


# Next work 
# Make it accept prompt while not terminated 
#real time undo redo 
#ability to type in real time and then input output