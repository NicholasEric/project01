from os import system
from os import mkdir
import json
import datetime
import time


wallet = -1
role = ""
roleMethod = ""
trolley = {}
history = []
date = datetime.datetime.now()
currName = ""
pw = ""
userData = {}


def loadItemObj():
  global itemObj
  with open('inventoryProject/projectGalleryData01.json', 'r') as document:
    itemObj = json.load(document)


def loadUserData():
  global userData
  with open('inventoryProject/projectGalleryUsernames01.json', 'r') as document:
    userData = json.load(document)


def saveItemObj():
  global itemObj
  with open('inventoryProject/projectGalleryData01.json', 'w') as document:
    json.dump(itemObj, document)


def saveUserData():
  global itemObj, userData
  for item in itemObj:
    userLoader(item)
  with open('inventoryProject/projectGalleryUsernames01.json', 'w') as document:
    json.dump(userData, document)


def defaultUserData():
  defaultUser = {
    "Poopoo": {
      "password": "1234", 
      "wallet": 246.0, 
      "history": ["eternal pain", "Sold a painting at 2020-11-06 17:02:12.651475", "Sold a painting at 2020-11-06 21:22:33.114185"], 
      "item": {
        "Tyler1": {
          "total": 8, 
          "time of purchase": ["Fri Nov  6 21:21:57 2020", "Fri Nov  6 21:22:07 2020"]
        }  
      }
    }
  }
  with open('inventoryProject/projectGalleryUsernames01.json', 'w') as document:
    json.dump(defaultUser, document)
  


itemObj = {
  "Juan" : {
    "total" : 10,
    "cost" : 700,
    "distribution date" : [2020,10,1,23,59,59],
    "label" : """
                                 |\\    /|
                              ___| \\,,/_/ 
                           ---__/ \\/    \\ 
                          __--/     (D)  \\ 
                          _ -/    (_      \\ 
                         // /       \\_ /  -\\ 
   __-------_____--___--/           / \\_ O o) 
  /                                 /   \\__/ 
 /                                 / 
||          )                   \\_/ 
||         /              _      /  | 
| |      /--______      ___\\    /\\  : 
| /   __-  - _/   ------    |  |   \\ \\ 
 |   -  -   /                | |     \\ ) 
 |  |   -  |                 | )     | | 
  | |    | |                 | |    | | 
  | |    < |                 | |   |_/ 
  < |    /__\\                <  \\ 
  /__\\                       /___\\ 
    """
  },
  "Metamorphosis" : {
    "total" : 5,
    "cost" : 120,
    "distribution date" : [2020,10,1,23,59,59],
    "label" : """
.78,M$$$M8$$7?MMMM:..:,.8 D.M7:...NO:~, :,::O,=8~I.I,,.,:::::,+O~7ZDN8I=        
.IND~Z?I8M,,I~?.~.,.:..:+.MZI.=DD8888888..O . +, .O7MMMMI:::,:::8ZI=:,:,        
.Z~N.M$MZ7$7$$Z~,.,..= ,. .,+OOOO=O88OOOOOONMMM8=:~I~::,::,:::,=MD:,:,:7        
,~,.=ZZN?777I$7..I ...:,..$~7I,$7..:+OIOOZOZ:ZMNMOMM777$I$,:,,,ZNN==:7I$..      
 .. ,778+$DZNMM:?,I=,,~: $   ~.=:77:+,,,I++~I+Z~=77M87$O77~7~........,,,.       
.~?MM$7$ZD$DZI=?.O..,==? ,ZDNMM.,M88NMOO,DM?,7?,.NO $.8:77.7=:,::,.:,::. .      
,,MMMO$ZM$DM7MMMMI...,.~NMMM$N ..ZMMMN8MMMMMMND?.DO.Z8ODM7.$= D:=NDO$77 .       
.8$7MMM?$78M7$MMMM$ .+:IMMMNZN. ~:DNN+.?NMMMMMM:MDZ 7.Z:$?II? . :. .. ...       
 II77$7ZZONMM8DZNZD.Z$,DNNDDM, .,,,D8:..~DNNNMMM$=7=O Z:$I.Z+.:$I      ..       
 7?7?778NZMMDZDMMMMMI8.D88MNMMMMMNMNMDMMMMMDDDMN?MZ.M+O?$$.7+7IN: .......       
.MM777IOMOMMZZOMMMM$7I7O8DDD:.:::D..,N+:8,N8DDDD+Z$D$.8+$7.8?D.:+.,,,=~: .      
        .             .88D8DDDONM=.  ,NMMMZ8D88D7.                              
       ..             .8888D..... .~..   ..8D88DD.                              
.MMMMMMMMMMM+MMMMMMMMM=D888D:.       .    ,D8D88::,:::~.   ......,  ...,        
.MMMMMMMMMMMM=M=DZDI+??78DDDM.    ,..   . NDD88+=I.,,:.Z:... $:?..    ,:.       
.MNIOMMMMMMMMI8Z~Z~~O=?ODOOOMM ...., .. .DDDDOO~=7~+?Z,+$,   ~.,,.   .+:..      
.N.  :MMMMN,:7O$Z=+7Z,..:D888DM. .  ..,.MM8O8OIN:?$8:,ZZ   ..MZ. +.. ,:, .      
 7 ...NNNO,, :,=:...Z. ,:DO88DMMMM.  MMMMM8OZI?,:=.,Z8?.,. ,MMM~, ~ .,::..      
  7$8INN8:$I7=.. ...O7.D7M7O8OD8M?8MNZOMMMODD .?II:+?I.I?M. :MM=Z?: ,,=,.       
.I. ..DO8MMM8:7N~7,$MMDM=M$88DDND::+=:+ONDODOO+.,:.,::==$D7IOOOO8.~.,,:~..      
,8.  88INMMMM:DMMO:MMMMMMO8ONZ+=+,:,,,.$I78ONM, .,, ,8. .8$ZZOZZD.::,,:,..      
 ZOZ8DZNMNMM=.+MMMDNMMMM7OO8ZZND. ,  , .~77MNOZ,. .+?=?,ZZZOD$OZ$  .,,:,..      
.O?$7ZIMMN8D::.N8NMMNNMMMMMMMDI....,. , $II8ZZZ..,,:DMD8O7$Z$Z$$$..$,:::.       
 $Z++ZZODO8$, .~$ZDM$$777M8ZZ7?..~,,,,..7778Z$877+:,7Z88$=:$+:Z87I .,,:,.       
.7$I??$=$MNMMMNMM77IDZI7ZOO887ID. .....?$I7OOOO77?I7$7$$78,=Z. 8N7~.,::,.       
.?I?I?+=:$,N:=,NMM?77$7$788D~?77=.I$$$,$77I$DOO$I?I=$77$ZO... .,D$$ZNMMM.       
.??+=~+=7.,+Z.=8$7I+77IIN$ON.7I77=7I77O77++.Z$OZ7ZI=MMMDOIZ7, O?$IZ:O:=$..      
.??~+?I=.   .:, ....I7I7OOIZ.,Z.III7I7$7$:,,7ZO7$7I+MNZMOO+D7,:,:+Z8Z::=.       
 ==II:,~           .77I778II~, ,O:$77?~$. .OD7O87?IIMZMMZ$?O$=  .,D$$NM?..      
.~=++~~~.          .$77O$OII7I:.:,8:II.:.8777O7$7I77MO78N$7$$   ..M78NM8        
.~~I=~+.,=        :.8O$$DD7777I7OO?.:,:77I77Z$D$$I7ZMN$$NIZ7Z::+?::NNMNM..      
,=:.,~,,~+:M~.......O$Z$$$$$$$$Z$$D:+~$$$Z$$O77O777+MZ7O$7$$$.Z++,.DNMNN .      
.==.~..==. ..      ,7O$OZ$$ZZ$$$$$$D+7Z$ZZ$$OOO$$7Z?7$~..O$$Z::=7~ M8MMM .      
.~:~:.::~~.  .. ..,~7OZZ7I88$Z$ZZ7 I.~ $$Z$Z77ON$III7Z.  .$78.?:,,.NNMMM.       
..8.$8+,:~.,~$7I?8=Z7Z7$ZZ8Z$Z7ZOZ,,+.~,Z7$$ODZ$$7I7I~..  D$8. .. :$NNNM.       
.=O:Z~::.=.:~~==+D=77$$Z?I777IIZZ..~ ::.ZI7ZIIM$$I?87 $IZ?.M87I...78NNDN.       
.,7=II.,,,~:~::+=7M777$7$$$OII7I7: ,7~I.?I7Z$7MI$Z77N..:,..MZ$IIIII88DD8 .      
 .:.,::... ,.~:7M$M8O7Z$??I$ZII77$I$$$.,7I7I??MO7I?IM .IOO.M$$77III88888..      
.=:,.:,.:: :+===~DO7$O7Z$??77I7777IIII ,I$ZO7?MZ$Z$IZ,....:M$O7II7O88888.       
 ~:,,,,:,.,+?MMNZMOI$$7$8O8777I777,77I7.$$77M~?OZ777$M.  .NM888$77888888..      
.,....,. .,?IMMZM$=77$$8?OZ$77I7I7,I7$7.III7?+IZ?Z7$7N?..$MMM8888O888DD8 .      
.,:,,..,..?7?M8M7$7I7I?I??7?$$7??I+IIII+7I7OI?+II$777=MII?7DMDDD8DDDDDDD..      
..,:, ,.:$?7MMM$$7II7$I+ZIO$$Z$7IIIIII7I7I7$I7ZI?$$77$M7778DMMMMNDDDDD88..      
...,..,.,7++Z~I7I~II7$?I+7?DI$$IIO7IIIII7$$I7Z7ID$IZ77NMZ88DMMMMMMMMMMMN .      
.......:+++O$8MMZ$I7$$7?IMZOZNMMMNMMMMMMMMMDMDZ$NI7$7I+MM88MNMMMNNMMMMMM..      
 .,....7MMM7:~...$I$7$$$OMI7I7$N7$7I8NO7OZZ$$I$$ON7$77$MMM$MNNMMM88DDNMM .      
 ..:~~~NNI=~:,,:,7$Z$Z$DZZI$7II$Z$D$IZZ7OZ$$77$7Z7O7Z7OZMMMNMDMMM88888DD.. 
    """
  },
  "Alpha Male" : {
    "total" : 0,
    "cost" : 135,
    "distribution date" : [2020,10,1,23,59,59],
    "label" : """                                                                                
                                 M+::~+M=:~~~~NZM= ,MZDM                        
                              O~~~~D7~~~~~~:?~:M:~I7~~~~.                       
                            :~~~:MM:~,~~~,DMMM:.$7~~~++~~:N                     
                       ZOOZM:~~NOOON.~~~~MMMZIO~~~~DMMM?:~~M                    
                      NOOOOOZ7MOOOODI=~?77~~~~~~~~:~7$MMI:~:MNZZON              
                      8OOO888DOOOOODI~~+~~~~~~~~~~.~~~+ZMI~~.M888Z              
                      8OOO8888ZOOO8MI.:~:::::~~~~~~.~~~~?MI~~~D88Z              
                      NOOZD8888OOD8I,$..............N...~.M7~,M888              
                      M888M8N8N88D$IZ..7...,...............$:~.ND               
                      =IMZO8MOZNII7.7+:,...8......:..D..+..?I..DO               
      8              NNZOONIOZOZI:~OI~~=NNDN~~~~~~?~:D?,.7..M:..N               
      M=             NOOOM7I?ZOOD::Z?~~+IM?N~~~~~~7~~8++N~D~I7..?8N             
       7~$          NZOOOII77NOOOM.III?M+:+M~~~::~?~:M,IM7,,:$:~.N8N            
        7~Z          .IZ7:II~ZOZZM$8MMMMDO+87~7M~~~~~?...?IN78:~,,ND            
         I~M         ~+.7I$7~~7II~MZ=Z8MMMMMIIZM+::IZDMMMMMOIDI~~...            
          7:$       NMMMZNI+~~~~~~8,O=7$$$I?DM,M??IIMMZ7$,7MNM7~~O..N           
          I7~N      .+OIIDI:~~~~~:I,M=$77$=$,,,M7M?$=$8$=:,,NM7::NDOON          
           M7~D    M:III77I~I~~:~,+,N=$77$~?,,,ZI8.N+7D$=+,,$MI~:8              
            M7:O  ~~7DI?$IO~7:::~,:,.=+$7~$.,,,..,,N=$$I~.,,,MI~~8              
             D7~7$:78I=O$8M~77~:~,~,,O===+.,,,,,,,,,~$$=D,,,.MI::N              
              87~ZZ?I8~IIIMI8I:+~:~,,,,..,,,,,,,,,,,:8IN,,,,,OI::               
               $7~++?I~7IN8I$77D~~+,,,,,,,,,,,,,,,.,,,,,,,,,,.IZ:               
                I7~:N~ZIIMIII7IO+~D,,,,,,,,,,,,,,,,,,,,,,,,,,.IZ87              
                 7$~~?IMMM7DIO7II~Z,,,,,,,,I,,,,,,,,,,,,,,,,,D:I?:              
                 777:,   O+??IN7NI?N7=?=..,,.NO.,,,,,,,,,,,.MIDM7D,7            
                  MI~.Z $.O.O8?M78IM???+MMMMNDO$I+==+7OMDID8N?O :MM             
                   M==,==$,O.. ?IMOI???=7$$$77777O??=7I8IIIMM                   
                   D==~N~MZN...,.=?+..??=DO+IZZZIM+.?=DMIIIMO                   
                  $IN7$7DO?DM??O???M7+7O.MOZZZZZZ=7++I+~+=I7                    
                 7$7$NN.....MI7D8?+..==.$MI777IZ~.~ON7+~~D:                     
                       ?.....Z+DDDDDMN8ZOOZ?=M88~..?=NOI$IM                     
                       D?+..O88ND8888ZOOOOOZ8ZO8+..~II::~=D                     
                     7??M~=M$8 I8888ZZOOOOOMOOOD8..,M7M~~8::                    
                   M????7Z+MO.DD88OODOOOOOZ8OO8NN..DDDM?7NZOO                   
                  +????+Z8OZ8ZNONZOZZOOOOOZZOOO8D..MOOOD8DOOO                   
                 ?????$ZZZZZZZ8DOI.IMOZ8OODOOOZ88M.~ZOZMI78D                    
                Z????+ M8OZZZM7$=7NIM...,8MNMMMMD=,.I??I7N~:M                   
                M???+     MZZD7~MZ$~~MDIO:M~MZ?DMMN.?D7?I?$~.8                  
                 +??M       M7.I.NO8NN7?I~:M..,~IN?M.?=MN:....$                 
                 Z??        ?=~ODZOOOD$ZMZNM=O8,,O+N?..........                 
                  ?M           DI~=~+DMMMD8NN8OM=777 .........M                 
                                 O?+=$8MMNDO$I77DM++ +.......$                  
                                  88888DD888D    +?+  8.....Z                   
                                  N88OOD88OOM    M??D  ....M                    
                                   88OON88OZ      ??D  ~:=                      
                                    7?,~+=:N      ++$                           
                                    M?..+.         $+                           
                                     7,.Z M        M$                           
                                     OD78=M                                     
                                .:=IZDMMMMDZ7+:                                                                               
    """
  },
  "Asep" : {
    "total" : 20,
    "cost" : 75,
    "distribution date" : [2020,10,1,23,59,59],
    "label":"""

77777777,7III 77777777777?.7I7I777777I7777I::::~~::~::::::,::~~~::777I+:I7?~7777
77777777+~?77II777777777?,..,.,,.,,,,...,::~~:~::~:~:~:~:~,:~::~::~+I==+?+77777?
77777777I..+??7I77?=:,:,,,,,:~~:::...,,,~::::::::::~::::::::~~:~:::~:I7I?=7777?~
77777777?......:~::::~:~~?+=7I+~...:.::::::::::::::::::::::~:,~::::~::?7?:7777=?
77777777+....:::~:~~:~=?~77=:....,,,::::::::~~:::::::::~=,:~:~:::~~:~::7+=7777?7
77777777,...:::~:~:~+?:?I::.....,,::::::::~~~~~:::~::~:=,~::?:::::~:~~.:~I7777::
77777777..:::~~::~:?==7~:.....:.,,::~:::~:~::::::~::?I.::~:?I~:::::~~:~7777I7I77
7777777~.::::::::=?~+=:.....,:.:,,,:=~,:~=IIII+==~:.......?7=::::::::~?77I~7I=?7
777777=.:::::::~=I:?=.......:II??=...:,??????+????????+~,?77~.:~::~:~:77?+?:??==
777777.:::::::~~7~7=.....+77II?I,,+?=??+~??+????????????7777=.,:::~:~:7~I=I?7?+I
7777I,~~::::::=I~I~,..,I7IIII??:=??~?????+????????????+I?+?77+??~:~:~:I?I=+77~77
II7I.~:~::~::=?~I:..=II??I???==:??I,?????????I+?=?????:????77=~~:~+?:,+I?I.77I77
7II+~:~:~:~:=?=I:.:I??I?????+?=+???:?????????????I++?:?????I7=I?=:::::I~+?+I:7?=
I??,:::::::~7~I:==????????I?=+=~??I=???????????????+++?????I++?I?I~:::777=I~77~I
?7:~~:::~~=7:7=I+???I?I????:?==:??I=?????+???????????+????+?+?++?77+,,7777?777:+
7?::::::~+?:+I???????????????++,???~???????????????++?????:+???++?I77+?777777777
?~~::~:~~7~~I????????????????++.???:??????????+=?+??????++,?++?+++7?I7~777=++777
?:::~::~7~?I+???????????+??????.+??~????????????+?+?????+++??++??+?77I7,I7+I=777
 :~::::=7+??+??????????????+?+?:=??+???????+????+=++???++=??++++?++7III7+?+II==?
.:,::::I???+?????????????????~??,??+??????????+??????++++++++?++++??77+II++II+II
.:,,::=+???????????????+++???+=?:?+???+++????????+?+++++++++++++++?7?7I+I+~=I7I?
.::.::+?=?+I????????I++?+?????++I~?+????+++??+??++I+++++++?+++?+++?7I7I++I+:~7~+
.::::=+~I??I??????+?I??=????++?~++=+++?++++??++?++7+++++++?+++:+++III++I++?=:~I7
,:~:++.+??I??????++?I=??++++??+?~+I=+?+?+++++?+I++I?=+++++?++?=~++++++++?=?+++~:
:::=::=I+II?+?+??+?I+=+?+++++++++=~I~++++++++++I++77:+++??7++++~~++++++=+=+?,=?I
~,??,I???7I????+I+I7+?=I++++++++=?+~I=+++++++??7+=77=,+++++++~++~=++=++++=+=?,+=
:?+::II~+77???+?7?77=+~7+?++++++~++++~I=+++?I7?7++?I?.++++++=+,++,=+=+++=+==+?.,
=~::~?7I+II++??7I+7I~++7II?7++++~=+I+++==,~=+++++~:?7~,===+=+:+,=~~====++==+=,I7
=:::~+777+++++++??7?,+?I??++++++~~+??+++=++=:,,~+=,+I~I:~:====,:+~.=====+====~~?
:~~~:II7I77=+++++?I?,+++++++++++~?~+=+++=+++++++++.+?:II.:=+=+,=++.:=~==+==~+~.:
~::~:~77++~=++++++??,=++++++++++~I?==+++++=+++===+I,::III:.=+==~:I~.~:==+==~==..
++:,,+=?I+++:+++++?+,:=++++++=~+~I?,+=++=++==+=~=,I==~I=~++:=+~+~II,,:=====:~+:=
,+:..++=7=+++~+=++++,:+++++++~~==+I?:~++=++=+==:~~I++=7II7?~::=I:7II:~==+==:,=.:
:::..+++=7++++++++++.:==+++++~:=~+7I,.====+=+=+:,II++7 7777I=~7I=I?II,~====,.+..
+,:.,++++==+++++++==.,+~==+++,:~:IIII.~=+======:II?+?7777777=+7+777II,:====:.+..
....==++:=?====++==+.,=,=+=+=..~7?77I=,+=====,=~77I+?77?+==?I7777777I+:==~+~,,..
....==++~++~=+++=~==..=,==:+,~~77 777I======,I~I777==,.........,~I777::~~:=~.~:,
I..,:+=+===+:+==+:==,.=,==.:=:?I77I77II~=+=:I7??77?~=+=.......,~:.,I7.=+~=~:,~=~
I?,=:++=+===+,=++==+:.,==,.:II7?7I I77I~==.I77I= II77~..::~~~?,~.7+7I.=.~:~~~===
?+=.==+==~===+======~..==.+7+7+.....:?I?I~777I77I77I7+??+?I?77??I7+7I,,=~:~~=~,~
I~..===~=+=====+=====..I~77I~.....:~I77II77IIIIIIIIII?+II7I7IIIII7I??=:~~~=~?~..
:...===~==~=+========:.II7?......==~.77I7IIIIIIIIIII7I??II?II?777II77.~~~~~~7~,.
,=,.+=~====~========~=,I7,.:..,:~+,I=I?IIIIIIIII?IIII?IIIIIIIIIIII777,~~~~~+7~::
?7==+=:=,============:=?,~~,:++I?IIIIIIIIIIIII??IIIIIIIIII7I777?I777?:~~~~~?7~,.
II~==~:~.==+=========~::.I?I+I77IIII7IIII7I?III+IIIII777777777777777~:~~~~~I7~,.
7?===,::.===========++~:~?77??I777IIII7IIIIIIII7I777777777777777777?~~~=~I+7I:,.
7+===.:..~====~===~=====~~~?77I7777II7777777777?+==?777777777777777.~~~++I+7I:,~
77:~.....:===~~~~====~I~+~+I7I777II7777777777~,.....:,777777777777.:~:==+?I7I,=?
I7=+7,....~==~=,~==+I?II=+~+777777777777777I+:.==+=??+~7777777777.:~=~=?II7II,=I
7I+I77:...~=~~=~,==~+I+7I=+=+7777I777777777++I??+?IIIIII777777 =:=.=I??7777I?:+7
77?~77II.,=~~~:=.:~~~~+=77I?~~+II?+ 7777777:+???I7II?7I?7777I7.+I7?=?I?7I77I~~+7
77+~7777:,~~~~::.~:~:~~~~=?I+:~~+7I77777777+?IIIIIIIII+7777+?,.,:~==,,+III?=~++7
II77777I?:~~~~:..~,~,:~~~~:==~,.:??777777777??I?I77IIII77+...,..,,~,..~~~==~~:=I
777777I??~~~~~:..~.:,..=+~:=~~,..,=:?777777777II?77I7I7+?I...~.,:,~.::.~~::::~~=
777 77I=+::~~~:..~.,:,::~==~~+::,,:~:...~?I7777I77777I.?I7I....,::~::~,::::::~~=
+7?77I==~::~~~,.:~..~~=++=+I7I?,=,:=~~...,II+~,:?,...,I777?7III~:~,:::~?,:::::~:
.:77II,,.~.:~~.,~:..:~+I77777II:::?I7~~...+IIIII?I~=II7777?77I~~:=,~:~?~7,::::::
..:II=~.,:,~~.:~:~:,~7+I7777I?=~,~~~+~:...~II7I7I7?=::::~=~=~=,::=:::=?I+,,,,:::
...,++.,:,:~~~?777I~,=I7I7II??~:.~,.,:....+I77777I:??=~~~~==++~~:~~:~?~?:=?,,.,:
    """
  },
  "Tyler1" : {
    "total" : 7,
    "cost" : 10,
    "distribution date" : [2020,10,1,23,59,59],
    "label" : """

                                  7777777                                       
                             77~~~===~~~~:::=77                                 
                           7~=~=======~~~~~::::                                 
                         7~~========+==~~~~~~::::7                              
                        ==+=+==+==+=====~~~~:~~~:::7                            
                      7~=++++++++++=+==~=~~~~:~~:~::7                           
                    7I~=+++++++?+++=======~~~~~~~:::::77                        
                  7I~=+++??????????++=========~~~~~~~::=                        
                 7=+=+++???????I????+++++=======~~~~:::::77                     
                7=++++++?????????????++++==+++===~~~::::::?                     
                =++++++??????????????+++++++++===~~::::::::7                    
                ++++++++????????++??+++++++=====~~~::::::::,                    
                =++++++++++??++++??++++++++====~~~::::::::::                    
                =+++++++++++++?+?+?+???++++====~~~~:::::::::                    
                ~=+++++++?????????????++++++====~~:::::::::,                    
                7=++++++++????????????????+++===~~~::::::::7                    
                 =++++???????????????????+++===~~~~~~::::::                     
                 ?=++?+????????????++?+++++====~~==~~~~:::,                     
                 7=+======+++++++==++++====~~~~::::::,::::7                     
                +?=====~~:::::::~~~+++=~~:::,,,,,,::::,:::~:77                  
                +~===~~::~~:,,,::~~+++=~:::,,,,,,,,,,::::::::7                  
                ?++=~~:::=:,,,:::~=???+=:,,,,,,,,,:,,,,,:::::7                  
              77+?+++=~~=+::::~~~=+???+=~,:,,::,:::,,,,,:::::7                  
              77+?+++++=====~~:~++???I++~:::::~:::::,,:::::::7                  
                ??++???++++=+=+???????+=~:::~~~~:::::::::::,:7                  
                ??++????????+?????????+=~:::~~~=====~~~::::::7                  
                7?+++?????????????????+=~~~:~~=======~~::::::7                  
                7I++??????????????????+=~::::~======~~::::::I7                  
                 7?++??????????+????I?+=~:~~:~=====~~~:::::                     
                 7+++?????????+???????+=~~~=~~=====~~:::::7                     
                 7+++????????+?+++++++=~:::~::====~~~:::::7                     
                  7++???????????=~:==~~~,,,,,::~==~~::::::7                     
                  7++++??????????+++=:::,,,,:::~~~~~::::::7                     
                  7=++++??????????++=~~~:::::~~~~~::::::::                      
                  7+=++++++??+???+++==++=~~~~~=~=~:::::::I                      
                  77==+++++??++?+======~:::~~~~~~~:::::::?                      
                    ===+++++=:::::~~::::::,,,,,:~::::::::I                      
                    =====++===+++++++======~~~:::::::::::7                      
                  77=+===========++=======~::::::::::::,:7                      
                77=+=+==+===~~~~~~~~~~~~~::::::::::::::,,:7                     
            777?++++=+++=+=======~=~::,,,,,,,,,:,::,:,,,:,:::~77                
         77+++????++=++++====+++====~~~~:::::::::::::,,:,:::::::::7             
        ?+?????????++++++++=======~~~~~~::~:::::,::,,:,::::::::::~~~:7          
       +???????????+++++++++~=~=~~~~~~~~:::::::::,,,:::::::::~~:~~~~~::         
   77+++???????????+++++++++++~=~~~~~::~~::::::,,,:::::::::::~~~~~~~~~:::77     
  77=++???????????++++++++++++==~~~~~~~~~::::,,,:::::::::::::~~~~==~~~~~:::7    
  7=====+??????????+++++++++++++==~~:::::::::::::::::::::::::~~~~====~~~~~~~7   
  7++=+==++????????+++++++++++++====~~::::::::::::::::::::::~~~=============7   
  7++++++=+++??????++++++++++++++====~~~~~~~~~~~~::::::::::~~~=~~~~~~=======7   
  7++++++++++++++++++++++++++++++++=======~~~~==~~~~:~~::~~~~~~~~~~~~===+++=7   
  7++++??????+++++=====++++++++++++++========+===~~~=~~~~~~~~~~======~~=====7   
  7+??????????+++++++++=++++++?++++=======++++++========~===================7   
  7??????????????+?+++++++=+=+++++=======++++??+++++==========+========~====7   
  7?????????????????+++++++++===+=======++????++++++=+========+=+==+====~===7  
    """
  },
  "Kanye West" : {
    "total" : 35,
    "cost" : 20,
    "distribution date" : [2020,10,1,23,59,59],
    "label" : """
$NN?$DZ?DMMMMMMMM$?=~~~~~~===============ZNNMMMMMMMMM8?=======================++
N$DDMM8NDMMMMMMMM$?=~~~~~~~===========Z8MNMNNMMMMNMMMMMMM?======================
N88ZMD8NDMMMMMMMM$=~~~~~~~~=========ZDNNNDNNMMMMMMMMNMMMMNM+====================
NO?ZN?~$8$MMMMMMMO~~~~~~~~~~======+ODDDNDNDNNNNNNMMMMMMNMMMMN=~~=~==============
OO$7M?=7?IMMMMMMMN=~~~~~~~~~=====8DNDDNNNDND8NNNMMMNMMMMNMNNNM=~=~~~============
8NNDMDNN8$MMMMMMMM+~~~~~~~~~====NMDDO$Z777777$ZOD8OODNDDDNNNNNM=~~~~~~==========
OZOD8NNDODMMMMMMMMI~~~~~~~~~~==+ND8$7II??IIIII77$$$ZZOO888DNNNMM~~~~~~~~========
DZD$I7DD~~DMMMMMMMI~~~~~~~~~~==DDDO7I?????I???II7$$$$ZOOOO8DDNMM7~~~~~~~~=======
$8DN7$ON==ZMMMMMMM$~~~~~~~~~~=I888$I?++++++?????I7$7$$OOOOODDDNMM~~~~~~~~~======
NNDDNMNN8DDMMMMMMMO~~~~~~~~~~=D8OO7I??++==+++?+II777$$ZOOOODNDD8M~~~~~~~~~~~~===
Z8D?DNN8NDNMMMMMMMD~~~~~~~~~~=DO$ZII?+++++?++++?I777$$ZOO888D88DN~~~~~~~~~~~~~==
ZO+=7NO?ID8MMMMMMMM~~~~~~~~~~~8Z$I????+++++++I???II7$$ZZOO8OODODD=~~~~~~~~~~~~~=
ODD?NNN+?DOMMMMMMMM=~~~~~~~~~=DO7??I?++===+=+??I+?I77$ZZOO88OODDN~~~~~~~~~~~~~~~
DDDDMNNDND8NMMMMMMM+~~~~~~~~~~Z8I??I?+++++++?+?I+I7ZO88NDO888O8ND~~~~~~~~~~~~~~~
N$+?8N?O8D$NMMMMMMM?~~~~~~~~=7~DII?I8D8DNNNO$??7788DNNNNNMM88OO888O~~~~~~~~~~~~~
$~:+D?:~D$:=MMMMMMM$~~~~~~~~O??$I?I87I7ONDNZI+=IO888DZMMNDDD8OOOZ$8O~~~~~~~~~~~~
N$ZDDNID8Z~=NN8=?Z=O~~~~~~~~Z?~=IIIIODIZN88O$?=7ZD8Z7$O8ODDDOOOZO$OD~~~~~~~~~~~~
8DDDNNNNNDODDNN=?I:Z~~~~~~~~??~III?I????IZ7I?+?7O88OZZOOOO8OO88N8Z$7~~~~~~~~~~~~
I~+D87ZDNIOZMMMMMMMN~~~~~~~~~+I7I??++++=++=++??IOOOZ$Z$$$$ZO8O8$D8O~~~~~~~~~~~~~
7=+D+?ONZ=~DNMMMMMMN=~~~~~~~~II$II?+==+++=+++??7O88OZ$Z$7$ZO88O8DO7:::~~~~~~~~~~
DNDD88NNNIOZNMMMMMMN?~~~~~~~~~IIII++=++++++??+IIZ88DO$ZZZZZO88OZZO::::::~~~~~~~~
NDDD7MMNNNDDNMMD8MDN7~~~~~~~~~=+?I?++++++I?++=?I$OZOD8$$ZZOOO8O$7:::::::~~~~~~~~
=DD7:ZNDNNDI~NNN8MD8O~~~~~~~~~~?????+++?7+I8DI7ZDDO8OZI$ZZO888??:::::::::~~~~~~~
+OD8:ZNDN8=::8DDNO=::~~~~~~~~~~~~~I????I+==++I$?$ZOOZZZ$ZO8O88:::::::::::~~~~~~~
NDD88MNND8~::Z8NM8$+,:~~~~~~~~~~~~I???I??+???7$I$OOOOO8O$OOO8~::::::::::::~~~~~~
8DDDDNN8887::7ZMD8N88I~~~~~~~~~~~~=???ZIIII?7$7Z88D88D8OOZ888:::::::::::::~~~~~~
DDDDDOD8888+:IZND?I88Z~~~~~~~~~~~~~I??778$OZZOO888DDD88O$888::::::::::::::~~~~~~
DDD8~I?88888=?$888DI$I=~~~~~~~~~~~~~7I?I????I?I$ZOOOOO8D88D$:::::::::::::::~~~~~
DD?:~+~I8888ZI?I=~~?87=~~~~~~~~~~~~~=7III+???7$$$ZOOO8DDDDZ$D::::::::::::::~~~~~
87::==~=I888O?=?=?+:~O+~~~~~~~~===~~~?III?I?I7I$ZZOOO88D8OOI~M~::::::::::~~~~~~~
88I:=~~=~Z88OO77$~+?=~I~~~~~~~~====~=I?III???I777$ZZO8D88O$~~MN:::::::::~~~~~~~~
88O=~~==:=88O+I?D8~=?:7~~~~~~~~====88=??III??I777$Z8DD88O?=~7MNN::::::::~~~~~~~~
88OO~~==:~I8O+78$78:=~:~~~~~~~=DNNNN7,$???777$ZZZ8DDD88I===+MNNNNN::::::~~~~~~~~
8OO8Z~+=::=88+I$7::=~?:~~~~ONNNNNNND:,:+????II$8OO8O8?====+MMNNNMMMMO:::~~~~~~~~
888OO$+=:~~+8~=+~,,O:=?INNNNNNNNNNNN:,,:I????7$$$ZO~~~====8MMMNNMMMMMMMD:~~~~~~~
8O88O87=:~~:7:,~~,ZNNNNNNNNNNNNNNNNN:,,,,N?I7777?:::~~~==ZMMMMNMMMMMMMMMMMN~~~~~
=8O8O88+~~::~=?NNNNNNNNNNNNNNNNNNNNM:,,,,,$$I7:,,:::~~==7NMMMMMMMMMMMMMMMMMMMD~~
:=88O8DO~~:?NNNNNNNNNNNNNNNNNNNNNNNN,,,,,,I:~::::::~~==?NNMMMMMMMMMMMMMMMMMMMMMM
::?8O8D8I8NNNNNNNNNNNNNNNNNNNNNNNNN?,,,,$$7?=D8:::~~~~=INMMMMMMMMMMMMMMMMMMMMMMM
~::I88N8NMMMNNNNNNNNNNNNNNNNNNNNNNM,,,O7$78NN$78:~~~~=IMNMMMMMMMMMMMMMMMMMMMMMMM
::::$8D8MMNNNNNNNNNNNNNNNNNNNNNNNNM:,$+:$7ODND$ON7~~~+$NMMMMMMMMMMMMMMMMMMMMMMMM
~:::~ODNNNNNNNNNNNNNNNNNNNNNNNNNNNN~~:::7$8DDD8DO?=~~+NNMMMMMMMMMMMMMMMMMMMMMMMM
~:~::=DNNNNNNNNNNNNNNNNNNNNNNNNNNMN,~::~?$8DD8M$=~~:~NNMMMMMNMMMMMMMMMMMMMMMMMMM
~:~:::DNNNNNNNNNNNNNNNNNNNNNNNNNNMD,:::O?+?DNND=~:::7NNMMMNNMNNMMMMMMMMMMMMMMMMM
+:~::~NNDNNNNNNNNNNNNNNNNNNNNNNNNM7,::,O8M$IDN7~~::+NNNMNNNNNNNNMNMMMMMNMNMNMMMM
8~~~::NNNNNNNNNNNNNNNNNNNNNNNNNNNM:,:,DZMM=8DN+:::~8NNMMNNNNNNNNNMMMMMNNNNNNNMMM
8O=~:=NNNNNNNNNNNNNNNNNNNNNNNNNNMN,,,D7NM$ZOD8=:,:7NNNMNNNNNNNNNNNNNMNNNNNNNNNMM
88Z=~NNNNNNNNNNNNNNNNNNNNNNNNNNNMD,,D$DMD=8ODD7:,~DNNNNNNMNNNNNNMMMMMNMNNNNNNNNN
8887:NNNDMNNNNNNNNNNNNNDNNNNNNNNM8,$O$DZ?D$ODD$=,INNNNI7ZDNNNNMNMNMMMMNNNNNNNNNN
8888ONNNNMNNNNNNNNNNNDNNNNNNNNNNM7,8$+7ZOD78888=:NNNMN+++?NNNNNNNMMMMNNNNNNNNMNM
    """
  },
  "Honi" : {
    "total" : 20,
    "cost" : 20,
    "distribution date" : [2020, 11, 7, 12, 59, 59],
    "label" : """
    O8DNDMODDDZIIDMN8OZ$$I?+====?+I7$ZOOOOO$$7I?++.~==..?$OOZ$77?+?+.~===..=+7??.,=,=?++?.,,?+?:+++++++Z
ZO88DNN8ZDD7IDMDO$7I?=~:::::~=,,?I$$ZZ77II?+=+.++?+.:$ZNZZ$7???++=++===++,??..OZ.?+++.N,+++++++++++Z
ZZZO88DDNODM7DNDO$I+=~~:::,,:~=+:+I7?I?I?+++==+????+:IZONZZ$Z???++.~=+++++?+. ?:.?+=.+.,++++$++++++Z
ZZZZOO8D8NDDMND8Z7I?=~:::::::~~=+?=?,I+?++++=++??,+++?ZZDDZZ$Z??+~.==+++7++,Z.M.M,++.O+,.+++.++++++Z
ZZZZZOO888NM8MDDZ7??+~:~:~~~~~==++?+??~:===+?????.+.+.IOONDZZ$7++...,=++~=+.8,,.O.=.N$~,:===:++++++Z
$$ZZZZZO88DDM88OZI??++=~,.===+=++?+????=~?+~IIIIII??.=7O8DM8ZZZ+++=~.~=+,===,...,==, .7,.~===++++++Z
7777Z$$ZOO88DNNO$77II+=:...~=+???IIIII7II+=~~=$7$$$7.7ZONDDM8ZZZ?+=,.~==~~~.IDO77 ~~~.,,~~~~~?+++++Z
I7$$ZZZZZZO888D8$7II?+=.:=:.==??7$$7$ZO$Z$I~=:+I8OOZZZO88N8DM8ZZ$+=,,~~=~~:.MNI7O.:::.8,:::~.?==+++Z
N$ZZZZZZ$$ZZZZZO$II?I+,.===~,.=I7ZZZODDD8+$==?==IM8888888DN88M8Z$?+:~~~=,,,.$D,,7.,,,.8.,::::++=+++Z
78ZZZZZ$$$$$$$$$$7????=.+++++=??$ZO8DDMDO=$==??~+7D8888888DD88MO$I,~~:~~,,...:O.. ....8.,,:,.==++++Z
=$Z$$$$$$$7IIIIII7?+????++:+,+.I$O88DNN7~~7==??+~I8DND88888NDD8D$?.~.,:.,,...~..7,......,,,,,===+++Z
=+NZZ$$$$77I?++++????III?+.=.+.I$+ZNDN=~~=I~~?O?~?$:~~7DND8DN888OI~=:~.~,,..ZM=.M.........,,.===+++Z
++?8Z$$777I+==~===+??IIII??++?:7=O,DZ:~~=O?++I7I??7D::::~~IDNN88O$7?=:~=....D=M...........,,====+++$
===DZ$$7II?+=~~~~~=?II777III7777I7~+~,:::$???7O$77$Z=O:::~~:~?NNOZ$$I=~~$....,...........,,+~===+++$
=~~~N$II++==~~::~~=?II7$$$$$$$$7I7=7:,+IZZZ$$OZOZOZ+====?$::I~~~?8O$7I?~:I.. .~O$........,...~~===+Z
~~~:87I?=:~~~:::~==+II7$$$$$$Z$?=~::$:ZZZZ$,:::::=:+,::~~~:Z,:::::+OZ$I+:::.....N. .....,..~=.=====$
:::~:ZI+~~,....:~==+I$7$Z$7==I7:::~N+=+~::::::::::8,7::::::,:~:~:::,=O$I+::,+...........+.====.====Z
:::~:$I+~:.,::,..=+?I$ZZZO$7O+:::Z~Z:::::::::::::::Z,7::::::O:I~:::::I7ZI?:,,,I.......:~~===~=~====Z
::~~:I7?~,.::::~~=+?I$Z$$77O~~::$~:::::::::::::::::~,,~~:::::,:~::::::7?Z7?~::::,=OZ?::~==~,=~~~~==$
~~~~~~87+~.~~:~~==?II7Z77OZ~:::Z:::::::::::::::::::~Z::,+:::::?,:::~~~~7$8$?=::=:::~~~~===~,~.~.===$
~~====$O7?~~~.~.=.?I7$ODD$~~::::::~:::::::::::::::::::::::::::::$=+====~+IO$7I::~:~~~~======~~,~===$
==++??OD8Z7?+.===.?I7$OOO~=~::::::::,,::::::::::::::::::::::::~~=??+++,+=,NOO7I~:~~~~~====.~~~~~===$
+????IZM8ZO$I?+??II7$ZOO8~Z:::::::::~=~~::::::::::::::::::::~~~==O?++++==I,N=8$I?~~~~===~~.~~.~~~==$
IIIIINN8O88O$II???I$ZZO8+~Z~~~~~~~~~::=~~::::::::::::::::::~~~==O+++++=+=7,,=8D$$7=~~~~~~~.~:.~~~=~$
778MMMMOON8O$?.+=.I$ZOO87=Z~~~~~~=~~~~~I+:::::::::~::~::::~~~===+++++++++=~ZDO=DO$Z~~~~~~~:~~~~~~~~$
OOOZOO8ODD88ZI.,~.I$ZOOD88~~~~$,?=~=~~~~,=~:~:::~~~~=::::==:~===+?+$7+II?=:~N7,7MO$Z~~~~~~:~::~~~~~$
OZZOOOOON8D8O$:.+~7$ZOO8N7:=~=+,=++~=~+~=.~~~~~~~=~=:~~~==~~=~=+=Z:D8,I,::,..,.8DMO$$~~~:~~~~~~~~~~$
DOZO8888N8N88O$?II,$ZO88N::=++=+=+=+=+==~~~~==~~~~+:~~===~~~=~====7,,7.......=DDDDNZ$$?~~:~~~~~~~~~$
DDOOZ88O88D888Z?77$$OOO8D~==+=+++++=?+=+=$~I==~~~+:=~====~~=~===++$+:.........ZDDDND$$$?+I~:~::::~~$
OOD8OZ8888DD888OZZOOOO888?Z==++=?+=+?=++=O=:?==~=:=~~===~==~++~==~~,...........DDDDN8$77?+=7+::::~:$
D8OO8DM8888DDDD88O8OOOOOO8D=Z?+?=++?=++++Z+=:+~+~=~~=+=~~=~=+~~~=~:,............DDDDMZZ77+~~==I:~~~$
NNMMN8MN8D8DDDDD888OOOOOODD==~?++=?+++=++=:?~7=~=~~~+~~~+~==~~~~~~:,,.?0/??......8DDDNZ$$I+=:~=+O:~$
N?~=:?MMD888D8DD88OOOOOOO8I=+Z++=?+~:=?7?+:==:==~~~=~~~+=~=~=~~=~~:+?O0O%OOO?...,:MMDDDZ$7+I777++~~$
ODN=~,MMDD88DDDD88OOOOO8ON8~=+==+++=::$?=Z$~.:=:~:=~~~=~~=~==~~~~~::~MIM=NZ,D,,,,DNNNDNO$$?+$$?~I~~7
OOODM:ZMDDDDDD8D88OOOOOOOMD?~====,8M?:,,.,.?.,,::~:~==~~=====~~~~~::::,D7OMNMD$MMMN~~8DNZ$$++$+~,?I7
OOOO8N8DD8DDDDDDDD8OOOOOOM,~~:,,N,=:,.,.........::~~=~~=~~~=~~~~::::::~O,:,I+7Z+:::::=ZNMZ$7+?+~,NI7
OOOOOODND8DD8DDZDD8OOOOO887,~?:?................,=,+=~~~~~+~~~::::::::::,:~=$I,:::::::??NN$$?++=:+?N
OOOOOON+ZDDDDD++OD8OOOO888M=:,,,................,I:I:::::~,~::::::::::::::,:::::::::::::?MZ77+++=~OO
OOOOO8++IDDDD~~~ZNDOO8O888M?7,..... ........OOOO,D7,::::::7:.+:::::::::,,,,,:::::::,:,:M,ID$D?++?=,N
8OOOO~~~8NDD:..,:ND888O888ND7.............OOOOOO8ZZ,:::::::~:?:,::::,:,,,,,,,,,,,,,,=7,,+,$O$I++?==7
O88O,,,+:DDI:..=,MD8888888DMN8...........OOOO??MM7:,D:::::::::~:::,,,,,,,,,,,,,,,,,D,,,,,,:887+++I:$
888I,,D:ID8:,,,,:DDO8888888MN,..........OOONZNMM,,,Z,:::::::::,,,,,,,,,,,,,,,,,,,,8....,,?,:N$?+++?$
D8,,,,,:ODD,,,,,788OO88888MMMM8.........OO,MMM~,,N:,:::::::::,,:,,,,,,,,,,,,,,,,,,~.....,,,,IZ7?++?$
8~,..,:8DDD,,..,ODD8O8888D=~MMMMN7=,,~$MNMMN:,,N,,:::,,,,,,,,,,,,,,,,,,,,,,,.,,.,O......,,+,:8$?++?Z
M:,..,88D8D,...,Z8DDOO8887~::I:NMMMMMMNO::,87,,,,,,,,,,,,,,,,,,,,,,,,,,,......,D........,,,,,$$?++=O
D:,.,,D8D8N,...,I8D8OZOD87,,.??,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,......,,=N,........,,,.,+$+=+=Z
D:..,:8888N,...,?88NOZZ8OO~,..D:O,,,,,,,,,,,,,,,,,,,,,,,,,,,,..............,:8M..........,,I,~8I+==Z
O,..,~ZDD8D....,~888O$$Z8O,,...M:+,,,...,....,,,.,..................,......Z,N,..........,,:,=O$7++O
I,..:+Z8888,::::,M8DOZ$$ZZN,....7=::8:.......,..:$...,.,.....,.,,:~::+,.....7Z,........,.,,,,+O$$?+Z
~...:?O8888~~~~~:?88OZ$7$ZON,,,::?8,,,,................:Z.D.~..7M?,::,+.....NO........,,,,,,,$O$$I+Z
~,.,~I88888Z~~~~~:DD8Z$77$ZZI:~==~7+,,,...................,.......O?,?.......~.......,,.,,,,,ZO$77+Z
~::~=$888888:~~~~~O8DZ$$77$$N:~===?=,,,,,...........................?,?7,....8......,,,,,,,,,~O$$7?Z
:~~==Z888888$~~::::ZDO$$77$ZZ:~~~~~=7,,,,,...........................,.O,...,......,,,,,,,,,:=$$$$?Z
~~~===OO8888N~:::::~Z8$7777$$=:~~~:Z,,,,,,,,,,,........................,.......,...,+~,,,,,,7?$$$$IZ
$~~===+$OO88O,::,:::~ZZ$77777+:::::I,I.,,,,,,,.........................,,..........,=,=,,,,:=ZZ$$Z7Z
=N~~===+$OOO8+,,,,,::=8Z7777Z=~:::,:,,D,,,,,,,,,,,..............................,,,,.,.,,,::=ZZ$$O7O
=8O~~~~=+ZOZZ8,,,,,,,:~8788ND=~::::=~,,=,.,,,,,,..,,,...,,,,........,,,.,,,,,,,,,,,,,,,,,,:D7OZZZ8$8
==Z+~~~~=+8OZ8:,,,,,,,:::====::,::::7Z::,,,,,,,,,,...,,,,,,,,,,,.....,.,,,..,,,,,,,,,,,,,,,~Z8OZZDZO
===7::~:~~+DZN=:,,,,,...M......,,::$$Z==,:,,,,,,,,,.,,,,,,,,,,,,...,,,,,,,,,,.,,,,,,,,,,,:O?Z8OZO8O7
===~N:::,:~=7?Z=:.....7MM=.,88.,,::N$$O~::,,,,,,,,,.,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,,,,:~~$ZDOZ88Z7
==~~:O:,,.,:~~~+~,......NM+O$..,,:~O$$$8:,:8.,,,,,,,,,,,,,,.,,,,,,,...,,,,,,,,,,,,,,,,,,:+7ZONOO8D,7
~~:::~:,....,,,.?,....ONM.~?Z..,,:+7$$$Z8~?,M,,,,,,,,,,,~,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::I=$O88OO8I,7
:::,,,~,........,:.............,,:D7$$$$ZD7,,NI,,,,,,,,~.,.,,,,,,,,,,,,,,,,,,,,,,,,,,:::~$ZODOOOD,,7
:8:,,,,,:,........,............,,:N7$$$$$ODZ:7+,,,::,,,,,,7,,,,,,,,,,,,,,,,,,,,,,:,::::Z$ZO8OOOO=,:$
:~Z:,,,,.................Z7....,,:Z$$$Z$$$ON8Z:I+=:::,,,,,,.,,,,,,,,,,,,,,,,,,,,::::::$$ZZO8OOOZ:~~Z
==~O,.,........................,,I$$$$$O$$ZZNDZ7:D:$~::::,,,=,,,,,,,,,,,,,,,,:::::::~~7ZZOOOOZ8?++?O
DI=~Z,...................7?.....,DOZZZZZDOZ$ZDN8OZZ~ZZ::::::::,,,,,,,,,,,:::::::::::~$ZZOOOOO8II77I8
DD$=:7,.........................:NO8OOZZO88ZZZDD8O8O=::8~:::::::::::::::::::::::::~~OZZOOZZO8::+?7,I
DDDO=~?.....,............~~....,:NO8DOOOO88D8OO8DD888DZ:Z:Z=:::::::::::::::::::::~+8ZZOZOZOZ=+I7...I
DDDD?=~+....~..................,:MOO8888O888888OO88888888O7:~:N::::::::::::::::~~78OOZZZZOMNM7.....I
DDDNDI~:~.....,.............:,.,=NOO88D888888888OOO88888OOO8OOZ=::=$~::::::~~~~7ZZZZZZZZNDI,,,,...~Z
DDNNNDO~~:,.=.=..........M=.Z,,,I8N8888888888O888OOOO8OOOOOOOOOOOOZZZ7?+=?7??7OOOZZZZO8I~~::,,,:?+ZM
DDNNNNDN+~:,7.I............$,.,:ND8DND88888OOOOOOOOOOOOOOOOOOOOOOOZZZZ$ZZ$$I$$8ZZZZZ8MO~==~==+7DM8OD
DDNNNNNDO?=~::,,,,..,.....N..,:=NDNDDDND88OOOOOOOOZOOOOZZZZZOOOOOOZZ$.7$$7~I.ZOZZO8NO888MMMMM8O8OOOD
DDNNNNND8MI+~~::,,,,,,,.....,::NDDNNNDDDD88OOOOOZZ~$ZZZ$I.Z$ZZZZZZ$7.=$777:+.ZZODNN8888888888888OOOD
DDDDNDD8MNNI+=~~::::,.Z?MM.8,:=DDNNNNNDD8888OOOZZ$~$$$$?.I.7$$IZ$Z$$.,..~7.,778ZIINMDO88888888O8OOOD
OOOOO8OO8D8~D+=~~~~::,.?:..N8,$ODNNNNNDDD88OOOOOZ$:7=~7=.I.77?,~$$$=.II7$77:.=:++=+=OOOO8888888888OD
ZZZZZZOZZ$8~::$?++=~~,.8...$?,$ZDNNNNDDDDD88OOOOZ$=..=I+..?7$II,I$$$....OZ?.=?.++,.~=.:888888888888D
$$$$$$$7$$7Z::,..7I?=:.N..N.~7~88DNNNNDDDDDD888OOZ$,77777$ZZZZZ.$$ZZZO$====++=.++....:=ZMDDD8888888D
7777777,,7II7,,....,I=:.+=.,~~IN$Z8DDNNNNNNNNDDD8OZ=:IZZZOOOOOZZODD?~~~=~~~==+~===+~+==~~ZMDDDDD888N
D.III?.DM+,????,............,~$8NI??II$O8DDNNNNDDD888OOO888OZ$?~~~~~~~~~~~~=~=~~~~~~~~~~~~~IM8DDDDDN
?+??+.:88+.+=++++I.......=..~~:$8M:~=~~===+II77$7777I??==~~:~~~~~~~~7==~7~~~~~~~~~~~~~~~~~~~:NN8DDDN
:,+==.M,D7.======OOO87,,.,+. 7.ZDNN==+~+~~~~:~~~~~~~~~~~~~~=:~~~~~~=~~~=~~~~~~~~~~~~~~~~~~~::::M88DN
..===~....:=~~~~~OOOZ$7?.=$~?7Z8DNN=~~=~~~~~=~~:~~~~~~~~~~~~~~~~~~===~~~~~~~~~~~~~~~~~~:::::::::=MDN
""" 
  }
}


def dateReturn():
  return datetime.datetime.now()


def timeChecker():
  global date
  itemNum, hoursSpent, minutesSpent, secondsSpent = 0,0,0,0
  timeSpent = (datetime.datetime.now().hour*3600 + datetime.datetime.now().minute*60 + datetime.datetime.now().second)-(date.hour*3600 + date.minute*60 + date.second)
  hoursSpent = int(timeSpent/3600)
  timeSpent -= hoursSpent*3600    
  minutesSpent = int(timeSpent/60)
  timeSpent -= minutesSpent*60
  secondsSpent = int(timeSpent)
  return [hoursSpent, minutesSpent, secondsSpent]


def getDateDistribution(dateArr):
  return datetime.datetime(dateArr[0],dateArr[1],dateArr[2],dateArr[3],dateArr[4],dateArr[5])


def setDateDistribution(dateVal):
  return [dateVal.year, dateVal.month, dateVal.day, dateVal.hour, dateVal.minute, dateVal.second]


def userLoader(item):
  global currName, pw, userData, trolley, wallet, history
  userData[currName] = {
    "password": pw,
    "wallet": wallet,
    "history": history,
    "item": {}  
  }
  for item in trolley:
    userData[currName]["item"][item] = {} 
    userData[currName]["item"][item]["total"] = trolley[item]["total"] 
    userData[currName]["item"][item]["time of purchase"] = trolley[item]["time of purchase"]  


def buyerMethod():
  print("""
[A] - Show all paintings
[B] - Check painting
[C] - Buy painting
[D] - See your trolley 
[Q] - Exit
  """)


def showItem():
  for item in itemObj:
    print(f"""
name: {item}
total: {itemObj[item]["total"]}
cost: ${itemObj[item]["cost"]}
distribution date: {getDateDistribution(itemObj[item]["distribution date"])}
      """)
    time.sleep(1)
  input("Press any key to return ")


def checkItem(item):
  if not item in itemObj:
    if roleMethod == "C":
      return False
    print(f"Painting unavailable")
    input("Press any key to return ")
  elif item in itemObj:
    if itemObj[item]["total"] == 0:
      if roleMethod == "C":
        return "bruh"
      print("Painting is sold out, sorry")
      input("Press any key to return ")
    else:
      if roleMethod == "C" or roleMethod == "D" or roleMethod == "E":
        return True
      print(f"""
{itemObj[item]["label"]}
total: {itemObj[item]["total"]}
cost: ${itemObj[item]["cost"]}
distribution date: {getDateDistribution(itemObj[item]["distribution date"])}
        """)
      input("Press any key to return ")


def buyItem(item, total):
  global wallet
  if not checkItem(item):
    print("Painting is currently unavailable, sorry for the inconvenience")   
    input("Press any key to return ")
  elif checkItem(item) == "bruh":
    print("Painting is currently sold out, sorry for the inconvenience")
    input("Press any key to return ")
  elif itemObj[item]["total"] < total:
    print("Demand exceeds stocks, sorry for the inconvenience")
    input("Press any key to return ")
  elif wallet < itemObj[item]["cost"]*total:
    print("You nothin but a broke boy boy boy boy")
    input("Press any key to return ") 
  else:
    if not item in trolley:
      trolley[item] = {}
      trolley[item]["total"] = total
      trolley[item]["time of purchase"] = [datetime.datetime.now().strftime("%c")]
      trolley[item]["label"] = itemObj[item]["label"] 
    else:
      trolley[item]["total"] += total
      trolley[item]["time of purchase"].append(datetime.datetime.now().strftime("%c"))  
    print(f"""
Thank you for making a purchase!
Total cost: {itemObj[item]["cost"]*total}
Paid: {wallet}
Change: {wallet - itemObj[item]["cost"]*total}
Money left: {wallet -itemObj[item]["cost"]*total}
Time of purchase: {datetime.datetime.now()} 
      """)
    wallet -= itemObj[item]["cost"]*total
    itemObj[item]["total"] -= total
    input("Press any key to return ")
    saveItemObj()


def seeTrolley():
  if not trolley:
    print("You haven't made any purchases")
  else:
    slide, itemNum = 0,0
    timeSpent = timeChecker()
    for item in trolley:
      slide += 1
      itemNum += trolley[item]["total"]
      print(f"""
{itemObj[item]["label"]}
name: {item}
total: {trolley[item]["total"]}
time of purchase: {trolley[item]["time of purchase"]}
        """)
      input(f"Slide {slide}/{len(trolley)}")
      system("cls")
      if slide == len(trolley):
        print(f"""
Money: ${wallet}
Item bought: {itemNum}
Time spent: {timeSpent[0]} hours {timeSpent[1]} minutes {timeSpent[2]} seconds
          """ )
  input("Press any key to return ") 


def sellerMethod():
  print("""
[A] - Show all paintings
[B] - Check painting
[C] - Sell painting
[D] - Remove painting
[E] - Edit painting 
[F] - Check history
[Q] - Exit
  """)  


def sellItem():
  global wallet, dateObj
  itemName = input("Painting name: ").lower().title()
  if itemName in itemObj:
    print("Painting name already exist")
  else:
    try:
      itemTotal = int(input("Number of paintings: "))
      if itemTotal < 0:
        itemTotal *= -1
    except:
      print("Invalid integer!")
      print("Will only sell one instead")
      itemTotal = 1
    try:
      itemCost = float(input("Painting cost: $"))
      if itemCost < 0:
        itemCost *= -1
    except:
      print("Invalid number!")
      print("Will only sell as one dollar instead")
      itemCost = 1
    itemLabel = input("Painting preview: ")
    itemObj[itemName] = {}
    itemObj[itemName]["total"] = itemTotal
    itemObj[itemName]["cost"] = itemCost * 120/100 
    itemObj[itemName]["distribution date"] = setDateDistribution(datetime.datetime.now())
    itemObj[itemName]["label"] = itemLabel
    wallet += itemCost*itemTotal
    history.append(f"Sold a painting at {datetime.datetime.now()}")
    print("Deal completed!")
    time.sleep(1.5)
  input("Press any key to return ")
  saveItemObj()


def delItem(item):
  if checkItem(item) is True:
    del itemObj[item]
    history.append(f"Removed a painting at {datetime.datetime.now()}")
    print("Painting removed!")
    time.sleep(1.5)
    input("Press any key to return ")
    saveItemObj()


def editItem(item):
  if checkItem(item) is True:
    print("Use 0 if you want to keep it to default\n")
    name =  input("New name: ").lower().title()
    try: 
      total = int(input("New total of painting: "))
      if total < 0:
        total *= -1
    except:
      print("Invalid number, will use default value instead")
      total = 0
    try:
      cost = float(input("New cost of painting: $"))
      if cost < 0:
        cost *= -1
    except:
      print("Invalid number, will use default value instead")
      cost = 0
    label = input("New preview for painting: ")
    if name == "0":
      name = item
    if total == 0:
      total = itemObj[item]["total"]
    if cost == 0:
      cost = itemObj[item]["cost"]
    if label == "0":
      label = itemObj[item]["label"]
    itemObj[name] = itemObj.pop(item)
    itemObj[name]["total"] = total
    itemObj[name]["cost"] = cost
    itemObj[name]["distribution date"] = setDateDistribution(datetime.datetime.now())
    itemObj[name]["label"] = label
    history.append(f"Edited a painting at {datetime.datetime.now()}")
    input("Press any key to return ")
    saveItemObj()


def historyPrint():
  global history, wallet
  timeSpent = timeChecker()
  for events in history:
    print(events)
  print(f"Money: ${wallet}")
  print(f"Time spent: {timeSpent[0]} hours {timeSpent[1]} minutes {timeSpent[2]} seconds")
  input("Press any key to return")

  
def roleGenerator(role):
  global roleMethod, wallet, trolley
  system("cls")
  roleMethod = ""
  if role == "customer":
    while not wallet >= 0:
      try:
        wallet = float(input("How much money do you have on you? $"))
        if wallet < 0:
          print("broke lol")
      except:
        print("Type in a number pls")
        wallet = -1
    while roleMethod != "Q":
      system("cls")
      loadItemObj()
      print("Hello sir, how can I help you with?")
      buyerMethod()
      roleMethod = input("I'd like to: ").upper()
      system("cls")
      if roleMethod == "A":
        showItem()
      elif roleMethod == "B":
        wantedItem = input("What item do you want to check my good sir? ").lower().title()
        checkItem(wantedItem)
      elif roleMethod == "C":
        itemToBuy = ""
        itemTotal = 0
        while not itemToBuy:
          try:
            itemToBuy = input("What item do you want to buy my good lad?  ").lower().title()
          except:
            print("Value error bruh, pls type seriously")
            itemToBuy = ""
        while not itemTotal:
          try:
            itemTotal = int(input("How many items do you want to buy? "))
            if itemTotal < 0:
              itemTotal *= -1
            elif itemTotal == 0:
              print("Bro you tryna throw hands with me?")
          except:
            print("Value error bruh, pls type seriously")
            itemTotal = 0
        buyItem(itemToBuy, itemTotal)
      elif roleMethod == "D":
        seeTrolley()
    return True
  elif role == "seller":
    while not wallet >= 0:
      try:
        wallet = float(input("How much money do you have on you? $"))
        if wallet < 0:
          print("broke lol")
      except:
        print("Type in a number pls")
        wallet = -1
    while roleMethod.upper() != "Q":
      loadItemObj()
      system("cls")
      print("Welcome back boss, now what do you want to do today?")
      sellerMethod()
      roleMethod = input("I'd like to: ").upper()
      system("cls")
      if roleMethod == "A":
        showItem()
      elif roleMethod == "B":
        wantedItem = input("What item do you want to check boss? ").lower().title()
        checkItem(wantedItem)
      elif roleMethod == "C":
        sellItem()
      elif roleMethod == "D":
        item = input("What item do you want to remove boss? ").lower().title()
        delItem(item)
      elif roleMethod == "E":
        item = input("What item do you want to edit boss? ").lower().title()
        editItem(item)
      elif roleMethod == "F":
        historyPrint()
    return True
  else:
    print("Invalid role bruh")
    return False


print(f"Welcome to the online gallery")
time.sleep(1.5)
print("Now tell me what you're here for") 
time.sleep(1.5)


try:
  mkdir("./inventoryProject")
except:
  pass


try:
  loadItemObj()
except:
  saveItemObj()
  loadItemObj()


try:
  loadUserData()
except:
  defaultUserData()
  loadUserData()


while not role:
  while not currName:
    currName = input("Input username: ").lower().title()
    if currName in userData:
      pw = input("Input password: ")
      if pw == userData[currName]["password"]:
        print(f"Welcome back {currName}")
        wallet = userData[currName]["wallet"]
        for item in userData[currName]["item"]:
          trolley[item] = {
            "total": userData[currName]["item"][item]["total"],
            "time of purchase": userData[currName]["item"][item]["time of purchase"]
          }
          history = userData[currName]["history"]
      else:
        print("Wrong password! ")
        currName = ""
    else:
      if currName:
        while not pw:
          pw = input("Input password: ")
          if not pw:
            print("invalid password bruh")
      else:
        print("invalid username bruh")
  role = input("I'm a (customer/seller): ").lower()
  role = roleGenerator(role)
  if role:
    system("cls")
    exit = input("Are you sure you want to exit?(yes/no) ").lower()
    while exit != "yes":
      if exit == "no":
        role = ""
        date = dateReturn()
        print("ok welcome back i guess...")
        time.sleep(1.5)
        print("what's your role this time?")
        time.sleep(1.5)
        break
      else:
        print("Invalid reply bruh")
        exit = input("Are you sure you want to exit?(yes/no) ").lower()

print("ok bye bye")
saveUserData()