from ast import keyword
from lib2to3.pgen2 import token
from operator import truediv


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def format(lexeme, token):
    space = 20
    line = token
    for x in range(0, space-len(token)):
        line += " "
    line += lexeme
    return line


def main():
    # Write to Output
    token_types = {
        "keyword": ["while"],
        "separator": ['(', ')', ';'],
        "operator": ['<', '=']
    }

    token = []
    lexeme = []

    input = open("input_scode.txt", "r")
    cur_lex = ""
    for elems in input.read():
        if(elems not in token_types["separator"] and elems not in token_types["operator"] and elems != " "):
            cur_lex += elems
        else:
            if(cur_lex in token_types["keyword"]):
                token.append("Keyword")
            elif(cur_lex.isdigit() or isFloat(cur_lex)):
                token.append("Real")
            elif(cur_lex):
                token.append("Id")

            if(elems in token_types["separator"]):
                token.append("Separator")
            elif(elems in token_types["operator"]):
                token.append("operatior")

            if(cur_lex != ""):
                lexeme.append(cur_lex)

            if(elems != " "):
                lexeme.append(elems)
            cur_lex = "" 

    for count, value in enumerate(lexeme):
        if(value == " "):
            lexeme.pop(count)

    output = ""
    o = open("output.txt", "w")
    o.write("Token_______________Lexeme")
    o.write("\n")


    for a in range(len(lexeme)):
        o.write(format(lexeme[a], token[a]))
        o.write("\n")
    
# -----------------------------------------------------------------------------------------------------------------------------------------
# FSA
    tokens = ["LITERAL", "SYMBOL", "EXPRESSION", "IDENTIFIER", "CONSTANT"]
    keywords = ["while", "if", "loop"]
    
    fsainput = ["while", "LITERAL", "CONSTANT", "SYMBOL", "while", "LITERAL", "IDENTIFIER", "CONSTANT", "IDENTIFIER", "SYMBOL"]

    end = ""
    states = [["KEYWORD", "TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"], ["TOKEN"]]
    for count, elems in enumerate(states):
        if fsainput[count] in tokens:
            temp = "TOKEN"
        elif fsainput[count] in keywords:
            temp = "KEYWORD"
        print(temp)
        if temp in states[count]:
            end = "pass state"
        else:
            end = "error state"
            break
        
    return print(end)

if __name__ == '__main__':
    main()