import os
import random

print('''

     _                      _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'                                                
                     by: 0xAnuj with <3                                                      
--------------------------------------------------------------------------------
''')

def get_hex():
    return random.choice("abcdef0123456789")

def get_mac():
    new_mac = ""
    for i in range(0,5):
        new_mac += get_hex() + get_hex() + ":"
    new_mac += get_hex() + get_hex()
    return new_mac

print "Old MAC address: "
os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")

os.system("sudo ifconfig wlan0 down")
print " \nDoing : Wlan0 down"
# setting new random MAC address
os.system("sudo ifconfig wlan0 hw ether " + get_mac() )


os.system("sudo ifconfig wlan0 up")
print " \nDoing : Wlan0 Up"
print "\nNew MAC address: "
os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")
