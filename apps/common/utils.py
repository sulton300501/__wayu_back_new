import os
from django.utils import dateformat , timezone
from rest_framework.views import exception_handler
from rest_framework.serializers import as_serializer_error
from rest_framework.exceptions import ErrorDetail




def generate_upload_path(instance , filename):
    app_label = instance._meta.app_label  # apps/common
    model_name =instance._meta.model_name # model name
    now = dateformat.format(timezone.now() , 'Y-m-d H:i:s') # hozrgi vaqtni formati
    file , exc = split_file_name(filename)

    filepath = "%s/%s/%s-%s.%s" % (
        app_label , model_name , file , now , exc
    )

    return filepath




def split_file_name(filename):
    filename = filename.split(os.sep)[-1] #  misol: split_file_name("C:\\Users\\Admin\\myphoto.jpg")  bolsa bu yeradn myphoto.jpg olinadi    ...\\ boyicha  oladi 
    return [''.join(filename.split('.')[:-1]) , filename.split('.')[-1]]  



def custom_exception_handler(exc , context):
    handlers = {
        "ValidationError": _handle_validation_error ,
    }

    response = exception_handler(exc , context)
    
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc,context)
    return response



def _handle_validation_error(exc , context):  
    response = exception_handler(exc , context)
    errors = as_serializer_error(exc)

    if response is not None:
        response.data = {"status_code":response.status_code , "errors":[]}
        make_pretty_error(response.data , errors)
    return response
        
   


def make_pretty_error(data, errors):
    for error in errors:
        if isinstance(errors[error][0], ErrorDetail ) and len(errors[error])==1:
            data["errors"].append({"error":f"{errors[error][0].code}" , "message":errors[error][0]})
        elif isinstance(errors[error][0], dict) and len(errors[error])>=1:
            for er in errors[error]:
                make_pretty_error(data , er)
        else:
            data["errors"].append({"error":f"{error}","message":errors[error]})






