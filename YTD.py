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

start = "yes"

while start == "yes" or "no" or "opt":

    start = input("Do you want to continue and download a YouTube video? (yes/no/opt/): ")
    start == start.lower
                
    while start == "opt":
        quality_selection = input("Enter the video quality you want (1=highest, 2=lowest, 3=exit):")
        if quality_selection == "1":
            qs = 1
            break
        elif quality_selection == "2":
            qs = 2
            break
        elif quality_selection == "3":
            qs = 3
            break
        else:
            print("Invalid input!")
                
    while start == "yes":
        link = input("Enter the url of the video: ")
        yt = YouTube(link)
        print("\n")
        print("Title: ", yt.title)
        print("Author: ", yt.author)
        print("\n")
        print("\rDownloading...", end="")
        if qs == 1:
            yd = yt.streams.get_highest_resolution()
        elif qs == 2:
            yd = yt.streams.get_lowest_resolution()
        elif qs == 3:
            yd = yt.streams.get_highest_resolution()
        else:
            yd = yt.streams.get_highest_resolution()
            
        yd.download('./YTDownloaded')
        print("\rDownloaded succesfully, feel free to download another")
        print("! YTDownloaded folder was created in same folder as is this script !")
        print("\n")
        break

    if start == "no":
        print("See ya later")
        break
