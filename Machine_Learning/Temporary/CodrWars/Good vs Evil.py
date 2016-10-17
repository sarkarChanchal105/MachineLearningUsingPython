def goodVsEvil(good, evil):
    #TODO Go get'em boys...
    good=good.split()
    evil=evil.split()
    print (good,evil)
    sum_good=sum([int(x) for x in good ])
    sum_evil=sum([int(x) for x in evil])
    diff=sum_good-sum_evil
    if diff ==0:
        return 'Should be a tie'
    if diff<1:
        return 'Evil should win'
    if diff>1:
        return 'Good should win'


print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))

