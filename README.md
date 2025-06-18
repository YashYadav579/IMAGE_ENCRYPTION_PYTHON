# 🖼️ Pixel Manipulation for Image Encryption

This project is a simple Python GUI tool that performs **image encryption and decryption** using **pixel manipulation techniques**. It uses a basic XOR operation on RGB pixel values to encrypt and decrypt images.

---

## 📌 Task Description

> **Task-02: Pixel Manipulation for Image Encryption**  
> Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

---

## 🎯 Features

- ✅ Load an image from file.
- 🔐 Encrypt the image using XOR manipulation.
- 🔓 Decrypt the image using the same XOR key.
- 💾 Save encrypted/decrypted images.
- 🖥️ Simple GUI using Tkinter.

---

## 🛠️ How It Works

Each pixel’s RGB values are encrypted using a symmetric XOR key:

```python
encrypted_pixel = (r ^ key, g ^ key, b ^ key)
```
XOR is symmetric, so the same operation decrypts it:
```
decrypted_pixel = (r ^ key, g ^ key, b ^ key)
```
