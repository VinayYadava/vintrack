import torch
class Yolov5n:
    def create_model(debug=False):
        if debug:
            try:
                model = torch.hub.load(
                    repo_or_dir="ultralytics/yolov5",
                    model = "yolov5n",
                    pretrained = True
                )
            except Exception as e:
                print("Error Occured in pytorch_yolo5n.py while creating model")
                print(e)
        else:
            model = torch.hub.load(
                repo_or_dir="ultralytics/yolov5",
                model = "yolov5n",
                pretrained = True
            )
            

        return model


if __name__=="__main__":
    print("-------------------Executing tests in  'pytorch_yolo5n.py'------------------")
    try:
        print("creating model...")
        model= Yolov5n.create_model()

    except Exception as e:
        print("Error Occured in pytorch_yolo5n.py while creating model")
        print(e)

    ""
    print("Deleting garbage values.")
    del(model)