from model import Yolov5n, Yolov5s

class Detector:
    def __init__(self,model,param=None):
        self.param = param
        self.model = self.get_model(model,self.param)
    
    def get_model(self,name):
        if name == "yolov5n":
            model = Yolov5n.create_model()
            return model
        if name == "yolov5s":
            model = Yolov5s.create_model()
            return model

        
if __name__ == "__main__":
    detector = Detector("yolov5s")
    model = detector.model
    print(model)

