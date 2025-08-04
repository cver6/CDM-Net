# CDM-Net : A Framework for Cross-View Geo-localization with Multimodal Data

Installation using conventional LSD is as follows:
```
sudo apt-get install build-essential cmake libopencv-dev
git clone --recursive https://github.com/iago-suarez/pytlsd.git
cd pytlsd
pip3 install -r requirements.txt
pip3 install .
```

## Dataset

The release of the extraction code depends on the acceptance of the paper

### 1.CVGL-RGBT link: https://pan.baidu.com/s/1rFCCOiw00WkKu52jDsGa_g

Some examples of the RGBT dataset
![RGBT](RGBT.png)


### 2.Urban-500   link:  https://pan.baidu.com/s/16OXb636QKVv8D07lcshnvA

Some examples of the Urban-500 dataset
![Urban](Urban500.png)


### 3.For Multi-Weather University-1652 use Dynamic_Weather.py to generate

**Set mode=1:**

img_aug/

├── dark/

├── fog/

├── light/

└── wind/
![weather](weather.png)

**mode=2:**

img_aug/

├── rain/

├── snow/

├── fog_rain/

└── fog_snow/

## Acknowledgements

[University1652](https://github.com/layumi/University1652-Baseline)

[SUES-200-Benchmark](https://github.com/Reza-Zhu/SUES-200-Benchmark)

[GeoText-1652](https://github.com/MultimodalGeo/GeoText-1652)

[Janus](https://github.com/deepseek-ai/Janus)

[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL)

[IP-Adapter](https://github.com/tencent-ailab/IP-Adapter)

[glue-factory](https://github.com/cvg/glue-factory)

