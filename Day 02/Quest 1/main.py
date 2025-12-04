with open('input.txt', 'r') as file:
    content = file.read()
    sum=0
    isInvalid: bool = False
    # print(content)
    ranges:list = content.split(',')
    range_each = []
    for r in ranges:
        start, end = r.strip().split('-')
        range_each.append((int(start), int(end)))
    range_each.sort()
    
    for el in range_each:
        for i in range(el[0], el[1]+1):
            num_word = str(i)
            if len(num_word) % 2 == 0:
                for i in range(len(num_word)//2):
                    if num_word[i] == num_word[len(num_word)//2+i]:
                        isInvalid = True
                    else:
                        isInvalid = False
                        break
                if isInvalid:
                    sum += int(num_word)
    print(sum)
