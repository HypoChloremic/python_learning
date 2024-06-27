from utils.classes_to_be_imported import ClassCalledOnce

def method_to_be_called():
    return 1

def calling():
    res = method_to_be_called()
    print(res)
    c = ClassCalledOnce()
    c.save()