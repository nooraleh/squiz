with open('words.csv', 'r') as fo:
    counter = 0
    for line in fo.readlines():
        # import ipdb; ipdb.set_trace()
        if line.count(',') > 5:
            counter += 1

    print(counter)