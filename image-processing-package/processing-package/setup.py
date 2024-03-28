from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Descrição dos parametros dos pacote de processamento de imagem
setup(
    name="image_processing",
    version="0.0.1",
    author="Velcides Mezzomo",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Velcides/Processamento-de-Imagens-com-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)