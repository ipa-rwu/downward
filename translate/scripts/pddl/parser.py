__all__ = ["ParseError", "parse_nested_list"]

class ParseError(Exception):
    pass

# Basic functions for parsing PDDL (Lisp) files.
def parse_nested_list(input_file):
    input_file = input_file.split('\n')
    tokens = tokenize(input_file)
    next_token = next(tokens)
    if next_token != "(":
        raise ParseError("Expected '(', got %s." % next_token)
    result = list(parse_list_aux(tokens))
    for tok in tokens:  # Check that generator is exhausted.
        raise ParseError("Unexpected token: %s." % tok)
    return result

def tokenize(inputs):
    #print inputs
    for line in inputs:
        line = line.split(";", 1)[0]  # Strip comments.
        line = line.replace("(", " ( ").replace(")", " ) ").replace("?", " ?")
	#print line
        for token in line.split():
            yield token.lower()

def parse_list_aux(tokenstream):
    # Leading "(" has already been swallowed.
    while True:
        try:
            token = next(tokenstream)
        except StopIteration:
            raise ParseError()
        if token == ")":
            return
        elif token == "(":
            yield list(parse_list_aux(tokenstream))
        else:
            yield token
