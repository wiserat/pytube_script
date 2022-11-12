from pytube import YouTube
import sys

print(r"""
_____________________________________________________________      
|        ___    __    ____  ____        __          ___     |
|        | |   /  \   |   \ |  |       /  \        / _ \    |
|        | |  /    \  |    \|  |      /    \      | | \_\   |
|        | |  | || |  |  |  \  |     /  ||  \      \ \      |
|    __  | |  | || |  |  |\  \ |    /  ____  \  __  \ \     |
|    \ \/ /   \    /  |  | \   |   /  /    \  \ \ \_/  |    | 
|     \__/     \__/   |__|  \__|  /__/      \__\ \____/     |
|___________________________________________________________|
|                    _        ___       _  __               |
|              \ /  / \  |  |  |  |  | |_\ |_               |
|               |   \_/  \_/|  |  \_/| |_| |_               |
|       __   _                  _    _   __   __  __        |
|       | \ / \ \    / |\ | |  / \  /_\  | \  |_  |_\       |
|       |_/ \_/  \/\/  | \| |_ \_/ /   \ |_/  |_  | \       | 
|___________________________________________________________|
|                                                           |
|                https://github.com/wiserat                 |
|___________________________________________________________|
""")

another = ""
start = "y"
dir_path = ""
audeo = ""
link_presence = False
dir_name_presence = False

def directory(dir_name):
    for dir_path in dir_name:
        dir_path = dir_name
        return dir_path

try:
    if sys.argv[1] == "-a":
        another = "y"
        start = "auto"
        if sys.argv[2].startswith("https://www.youtube.com/watch?v="):
            link = sys.argv[2]
            link_presence = True
            
    elif sys.argv[1] == "-y":
        audeo = "y"
        another = "y"
        start = "y"
        selection = 0
        if sys.argv[2].startswith("https://www.youtube.com/watch?v="):
            link = sys.argv[2]
            link_presence = True
            if sys.argv[3] != "":
                dir_name_presence = True
                dir_name = sys.argv[3]
                
    elif sys.argv[1] == "-n":
        start = "y"
        another = "y"
        audeo = "n"
        if sys.argv[2] == "-l":
            selection = 2
            if sys.argv[3].startswith("https://www.youtube.com/watch?v="):
                link = sys.argv[3]
                link_presence = True
                if sys.argv[4] != "":
                    dir_name = sys.argv[4]
                    dir_name_presence = True
        elif sys.argv[2] == "-h":
            selection = 1
            if sys.argv[3].startswith("https://www.youtube.com/watch?v="):
                link = sys.argv[3]
                link_presence = True
                if sys.argv[4] != "":
                    dir_name = sys.argv[4]
                    dir_name_presence = True
    elif sys.argv[1] == "-h":
        print("-a = automatic download\n\t-a <YouTube link>\n-y = audio only\n\t-y <YouTube link> <directory name>\n-n = normal download, l = lowest video quality, h = highest video quality\n\t-n -l <YouTube link> <directory name>\n\t-n -h <YouTube link> <directory name>\n")
        
except IndexError:
    pass

while start == "y" or "n" or "auto":

    if another == "n":
        print("See ya later")
        break
        
    if another != "y":
        start = input("Do you want to continue and download a YouTube video? (y/n/auto): ").lower()
    
    if start == "n":
        print("See ya later")
        break
                
    while start == "y":
        if audeo == "":
            audeo = input("Do you want to download audio only? (y/n)").lower()
            if audeo == "y":
                selection = 0
            elif audeo == "n":
                while audeo == "n":
                    quality_selection = input("Enter the video quality you want (highest=h, lowest=l): ")
                    if quality_selection == "h":
                        selection = 1
                        break
                    elif quality_selection == "l":
                        selection = 2
                        break
                    else:
                        print("Invalid input!")
            else:
                print("Invalid input!")
                break
                    
        audeo = ""
        try:
            if link_presence == False:
                link = input("Enter the url of the video: ")
            yt = YouTube(link)
        except Exception:
            print("Invalid link!\n")
            another = ""
            link_presence = False
            break
        link_presence = False
        print("\n")
        print("Title: ", yt.title)
        print("Author: ", yt.author)
        print("\n")
        print("\rPreparing...", end="")
        if selection == 1:
            yd = yt.streams.get_highest_resolution()
        elif selection == 2:
            yd = yt.streams.get_lowest_resolution()
        elif selection == 0:
            yd = yt.streams.get_audio_only()
        else:
            yd = yt.streams.get_highest_resolution()
        
        if dir_name_presence == False:
            dir_name = input("\rType the name of the folder you want to download in: ")
        dir_name_presence = False
        print("\n")
        print("\rDownloading...", end="")
        yd.download(directory(dir_name))
        
        print("\rDownloaded succesfully, feel free to download another")
        print("! Your folder was created in same folder as is this script !")
        print("\n")
        another = input("Do you want to download another one? (y/n/auto): ")
        if another == "auto":
            start = "auto"
            break
        elif another == "y":
            break
        elif another == "n":
            break
        else:
            print("Invalid input!")
            break
    
    while start == "auto":
        try:
            if link_presence == False:
                link = input("Enter the url of the video: ")
            yt = YouTube(link)
        except Exception:
            print("Invalid link!\n")
            another = ""
            link_presence = False
            break
        link_presence = False
        print("\n")
        print("Title: ", yt.title)
        print("Author: ", yt.author)
        print("\n")
        print("\rDownloading...", end="")
        yd = yt.streams.get_highest_resolution()
        yd.download('./YTDownloaded')
        print("\rDownloaded succesfully")
        print("! YTDownloaded folder was created in same folder as is this script !")
        print("\n")
        another = input("Do you want to download another one?(y/n/auto): ")
        if another == "auto":
            print("\n")
        elif another == "n":
            break
        elif another == "y":
            start = "y"
            break
        else:
            print("Invalid input!")
            break
