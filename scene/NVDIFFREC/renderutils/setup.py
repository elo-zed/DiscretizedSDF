# setup.py
import os
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# 获取所有源文件
source_files = [
    'c_src/mesh.cu',
    'c_src/loss.cu',
    'c_src/bsdf.cu',
    'c_src/normal.cu',
    'c_src/cubemap.cu',
    'c_src/common.cpp',
    'c_src/torch_bindings.cpp'
]

# 统一的 C++ 和 CUDA 编译选项
# 注意：大部分 PyTorch 环境设置（如 TORCH_CUDA_ARCH_LIST）
# 在使用 setup.py 和 CUDAExtension 时会自动处理
common_opts = ['-DNVDR_TORCH']

setup(
    name='renderutils_plugin', # 扩展的名称
    version='1.0',
    author='Your Name', # 替换为你的名字
    description='A custom PyTorch CUDA extension for rendering utilities.',
    
    # 告诉 setuptools 这是扩展模块
    ext_modules=[
        CUDAExtension(
            name='renderutils_plugin', # 再次指定模块名
            sources=source_files,
            extra_compile_args={
                'cxx': common_opts, # C++ 编译选项
                'nvcc': common_opts  # CUDA 编译选项
            },
            # 注意：在 setup.py 中，通常不需要手动指定 -lcuda 或 -lnvrtc，
            # PyTorch 的 BuildExtension 会自动链接这些必需的库。
            # 如果你的项目需要额外的库，可以在这里添加：
            # extra_link_args=ldflags, 
        ),
    ],
    
    # 使用自定义的 BuildExtension
    cmdclass={
        'build_ext': BuildExtension.with_options(use_ninja=False) # 可以选择启用或禁用 Ninja
    },
    
    # 示例：如果项目包含其他 Python 文件
    # packages=find_packages(),
)