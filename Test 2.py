import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from bleak import BleakScanner, BleakClient
import asyncio
from PIL import Image, ImageTk  # Für die Verwendung von Bildern wie JPG oder PNG

# Scan for Bluetooth devices
async def scan_for_devices():
    devices = await BleakScanner.discover()
    return devices

# Connect to the device
async def connect_to_device(address):
    try:
        async with BleakClient(address) as client:
            return client
    except Exception as e:
        print(f"Unable to hold connection: {e}")
        return None

# Create GUI
def create_gui():
    global root
    global label
    global result_label

    root = tk.Tk()  # Main window
    root.title("Blood Sugar Monitoring")
    root.geometry("400x300")  # Fenstergröße

    # Hintergrundbild laden und anzeigen
    background_image = Image.open(r"C:\Users\Jan.Jochem\OneDrive - DUO-PLAST AG\Dokumente\Steckbrief ich\background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)  # Umwandeln in ein Tkinter-kompatibles Bild

    # Label für das Hintergrundbild
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # Bild über das ganze Fenster strecken

    # Vordergrund Label (Text über dem Hintergrundbild)
    label = tk.Label(root, text="1. To connect devices press the button.", font=("Arial", 24), bg='#30302e', fg='#ffffff')
    label.pack(pady=20)

    # Scan button
    scan_button = tk.Button(root, text="Device scan", command=on_scan, bg='#434341', fg='#ffffff')
    scan_button.pack(pady=10)

    # Connect button
    connect_button = tk.Button(root, text="Connect with Device", command=on_connect, bg='#434341', fg='#ffffff')
    connect_button.pack(pady=10)

    root.mainloop()  # Start the Tkinter event loop

# Button functions
def on_scan():
    devices = asyncio.run(scan_for_devices())
    if devices:
        label.config(text=f"Found devices: {[device.name for device in devices]}")

def on_connect():
    # Hier sollte eine Logik implementiert werden, um die Geräte auszuwählen
    label.config(text="Bitte ein Gerät auswählen")

if __name__ == "__main__":
    create_gui()
