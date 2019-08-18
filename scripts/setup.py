import urllib.request
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.makedirs('../test_data', exist_ok=True)

urllib.request.urlretrieve('https://github.com/altseed/OpenSoundMixer2/releases/download/TestData/bgm1.ogg', '../test_data/bgm1.ogg')
urllib.request.urlretrieve('https://github.com/altseed/OpenSoundMixer2/releases/download/TestData/se1.wav', '../test_data/se1.wav')



        
