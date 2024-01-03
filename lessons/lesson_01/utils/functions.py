def formatted_type(var):
    newline = "\n\n"
    try:
        typeis = type(var).__name__
        print(f"Input: {var}")
        print(" ")
        print(f"Data type: {typeis}")
       
    except:
        return "Couldn't determine type."


class Solutions:
    q1 = dict
    q2 = "New England Patriots"
    