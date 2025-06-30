# 🖼️ Image Encryption using Pixel Manipulation (GUI Version)

### ✅ Project Task - (Cyber Security Track)

In this Task, I developed a **simple image encryption and decryption tool** using **Python**, **Pillow**, and a **Tkinter-based GUI**.  
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

```bash
IMAGE_ENCRYPTION_PYTHON/   
├── pixel_encryption_gui.py       # Main Python GUI application   
├── README.md                     # Project documentation   
├── input_image.png               # Original input image   
├── encrypted_image.png           # Encrypted output  
└── decrypted_image.png           # Decrypted output   
```

---

## 🖥️ GUI Preview

![image](https://github.com/user-attachments/assets/9d016404-d6e6-4743-8460-1ccdf74e49d8))
![image](https://github.com/user-attachments/assets/594e4246-bf99-429e-a919-78fd906a84b4)

---

## 📸 Image Preview

| 🖼️ Input Image | 🔐 Encrypted Image | 🔓 Decrypted Image |
|----------------|-------------------|--------------------|
| ![Input](https://github.com/user-attachments/assets/6d7afc84-b461-4172-82da-16783924872a) | ![Encrypted](https://github.com/user-attachments/assets/dfddd196-8d07-49f2-8cad-ff454949ef03) | ![Decrypted](https://github.com/user-attachments/assets/c7446b62-1af4-4255-ad6b-290cc9ce987b) |


> The encrypted image will appear scrambled, while the decrypted image matches the original input.

---

## 🛠️ How to Run

> ⚠️ Ensure Python 3.x is installed.

### 👉 Steps:

1. **Clone the repository**:
```bash
git clone https://github.com/YashYadav579/IMAGE_ENCRYPTION_PYTHON.git
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
**Task**: _Pixel-Based Image Encryption using Python_  

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
