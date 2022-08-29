# places365_tagger_web
Uses pretraind Resnet50 on Places365 (https://github.com/CSAILVision/places365)  
Supported operations: get_tags

```pip3 install -r requirements.txt```  
You should install torch yourself https://pytorch.org/get-started/locally/.


```generate_tags.py ./path_to_img_folder``` -> generates tags, places them in id_tags.txt  
```image_tags_web.py``` -> web microservice   
