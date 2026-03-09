with open("C:\\Users\\user\\Documents\\task1.txt", "r",encoding="utf-8") as f:
    text = f.read()


punctuation = ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')']
symbols = ['@', '#', '$', '%', '&', '*', '+', '=', '<', '>', '/', '\\']

result = ""

for i in text:
    
    if i >= '0' and i <= '9':
        continue
    
    
    if i in punctuation:
        continue
    
    
    if i in symbols:
        continue
    
    
    if i >= 'A' and i <= 'Z':
        i = chr(ord(i) + 32)
    
    result = result + i

print(result)