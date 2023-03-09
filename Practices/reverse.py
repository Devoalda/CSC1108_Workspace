def reverse():
    ch = raw_input()
    if ch != 'end':
        reverse()
    print ch,

reverse()

# input:
# a b c d end

# output:
# end d c b a
