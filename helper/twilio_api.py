import os


from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('AC79363b9bb7c28f72841d1efd3415b9b2')
auth_token = os.getenv('e420450f9609c4fa3c97fd41d26187cb')
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.

    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send

    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )
