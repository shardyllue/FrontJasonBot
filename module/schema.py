from pydantic import BaseModel


class BotResult(BaseModel):

    id : int
    first_name : str
    username : str



class BotReponse(BaseModel):

    ok : bool
    result : BotResult = None


