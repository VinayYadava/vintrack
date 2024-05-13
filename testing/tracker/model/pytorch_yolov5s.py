import torch
class Yolov5s:
    def create_model():
        try:
            model = torch.hub.load(
                repo_or_dir="ultralytics/yolov5",
                model = "yolov5s",
                pretrained = True
            )
        except Exception as e:
            print("Error Occured in pytorch_yolo5s.py while creating model")
            print(e)

        return model


if __name__=="__main__":
    print("-------------------Executing tests in  'pytorch_yolo5s.py'------------------")
    try:
        print("creating model...")
        model= Yolov5s.create_model()

    except Exception as e:
        print("Error Occured in pytorch_yolo5s.py while creating model")
        print(e)

    ""
    print("Deleting garbage values.")
    del(model)