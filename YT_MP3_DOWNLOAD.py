import subprocess

shitfucklist = []
def ytdown(x):
    video_url = x
    command = f"yt-dlp -x --audio-format mp3 {video_url}"

    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("STDOUT:", process.stdout)
    print("STDERR:", process.stderr)
    print("Return code:", process.returncode)
def errrr():
    print("FUNKING ERROR")
    ask()
def addlink():
    asker = input("LINK: ")
    shitfucklist.append(asker)
    ask()
def ask():
    nema = input('ADD NEW LINK? y/n')
    if nema == 'y':
        addlink()
    elif nema == 'n':
        print(shitfucklist)
    else:
        errrr()

ask()
for i in shitfucklist:
    ytdown(i)
