IMAGE_HEIGHT: int = 640
IMAGE_WIDTH: int = 640
MINIMUM_CONFIDENCE: float = 0.70
MODEL: str = "yolo-Weights/yolov8n.pt"  # set to NCNN model for raspberry pi
NCNN_MODEL: str = "yolo-Weights/yolov8n_ncnn_model"
TEST_IMAGE: str = "tests/bus.jpg"
CLASS_NAMES: list[str] = ["persoon", "fiets", "auto", "motorfiets", "vliegtuig", "bus", "trein", "vrachtwagen", "boot",
                          "verkeerslicht", "brandkraan", "stopbord", "parkeermeter", "bank", "vogel", "kat",
                          "hond", "paard", "schaap", "koe", "olifant", "beer", "zebra", "giraf", "rugzak", "paraplu",
                          "handtas", "stropdas", "koffer", "frisbee", "ski's", "snowboard", "sportbal", "vlieger",
                          "honkbalknuppel", "honkbalhandschoen", "skateboard", "surfplank", "tennisracket", "fles",
                          "wijnglas", "beker", "vork", "mes", "lepel", "kom", "banaan", "appel", "sandwich",
                          "sinaasappel", "broccoli", "wortel", "hotdog", "pizza", "donut", "cake", "stoel", "bank",
                          "kamerplant", "bed", "eettafel", "toilet", "tv-monitor", "laptop", "muis",
                          "afstandsbediening", "toetsenbord", "mobiele telefoon", "magnetron", "oven", "broodrooster",
                          "gootsteen", "koelkast", "boek", "klok", "vaas", "schaar", "teddybeer", "haardroger",
                          "tandenborstel"]
