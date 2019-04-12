def delay(train):
    dep = train.get('departure')
    direction = dep.get('direction')
    if dep.get('delay') > 0:
        print 'train to {} has been delayed'.format(direction)