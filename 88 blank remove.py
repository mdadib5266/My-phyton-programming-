with open('sample.txt','r') as file:
    lines = file.readlines()
non_empty_lines = [line for line in lines if line.strip()]
with open('cleaned.txt','w') as file:
    content = file.writelines(non_empty_lines)
'''print(str(lines))
print(lines)
lines = str(lines).strip()
print(lines)'''