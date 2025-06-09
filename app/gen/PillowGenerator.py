import os
from PIL import Image

from app.gen.Generator import Generator


class PillowGenerator(Generator):

    def _gen_path(self, path: str | None = None) -> str:
        if not path:
            path = self.save_path

        img_path = os.path.join(self.save_path, "botpic.png")
        return img_path

    
    def generate(self) -> str:
        img_path = self._gen_path()
        img = Image.new("RGB", self.size, color=str(self.colors[0]))
        img.save(img_path)
        return img_path
