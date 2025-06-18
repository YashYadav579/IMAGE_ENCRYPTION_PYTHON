from tkinter import filedialog, Tk, Button, Label
from PIL import Image

# XOR-based simple encryption/decryption
def process_image(path, key, mode):
    img = Image.open(path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            if mode == "encrypt":
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)
            else:  # decrypt
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    return img

# GUI Functions
def encrypt_image():
    path = filedialog.askopenfilename()
    img = process_image(path, key=123, mode="encrypt")
    img.save("encrypted_image.png")
    Label(window, text="Image Encrypted and Saved!").pack()

def decrypt_image():
    path = filedialog.askopenfilename()
    img = process_image(path, key=123, mode="decrypt")
    img.save("decrypted_image.png")
    Label(window, text="Image Decrypted and Saved!").pack()

# GUI
window = Tk()
window.title("Image Encryption Tool")
window.geometry("300x200")

Label(window, text="Pixel Manipulation Tool").pack(pady=10)
Button(window, text="Encrypt Image", command=encrypt_image).pack(pady=5)
Button(window, text="Decrypt Image", command=decrypt_image).pack(pady=5)

window.mainloop()
