o
    RM|aΝ:  γ                   @   s°   d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dl mZ d dlm	Z	 dZ
dZdd ZG d	d
 d
Zdd Ze  e eje‘ dd Zdd Zdd Ze  dS )ι    N)Ϊsleep)Ϊargv)Ϊsystemz[31mϊ[0mc                 C   s   t d t ‘  d S )Nz% [-] Keyboard Interrupt! Terminaling!)ΪprintΪsysΪexit)ZsignumΪframe© r
   ϊnmap.pyΪsigint_handler   s   r   c                   @   s:   e Zd ZdZdZdZdZdZdZdZ	ddgZ
e e
‘ZdS )	Ϊbcolorsz[92mz[0;33mz[91mr   z[94mz[3;33mz[0;36N)Ϊ__name__Ϊ
__module__Ϊ__qualname__ZOKGREENZWARNINGZFAILZENDCZLITBUZYELLOWZCYANZcolorsΪrandomΪchoiceΪRANDr
   r
   r
   r   r      s    r   c                  C   sh   t  d‘j} | dkr.ttd t d  ttd t d  ttd t d  t ‘  d S td d S )Nz2http://flyzero.000webhostapp.com/project/serv1.phpΪ1z[-]z= Error code: 000 The server is full. Please try again later. z; Error code: 000 The system cannot start without a server. z Server Status: Is full (>.<)Ϊ )ΪrequestsΪgetΪtextr   ΪRΪWr   r   )r   r
   r
   r   Ϊ
serv_check   s   r   c                   C   s   t tjd  d S )NuΤ  
ββββ ββββββββ   βββ ββββ     β  ββββ βββββ βββ       ββββββ
βββββββ βββ βββ  βββ βββββ   β βββββββ βββββββββ    ββββ  βββ
βββ    ββββ  βββ ββββββ  ββ ββββββ    βββββββ  βββ  ββββ ββββ
βββ    βββ   β βββββββββ  ββββββββ    βββ βββββββββ βββββββ β
ββββ   ββββ  β βββββββββ   ββββββββ   ββββ ββ   ββββββββ β  β
β ββ   β  β   βββββ β ββ   β β β ββ   β  β ββ   ββββββββ β  β
β  β      β βββ βββ β ββ   β βββ  β      β  β   ββ βββ β
β      β    β β ββ     β   β β β      β     β   β   ββ
       β    β β              β        β         β  β
            β β

βββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββΊ
| Developer: mishakorzhik
βββββββββββββββββββββββββββββββββββββββββΊ Version: 1.1.0 [1;m
)r   r   r   r
   r
   r
   r   Ϊlogo+   s   r   c                   C   s   t   td d S )Na»    01] Default Scan
  02] Host Discovery
  03] Port(SYN) Scan
  04] Port(TCP) Scan
  05] Port(UDP) Scan
  06] Port Definition 
  07] Ping Scanner
  08] Scan and detect Server/Daemon
  09] Scan a host protected by firewall
  10] Scan a firewall for MAC address spoofing
  11] Dns Brute force
  12] Service and Version Discovery
  13] OS Analysis and Version Discovery
  14] Nmap Script Engineering
  15] About Utility
  00] Exit Utility
        )r   r   r
   r
   r
   r   Ϊmenu=   s   r   c                  C   s
  t  d‘ t  td} | dks| dkr`td t d‘ t  d‘ t  td td}t  d	| d
 | ‘ td td}|dkrGt  |dkrTtd t	 
‘  ntd t d‘ t  | dksh| dkr΄td t d‘ t  d‘ t  td td}t  d| d
 | ‘ td td}|dkrt  |dkr¨td t	 
‘  ntd t d‘ t  | dks½| dkr	td t d‘ t  d‘ t  td td}t  d| d
 | ‘ td td}|dkrπt  |dkrύtd t	 
‘  ntd t d‘ t  | dks| dkratd t d‘ t  d‘ t  td td}t  d| d
 | ‘ td td}|dkrGt  |dkrUtd t	 
‘  ntd t d‘ t  | dksk| dkr»td t d‘ t  d‘ t  td td}	t  d |	 d
 |	 d! ‘ td td}
|
dkr‘t  |
dkr―td t	 
‘  ntd t d‘ t  | d"ksΕ| d#krtd$ t d‘ t  d‘ t  td td}t  d%| d
 | d! ‘ td td}|dkrϋt  |dkr	td t	 
‘  ntd t d‘ t  | d&ks| d'kritd( t d‘ t  d‘ t  td) td}t  d*| ‘ td td}|dkrOt  |dkr]td t	 
‘  ntd t d‘ t  | d+kss| d,kr½td- t d‘ t  d‘ t  td td}t  d.| ‘ td td}|dkr£t  |dkr±td t	 
‘  ntd t d‘ t  | d/ksΗ| d0krtd1 t d‘ t  d‘ t  td td}t  d2| ‘ td td}|dkrχt  |dkrtd t	 
‘  ntd t d‘ t  | d3kr`td4 t d‘ t  d‘ t  td td}t  d5| ‘ td td}|dkrFt  |dkrTtd t	 
‘  ntd t d‘ t  | d6kr―td7 t d‘ t  d‘ t  td td}t  d8| ‘ td td}|dkrt  |dkr£td t	 
‘  ntd t d‘ t  | d9krtd: t d‘ t  d‘ t  td td}t  d;| d
 | d! ‘ td td}|dkrκt  |dkrψtd t	 
‘  ntd t d‘ t  | d<krYtd= t d‘ t  d‘ t  td td}t  d>| d
 | d! ‘ td td}|dkr?t  |dkrMtd t	 
‘  ntd t d‘ t  | d?kr³td@ t d‘ t  d‘ t  td td}t  dA| d
 | d! ‘ td td}|dkrt  |dkr’td t	 
‘  nt  d‘ td t d‘ t  | dBkrΰtdC tdD tdE tdF tdG tdH tdI tdJ t dK‘ t  | dLksκ| dMkrτtdN t	 
‘  d S tdO t dP‘ tdQ t dR‘ tdS t dR‘ tdT t dU‘ tdV t dW‘ tdX t dU‘ tdY t dR‘ tdZ t dW‘ t  d S )[NΪclearz  Diya: r   Z01z6 Starting Default Scan (--reason <text> -oN <text>)...ι   z& Enter your IP address or: example.comz While your IP: znmap --reason -d z -oN z/
 [1;91m01] Back to Main Menu 
 02] Exit [1;mzOption: Ϊ2z [1;91m@Good bye[1;mzR Please enter one of the options in the menu. 
 You are directed to the main menu.ι   Z02z Starting Host Discovery...z	nmap -Pn Ϊ3Z03z Starting Port(SYN) Scan...z While your IP:  z	nmap -sS Ϊ4Z04z Starting Port(TCP) Scan...u   nmap βsT Ϊ5Z05z Starting Port(UDP) Scan...u   nmap βsU z.txtΪ6Z06z% Starting Port Definition (-sS -F)...znmap -sS -F Ϊ7Z07z Starting Ping Scanner (-sn)...z* Enter your IP address or: 142.250.201.206z	nmap -sn Ϊ8Z08z(  Scan and detect Server/Daemon (-PN)...z	nmap -PN Ϊ9Z09z5  Starting scan a host protected by firewall (-sV)...z	nmap -sV Z10zQ  Starting scan A Firewall for MAC Address Spoofing (-v -sT -PN --spoof-mac 0)...znmap -v -sT -PN --spoof-mac 0 Z11z2  Starting dns brute force (--script dns-brute)...znmap --script dns-brute  Z12zE Starting Service and Version Discovery (-sS -F <text> -oN <text>)...u   nmap βsS -F Z13z-Starting OS Analysis and Version Discovery...u   nmap βsS -O Z14z$ Starting Nmap Script Engineering...u   nmap βsC Z15z[^_^] Tool Name: MyNmap v1.1.0z[^_^] Menu Type: About Utility!r   z/[>] Developer : misha korzhik                  z/[>] Company   : Flyzero copyring 2019          z/[>] Version   : Tool version 1.1.0             z/[>] Telegram  : @MishaKorzhikTelegram          z/[>] Github    : https://github.com/mishakorzik ι   Ϊ0Z00z+ [1;91@[^_^] Bye Bye have a nice day![1;mzX [0_0] Please enter one of the options in the menu. 
 You are directed to the main menu.g      ΰ?z; Processing And Tasking: 11% 
 Processing And Tasking: 24% gΙ?z Processing And Tasking: 29% z Processing And Tasking: 41% gΉ?z; Processing And Tasking: 56% 
 Processing And Tasking: 69% g333333Σ?z Processing And Tasking: 77% z Processing And Tasking: 82% z Processing And Tasking: 91% )Ϊosr   r   Ϊinputr   Ϊtimer   r   Ϊ	baslangicr   r   )ΪopZbirhedefZsecimbirZikihedefZsecimikiZuchedefZsecimucZ	dorthedefZ	secimdortZbeshedefZsecimbesZ	altihedefZ	secimaltiZ
ultifhedefZ	secimaytoZoiltefhedefZ	yecimaytoZoilkoefhidefZ
yecimayto0Zoilkoefh01idefZy0ecimayto0Z	yedihedefZ	secimyediZ
sekizhedefZ
secimsekizZ
dokuzhedefZ
secimdokuzr
   r
   r   r.   R   s>  































































































r.   )r   r+   r-   Ϊsignalr   r   r   r   Ϊplatformr   r   r   r   r   r   ΪSIGINTr   r   r.   r
   r
   r
   r   Ϊ<module>   s,    	  
E