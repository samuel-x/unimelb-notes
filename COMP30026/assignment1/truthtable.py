def tfSeq(size):
    ''' Generates a list of the given size containing all combinations
    of True and False.  Starts with all Trues and ends with all
    Falses.
    '''

    if size > 1:        
        for head in tfSeq(size-1):
            yield head + [True]
            yield head + [False]
    else:
        yield [True]
        yield [False]

def truthtable(vars, funcs):
    ''' 
    :vars: A list of variable names.  This will be output as LaTeX
           math labels.  

           Example: ['p','q','r']
    
    :funcs: A list of label/function pairs.  The label is a LaTeX math
            representation of the function.  The function is a Python
            function that takes the same number of arguments as there
            are variables in vars.  

            Example: [('p \and q',lambda p,q: p and q)]

    Returns a string containing code suitable for inserting directly
    into a LaTeX document.
    '''

    output = ''

    lVars = str(len(vars))
    lFuncs = str(len(funcs))
    output += r'\begin{tabular}{*{'+lVars+r'}{c}|*{'+lFuncs+r'}{c}}'

    labels = vars + [func[0] for func in funcs]
    output += '&'.join(['$'+label+'$' for label in labels]) + r'\\'
    output += '\n\\hline\n'

    tfText = {True:'T', False:'F'}

    for tf in tfSeq(len(vars)):
        values = [tfText[val] for val in tf] 
        values += ([tfText[func[1](*tf)] for func in funcs])
        output += '&'.join(values) + '\\\\\n'
        

    output += r'\end{tabular}'

    return output