# EasyPDF2Image

## Table of Contents

- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [Installation](#installation)

**Note:** This repository inlcuding script was created using strategic prompting on `Gemini` and `ChatGPT o1`, starting with zero-shot, then few-shot, and refining through iteration.

---

## Introduction

**EasyPDF2Image** is a simple Python script that converts PDF files into image formats like PNG or JPEG. This tool makes it easy to turn each page of a PDF into separate image files, which can be useful for presentations, sharing, or archiving.

---

## Motivation

I created **EasyPDF2Image** to help my colleague who was manually converting PDF files to images by taking screenshots of each page. This method was time-consuming and not very efficient. Additionally, my colleague did not want to upload sensitive PDF files to online services because of confidentiality concerns.

To solve these problems, I developed this script to allow secure and quick conversion of PDF files to images directly on a local computer. This way, all files remain safe and private.

---

## Features

- **Convert Multiple PDFs:** Process several PDF files at once by placing them in the `input` folder.
- **Choose Image Format:** Select between PNG and JPEG formats for the output images.
- **Organized Output:** All images are saved in the `output` folder with clear names like `document_page_1.png`.
- **Local Processing:** Converts files on your computer without needing an internet connection, ensuring your data stays private.
- **Easy to Use:** Simple command-line prompts guide you through the conversion process.

---

## Installation

Follow these steps to set up **EasyPDF2Image** on your local machine:

### 1. **Clone the Repository**

Open your terminal or command prompt and run:

```bash
git clone https://github.com/siddqamar/EasyPDF2Image.git
```

### 2. **Navigate to the Project Directory**

```bash
cd EasyPDF2Image
```

### 3. **Create a Virtual Environment**

It's a good practice to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

### 4. **Activate the Virtual Environment**

```bash
venv\Scripts\activate
```

### 5. **Install Dependencies**

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
