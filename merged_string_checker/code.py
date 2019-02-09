def is_merge(s, part1, part2):
    return merge(s, part1, part2) or merge(s, part2, part1)
        
def merge(s, part1, part2):
    if (s == '' and part1 == '' and part2 == ''):
        return True
    elif (s != '' and part1 != '' and s[0] == part1[0]):
        return is_merge(s[1:], part1[1:], part2)
    elif (s != '' and part2 != '' and s[0] == part2[0]):
        return is_merge(s[1:], part1, part2[1:])
    else:
        return False