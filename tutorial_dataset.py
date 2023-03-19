import json
import cv2
import numpy as np
import os
from torch.utils.data import Dataset

json_path = r'C:\Users\guodi\Desktop\camouflaged_dataset\camo_diff\testjson_dict.json'

class MyDataset(Dataset):
    def __init__(self):
        self.data = []
        with open(json_path, 'rt') as f:
            for line in f:
                self.data = json.loads(line)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        source_filename = item['source']
        target_filename = item['target']
        prompt = item['prompt']


        source = cv2.imread(os.path.join(r"C:\Users\guodi\Desktop\camouflaged_dataset", source_filename))
        target = cv2.imread(os.path.join(r"C:\Users\guodi\Desktop\camouflaged_dataset", target_filename))

        # Do not forget that OpenCV read images in BGR order.
        source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

        # Normalize source images to [0, 1].
        source = source.astype(np.float32) / 255.0

        # Normalize target images to [-1, 1].
        target = (target.astype(np.float32) / 127.5) - 1.0

        return dict(jpg=target, txt=prompt, hint=source)

dataset = MyDataset()
print(len(dataset))

item = dataset[1234]
jpg = item['jpg']
txt = item['txt']
hint = item['hint']
print(txt)
print(jpg.shape)
print(hint.shape)