import random
import math
import time
import operator



_question=2

_operators=['+','-','*']
_max=10
_min=1

_ops={ '+':operator.add, '-': operator.sub, '*':operator.mul}

def random_math_problem(_operators):
    _term1=random.randint(_min,_max)
    _term2=random.randint(_min,_max)
    _operator= random.choice(_operators)
    _expr= str(_term1) + " "+_operator+" "+ str(_term2)
    _answer=_ops[_operator](_term1,_term2)
    return _expr,_answer

while True:
    _choice=input('Press "y" to start timer and solve math problems or press "n" to quit the game: ').lower()
    print("--------------------------------------------------------------------------------------")
    
    if _choice=='y':
        _count = 0
        start_time=time.time()
        for value in range(0,_question):
            try:
                _expression,_answer=random_math_problem(_operators)
                while True:
                    _userAnswer= int(input('Solve {}  : '.format(_expression)))
                    _count+=1
                    if math.ceil(_userAnswer) ==_answer :
                        break
                    else:
                        continue
            except ValueError as e:
                print('Error!! ',e)
                continue
        end_time=time.time()
        _time= end_time - start_time

        print("--------------------------------------------------------------------------------")
        print('Time: {} seconds     Accurary:{}%'.format(_time,float((_question/_count)*100)))

        exit()
    elif _choice=='n':
        print("Thank You For Playing")
        break
    else:
        print('Invalid Choice')
    
        
    
