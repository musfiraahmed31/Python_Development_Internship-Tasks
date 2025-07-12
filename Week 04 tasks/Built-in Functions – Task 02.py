UserExpression = input("Enter a Python expression: ")

try:
    LocalScope = {}
    exec("Result = " + UserExpression, {}, LocalScope)
    print("Result of the expression:", LocalScope['Result'])
    
except Exception as Error:
    print("An error occurred while evaluating:", Error)
