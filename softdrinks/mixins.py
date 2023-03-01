
class UserQuerySetMixin():
    user_field = 'Owner' #this is a class atr for generics which maps to the model
    def get_queryset(self,*args,**kwargs):# we set the lookup_data as an empty dict then add a user field to filter the qs
        lookup_data={}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args,**kwargs)#this was the 'original' function in the baseclass that got the initial query
        return qs.filter(**lookup_data)# unapcking it like this makes it into self.request.user ->kwargs