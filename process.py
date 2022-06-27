from PIL import Image
import os
from torchvision import transforms

def read(path):
    with open(path,'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')
    

root = r'C:\Users\v-xiaodwang\home\Super-Resolution\DIV2K_valid_HR\DIV2K_valid_HR'
# file = '0437.png'
# img = read(os.path.join(root,file))

trans = transforms.Compose([
    transforms.CenterCrop(648),
    transforms.Resize(1024)]
)
# trans_img = trans(img)
des = os.path.join(r'C:\Users\v-xiaodwang\home\Super-Resolution\DIV2K_valid_HR','1k')
if not os.path.exists(des):
    os.makedirs(des)

# trans_img.save(os.path.join(des,'0437_1024x1024.png'),quality=95)
files = os.listdir(root)
cnt=0
for file in files:
    suffix = os.path.splitext(file)[-1]
    if suffix == '.jpg' or suffix == '.png':
        cnt += 1
        img = read(os.path.join(root,file))
        w, h = img.size[0], img.size[1]
        print(cnt,img.size)
        mins = min(w,h)
        trans = transforms.Compose([
            transforms.CenterCrop(mins),
            transforms.Resize(1024)]
        )
        trans_img = trans(img)
    trans_img.save(os.path.join(des,file),quality=95)
# print(minh, minw, cnt)#648, 1116
## crop 1024x1024, if < 1024, 648x648 