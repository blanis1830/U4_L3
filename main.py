from StackClass import ArrayStack
import os
import re

def clean(text):
  return re.sub(r'[^a-zA-Z\s]', '', text)

def reversed():
    stack = ArrayStack()
    with open("earnest.txt", 'r') as openFile:
      original = openFile.read()
    cleaned = clean(original)
    words = cleaned.split()
    for word in words:
      stack.push(word)
    reversed_text = []
    while len(stack) > 0:
      reversed_text.append(stack.pop())
    with open("tsenrae.txt", 'w') as newFile:
      newFile.write(' '.join(reversed_text))
    
        
def main():
    reversed()


if __name__ == "__main__":
    main()