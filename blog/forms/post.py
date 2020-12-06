from django.forms import ModelForm
from blog.models import Post
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from PIL import Image


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        slug = slugify(title)
        if Post.objects.filter(slug=slug).exists() and not Post.objects.filter(id=self.instance.id).exists():
            raise ValidationError("The title already exists.Use unique post title")
        self.instance.slug = slug
        return title

    def clean_image(self):
        IMG_HEIGHT = 449
        image = self.cleaned_data['image']
        print(image)
        if image != 'default.png':
            with Image.open(image.file) as img:
                if img.height < IMG_HEIGHT or img.width < IMG_HEIGHT*1.5:
                    raise ValidationError("Image is too small. Minimum size of image is 500 x 750")
        return image
