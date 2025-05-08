# 🚗 Fahrzeugverfolgung mit YOLOv8 + BoxMOT

Dieses Projekt nutzt **YOLO** zusammen mit dem **BoxMOT-Framework** und dem **ByteTrack-Tracker**, um Fahrzeuge wie Autos, LKWs und Busse zuverlässig in Videos zu erkennen und über mehrere Frames hinweg zu verfolgen.

---

## 📦 Inhalt
- [✨ Features](#✨-features)
- [🔧 Voraussetzungen](#🔧-voraussetzungen)
- [🛠️ Installation](#🛠️-installation)
- [▶️ Verwendung](#▶️-verwendung)
- [💾 Ausgabe](#💾-ausgabe)
- [🧩 GUI (optional)](#🧩-gui-optional)
- [🛠️ Fehlerbehebung](#🛠️-fehlerbehebung)
- [📄 Lizenz](#📄-lizenz)
- [👤 Autor](#👤-autor)

---

## ✨ Features

- Echtzeit-Erkennung mit [YOLOv8](https://github.com/ultralytics/ultralytics)
- Multi-Objekt-Tracking mit [ByteTrack](https://github.com/ifzhang/ByteTrack) oder StrongSORT
- Unterstützung für Videos, Webcam oder Bildordner
- Ausgabevideo mit farbiger ID-Anzeige
- Einschränkbar auf Fahrzeugklassen (Auto, Bus, LKW)
- CSV-Export (optional integrierbar)
- Grafische Benutzeroberfläche (GUI) mit **Tkinter**

---

## 🔧 Voraussetzungen

- Python 3.9–3.11 (Python 3.12 wird **nicht empfohlen**)
- Git
- `ffmpeg`
- NVIDIA GPU mit CUDA (empfohlen für Echtzeit)

---

## 🛠️ Installation

### 1. Projekt klonen

```bash
git clone --recurse-submodules https://github.com/ArisenGHG/KFZ-Erkenner
cd boxmot
````

### 2. Virtuelle Umgebung aktivieren

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 3. Abhängigkeiten mit `uv` installieren

```bash
pip install uv
uv sync --group yolo
```

---

## ▶️ Verwendung

### 🔹 Videoverfolgung

```bash
python tracking/track.py --source "Traffic.mp4" --yolo-model yolov8n.pt --tracking-method bytetrack --project "D:/TrackingErgebnisse" --name "video1" --save
```

### 🔹 Webcam

```bash
python tracking/track.py --source 0 --yolo-model yolov8n.pt --tracking-method bytetrack --show --save
```

### 🔹 Nur Fahrzeuge erkennen (Autos, Busse, LKWs)

```bash
python tracking/track.py --source "video.mp4" --yolo-model yolov8n.pt --tracking-method bytetrack --classes 2 5 7 --save
```

> COCO-Klassen:
>
> * Auto: `2`
> * Bus: `5`
> * LKW: `7`

---

## 💾 Ausgabe

Die Ergebnisse werden unter dem gewählten Projektordner gespeichert:

```
<Projekt>/<Name>/
z. B.: D:/TrackingErgebnisse/video1/
```

Inhalt:

* `video.mp4`: getracktes Video
* ggf. Textdateien mit Trackingdaten, Objekt-Crops etc.

---

## 🧩 GUI (optional)

Du kannst eine einfache grafische Oberfläche nutzen:

```bash
python boxmot_gui_tkinter.py
```

Funktionen:

* Video auswählen
* Modell und Tracker wählen
* Ausgabeordner angeben
* Tracking starten per Klick

Keine Installation zusätzlicher Bibliotheken nötig – basiert auf Python-Standardmodul `tkinter`.

---

## ⚠️ YOLOv12 Hinweis

> **YOLOv12 wird von BoxMOT aktuell nicht offiziell unterstützt.**
> Das Modell muss ggf. angepasst werden, um mit `track.py` kompatibel zu sein. Für produktiven Einsatz weiterhin **YOLOv8** empfohlen.

---

## 🛠️ Fehlerbehebung

### PowerShell: `.ps1 kann nicht geladen werden`

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### StrongSORT Fehler mit `plot_results`

Verwende `--tracking-method bytetrack` oder aktualisiere auf einen stabilen Tracker.

### Windows: Fehler bei Leerzeichen im Pfad

Pfadangaben immer in **"Anführungszeichen"** setzen.

---

## 📄 Lizenz

Dieses Projekt verwendet Open-Source-Komponenten und steht unter der [MIT-Lizenz](https://opensource.org/licenses/MIT).

Achte auf die Lizenzen von:

* [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
* [BoxMOT](https://github.com/mikel-brostrom/boxmot)
* [ByteTrack](https://github.com/ifzhang/ByteTrack)

---

## 👤 Autor

Anpassung & GUI-Integration durch [ArisenGHG](https://github.com/ArisenGHG).
Grundlage: BoxMOT (Mikel Brostrom) + YOLOv8 (Ultralytics)

---

```

---

Wenn du willst, kann ich dir zusätzlich einen Screenshot einbauen (GUI-Vorschau oder Ergebnisvideo). Möchtest du das?
```
