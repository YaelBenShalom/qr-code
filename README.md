# QR code

QR code generation and reader

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [QR Code Generation](#qr-code-generation)
  - [QR Code Reader](#qr-code-reader)

## Description

This repository contains my implementation of QR Code generation and reader, and is based on `qrcode` and `OpenCV`.

## Installation

Install required dependencies:

To install `qrcode` from the command line:

```
pip install qrcode
```

To install `opencv` from the command line:

```
pip install opencv-python
```

## Usage:

### QR Code Generation

To create a QR code from a URL, run:

```
python3 QR_code_generator.py --url=<website-url>
```

You can also change the fill/background color or the box/border size:

```
python3 QR_code_generator.py --url=<website-url> --fill=<fill-color> --back=<background-color> --size=<box-size> --border=<border-size>
```

For example:

- Input:
  ```
  python3 QR_code_generator.py --url=https://yaelbenshalom.github.io
  ```

  Output:<br>
  <p align="center">
     <img style="text-align: center" src="https://github.com/YaelBenShalom/qr-code/blob/master/images/myQR.png" width=30%>
  </p>

- Input:
  ```
  python3 QR_code_generator.py --url=https://yaelbenshalom.github.io --fill=yellow --back=green --border=1
  ```

  Output:<br>
  <p align="center">
     <img style="text-align: center" src="https://github.com/YaelBenShalom/qr-code/blob/master/images/myQR2.png" width=30%>
  </p>

Check out this QR code!

### QR Code Reader

To decode a QR code from image, run:

```
python3 QR_code_reader.py --image=<image-name>
```

For example:

- Input:
  ```
  python3 QR_code_reader.py --image=myQR.png
  ```
  Output:
  ```
  Website:    https://yaelbenshalom.github.io
  ```

By the way, this is my personal portfolio. You should scan it and check it out!
