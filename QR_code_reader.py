import argparse
import cv2


def main(args):
    # Load the arguments
    image_name = args["image"]

    # Read QR code image
    image = cv2.imread("images/myQR.png")

    # Decode QR code image
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(image)

    # If a QR code is detected
    if bbox is not None:
        print("Website:\t{}".format(data))

        # Display the image with with detected bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i + 1) % n_lines][0])
            cv2.line(image, point1, point2, color=(255, 0, 0), thickness=2)

    # display the result
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="QR code image")
    args = vars(parser.parse_args())
    main(args)
