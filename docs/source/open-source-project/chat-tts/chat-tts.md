# ChatTTS

<https://github.com/2noise/ChatTTS>
<https://colab.research.google.com/drive/1Vu4f3nPIE9vCpevtiyca79HPbCTb77Cs?usp=sharing>

## Installation on Ubuntu

``` sh
conda create -n chattts python=3.11
conda activate chattts

git clone https://github.com/2noise/ChatTTS.git
cd ChatTTS
pip install -r requirements.txt
# conda install -c conda-forge cudatoolkit=12.1 cudnn=8.9
pip install gradio
pip install WeTextProcessing
conda install -c conda-forge pynini=2.1.5 && pip install nemo_text_processing
```
