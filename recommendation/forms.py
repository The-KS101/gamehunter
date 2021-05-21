from django import forms

class gameSearched(forms.Form):
    CONSOLE_CHOICE = [
                ('all', 'Filter By'),
                ('Xbox Series X', 'Xbox Series X'),
                ('PlayStation 5', 'PlayStation 5'),
                ('Xbox One', 'Xbox One'),
                ('PlayStation 4', 'PlayStation 4'),
                ('PC', 'PC'),
                ('Switch', 'Switch'),
                ]

    gameName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Discover new games...', 'list': 'games'}), required=True, error_messages={'required': 'Enter a Game Name'})
    platforms = forms.ChoiceField(choices=CONSOLE_CHOICE, required=False)
