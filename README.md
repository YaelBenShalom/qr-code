# QR code
QR code generation and reader



## QR Code Generation
Install required dependencies:
```
pip install qrcode
```

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
    python3 QR_code_generator.py --url=https://yaelbenshalom.github.io/
    ```
    Output:<br>
    <img class="center" src="https://github.com/YaelBenShalom/qr-code/blob/master/myQR.png">

- Input:
    ```
    python3 QR_code_generator.py --url=https://yaelbenshalom.github.io/ --fill=yellow --back=green
    ```
    Output: <br>
    <img class="center" src="https://github.com/YaelBenShalom/qr-code/blob/master/myQR2.png">



## QR Code Reader
Installing required dependencies:
```
pip install opencv-python
```

To decode a QR code, run:
```
python3 QR_code_reader.py>
```

For example:

- Input:
    ```
    python3 QR_code_reader.py --image=myQR.png
    ```
    Output:<br>
    Website:    https://yaelbenshalom.github.io/
