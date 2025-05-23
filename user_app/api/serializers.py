from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    
    def save(self):
        
        # check both password and password confirmation are identical
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError("Passwords are NOT identical")
        
        #check if the user email exists before registration
        user_email = User.objects.filter(email=self.validated_data['email'])
        if user_email.exists():
            raise serializers.ValidationError("Email Already exists!")
        
        # creating the account manually
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(self.validated_data['password'])
        
        account.save()
        return account
        
        
        