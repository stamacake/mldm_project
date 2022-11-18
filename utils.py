import pickle
from PIL import Image
import os



def save_pickle(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

        
def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
    
    
class ImageSearcher:
    def __init__(self, folder, low_quality_size=300):
        self.folder = folder
        self.low_quality_size = low_quality_size
    
    def find(self, name, low_quality=False):
        files = os.listdir(self.folder)
        cands = [e for e in files if os.path.splitext(e)[0] == name]
        if not cands:
            return None
        
        fp = os.path.join(self.folder, cands[0])
        img = Image.open(fp)
        
        if low_quality:
            s = self.low_quality_size / min(img.size)
            low_size = [int(s*e) for e in img.size]
            img = img.resize(low_size)
            
        return img