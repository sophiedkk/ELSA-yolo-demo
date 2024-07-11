import cv2
from ultralytics import YOLO

import settings as s


def capture_and_process_frames(model: YOLO):
    results = model("tcp://127.0.0.1:8888", stream=True, conf=s.MINIMUM_CONFIDENCE, imgsz=(s.IMAGE_HEIGHT, s.IMAGE_WIDTH))
    for r in results:
        img = r.orig_img
        for box in r.boxes:
            x1, y1, x2, y2 = [int(value) for value in box.xyxy[0]]
            box_class = s.CLASS_NAMES[int(box.cls[0])]

            cv2.rectangle(img, (x1, y1), (x2, y2), color=(214, 66, 71), thickness=3)
            cv2.putText(img, text=f"{box_class}: {box.conf[0] * 100:.0f}%", org=[x1, y1], fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=(255, 86, 180), thickness=2)
    cv2.imshow("Webcam", img)
    


if __name__ == "__main__":
    yolo_model = YOLO(s.MODEL, task="detect")

    # Event loop
    while True:
        capture_and_process_frames(yolo_model)

        if cv2.waitKey(1) == ord("q"):
            break

    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()
