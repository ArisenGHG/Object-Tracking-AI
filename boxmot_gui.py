import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def browse_video():
    filepath = filedialog.askopenfilename(filetypes=[("MP4 Dateien", "*.mp4")])
    if filepath:
        video_path.set(filepath)

def browse_model():
    filepath = filedialog.askopenfilename(filetypes=[("YOLO Model", "*.pt")])
    if filepath:
        model_path.set(filepath)

def browse_output():
    folderpath = filedialog.askdirectory()
    if folderpath:
        output_path.set(folderpath)

def start_tracking():
    video = video_path.get()
    model = model_path.get()
    tracker = tracker_var.get()
    output = output_path.get()

    # Pfad zur track.py als raw string
    script_path = r"D:\Object Tracking AI\boxmot\tracking\track.py"

    if not all([video, model, tracker, output]):
        messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen.")
        return

    cmd = f'python "{script_path}" --source "{video}" --yolo-model "{model}" --tracking-method {tracker} --project "{output}" --name gui_output --save'

    output_console.insert(tk.END, f"\n▶️ Starte Tracking mit:\n{cmd}\n\n")
    output_console.see(tk.END)

    try:
        subprocess.run(cmd, check=True, shell=True)
        output_console.insert(tk.END, "\n✅ Tracking abgeschlossen.\n")
    except subprocess.CalledProcessError as e:
        output_console.insert(tk.END, f"\n❌ Fehler: {e}\n")


# GUI Start
root = tk.Tk()
root.title("BoxMOT GUI (YOLO Tracking)")
root.geometry("700x500")

video_path = tk.StringVar()
model_path = tk.StringVar()
output_path = tk.StringVar()
tracker_var = tk.StringVar(value="bytetrack")

tk.Label(root, text="Video-Datei:").pack()
tk.Entry(root, textvariable=video_path, width=80).pack()
tk.Button(root, text="Durchsuchen", command=browse_video).pack()

tk.Label(root, text="YOLOv-Modell (.pt):").pack()
tk.Entry(root, textvariable=model_path, width=80).pack()
tk.Button(root, text="Durchsuchen", command=browse_model).pack()

tk.Label(root, text="Tracking-Methode:").pack()
tk.OptionMenu(root, tracker_var, "bytetrack", "strongsort").pack()

tk.Label(root, text="Speicherort:").pack()
tk.Entry(root, textvariable=output_path, width=80).pack()
tk.Button(root, text="Durchsuchen", command=browse_output).pack()

tk.Button(root, text="🚀 Tracking starten", command=start_tracking, bg="green", fg="white").pack(pady=10)

output_console = tk.Text(root, height=15, width=85)
output_console.pack()

root.mainloop()
