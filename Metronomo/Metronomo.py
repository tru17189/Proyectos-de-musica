from tkinter import *
from PIL import ImageTk, Image
from winsound import Beep, PlaySound, SND_FILENAME
import time

class metronomo:
    def __init__(self, root, beats):
        self.root = root
        self.beats = beats

        self.start = False
        self.bpm = 0
        self.count = 0
        self.beat = 0
        self.time = 0
        self.beat2 = False

        self.var = StringVar()
        self.var.set(self.count)

        self.gui()

    def gui(self):
        frame = Frame(bg="#dfe3ee")
        frame.pack()

        entry = Entry(frame, width=15, justify="center")
        entry.insert(0, "60")
        entry.grid(row=2, column=0, padx=5, sticky="E")

        spinbox = Spinbox(frame, width=13, justify="center", values=self.beats, wrap=True)
        spinbox.grid(row=2, column=1, padx=10, sticky="E")

        label_bpm = Label(frame, width=13, justify="center", text="BPM:")
        label_bpm.grid(row=1, column=0, sticky="W")

        label_time = Label(frame, width=13, text="Time:")
        label_time.grid(row=1, column=1, padx=10, sticky="W")

        label_count = Label(frame, textvariable=self.var, font=("Impact", 50), bg="#dfe3ee")
        label_count.grid(row=0, column=0, columnspan=2)

        Start = Button(frame, text="Play", width=10, height=2, bg="#33e21e",
                              command=lambda: self.start_counter(entry, spinbox))
        Start.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        tercer = Button(frame, text="Tercer tono", width=10, height=2, bg="#6897bb",
                              command=lambda: self.tercer_counter())
        tercer.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        Stop = Button(frame, text="Parar", width=10, height=2, bg="#ee1c25",
                             command=lambda: self.stop_counter())
        Stop.grid(row=4, column=2, padx=5, pady=10, sticky="E")
    
    def start_counter(self, entry, spinbox):
            if not self.start:
                try:
                    self.bpm = int(entry.get())
                except ValueError:
                    self.bpm = 60
                else:
                    if self.bpm > 300:  # Limits BPM
                        self.bpm = 300

                self.start = True
                self.counter(spinbox)
    
    def tercer_counter(self):
        #PlaySound('sound.wav', SND_FILENAME)
        self.beat2 = True

    def stop_counter(self):
        self.start = False

    def counter(self, spinbox):
       if self.start:
            self.beat = int(spinbox.get()[0])

            if self.beat == 7:  # 6/8 time
                self.time = int((60 / (self.bpm / .5) - 0.1) * 1000)
            else:
                self.time = int((60 / self.bpm - 0.1) * 1000)  # Math for delay

            self.count += 1
            self.var.set(self.count)

            if self.count == 1:
                Beep(880, 100)
                if self.beat2 == True:
                    time.sleep(0.2)
                    PlaySound('sound.wav', SND_FILENAME)
            elif self.count >= self.beat:
                self.count = 0
                Beep(440, 100)
                if self.beat2 == True:
                    time.sleep(0.2)
                    PlaySound('sound.wav', SND_FILENAME)
            else:
                Beep(440, 100)
                if self.beat2 == True:
                    time.sleep(0.2)
                    PlaySound('sound.wav', SND_FILENAME)

            self.root.after(self.time, lambda: self.counter(spinbox))

def main():
    root = Tk()
    root.title("Metronomo")

    beats = ["2/4", "3/4", "4/4", "5/4", "6/4", "7/4"]
    metronomo(root, beats)

    root.mainloop()

if __name__ == "__main__":
    main()
        