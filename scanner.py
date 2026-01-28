import argparse
import webbrowser
import sys
from colorama import Fore, Style, init

# Windows/Linux renk uyumu için başlat
init()

# Banner (Hacker hissiyatı için önemlidir :) )
def print_banner():
    print(Fore.CYAN + """
    ########################################
    #      MY PERSONAL DORK SCANNER        #
    #      Coded by: MrJaqu                #
    ########################################
    """ + Style.RESET_ALL)

# Dork Listemiz (Burayı istediğin kadar geliştirebilirsin)
def get_dorks(target):
    return [
        {"name": "SQL Injection", "dork": f"site:{target} inurl:php?id="},
        {"name": "Log Dosyalari", "dork": f"site:{target} ext:log"},
        {"name": "Env Yapilandirma", "dork": f"site:{target} ext:env"},
        {"name": "WordPress Users", "dork": f"site:{target} inurl:wp-content/uploads ext:sql"},
        {"name": "Acik Dizinler", "dork": f"site:{target} intitle:\"index of\""},
        {"name": "Admin Panelleri", "dork": f"site:{target} inurl:admin OR inurl:login"},
        {"name": "Public Dosyalar", "dork": f"site:{target} filetype:pdf OR filetype:xls OR filetype:docx"}
    ]

def main():
    print_banner()
    
    # Kullanıcıdan veri alma (CLI Argümanları)
    parser = argparse.ArgumentParser(description="Otomatik Google Dork Oluşturucu")
    parser.add_argument("-t", "--target", help="Hedef Domain (orn: site.com)", required=True)
    parser.add_argument("-o", "--open", help="Sonuclari tarayicida otomatik ac", action="store_true")
    
    args = parser.parse_args()
    target = args.target

    print(Fore.GREEN + f"[+] Hedef Belirlendi: {target}" + Style.RESET_ALL)
    print(Fore.YELLOW + "[*] Dorklar olusturuluyor...\n" + Style.RESET_ALL)

    dorks = get_dorks(target)

    for item in dorks:
        print(f"{Fore.RED}[SCAN]{Style.RESET_ALL} {item['name']} icin tarama linki:")
        # Google arama linki oluşturma
        search_query = f"https://www.google.com/search?q={item['dork']}"
        print(Fore.BLUE + search_query + Style.RESET_ALL)
        print("-" * 50)

        # Eğer -o parametresi verildiyse tarayıcıda aç
        if args.open:
            webbrowser.open(search_query)

if __name__ == "__main__":
    main()
