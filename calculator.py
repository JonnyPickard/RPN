import re

precidence = {
        '+' : 1,
        '*' : 2
        }

def answer(str):
    output = []
    stack = []
    chars = list(str)

    for char in chars:
        if re.match(r'(\d)', char):
            output.append(char)

        elif not stack:
            stack.append(char)

        elif stack[-1] == char:
            stack.append(char)

        elif precidence[stack[-1]] < precidence[char]:
            stack.append(char)

        elif precidence[stack[-1]] > precidence[char]:
            count = 0

            for s in stack:
                if precidence[s] > precidence[char]:
                    output.append(s)
                    count += 1

            del stack[-count:]
            stack.append(char)

    for x in reversed(stack):
        output.append(x)

    return "".join(output)
