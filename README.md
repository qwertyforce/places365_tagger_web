# places365_tagger_web
Uses pretraind Resnet50 on Places365 (https://github.com/CSAILVision/places365)  
Supported operations: get_tags

```pip3 install -r requirements.txt```  
You should install torch yourself https://pytorch.org/get-started/locally/.


```generate_tags.py ./path_to_img_folder``` -> generates tags, places them in id_tags.txt  
```image_tags_web.py``` -> web microservice   
### Docker
build image - ```docker build -t qwertyforce/image_tags_web:1.0.0 --network host -t qwertyforce/image_tags_web:latest ./```  

run as deamon - ```docker run -d --rm -p 127.0.0.1:33341:33341 --network=ambience_net --name image_tags_web qwertyforce/image_tags_web:1.0.0``` 
