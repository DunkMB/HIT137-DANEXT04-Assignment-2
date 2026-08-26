##Reading from an input text
#Open input text
with open('input_text.txt', 'r', encoding='utf-8') as f:
    input_content = f.read()
    for i, line in enumerate(f, 1):
        print(f"line {i}: {line.strip()!r}")

#Producing a tree

#Producing tokens (Darren)

#Evaluating the expression


#Creating an outut text
with open('output_text.txt', 'w', encoding='utf-8') as f:
    f.write(output_text) #This is where you need to add all outputs you wish to produce
   #Input value
   #Tree
   #Tokens
   #Answer to expression
