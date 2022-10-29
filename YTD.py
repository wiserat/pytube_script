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

another = "yes"

start = input("Do you want to continue and download a Youtube video? (yes/no): ")
start = start.lower()

if start == "yes":
    while another == "yes":
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
        another = input("Wanna download another one? (yes/no): ")
        another = another.lower()
        if another == "no":
            print("Pleasure working for you!")
            break
elif start == "no":
    print("Maybe next time")        

else:
    print("'" + start  + "'" + " is not valid!")