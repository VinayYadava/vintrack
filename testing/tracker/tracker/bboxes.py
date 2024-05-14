"""
Bboxes Module
Author: Vinay Kumar Yadav
Github: https://github.com/VinayYadava/vintrack.git
This module provides a class `Bboxes` for handling bounding boxes. The `Bboxes` class allows conversion between different bounding box formats, including (x, y, w, h) and (x1, y1, x2, y2) formats.

Example:
    bounding_boxes = [[1,2,4,5], [1,2,42,52]]
    bboxes_numpy = np.array(bounding_boxes)
    bboxes = Bboxes(bboxes_numpy)
    print(bboxes.to_xyxy())

Classes:
    Bboxes: A class to handle bounding boxes.

"""
import numpy as np

class Bboxes:
    '''
    A class to handle bounding boxes.

    Parameters:
        bboxes (array-like): A list or NumPy array of bounding boxes in (x, y, w, h) format.

    Attributes:
        bboxes (numpy.ndarray): The bounding boxes stored as a NumPy array.
        xyxy (numpy.ndarray): The bounding boxes converted to (x1, y1, x2, y2) format.
    '''
    def __init__(self, bboxes):
        '''
        Initializes Bboxes object with the provided bounding boxes.

        Parameters:
            bboxes (array-like): A list or NumPy array of bounding boxes in (x, y, w, h) format.
        '''
        self.bboxes = bboxes if isinstance(bboxes, np.ndarray) else np.array(bboxes)\
            if isinstance(bboxes, list) else None
        self.xyxy = self.to_xyxy()

    def to_xyxy(self):
        '''
        Converts bounding boxes from (x, y, w, h) format to (x1, y1, x2, y2) format.

        Returns:
            numpy.ndarray: Bounding boxes in (x1, y1, x2, y2) format.
        '''
        boxes = self.bboxes.copy()
        boxes[:,2] += boxes[:,0]
        boxes[:,3] += boxes[:,1]
        return boxes

    def to_xyah(self):
        '''
        Converts bounding boxes from (x, y, w, h) format to (x, y, aspect ratio, height) format.

        Returns:
            numpy.ndarray: Bounding boxes in (x, y, aspect ratio, height) format.
        '''
        boxes = self.bboxes.copy().astype(np.float16)
        boxes[:,2]= np.divide(boxes[:,2] , boxes[:,3])
        return boxes

    def to_xywh(self):
        '''
        Returns the bounding boxes as-is.

        Returns:
            numpy.ndarray: Bounding boxes in (x, y, w, h) format.
        '''
        return self.bboxes
    
    def __repr__(self):
        return f"{self.bboxes}"


if __name__ == "__main__":
    bounding_boxes = [[1,2,4,5], [1,2,42,52]]
    bboxes_numpy = np.array(bounding_boxes)
    bboxes = Bboxes(bboxes_numpy)
    print(bboxes)
    print(bboxes.to_xyah())
