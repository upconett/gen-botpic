import os
import numpy as np

from PIL import Image

from app.gen.Generator import Generator
from app.gen.exceptions import PosOutsideImage
from app.models import Color


class PillowGenerator(Generator):

    def generate(self) -> str:
        img_path = self._gen_path()

        img = Image.new("RGBA", self.size, color=self.colors[0].hex)
        self._add_radial_gradient(img, self.colors[1], 500, (0, 0))
        self._add_emoji(img)

        img.save(img_path)
        return img_path


    def _gen_path(self, path: str | None = None) -> str:
        if not path:
            path = self.save_path

        img_path = os.path.join(self.save_path, "botpic.png")
        return img_path

    
    def _add_emoji(
        self,
        img: Image.Image
    ):
        if not self.emoji:
            return

        emoji_img = Image.open(self.emoji.path)

        # Resize emoji a bit
        emoji_size = (
            int(emoji_img.size[0]*1.5),
            int(emoji_img.size[1]*1.5),
        )
        emoji_img = emoji_img.resize(emoji_size)

        # Placing emoji in the middle of the image
        emoji_pos = (
            self.size[0]//2 - emoji_img.size[0]//2,
            self.size[1]//2 - emoji_img.size[1]//2,
        )

        self._alpha_paste(img, emoji_img, emoji_pos)


    def _add_radial_gradient(
        self,
        img: Image.Image,
        color: Color,
        radius: int,
        pos: tuple[int, int],
    ):
        """ Adds radial gradient to the image """
        if not _pos_in_img(pos, img):
            raise PosOutsideImage
            
        pos = _fix_pos(pos, radius)
        grad = self._gen_radial_gradient(img, color, radius)
        self._alpha_paste(img, grad, pos)

    
    def _gen_radial_gradient(
        self,
        img: Image.Image,
        color: Color,
        radius: int,
    ) -> Image.Image:
        size = (radius*2, radius*2)
        grad = Image.new("RGBA", size=size, color=color.hex)

        Y = np.linspace(-1, 1, size[0])[None, :]*255
        X = np.linspace(-1, 1, size[1])[:, None]*255

        alpha = np.sqrt(X**2 + Y**2)
        alpha = 255 - np.clip(0, 255, alpha)

        grad.putalpha(Image.fromarray(alpha.astype(np.uint8)))

        return grad

    
    def _alpha_paste(
        self,
        img1: Image.Image,
        img2: Image.Image,
        pos: tuple[int, int] = (0,0)
    ):
        larger_img2 = Image.new("RGBA", img1.size, color=(0,0,0,0))
        larger_img2.paste(img2, pos)
        img1.paste(Image.alpha_composite(img1, larger_img2))


def _pos_in_img(pos: tuple[int, int], img: Image.Image) -> bool:
    return all([
        0 <= x <= img_x
        for x, img_x
        in zip(pos, img.size)
    ])


def _fix_pos(pos: tuple[int, int], radius: int) -> tuple[int, int]:
    return (
        pos[0]-radius,
        pos[1]-radius
    )
