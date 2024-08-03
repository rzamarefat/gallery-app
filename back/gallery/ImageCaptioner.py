from typing import Any
from transformers import BlipProcessor, BlipForConditionalGeneration

class ImageCaptioner:
    def __init__(self) -> None:
        self._processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self._model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def __call__(self, img):
        inputs = self._processor(img, return_tensors="pt")
        out = self._model.generate(**inputs)
        caption = self._processor.decode(out[0], skip_special_tokens=True)
        
        return caption