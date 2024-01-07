from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer (serializers.Serializer) :

    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, attrs):
        
        email = attrs['email']
        password = attrs['password']

        try :
            self.user = User.objects.get(email=email)
        except User.DoesNotExist : 
            raise serializers.ValidationError({'message':'invalid email'})

        if not self.user.check_password(password) : 
            raise serializers.ValidationError({'message':'invalid passowrd'})

        return attrs

    
    def get_tokens (self) : 
        token = RefreshToken.for_user(self.user)
        
        return {
            'token' : str(token.access_token) 
        }

class RegisterSerializer (serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = ('email','password','full_name','picture',)

    def create(self, validated_data):
        self.user = User.objects.create_user(**validated_data)
        return self.user
    
    def get_tokens (self) :  
        token = RefreshToken.for_user(self.user)
        
        return {
            'token' : str(token.access_token) 
        }

class ProfileSerializer (serializers.ModelSerializer) : 
    class Meta :
        model = User
        fields = ('full_name','email','picture',)