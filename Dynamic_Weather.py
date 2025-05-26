import imgaug.augmenters as iaa
import os
from PIL import Image
import numpy as np

def pil_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

# 定义增强环境
environments = {
    'dark': iaa.Sequential([iaa.MultiplyAndAddToBrightness(mul=0.4, add=-10, seed=1991)]),
    'fog': iaa.Sequential([iaa.CloudLayer(
        intensity_mean=215, intensity_freq_exponent=-2, intensity_coarse_scale=2, alpha_min=1.0,
        alpha_multiplier=0.6, alpha_size_px_max=10, alpha_freq_exponent=-2, sparsity=0.7, density_multiplier=0.6, seed=35)]),
    'light': iaa.Sequential([iaa.MultiplyAndAddToBrightness(mul=1.3, add=(0, 30), seed=1992)]),
    'wind': iaa.Sequential([iaa.MotionBlur(15, seed=17)])
}

# 输入文件夹路径（包含所有待处理图像）
input_folder = './drone_dataset/university1652_test'
# 输出文件夹路径（保存增强后的图像）
output_folder = './drone_dataset/university1652_test/img_aug'

# 获取输入文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

# 遍历每个图像文件
for image_file in image_files:
    # 构造完整的图像路径
    img_path = os.path.join(input_folder, image_file)
    
    # 加载图像
    img = pil_loader(img_path)
    img = np.array(img)
    
    # 对每种环境进行增强并保存
    for env_name, seq in environments.items():
        # 创建对应环境的输出子文件夹
        env_output_folder = os.path.join(output_folder, env_name)
        os.makedirs(env_output_folder, exist_ok=True)
        
        # 应用增强
        img_aug = seq(image=img)
        img_aug = Image.fromarray(img_aug)
        
        # 保存增强后的图像
        output_path = os.path.join(env_output_folder, image_file)
        img_aug.save(output_path)

print("图像增强完成，结果已保存至指定文件夹。")
