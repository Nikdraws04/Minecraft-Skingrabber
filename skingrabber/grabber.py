from skingrabber import skingrabber
import urllib.request
import colorama
from colorama import Fore
import pyfiglet
colorama.init(autoreset=True)

more = "y"

while more == "y":
    sg = skingrabber()

    #make startup banner
    Startup_Banner = pyfiglet.figlet_format("SKIN GRABBER")
    #print the startup banner in blue
    print(f"{Fore.BLUE}{Startup_Banner}")
    skin = input("Which skin do you want?: ")
    name = input("How should the skin be called?: ")

    #get skin data
    response = sg.get_skin(user=skin)
    #download the skin 
    urllib.request.urlretrieve(response, name+".png")
    print(f"{Fore.GREEN}Skin saved under the name {name}.png")
    #print skin link
    print(response)

    #if more = y the program starts again
    more = input("Do you want to download another skin (y/n)?: ")
 ")
