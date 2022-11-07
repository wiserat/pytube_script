from pytube import YouTube

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

def directory(dir_name):
    for dir_path in dir_name:
        dir_path = dir_name
        return dir_path

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
                
        link = input("Enter the url of the video: ")
        yt = YouTube(link)
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
        
        dir_name = input("\rType the name of the folder you want to download in: ")
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
        link = input("Enter the url of the video: ")
        yt = YouTube(link)
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
