from auth.service import create_user
from auth.schemas import UserInputSchema

async def init_user_fixture():
    
    init_user_data = {
        'email': 'example@email.com',
        'password': 'example_password',
    }

    init_user = UserInputSchema(**init_user_data)
    try:
        await create_user(init_user)
    except Exception as e:
        print(e)