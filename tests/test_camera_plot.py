import cv2

import yolodemo.settings as s


def capture_frame(device: cv2.VideoCapture):
    success, img = device.read()
    if not success:
        return

    cv2.putText(img, text=f"test", org=[20, 20], fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 86, 180), thickness=2)
    cv2.rectangle(img, (20, 20), (50, 50), color=(214, 66, 71), thickness=3)
    cv2.imshow('Webcam', img)


if __name__ == "__main__":
    video_capture = cv2.VideoCapture(-1)
    video_capture.set(3, s.IMAGE_HEIGHT)
    video_capture.set(4, s.IMAGE_WIDTH)

    # Event loop
    while True:
        capture_frame(video_capture)

        if cv2.waitKey(1) == ord('q'):
            break

    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()
