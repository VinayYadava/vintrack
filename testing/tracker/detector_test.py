from detector import Detector

if __name__ == "__main__":
    det = Detector(name = "yolov5s")
    model = det.model
    result = model("download.jpg")
    result.show()
