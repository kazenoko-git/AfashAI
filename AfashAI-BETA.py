from g4f.client import Client
import random, threading, ctypes, keyboard
from PIL import Image as imgk
from PIL import ImageTk
from tkinter import *

"""device = "cuda" if torch.cuda.is_available() else "cpu"
print(TTS().list_models())
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
"""

isPressed = False
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
client = Client()


def get():
    global x, y,e,l, isPressed
    x = e.get()
    e.delete(0, END)
    y = AI(x)
    l.config(text=y)
    isPressed = False

def gui():
    global e,l
    app = Tk()
    app.title("AfashAI BETA")
    ico = imgk.open("source/img/icon.png")
    photo = ImageTk.PhotoImage(ico)
    app.wm_iconphoto(False, photo)
    app.config(bg="black")
    e = Entry(app, width=50, font=('Arial', 12))
    l = Label(app, font=("Helvetica", 14), bg="black", fg="white")
    b = Button(app, text="Enter", command=lambda: get(), width=10, height=2)
    l.pack()
    e.pack()
    b.pack()
    app.mainloop()

def keytrack():
    global isPressed
    while 1:
        try:
            if keyboard.is_pressed('return'):
                print("detect ENTER")
                isPressed = True
                get()
        except:
            pass

def AI(userIN:str="BOOT"):
    if userIN == "BOOT":
        pass
    else:
        try:
            def chat(prompt):
                tprompt = f"respond to \"{prompt}\" in a really silly, unserious and stupid tone and make sure to use english, or invent a language using the letters A, F, R, I, S, H, D. also make sure it's below 20 words."
                response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                          messages=[{"role": "user", "content": tprompt}])
                return response.choices[0].message.content.strip()
            try:
                while 1:
                    if userIN.lower() == "q" or userIN.lower() == "quit" or userIN.lower() == "exit" or userIN.lower() == "close" or userIN.lower() == "break":
                        break
                    else:
                        response = chat(userIN)
                        print("Afarh:", response)
                        return f"Afarh: {response}"
            except KeyboardInterrupt as e:
                intt = random.randrange(0, 4)
                if intt == 0:
                    x = "Afarh: Goodbye."
                elif intt == 1:
                    x = "Afarh: Goodnight."
                elif intt == 2:
                    x = "Afarh: Bye Bye."
                elif intt == 3:
                    x = "Afarh: Ghs."
                elif intt == 4:
                    x = "Afarh: Farfahfa!"
                print(x)
                exit(0)
        except RuntimeError as e:
            print("Afarh: I think there's something wrong with my AI.")
            return "Afarh: I think there's something wrong with my AI."

aithr = threading.Thread(target=AI)
aithr.start()
aithr.join()
tkthr = threading.Thread(target=gui)
tkthr.start()
tkthr.join()
ktthr = threading.Thread(target=keytrack)
ktthr.start()
ktthr.join()

# NOTE: GTTS sounds lame asf wtf
# don't use this

"""def GTTS(x:str="TEST"):
    mp3fp = BytesIO()
    z = gTTS(x)
    filename = f"TEMP{random.randrange(0,65536)}.mp3"
    z.save(filename)
    playsound.playsound(filename)
    os.remove(filename)"""

# TODO: what the fuck happened with this code below, don't uncomment it please
# FIXME: playsound doesn't play sound. gives an error instead.

"""def voice(msg:str="TEST"): # DONT USE THIS FUNCTION WHAT THE FUCK HAPPENED HERE
    location = site.getsitepackages()[0]
    path = location+"/TTS/models.json"
    model_manager = ModelManager(path)
    model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")
    voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])
    synthesiser = Synthesizer(tts_checkpoint=model_path, tts_config_path=config_path,vocoder_checkpoint=voc_path,vocoder_config=voc_config_path)
    output = synthesiser.tts(msg)
    filename = f"TEMP{random.randrange(0, 65536)}.mp3"
    synthesiser.save_wav(output, filename)
    playsound.playsound(filename)
    os.remove(filename)
    filename = f"TEMP{random.randrange(0, 65536)}.wav"
    tts.tts_to_file(text="Hello world!", speaker_wav=filename, language="en", file_path=filename)
    playsound.playsound(filename)
    os.remove(filename)"""