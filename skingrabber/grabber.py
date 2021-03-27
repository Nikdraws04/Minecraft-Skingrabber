from skingrabber import skingrabber
import urllib.request
import colorama
from colorama import Fore
import pyfiglet
colorama.init(autoreset=True)

more = "y"

while more == "y":
    sg = skingrabber()

    Startup_Banner = pyfiglet.figlet_format("SKIN GRABBER")
    print(f"{Fore.BLUE}{Startup_Banner}")
    skin = input("Which skin do you want?: ")
    name = input("How should the skin be called?: ")

    response = sg.get_skin(user=skin)
    urllib.request.urlretrieve(response, name+".png")
    print(f"{Fore.GREEN}Skin saved under the name {name}.png")
    print(response)

    more = input("Do you want to download another skin (y/n)?: ")
