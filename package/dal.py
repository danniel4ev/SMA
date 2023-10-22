from typing import Literal,Union
from os.path import isfile

def save_dal(content: Union[str,list[str]], file_path:str, mode="a", write_state: Literal["wr","wl"]="wr") -> tuple[Literal["SUCCESS","ERROR"], Union[str,None]]:

    try:
        file_object = open(file=file_path, mode=mode)

        if write_state=="wr":
            file_object.write(content)
        elif write_state=="wl":
            file_object.writelines(content)

    except BaseException as err:
        return ("ERROR", err)
    
    else:
        return ("SUCCESS", None)

    finally:
        if "file_object" in locals() and (not file_object.close()):
            file_object.close()

def read_dal(file_path:str):

    if not isfile(file_path):

        try:
            file_object = open(file=file_path, mode="x")

        except BaseException as err:
            return ("ERROR", err)
        
        else:
            return ("SUCCESS", tuple())

        finally:
            if "file_object" in locals() and (not file_object.close()):
                file_object.close()


    try:
        file_object = open(file=file_path)
        res = file_object.readlines()
        
    except BaseException as err:
        return ("ERROR", err)
    
    else:
        return ("SUCCESS", tuple(res))

    finally:
        if "file_object" in locals() and (not file_object.close()):
            file_object.close()





