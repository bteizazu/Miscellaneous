from PyDictionary import PyDictionary
import os.path

dictionary = PyDictionary()

mac_string = 'macmacacomacacusmacadammacadamizationmacadamizemacadamizingmacaomacaquemacarizemacaronimacaronianmacaronicmacaroonmacartneymacaumacaucomacavahumacawmaccabeanmaccaboymaccomaccoboymacemacedoniamacedonianmacedonianismmacermaceratemaceratermaceratingmacerationmacfadyenamachaerantheramachaerodusmachairodusmachakosmachalamachapucharemachengmachermachetemachiavelianmachiavelianismmachiavelismmachicolatedmachicolationmachicoulismachidamachilipatnammachinalmachinatemachinatingmachinationmachinatormachinemachine-gunmachine-headmachine-mademachinermachine-readablemachinerymachiningmachinistmachomacilencymacilentmacintoshmackayamackenziemackerelmackintoshmacklemaclemacleaniamacleayamacledmacluramaclureamaclurinmacrencephalicmacrencephalousmacrobioticmacrobioticsmacrocephalousmacrocosmmacrocosmicmacrocystismacrodactylmacrodactylicmacrodactylousmacrodiagonalmacrodomemacrodontmacrofaradmacroglossiamacrognathicmacrologymacrometermacronmacropetalousmacrophyllousmacropidiamacropinacoidmacropodmacropodalmacropodianmacropodousmacroprismmacropterousmacropusmacropyramidmacroscopicmacroscopicalmacrosporangiummacrosporemacrosporicmacrotonemacrotousmacrouramacrouralmacrozamiamacrozoosporemacruralmacruranmacruroidmacrurousmactationmactramaculamaculatemaculatedmaculationmaculatorymaculaturemaculemaculose'
macwords = []
macphrase_list = []
mac11 = 0
mac12 = mac11 + 3
mac21 = 3
mac22 = mac21 + 3
while mac21 <= (len(mac_string) - 2):
    print(str(mac21) + '/' + str(len(mac_string)))
    if mac_string[mac21:mac21+3] == 'mac':
        mac_word = mac_string[mac12:mac21]
        macwords.append(mac_word)
        macwords.append('       ' + 'mac' + mac_word)
        macwords.append('')
        #if (bool(dictionary.meaning(mac_word))):
            #macphrase_list.append(mac_word + ' mac' + mac_word)
        mac11 = mac21
        mac12 = mac11 + 3
    mac21 += 1
os.remove('/Users/bonssateizazu/Desktop/macPhrases.txt')
with open('/Users/bonssateizazu/Desktop/macPhrases.txt', "a") as f:
    print(*macwords, sep = "\n", file = f)
