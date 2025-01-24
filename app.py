from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import time

def generate_key():
    """Generate a key and save it to a file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Key generated and saved to 'key.key'.")

def load_key():
    """Load the key from the 'key.key' file."""
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    """Encrypt the contents of a file."""
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", f"File '{file_path}' has been encrypted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def decrypt_file(file_path):
    """Decrypt the contents of a file."""
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", f"File '{file_path}' has been decrypted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {e}")

def select_file(operation):
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All Files", "*.*")])
    if not file_path:
        return
    if operation == "encrypt":
        encrypt_file(file_path)
    elif operation == "decrypt":
        decrypt_file(file_path)

def animate_progress_bar(progress_bar):
    for i in range(101):
        time.sleep(0.01)
        progress_bar["value"] = i
        progress_bar.update()

def main():
    root = tk.Tk()
    root.title("File Encrypt/Decrypt")
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 10), padding=5)
    style.configure("TProgressbar", thickness=10)

    canvas = tk.Canvas(root, width=500, height=300, bg="#f0f0f0", highlightthickness=0)
    canvas.create_oval(-150, -150, 650, 650, fill="#e3f2fd", outline="")
    canvas.pack(fill="both", expand=True)

    header = tk.Label(root, text="File Encryption & Decryption", font=("Helvetica", 18, "bold"), bg="#e3f2fd", fg="#333")
    header.place(relx=0.5, rely=0.2, anchor="center")

    progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(relx=0.5, rely=0.35, anchor="center")

    btn_generate = ttk.Button(root, text="Generate Key", command=lambda: [animate_progress_bar(progress_bar), generate_key()])
    btn_generate.place(relx=0.5, rely=0.5, anchor="center", width=200)

    btn_encrypt = ttk.Button(root, text="Encrypt File", command=lambda: [animate_progress_bar(progress_bar), select_file("encrypt")])
    btn_encrypt.place(relx=0.5, rely=0.6, anchor="center", width=200)

    btn_decrypt = ttk.Button(root, text="Decrypt File", command=lambda: [animate_progress_bar(progress_bar), select_file("decrypt")])
    btn_decrypt.place(relx=0.5, rely=0.7, anchor="center", width=200)

    btn_exit = ttk.Button(root, text="Exit", command=root.quit)
    btn_exit.place(relx=0.5, rely=0.8, anchor="center", width=200)

    root.mainloop()

if __name__ == "__main__":
    main()
