messages = []
total_chars = 0
participants = set()

while True:
    try:
        line = input()
        if line[0] == '+':
            participants.add(line[1:])
        elif line[0] == '-':
            participants.remove(line[1:])
        else:
            msg_len = len(line.split(':')[1])
            total_chars += len(participants) * msg_len
    except:
        break

print(total_chars)
