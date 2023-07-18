#Exercício Python 114:
import urllib.request

try:
    site = urllib.request.urlopen('http//www.pudim.com.br')
except urllib.error.URLError: