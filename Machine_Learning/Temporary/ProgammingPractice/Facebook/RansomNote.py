def ransom_note(magazine, rasom):
    for e in ransom:
        if e not in magazine:
             return False
        else:
             magazine.remove(e)
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
#print (magazine, ' - ', ransom)
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

