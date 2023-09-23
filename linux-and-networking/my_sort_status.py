import sys
def error_sort():
    user_input = sys.stdin.readlines()
    sorted_user = sorted(user_input, reverse=True)
    #strip?
    print(''.join(sorted_user), end='', file=sys.stderr)

error_sort()