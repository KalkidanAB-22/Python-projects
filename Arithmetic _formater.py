def arithmetic_arranger(problems, show_answers=False):
    
    # Rule 1: no more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top = []
    bottom = []
    dashes = []
    answers = []
    
    for problem in problems:
        first, operator, second = problem.split()
        
        # Rule 2: operator must be + or -
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Rule 3: numbers must be digits only
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Rule 4: max 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # width of each formatted problem
        width = max(len(first), len(second)) + 2
        
        # build formatted lines
        top.append(first.rjust(width))
        bottom.append(operator + second.rjust(width - 1))
        dashes.append('-' * width)
        
        # compute answer if requested
        if show_answers:
            if operator == '+':
                result = int(first) + int(second)
            else:
                result = int(first) - int(second)
            answers.append(str(result).rjust(width))
    
    # join with four spaces
    space = "    "
    arranged = (
        space.join(top) + "\n" +
        space.join(bottom) + "\n" +
        space.join(dashes)
    )
    
    if show_answers:
        arranged += "\n" + space.join(answers)
    
    return arranged
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
