# Imports
from django import forms

from .models import UserProfile

# User profile update
class ProfileForm(forms.ModelForm):

    gallery_choices = [
        ('worm_beanie.webp', 'Worm in a Beanie'),
        ('worm_computer.webp', 'Worm with computer background'),
        ('worm_cowboy.webp', 'Worm in a cowboy hat'),
        ('worm_feathered_hat.webp', 'Fancy worm'),
        ('worm_moustache.webp', 'Worm with a moustache'),
        ('worm_paper.webp', 'Worm with a paper background'),
        ('worm_strawhat.webp', 'Worm with a strawhat'),
        ('worm_student.webp', 'Student worm'),
        ('worm_witch.webp', 'Witch worm'),
    ]
    
    # A field for the user to select from pre-set gallery images
    gallery_picture = forms.ChoiceField(
        choices=gallery_choices, 
        required=False, 
        label='Choose from Gallery',
        widget=forms.RadioSelect,)

    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'website', 'profile_picture', 'gallery_picture')

    def clean(self):
        cleaned_data = super().clean()
        profile_picture = cleaned_data.get('profile_picture')
        gallery_picture = cleaned_data.get('gallery_picture')
        
        # Ensure that the user selects either a gallery picture or uploads one, but not both
        if profile_picture and gallery_picture:
            raise forms.ValidationError("Please either upload a picture or choose one from the gallery, not both.")
        
        return cleaned_data