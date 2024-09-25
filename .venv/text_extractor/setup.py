from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="text_extractor",
    version="0.1",
    author="Sandra Costa",
    author_email="sandralin.9@gmail.com",
    description="Um pacote para extrair textos de imagens usando pytesseract",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/text_extractor",  # URL do seu repositório (opcional)
    packages=find_packages(),
    install_requires=[
        "pytesseract>=0.3.7",
        "Pillow>=8.0.0",
        "opencv-python>=4.5.1.48"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
