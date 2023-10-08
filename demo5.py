
def input_by_type(msg, req_type):
    inp = input(msg)
    return req_type(inp)

inp = input_by_type("Input:", int)

print(type(inp))

