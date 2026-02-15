import customtkinter as ctk
import subprocess
import threading
import os
import sys
import ctypes
import re
import time

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class XAIDPI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("XAIDPI")
        self.geometry("880x640")
        self.attributes("-alpha", 0.96)
        
        self.font_logo = ("SF Pro Display", 46, "bold")
        self.font_ver = ("SF Pro Display", 12, "bold")
        self.font_ui = ("SF Pro Display", 14, "bold")
        self.font_btn = ("SF Pro Display", 18, "bold")
        self.font_mono = ("Consolas", 10)

        if getattr(sys, 'frozen', False):
            self.internal_dir = sys._MEIPASS
        else:
            self.internal_dir = os.path.dirname(os.path.abspath(__file__))

        self.bin_f = os.path.join(self.internal_dir, "bin")
        self.lst_f = os.path.join(self.internal_dir, "lists")
        self.engine = os.path.join(self.bin_f, "engine.exe")

        self.strategies = {
            "SIMPLE FAKE ALT2": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_max_ru.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_max_ru.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"',
            "General (Default)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=multisplit --dpi-desync-split-seqovl=568 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_4pda_to.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=multisplit --dpi-desync-split-seqovl=568 --dpi-desync-split-pos=1 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_4pda_to.bin"',
            "ALT (Fake Split)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake,fakedsplit --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fakedsplit-pattern=0x00 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake,fakedsplit --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fakedsplit-pattern=0x00 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,fakedsplit --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fakedsplit-pattern=0x00 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,fakedsplit --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fakedsplit-pattern=0x00 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"',
            "ALT 2 (MultiSplit)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=multisplit --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin"',
            "ALT 3 (Host Fake Split)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake,hostfakesplit --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --dpi-desync-hostfakesplit-mod=host=www.google.com,altorder=1 --dpi-desync-fooling=ts --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake,hostfakesplit --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --dpi-desync-hostfakesplit-mod=host=www.google.com,altorder=1 --dpi-desync-fooling=ts --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,hostfakesplit --dpi-desync-fake-tls-mod=rnd,dupsid,sni=ya.ru --dpi-desync-hostfakesplit-mod=host=ya.ru,altorder=1 --dpi-desync-fooling=ts --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,hostfakesplit --dpi-desync-fake-tls-mod=rnd,dupsid,sni=ya.ru --dpi-desync-hostfakesplit-mod=host=ya.ru,altorder=1 --dpi-desync-fooling=ts --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"',
            "ALT 4 (BadSeq)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake,multisplit --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-badseq-increment=1000 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake,multisplit --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-badseq-increment=1000 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,multisplit --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-badseq-increment=1000 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,multisplit --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-badseq-increment=1000 --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"',
            "ALT 5 (Disorder)": f'--wf-tcp=443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-l3=ipv4 --filter-tcp=443,2053,2083,2087,2096,8443 --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=syndata,multidisorder --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin"',
            "ALT 9 (Host Mix)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=hostfakesplit --dpi-desync-repeats=4 --dpi-desync-fooling=ts --dpi-desync-hostfakesplit-mod=host=www.google.com --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=hostfakesplit --dpi-desync-repeats=4 --dpi-desync-fooling=ts --dpi-desync-hostfakesplit-mod=host=www.google.com --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=hostfakesplit --dpi-desync-repeats=4 --dpi-desync-fooling=ts,md5sig --dpi-desync-hostfakesplit-mod=host=ozon.ru --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=hostfakesplit --dpi-desync-repeats=4 --dpi-desync-fooling=ts --dpi-desync-hostfakesplit-mod=host=ozon.ru',
            "ALT 10 (None Mod)": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=none --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_www_google_com.bin" --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_4pda_to.bin" --dpi-desync-fake-tls-mod=none --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls-mod=rnd,sni=www.google.com --dpi-desync-fake-tls="{self.bin_f}\\tls_clienthello_4pda_to.bin" --dpi-desync-fake-tls-mod=none --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"',
            "FAKE TLS AUTO ALT3": f'--wf-tcp=80,443,2053,2083,2087,2096,8443 --wf-udp=443,19294-19344,50000-50100 --filter-udp=443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new --filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-fooling=ts --dpi-desync-repeats=8 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --new --filter-tcp=443 --hostlist="{self.lst_f}\\list-google.txt" --ip-id=zero --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-fooling=ts --dpi-desync-repeats=8 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --new --filter-tcp=80,443 --hostlist="{self.lst_f}\\list-general.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-fooling=ts --dpi-desync-repeats=8 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin" --new --filter-udp=443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fake-quic="{self.bin_f}\\quic_initial_www_google_com.bin" --new --filter-tcp=80,443 --ipset="{self.lst_f}\\ipset-all.txt" --hostlist-exclude="{self.lst_f}\\list-exclude.txt" --ipset-exclude="{self.lst_f}\\ipset-exclude.txt" --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=681 --dpi-desync-split-pos=1 --dpi-desync-fooling=ts --dpi-desync-repeats=8 --dpi-desync-split-seqovl-pattern="{self.bin_f}\\tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=rnd,dupsid,sni=www.google.com --dpi-desync-fake-http="{self.bin_f}\\tls_clienthello_max_ru.bin"'
        }

        self.process = None
        self.is_running = False
        self.selected_method = ctk.StringVar(value="SIMPLE FAKE ALT2")
        self.is_multicolor = False
        self.rainbow_colors = ["#FF3B30", "#FF9500", "#FFCC00", "#34C759", "#007AFF", "#5856D6", "#AF52DE"]
        self.color_idx = 0

        self.setup_ui()

    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color="#0D0D0D")
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.logo = ctk.CTkLabel(self.sidebar, text="XAIDPI", font=self.font_logo, text_color="#007AFF")
        self.logo.pack(pady=(50, 0))
        
        self.ver = ctk.CTkLabel(self.sidebar, text="1.00 stable", font=self.font_ver, text_color="#48484A")
        self.ver.pack(pady=(0, 40))

        ctk.CTkLabel(self.sidebar, text="МЕТОД ОБХОДА", font=self.font_ver, text_color="#636366").pack(pady=5, padx=30, anchor="w")
        self.option_menu = ctk.CTkOptionMenu(
            self.sidebar, 
            values=list(self.strategies.keys()), 
            variable=self.selected_method,
            font=self.font_ui,
            fg_color="#1C1C1E",
            button_color="#007AFF",
            height=48,
            corner_radius=12,
            dropdown_font=self.font_ui,
            dropdown_hover_color="#2C2C2E"
        )
        self.option_menu.pack(pady=10, padx=25, fill="x")

        ctk.CTkLabel(self.sidebar, text="НАСТРОЙКИ ТЕМЫ", font=self.font_ver, text_color="#636366").pack(pady=(30, 5), padx=30, anchor="w")
        
        self.theme_menu = ctk.CTkOptionMenu(
            self.sidebar, 
            values=["Темная", "Светлая", "Системная", "Разноцветная"],
            command=self.change_theme,
            font=self.font_ui,
            fg_color="#1C1C1E",
            button_color="#3A3A3C",
            height=38,
            corner_radius=10
        )
        self.theme_menu.pack(pady=5, padx=25, fill="x")

        ctk.CTkLabel(self.sidebar, text="ПРОЗРАЧНОСТЬ", font=self.font_ver, text_color="#636366").pack(pady=(20, 5), padx=30, anchor="w")
        self.trans_slider = ctk.CTkSlider(self.sidebar, from_=0.4, to=1.0, number_of_steps=20, command=self.change_opacity)
        self.trans_slider.set(0.96)
        self.trans_slider.pack(pady=5, padx=25, fill="x")

        self.btn_reset = ctk.CTkButton(self.sidebar, text="Сброс драйвера", command=self.fix_driver, 
                                       fg_color="transparent", border_width=1, border_color="#3A3A3C", 
                                       text_color="#8E8E93", height=32, corner_radius=10)
        self.btn_reset.pack(side="bottom", pady=30, padx=25, fill="x")

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

        self.status_lbl = ctk.CTkLabel(self.main_frame, text="SYSTEM READY", font=self.font_ui, text_color="#30D158")
        self.status_lbl.pack(anchor="w", padx=5)

        self.console_box = ctk.CTkFrame(self.main_frame, fg_color="#000000", corner_radius=20, border_width=1, border_color="#1C1C1E")
        self.console_box.pack(fill="both", expand=True, pady=15)

        self.txt = ctk.CTkTextbox(self.console_box, fg_color="transparent", text_color="#32D74B", font=self.font_mono, padx=20, pady=20)
        self.txt.pack(fill="both", expand=True)

        self.action_btn = ctk.CTkButton(
            self.main_frame, 
            text="START ENGINE", 
            command=self.toggle,
            font=self.font_btn,
            height=75,
            corner_radius=25,
            fg_color="#007AFF",
            hover_color="#005BB5"
        )
        self.action_btn.pack(fill="x", pady=(15, 0))

    def log(self, msg):
        t = time.strftime("%H:%M:%S")
        self.txt.insert("end", f"[{t}] {msg}\n")
        self.txt.see("end")

    def change_theme(self, choice):
        self.is_multicolor = False
        if choice == "Темная": ctk.set_appearance_mode("Dark")
        elif choice == "Светлая": ctk.set_appearance_mode("Light")
        elif choice == "Системная": ctk.set_appearance_mode("System")
        elif choice == "Разноцветная":
            self.is_multicolor = True
            self.run_multicolor_loop()

    def run_multicolor_loop(self):
        if not self.is_multicolor: return
        color = self.rainbow_colors[self.color_idx]
        self.logo.configure(text_color=color)
        self.action_btn.configure(fg_color=color)
        self.option_menu.configure(button_color=color)
        
        self.color_idx = (self.color_idx + 1) % len(self.rainbow_colors)
        self.after(1000, self.run_multicolor_loop)

    def change_opacity(self, val):
        self.attributes("-alpha", val)

    def fix_driver(self):
        self.log("Очистка WinDivert...")
        subprocess.run("taskkill /f /im engine.exe", shell=True, capture_output=True)
        subprocess.run("sc stop WinDivert", shell=True, capture_output=True)
        subprocess.run("sc delete WinDivert", shell=True, capture_output=True)
        self.log("Драйвер очищен.")

    def toggle(self):
        if self.is_running: self.stop_engine()
        else: self.start_engine()

    def start_engine(self):
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return

        method_name = self.selected_method.get()
        args = self.strategies[method_name]
        
        args = re.sub(r'--[a-z0-9-]+=\s*(?=--|$)', '', args)
        args = re.sub(r',\s*(?=--|$)', ' ', args)
        args = re.sub(r',+', ',', args)

        cmd = f'"{self.engine}" {args}'
        self.log(f"Запуск {method_name}...")

        try:
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                          stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW, 
                                          shell=True, cwd=self.bin_f)
            self.is_running = True
            self.action_btn.configure(text="STOP ENGINE", fg_color="#FF3B30")
            self.status_lbl.configure(text="ACTIVE", text_color="#007AFF")
            threading.Thread(target=self.monitor, daemon=True).start()
        except Exception as e: self.log(f"Сбой: {e}")

    def monitor(self):
        while self.is_running and self.process:
            line = self.process.stdout.readline()
            if not line: break
            try:
                msg = line.decode("cp866", errors="ignore").strip()
                if msg: self.after(0, lambda m=msg: self.log(m))
            except: pass
        self.after(0, self.stop_engine)

    def stop_engine(self):
        if self.process:
            subprocess.run(f"taskkill /F /T /PID {self.process.pid}", shell=True, capture_output=True)
            self.process = None
        self.is_running = False
        self.action_btn.configure(text="START ENGINE", fg_color="#007AFF" if not self.is_multicolor else self.rainbow_colors[self.color_idx-1])
        self.status_lbl.configure(text="SYSTEM READY", text_color="#30D158")
        self.log("Двигатель остановлен.")

    def on_closing(self):
        self.stop_engine()
        self.destroy()

if __name__ == "__main__":
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        app = XAIDPI()
        app.protocol("WM_DELETE_WINDOW", app.on_closing)
        app.mainloop()
