import time

def type_text_slowly(text, delay = 0.05):
    for char in text:
        print(char, end='', flush=True)  
        time.sleep(delay) 
    print() 

if __name__ == "__main__":
    type_text_slowly('test')