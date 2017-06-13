from distutils.core import setup

setup(
    name='Breseq_Extracor',
    version='1.0.0',
    packages=['Hansel_HTMLscrapper'],
    url='www.sahilshetye.com',
    license='Apache',
    author='sahilshetye',
    author_email='sahildevilster@gmail.com',
    description='Breseq Extractor for  extracting data from HTML output file generated in Breseq',
    install_requires=['beautifulsoup4','lxml','Cython','PyVCF','genomediff','mysql-connector-python-rf','samtools-tool','setuptools','protobuf','pysam']
)
