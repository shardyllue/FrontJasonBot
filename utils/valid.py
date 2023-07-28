from aiohttp import ClientSession

import utils.config as uconfig
import module.schema as mschema



async def valid_token(token : str) -> mschema.BotResult:

    bot_link = uconfig.AUTH_BOT_LINK.format(
        token=token
    )

    async with ClientSession() as session:

        async with session.get(bot_link) as response:    

            json = await response.json()

            auth_response = mschema.BotReponse(**json)

    

    if auth_response.ok is False:
        return False
    
    return auth_response.result
    
