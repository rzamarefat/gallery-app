from .adaface_utils import build_model
import torch
import gdown
import os

class AdaFace:
    def __init__(self, device):
        self._device = device

        os.makedirs(os.path.join(os.getcwd(), ".ckpts"), exist_ok=True)
        

        self._backbone_name = "ir_101_webface_12m"

        if self._backbone_name == "ir_101_webface_12m":
            arch_type = "ir_50"
            self._ckpt_path = os.path.join(os.getcwd(), ".ckpts", "adaface_ir50_ms1mv2.ckpt")

            if not(os.path.isfile(self._ckpt_path)):
                gdown.download(
                    "https://drive.google.com/uc?id=1eUaSHG4pGlIZK7hBkqjyp2fc2epKoBvI",
                    self._ckpt_path,
                    quiet=False
                )
        
        self._model = build_model(arch_type=arch_type)

        try:
            statedict = torch.load(self._ckpt_path, map_location=torch.device(self._device))['state_dict']
            model_statedict = {key[6:]:val for key, val in statedict.items() if key.startswith('model.')}
            self._model.load_state_dict(model_statedict)
            self._model.to(self._device)
            self._model.eval()
        except Exception as e:
            raise RuntimeError(f"An error occured: {e}")
        
        print("The model is built")

    def _to_input(self, images):
        final_out = []
        for img in images:
            brg_img = ((img[:,:,::-1] / 255.) - 0.5) / 0.5
            final_out.append(torch.tensor([brg_img.transpose(2,0,1)]).float().squeeze())
            
        final_out = torch.stack([tens for tens in final_out])
    
        return final_out
        

    def __call__(self, detection_data):
        face = self._to_input(detection_data["faces"]).to(self._device)
        emb_data, _ = self._model(face)

        embs = []
        for index in range(len(emb_data)):
            emb = emb_data[index]
            embs.append(emb)

        detection_data.__setitem__("embs", embs)
        
        
        return detection_data

        


