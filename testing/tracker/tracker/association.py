''' 
Association Marix to implement association matrix 2024.
Name: Vinay Kumar Yadav
Email: vinay.yadav4501@gmail.com
Github: VinayYadava
'''
import numpy as np
class AssociationMatrix:
    def __init__(self,previous , current ,det_format = "xywh"):
        self.previous = previous # prev detections
        self.current = current # current detections
        self.association_matrix   = None
        self.association_matrix   = self.get_association_matrix(previous=previous , current=current )
        self.next = self.get_next()

    def get_association_matrix( self):
        m,n = len(self.previous),len(self.current)
        association_matrix  = np.zeros((m,n))
        self.previous = self.previous
        self.current = self.current
        return association_matrix  
    def get_next(self):
        print("")

if __name__ == "__main__":
    m_predictions = np.array([[1, 2, 3, 4],    # Format: [x, y, w, h]
                               [2, 3, 4, 5],
                               [3, 4, 5, 6]])

    n_predictions = np.array([[5, 6, 7, 8],
                               [6, 7, 8, 9]])

    all_predictions = np.stack((n_predictions , m_predictions) , axis = 0) 
    reshaped_predictions = all_predictions.reshape(all_predictions.shape[0], -1)
    covariance_matrix = np.cov(reshaped_predictions, rowvar=False)