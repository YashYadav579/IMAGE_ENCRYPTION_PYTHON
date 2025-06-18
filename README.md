# 🖼️ PRODIGY_CS_02 - Image Encryption using Pixel Manipulation (GUI Version)

### ✅ Internship Task - Prodigy Infotech (Cyber Security Track)

This repository contains **Task 02** of the **Prodigy Infotech Cyber Security Internship**, where I developed a **simple image encryption and decryption tool** using **Python**, **Pillow**, and a **Tkinter-based GUI**.  
The tool encrypts images by manipulating their pixel values using a symmetric XOR operation.

---

## 🧠 What is Pixel-Based Image Encryption?

Pixel manipulation involves modifying each pixel of an image to make it unrecognizable without the correct decryption key. In this project, each pixel’s **RGB** values are **XOR’ed with a secret key** for encryption and the same operation reverses it for decryption.

Example:  
Encrypted: R' = R ^ key  
Decrypted: R = R' ^ key

---

## 🎯 Features of This Project

- 🖼️ Load any image (PNG, JPG, etc.)
- 🔐 Encrypt the image using a basic XOR pixel operation
- 🔓 Decrypt the image using the same XOR key
- 🧮 Simple pixel-level manipulation logic
- 🖥️ GUI built using `Tkinter` for user interaction
- 💾 Save encrypted and decrypted images with one click

---

## 📂 File Structure

PRODIGY_CS_02/

├── pixel_encryption_gui.py # Main Python GUI application

└── README.md # Project documentation


---

## 🛠️ How to Run

> ⚠️ Ensure Python 3.x is installed.

### 👉 Steps:

1. **Clone the repository**:
```bash
git clone https://github.com/YashYadav579/PRODIGY_CS_02.git
```

2. **Navigate to the project folder**:
```bash
cd PRODIGY_CS_02
```

3. **Install Pillow (if not already installed)**:
```bash
pip install pillow
```

4. **Run the GUI application**:
```bash
python pixel_encryption_gui.py
```
💡 A window will appear where you can choose to encrypt or decrypt images.

---

## 🙋‍♂️ About Me

**Name**: _Yash Yadav_  
**Intern** @ **Prodigy Infotech** – Cyber Security Track  
**Task**: _Pixel-Based Image Encryption using Python_  
**Task ID**: PRODIGY_CS_02  

---

## 🔗 Connect with Me

- 💼 [LinkedIn](https://www.linkedin.com/in/yashyadav-5790abc/)
- 💻 [GitHub](https://github.com/YashYadav579)

---

## 🏁 Conclusion

This project enhanced my understanding of:
- Image processing using Python
- Pixel-level data encryption using XOR
- GUI development with Tkinter
- Real-world implementation of encryption concepts

Special thanks to Prodigy Infotech for this hands-on learning opportunity!
