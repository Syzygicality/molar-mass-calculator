from table import table

def calculate(element, count):
    periodic_table = table()
    valid_elements = list(periodic_table.keys())
    if element not in valid_elements:
        return None
    if count == "":
        count = 1 
    molar_mass = periodic_table[element]
    return molar_mass * int(count)

def check(chemical, coefficient):
    element, count = "", ""
    total_mass = 0
    bracket_level = 0
    add_brackets = False
    if chemical[0].islower() or chemical[0].isdigit():
        return None
    for cursor in chemical:
        print(cursor)
        if bracket_level == 0:
            if cursor.isupper():
                if element == "":
                    element += cursor
                else:
                    if add_brackets is True:
                        if check(element, int(count)) is None:
                            return None
                        total_mass += check(element, int(count))
                        element, count = "", ""
                        add_brackets = False
                    else:
                        if calculate(element, count) is None:
                            return None
                        total_mass += calculate(element, count)
                        element, count = cursor, ""
                
            elif cursor.islower():
                if element == "":
                    return None
                else:
                    element += cursor
            
            elif cursor.isdigit():
                count += cursor
            
            elif cursor == "(":
                bracket_level += 1
                add_brackets = True
                if calculate(element, count) is None:
                    return None
                total_mass += calculate(element, count)
                element, count = "", ""
        else:
            if cursor == "(":
                bracket_level += 1
            elif cursor == ")":
                bracket_level -= 1
            if bracket_level == 0:
                continue
            element += cursor
    
    if element != "":
        if add_brackets is True:
            if check(element, int(count)) is None:
                return None
            total_mass += check(element, int(count))
        else:
            if calculate(element, count) is None:
                return None
            total_mass += calculate(element, count)
    
    if coefficient is not None:
        total_mass *= coefficient
    return round(total_mass, 2)

while True:
    answer = check(input("> "), None)
    if answer is not None:
        print("M = " + str(answer))
    else:
        print("Invalid Input.")