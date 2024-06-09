import time
import tkinter as tk
from tkinter import ttk
from playsound import playsound

class Stopper:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.paused = False

    def kezdes(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.paused = False

    def vege(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def szunet(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
            self.paused = True

    def folytatas(self):
        if not self.running and self.paused:
            self.start_time = time.time()
            self.running = True
            self.paused = False

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.paused = False

    def get_elapsed_time(self):
        if self.running:
            return self.elapsed_time + time.time() - self.start_time
        else:
            return self.elapsed_time

class StopperGUI:
    def __init__(self, root):
        self.stopper = Stopper()
        self.root = root
        self.root.title("Stopper")

        self.time_label = ttk.Label(root, text="00:00:00", font=("Helvetica", 48, "bold"))
        self.time_label.pack(pady=20)

        self.message_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold"))
        self.message_label.pack(pady=10)

        self.start_button = ttk.Button(root, text="Kezdés", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = ttk.Button(root, text="Szünet", command=self.pause)
        self.pause_button.pack(side="left", padx=10)

        self.resume_button = ttk.Button(root, text="Folytatás", command=self.resume)
        self.resume_button.pack(side="left", padx=10)

        self.stop_button = ttk.Button(root, text="Vége", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        self.exit_button = ttk.Button(root, text="Kilépés", command=self.exit)
        self.exit_button.pack(side="left", padx=10)

        self.update_time()

    def start(self):
        playsound('hangok/start.wav')
        self.stopper.kezdes()
        self.message_label.config(text="Elindult a stopper")
        self.update_time()

    def pause(self):
        playsound('hangok/pause.wav')
        self.stopper.szunet()
        self.message_label.config(text="A stopper szünetel")
        self.update_time()

    def resume(self):
        playsound('hangok/resume.wav')
        self.stopper.folytatas()
        self.message_label.config(text="A stopper folytatódik")
        self.update_time()

    def stop(self):
        playsound('hangok/stop.wav')
        self.stopper.vege()
        self.message_label.config(text="A stopper megállt")
        self.update_time()

    def reset(self):
        playsound('hangok/reset.wav')
        self.stopper.reset()
        self.message_label.config(text="A stopper alaphelyzetbe állt")
        self.update_time()

    def exit(self):
        playsound('hangok/exit.wav')
        self.root.destroy()

    def update_time(self):
        elapsed_time = self.stopper.get_elapsed_time()
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_string = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        self.time_label.config(text=time_string)
        if self.stopper.running:
            self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    gui = StopperGUI(root)
    root.mainloop()
