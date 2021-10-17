# install this in terminal before using easyocr
# pip install torch torchvision torchaudio
# pip install easyocr

# importing easyocr
import easyocr

# reading the image
IMAGE_PATH = 'Sample_quote.jpg'

# setting the reader to english and GPU to false(since there's no CUDA)
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)

# printing the lines
for i in result:
    print(i[1])
