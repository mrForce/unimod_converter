import argparse
import re

parser = argparse.ArgumentParser(description='Convert UNIMOD in PIN file to mass')
parser.add_argument('input_pin', help='location of the pin to read from')
parser.add_argument('output_pin', help='Where to write output')
args = parser.parse_args()


conversion_map = {1: '42.010565', 2: '-0.984016', 3: '226.077598', 4: '57.021464', 6: '58.005479', 8: '486.251206', 9: '494.30142', 10: '-29.992806', 12: '450.275205', 13: '442.224991', 17: '99.068414', 21: '79.966331', 24: '71.037114', 25: '119.037114', 27: '-18.010565', 28: '-17.026549', 29: '127.063329', 30: '21.981943', 31: '105.057849', 34: '14.01565', 36: '28.0313', 37: '42.04695', 40: '79.956815', 41: '162.052824', 42: '188.032956', 43: '203.079373', 44: '204.187801', 45: '210.198366', 46: '229.014009', 47: '238.229666', 48: '272.250401', 49: '340.085794', 50: '783.141486', 51: '788.725777', 52: '42.021798', 53: '156.11503', 54: '176.032088', 55: '305.068156', 56: '45.029395', 58: '56.026215', 59: '59.036279', 60: '127.099714', 61: '130.118544', 62: '133.137375', 63: '136.156205', 64: '100.016044', 65: '104.041151', 66: '104.029463', 89: '225.093583', 90: '338.177647', 91: '348.240414', 94: '68.037448', 95: '72.062555', 97: '74.055944', 105: '227.126991', 106: '236.157185', 107: '159.035399', 108: '125.047679', 118: '490.174218', 119: '316.138088', 121: '114.042927', 122: '27.994915', 123: '345.097915', 124: '351.118044', 126: '87.998285', 128: '388.082112', 129: '125.896648', 130: '251.793296', 131: '377.689944', 134: '208.182715', 135: '206.167065', 136: '104.026215', 137: '1216.422863', 139: '233.051049', 140: '-29.00274', 141: '41.026549', 142: '349.137281', 143: '406.158745', 144: '486.158471', 145: '495.19519', 146: '511.190105', 147: '552.216654', 148: '568.211569', 149: '656.227613', 150: '698.274563', 151: '700.253828', 152: '714.269478', 153: '730.264392', 154: '821.280102', 155: '846.311736', 156: '860.327386', 157: '862.306651', 158: '876.322301', 159: '892.317216', 160: '947.323029', 161: '923.290978', 162: '47.944449', 170: '2.988261', 176: '218.167065', 178: '87.050655', 184: '9.030193', 185: '88.996524', 186: '132.021129', 187: '282.052824', 188: '6.020129', 193: '4.008491', 194: '170.048013', 195: '171.149738', 196: '174.168569', 197: '184.157563', 198: '189.188947', 199: '32.056407', 200: '75.980527', 205: '94.041865', 206: '56.026215', 207: '38.01565', 208: '76.0313', 209: '112.05243', 211: '85.052764', 212: '90.084148', 213: '541.06111', 243: '296.016039', 253: '70.041865', 254: '26.01565', 255: '28.0313', 256: '40.0313', 258: '2.004246', 259: '8.014199', 260: '95.943487', 261: '214.971084', 262: '3.01883', 264: '121.035005', 267: '10.008269', 268: '6.013809', 269: '10.027228', 270: '362.136553', 271: '380.147118', 272: '135.983029', 273: '253.095023', 275: '28.990164', 276: '183.035399', 278: '44.026215', 280: '28.0313', 281: '765.09956', 284: '16.028204', 285: '155.004099', 286: '161.024228', 288: '13.979265', 291: '201.970617', 292: '322.020217', 293: '145.019749', 294: '326.141261', 295: '146.057909', 298: '17.03448', 301: '190.074228', 303: '75.998285', 305: '1444.53387', 307: '1606.586693', 308: '1768.639517', 309: '1298.475961', 310: '1460.528784', 311: '1622.581608', 312: '119.004099', 313: '-128.094963', 314: '111.032028', 316: '78.04695', 318: '62.01565', 319: '54.010565', 320: '143.058243', 323: '713.093079', 327: '44.008456', 329: '18.037835', 330: '36.07567', 332: '525.142894', 335: '158.13068', 337: '13.031634', 340: '77.910511', 342: '15.010899', 344: '-43.053433', 345: '47.984744', 350: '19.989829', 351: '3.994915', 352: '-1.031634', 354: '44.985078', 359: '13.979265', 360: '-30.010565', 366: '2.988261', 368: '-33.987721', 371: '86.036779', 372: '-42.021798', 374: '-1.007825', 375: '143.118438', 376: '220.182715', 377: '576.511761', 378: '72.021129', 379: '87.068414', 380: '266.203451', 381: '14.96328', 382: '-33.003705', 387: '586.279135', 388: '588.294785', 389: '584.263485', 390: '616.177295', 391: '521.884073', 392: '29.974179', 393: '340.100562', 395: '881.146904', 396: '197.04531', 397: '469.716159', 398: '595.612807', 400: '-94.041865', 401: '-2.01565', 402: '-17.992806', 403: '-15.010899', 405: '329.05252', 407: '146.036779', 408: '148.037173', 409: '454.088965', 410: '634.662782', 411: '119.037114', 412: '124.068498', 413: '345.047435', 414: '30.010565', 415: '1620.930224', 416: '418.137616', 417: '306.025302', 419: '154.00311', 420: '15.977156', 421: '31.972071', 422: '70.005479', 423: '79.91652', 424: '1572.985775', 425: '31.989829', 426: '126.104465', 428: '283.045704', 429: '242.019154', 431: '236.214016', 432: '368.344302', 433: '264.187801', 434: '294.183109', 435: '109.052764', 436: '614.161645', 437: '386.110369', 438: '24.995249', 439: '342.786916', 440: '42.021798', 442: '438.094051', 443: '456.104615', 444: '922.834855', 445: '59.04969', 447: '-15.994915', 448: '831.197041', 449: '154.135765', 454: '161.068808', 464: '220.991213', 478: '421.073241', 490: '192.063388', 499: '298.022748', 510: '34.063117', 526: '-48.003371', 528: '14.999666', 529: '29.039125', 530: '37.955882', 531: '61.921774', 534: '155.821022', 535: '383.228103', 695: '7.017164', 772: '5.016774'}

replacements = [('[UNIMOD:' + str(key) + ']', '[' + value + ']') for key, value in conversion_map.items()]
with open(args.input_pin, 'r') as input_file:
    with open(args.output_pin, 'w') as output_file:
        for line in input_file:
            if 'UNIMOD' in line:                
                for old, new in replacements:
                    #probably not the most efficient way to do this, but it works
                    line = line.replace(old, new)
            output_file.write(line)
                
