import re

def calculate(string):
    expression = re.findall("\s([0-9\+\-/\*\(\)\.\s]+)", string)
    
    if not expression:
        print "I can't calculate that."
        return

    expression = expression[0]

    # NOTE: eval is SAFE in this context! The regex will disallow anything
    #       other than a mathematical expression, which is harmless when
    #       fed to Python's eval() function.
    try:
        print eval(expression)
    except SyntaxError:
        print "I can't calculate that."
        return
