import sys
def sort_reverse():
    user_input = sys.stdin.readlines()
    sorted_user = sorted(user_input, reverse=True)
    #strip?
    print(''.join(sorted_user), end='') #gets rid of end line characters and list wrappings
sort_reverse()
