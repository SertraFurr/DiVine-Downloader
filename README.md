
# Divine.Video Downloader

A tiny script to download new https://divine.video videos.


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-Apache_2.0-green.svg?style=for-the-badge" alt="License">
</p>

# ⚡ Features

- Accepts a full https://divine.video/video/... URL or just the raw 64-character hex event ID
- Connects directly to the official relay wss://relay.divine.video/

# 📋 Requirements

Install the dependencies:
```Bash
pip install websocket-client, requests
```
or
```Bash
pip install -r requirements.txt
```

# 📖 Usage
```
# With full URL
python main.py https://divine.video/video/61df2bd8fe70296338c0f73cca336011c071ac6ed6f2f5fa9efebf7d1659c6e4


# Or with just the event ID
python main.py 61df2bd8fe70296338c0f73cca336011c071ac6ed6f2f5fa9efebf7d1659c6e4
```

# ✅ Example output
```bash
python main.py https://divine.video/video/61df2bd8fe70296338c0f73cca336011c071ac6ed6f2f5fa9efebf7d1659c6e4
Connecting to relay... wss://relay.divine.video/
Video URL: https://cdn.divine.video/74509dbb704b9adc869aa14c7e46b4a078a06e12a1b6accdec2da929f4cc9326.mp4
Trying to download video...
Video downloaded successfully as 74509dbb704b9adc869aa14c7e46b4a078a06e12a1b6accdec2da929f4cc9326.mp4
Download completed. Saved in ./DiVine/
```
<div align="center">

## 🤝 Contributing


We welcome contributions! Here's how you can help:

[![Issues](https://img.shields.io/badge/Issues-Welcome-blue?style=for-the-badge)](https://github.com/sertrafurr/DiVine-Downloader/issues)
[![Pull Requests](https://img.shields.io/badge/PRs-Welcome-green?style=for-the-badge)](https://github.com/sertrafurr/DiVine-Downloader/pulls)
[![Discussions](https://img.shields.io/badge/Discussions-Join-purple?style=for-the-badge)](https://github.com/sertrafurr/DiVine-Downloader/discussions)

</div>
<div align="center">

### 🐛 Found a Bug?
 Check existing [issues](https://github.com/sertrafurr/DiVine-Downloader/issues)
 Create a new issue with:
    📝 Clear description
    🔄 Steps to reproduce

### 💡 Feature Request?
 Open a [discussion](https://github.com/sertrafurr/DiVine-Downloader/discussions)
 Explain your idea
 Community feedback welcome!

---
<div align="center">

## 📄 License

<div align="center">

This project is licensed under the **Apache 2.0 License**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg?style=for-the-badge)](https://opensource.org/license/apache-2-0)

</div>

---
<div align="center">

## ⚠️ Disclaimer

<strong>📢 Important Notice</strong>

- 🎯 This tool is for **educational purposes** only


<div align="center">

## 🙏 Acknowledgments

<img src="https://img.shields.io/badge/Made_with-❤️-red?style=for-the-badge">

---

### 🌟 Star this repo if it helped you!
