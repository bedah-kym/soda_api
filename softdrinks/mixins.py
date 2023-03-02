
class UserQuerySetMixin():
    def get_queryset(self,*args,**kwargs):# we set the lookup_data as an empty dict then add a user field to filter the qs
        user=self.request.user
        lookup_data={}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args,**kwargs)#this was the 'original' function in the baseclass that got the initial query
        if user.is_staff:
            return qs
        return qs.filter(**lookup_data)# unapcking it like this makes it into self.request.user ->kwargs