from ultralytics import YOLO

from yolodemo import settings as s


if __name__ == "__main__":
    model = YOLO(s.MODEL, task="detect")
    results = model(s.TEST_IMAGE, conf=s.MINIMUM_CONFIDENCE, imgsz=(s.IMAGE_HEIGHT, s.IMAGE_WIDTH))

    ncnn_model = YOLO(s.NCNN_MODEL, task="detect")
    ncnn_results = ncnn_model(s.TEST_IMAGE, conf=s.MINIMUM_CONFIDENCE, imgsz=(s.IMAGE_HEIGHT, s.IMAGE_WIDTH))
