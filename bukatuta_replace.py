mezuKod = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
mezua = mezuKod
print(mezua)
abezedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
abezedarioFrek = "eaolsndruitcpmyqbhgfvjñzxkw"
letraFrek = {}
kont = 0

while kont < len(abezedario):
    letraFrek[abezedario[kont]] = mezua.count(abezedario[kont])
    kont = kont + 1
    
kont = 0

import operator
letraFrekOrd = sorted(letraFrek.items(), reverse=True, key=operator.itemgetter(1))

ind = 0

while kont <2:
    for letraKod in mezua:
        if letraKod == letraFrekOrd[kont][0]:
            mezua = mezua.replace(mezua[ind],abezedarioFrek[kont])
        ind = ind + 1
    ind = 0
    kont = kont + 1
    
mezua = ''.join(mezua)
print(mezua)

#mezuari begiratuz eta hitz laburrak analizatuz, gutxinaka aldaketak begi bistaz ikusten dira
mezua = mezua.replace('T','l')
mezua = mezua.replace('A','d')
mezua = mezua.replace('J','n')
mezua = mezua.replace('N','s')
mezua = mezua.replace('Z','u')
mezua = mezua.replace('S','q')
mezua = mezua.replace('O','f')
mezua = mezua.replace('C','i')
mezua = mezua.replace('R','c')
mezua = mezua.replace('K','r')
mezua = mezua.replace('P','m')
mezua = mezua.replace('I','o')
mezua = mezua.replace('H','t')
mezua = mezua.replace('U','g')
mezua = mezua.replace('G','j')
mezua = mezua.replace('Q','b')
mezua = mezua.replace('D','p')
mezua = mezua.replace('F','x')
mezua = mezua.replace('V','y')
mezua = mezua.replace('M','h')
mezua = mezua.replace('L','z')
print(mezua)
