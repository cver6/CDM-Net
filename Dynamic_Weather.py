import imgaug.augmenters as iaa
import os
from PIL import Image
import numpy as np

def pil_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

# 设置模式：1为基础四种模式，2为雨雪雾组合模式
mode = 1

# 定义增强环境
if mode == 1:
    environments = {
        'dark': iaa.Sequential([iaa.MultiplyAndAddToBrightness(mul=0.4, add=-15, seed=1991)]),
        'fog': iaa.Sequential([iaa.CloudLayer(
            intensity_mean=215, intensity_freq_exponent=-2, intensity_coarse_scale=2, alpha_min=1.0,
            alpha_multiplier=0.6, alpha_size_px_max=10, alpha_freq_exponent=-2, sparsity=0.7, density_multiplier=0.6, seed=35)]),
        'light': iaa.Sequential([iaa.MultiplyAndAddToBrightness(mul=1.3, add=(0, 30), seed=1992)]),
        'wind': iaa.Sequential([iaa.MotionBlur(15, seed=17)])
    }
elif mode == 2:
    environments = {
        'rain': iaa.Sequential([iaa.Rain(drop_size=(0.05, 0.1), speed=(0.04, 0.06), seed=38),
                               iaa.Rain(drop_size=(0.05, 0.1), speed=(0.04, 0.06), seed=35),
                               iaa.Rain(drop_size=(0.1, 0.2), speed=(0.04, 0.06), seed=73),
                               iaa.Rain(drop_size=(0.1, 0.2), speed=(0.04, 0.06), seed=93),
                               iaa.Rain(drop_size=(0.05, 0.2), speed=(0.04, 0.06), seed=95)]),
        'snow': iaa.Sequential([iaa.Snowflakes(flake_size=(0.5, 0.8), speed=(0.007, 0.03), seed=38),
                               iaa.Snowflakes(flake_size=(0.5, 0.8), speed=(0.007, 0.03), seed=35),
                               iaa.Snowflakes(flake_size=(0.6, 0.9), speed=(0.007, 0.03), seed=74),
                               iaa.Snowflakes(flake_size=(0.6, 0.9), speed=(0.007, 0.03), seed=94),
                               iaa.Snowflakes(flake_size=(0.5, 0.9), speed=(0.007, 0.03), seed=96)]),
        'fog_rain': iaa.Sequential([iaa.CloudLayer(intensity_mean=225, intensity_freq_exponent=-2, intensity_coarse_scale=2, alpha_min=1.0,
                                   alpha_multiplier=0.9, alpha_size_px_max=10, alpha_freq_exponent=-2, sparsity=0.9, density_multiplier=0.5, seed=35),
                                   iaa.Rain(drop_size=(0.05, 0.2), speed=(0.04, 0.06), seed=35),
                                   iaa.Rain(drop_size=(0.05, 0.2), speed=(0.04, 0.06), seed=36)]),
        'fog_snow': iaa.Sequential([iaa.CloudLayer(intensity_mean=225, intensity_freq_exponent=-2, intensity_coarse_scale=2, alpha_min=1.0,
                                   alpha_multiplier=0.9, alpha_size_px_max=10, alpha_freq_exponent=-2, sparsity=0.9, density_multiplier=0.5, seed=35),
                                   iaa.Snowflakes(flake_size=(0.5, 0.9), speed=(0.007, 0.03), seed=35),
                                   iaa.Snowflakes(flake_size=(0.5, 0.9), speed=(0.007, 0.03), seed=36)])
    }

# 输入文件夹路径（包含所有待处理图像）
input_folder = '/media/hk/soft/zx/drone_dataset/tgrs_duibi-method/Safe-Net/data/University-Release/test/query_drone'
# 输出文件夹路径（保存增强后的图像）
output_folder = '/media/hk/soft/zx/drone_dataset/tgrs_duibi-method/Safe-Net/data/University-Release/test/img_aug'

print(f"当前运行模式: {mode}")
print(f"增强类型: {list(environments.keys())}")

# 遍历query_drone下的所有子文件夹
for root, dirs, files in os.walk(input_folder):
    # 获取相对于input_folder的相对路径
    relative_path = os.path.relpath(root, input_folder)
    
    # 过滤出图像文件
    image_files = [f for f in files if f.lower().endswith(('jpg', 'jpeg', 'png'))]
    
    # 如果当前文件夹有图像文件，则进行处理
    if image_files:
        print(f"正在处理文件夹: {relative_path}")
        
        # 遍历每个图像文件
        for image_file in image_files:
            # 构造完整的图像路径
            img_path = os.path.join(root, image_file)
            
            # 加载图像
            img = pil_loader(img_path)
            img = np.array(img)
            
            # 对每种环境进行增强并保存
            for env_name, seq in environments.items():
                # 创建对应环境的输出子文件夹，保持原有目录结构
                if relative_path == '.':
                    # 如果是根目录下的图片
                    env_output_folder = os.path.join(output_folder, env_name)
                else:
                    # 如果是子文件夹下的图片，保持原有结构
                    env_output_folder = os.path.join(output_folder, env_name, relative_path)
                
                os.makedirs(env_output_folder, exist_ok=True)
                
                # 应用增强
                img_aug = seq(image=img)
                img_aug = Image.fromarray(img_aug)
                
                # 保存增强后的图像，保持原有文件名
                output_path = os.path.join(env_output_folder, image_file)
                img_aug.save(output_path)

print("图像增强完成，结果已保存至指定文件夹。")
