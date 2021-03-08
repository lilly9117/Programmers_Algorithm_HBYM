def solution(m, musicinfos):
    answer = ''
    m = m.replace('A#','H')
    m = m.replace('C#','I')
    m = m.replace('D#','J')
    m = m.replace('F#','K')
    m = m.replace('G#','L')
    dic = dict()

    for info in musicinfos:
        start, end, title, sound = info.split(',')

        s_h, s_m = start.split(':')
        e_h, e_m = end.split(':')
        time = (int(e_h)-int(s_h))*60 + (int(e_m)-int(s_m))
        sound = sound.replace('A#','H')
        sound = sound.replace('C#','I')
        sound = sound.replace('D#','J')
        sound = sound.replace('F#','K')
        sound = sound.replace('G#','L')

        sound = sound * (time//len(sound)) + sound[0:time%len(sound)]
        dic[sound] = title

    for s in dic.keys():
        if m in s:
            if answer == '':
                answer = s
            elif len(answer) < len(s):
                answer = s
            else:
                pass
    
    if answer != '':
        return dic[answer]
    else:
        return "(None)"
    
    return answer

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# print(solution(m, musicinfos))