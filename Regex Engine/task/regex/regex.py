def compare(r, inp):
    if r == inp:
        return True
    elif r == '.' and inp:
        return True
    elif not r and inp:
        return True
    elif r and not inp:
        return False
    else:
        return False


def check(regex, input_, f, n_r, n_i):

    if len(regex.strip('\\')) == n_r:
        return True
    if len(input_) == n_i:
        return False
    output = compare(regex[n_r], input_[n_i])

    if output and len(regex) == n_r + 1:
        return True
    if output:
        if regex[n_r + 1] in ('+', '*') and regex[n_r] != regex[n_r - 1] != '\\':
            if len(input_) - 1 == n_i:
                n_r = len(regex) - 1
            else:
                n_i += 1
        elif regex[n_r + 1] == '?' and regex[n_r] != '\\':
            n_r += 2
            n_i += 1
        else:
            n_r += 1
            n_i += 1
        return check(regex, input_, f, n_r, n_i)

    elif len(regex) > n_r + 1 and regex[n_r + 1] in ('?', '*') and regex[n_r] != '\\':
        n_r += 2
        return check(regex, input_, f, n_r, n_i)

    elif len(regex) > n_r + 1 and regex[n_r + 1] in ('+', '*') and n_r != n_i and regex[n_r] != '\\':
        n_r += 2
        return check(regex, input_, f, n_r, n_i)

    elif f != 'start' and len(input_) > len(regex):
        n_r += 1
        n_i += 1
        return check(regex, input_, f, n_r, n_i)
    return False


def main():
    line = input()
    f = None

    my_line = line.strip().split('|')

    if my_line[0].startswith('^') and my_line[0].endswith('$'):
        f = 'start'
        end = my_line[0][-2]
        reg = my_line[0][1:-1]
        # my_line[0] = my_line[0][1:-1]
        if '?' not in reg and '*' not in reg and '+' not in reg:
            out = check(reg, my_line[1], f, 0, 0) and check(reg[::-1], my_line[1][::-1], f, 0, 0)
            print(out)
        else:
            out = check(reg, my_line[1], f, 0, 0)
            print(bool(out and end == my_line[1][-1]))

    else:
        if my_line[0].startswith('^'):
            f = 'start'
            my_line[0] = my_line[0][1:]
        if my_line[0].endswith('$'):
            f = 'start'
            my_line[0] = my_line[0][:-1]
            my_line[0] = my_line[0][::-1]
            my_line[1] = my_line[1][::-1]

        regex = my_line[0]
        input_ = my_line[1]

        out = check(regex, input_, f, 0, 0)

        print(out)


if __name__ == "__main__":
    main()
