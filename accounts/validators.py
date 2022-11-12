from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] #cover-mage.jpg
    print(ext)
    value_extension = ['.png','jpg','jpeg']
    if not ext.lower() in value_extension:
        raise ValidationError("Unsupported file extension. Allowed  extension"+str(value_extension))