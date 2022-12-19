README for NXP:
# PiBook_tracker
A book reading tracker via Rasbperry Pi/OM5577/PN7120SM platform

The project use NXP 7120 controller, the information of NXP is below:
linux_libnfc-nci
================
Linux NFC stack for NCI based NXP NFC Controllers (PN7150, PN7120).

Information about NXP NFC Controller can be found on [NXP website](https://www.nxp.com/products/identification-and-security/nfc/nfc-reader-ics:NFC-READER).

Further details about the stack [here](https://www.nxp.com/doc/AN11697).

PiBook_tracker.py: main function

PN7210.py: migrated from Doron Horwi code: 
https://gist.github.com/doronhorwitz/fc5c4234a9db9ed87c53213d79e63b6c

Need NXP nfcDemoApp as the dependencies:

Running out-of-box PN7120 applications on Raspberry PI
a.	Install tools for PN7210 driver on Raspberry Pi
$ sudo apt-get install autoconf automake libtool git
b.	Clone NXP PN7120 from NXP Github
$ git clone https://github.com/NXPNFCLinux/linux_libnfc-nci.git
c.	Configure the library
$ cd linux_libnfc-nci
$ ./bootstrap
$ ./configure –enable-alt
d.	Build and install the library
Execute the commands(take up to 5 minutes to build libraries)
$ make
$ sudo make install
$ export LD_LIBRARY_PATH=/usr/local/lib

Testing eBay NTAG215 chips
Run demo application in poll mode executing the command:
$ nfcDemoApp poll
