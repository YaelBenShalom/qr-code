import argparse
import qrcode


def main(args):
    # Load the arguments
    website = args["url"]
    fill_color = args["fill"]
    back_color = args["back"]
    box_size = args["size"]
    border = args["border"]

    image_name = "images/myQR.png"

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(website)
    qr.make()

    # Generate QR code image and save it
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(image_name)


if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="website URL")
    parser.add_argument("--fill", default="black",
                        help="fill color. default=black")
    parser.add_argument("--back", default="white",
                        help="background color. default=white")
    parser.add_argument("--size", default=10, help="box size. default=10")
    parser.add_argument("--border", default=4, help="border size. default=4")
    args = vars(parser.parse_args())
    main(args)
