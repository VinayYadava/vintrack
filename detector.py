from model import Yolov5n, Yolov5s
class Detector:
    def __init__(self,name ,param=None):
        self.param = param
        valid_names =  ["yolov5n","yolov5s"]
        if name not in valid_names:
            print(f"Error: kindly choose name available in {valid_names}")
            raise NameError
        

        self.model = self.get_model(name,self.param)
    
    def get_model(self,name,param):
        if name == "yolov5n":
            model = Yolov5n.create_model()
            return model
        if name == "yolov5s":
            model = Yolov5s.create_model()
            return model

        
if __name__ == "__main__":
    det = Detector(name = "yolov5s")
    model = det.model
    result = model("download.jpg")
    result.show()

