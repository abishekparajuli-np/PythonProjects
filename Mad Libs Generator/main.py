import re
import os

_stories=['movie','pizza','space','zoo','school']

def _choice(_storyChoice):
    if _storyChoice in _stories:
                return _storyChoice
    else:
        print('Invalid Story Name! Enter Again!!')
        return 'invalid'
        
while True:
    print('Press zoo for "A Day at the Zoo"\nspace for "Space Adventure"\nschool for "First Day of School"\n movie for "Movie Madness"\n pizza for "Pizza Party Gone Wrong"')
    _storyChoice=input('Enter the story you want to choose:  ').lower().strip()

    _filename = f"Mad Libs Generator/{_choice(_storyChoice)}.txt"
    if not _filename == 'invalid.txt':
        break

def get_story(_filename):
    if not os.path.exists(_filename):
        print(f"File not found: {_filename}")
        print("Current working directory is:", os.getcwd())
        exit()
    with open(_filename,'r') as f:
        story=f.read()
        return story
        
    
def get_replaceable_words(story):
    _replace=[]
    for words in re.findall(r"{(.*?)}",story):
        _replace.append(words)
    return _replace

def get_input(_placeHolder):
    inputs={}
    for words in _placeHolder:
        _input=input("Enter a {}: ".format(words))
        inputs[words]=_input
    return inputs

def fill_story(_inputs,_story):
    for key,value in _inputs.items():
        _story=_story.replace(f"{{{key}}}",value)
    return _story



_story=get_story(_filename)

_placeHolder=list(dict.fromkeys(get_replaceable_words(_story)))

_userInputs=get_input(_placeHolder)

_newStory=fill_story(_userInputs,_story)

print('YOUR STORY\n')
print(_newStory)