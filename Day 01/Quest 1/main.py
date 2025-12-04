with open('input.txt', 'r') as file:
    content = file.readline()
    dialer:int = 50
    password:int = 0
    line_num:int = 1
    while(content):
        content = content.strip()
        if(content[0] == 'R'):
            dialer += int(content[1:])
        elif(content[0] == 'L'):
            dialer -= int(content[1:])
        dialer %= 100

        if(dialer == 0):
            password += 1
        print(f'Line {line_num}: Dialer: {dialer}, Password: {password}')
        line_num += 1
        content = file.readline()
