import os
import logging
from typing import Optional
import dotenv
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from twilio.base.exceptions import TwilioRestException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress Twilio API request logs
logging.getLogger('twilio.http_client').setLevel(logging.WARNING)

# Load environment variables
dotenv.load_dotenv()

# Twilio configuration
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
VIDEOSDK_MEETING_ID = os.getenv("VIDEOSDK_MEETING_ID")
VIDEOSDK_SIP_USERNAME = os.getenv("VIDEOSDK_SIP_USERNAME")
VIDEOSDK_SIP_PASSWORD = os.getenv("VIDEOSDK_SIP_PASSWORD")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

# Validate required environment variables
required_env_vars = {
    "TWILIO_SID": TWILIO_SID,
    "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
    "TWILIO_PHONE_NUMBER": TWILIO_PHONE_NUMBER,
    "VIDEOSDK_MEETING_ID": VIDEOSDK_MEETING_ID,
    "VIDEOSDK_SIP_USERNAME": VIDEOSDK_SIP_USERNAME,
    "VIDEOSDK_SIP_PASSWORD": VIDEOSDK_SIP_PASSWORD,
    "TO_PHONE_NUMBER": TO_PHONE_NUMBER,
}

missing_vars = [var for var, value in required_env_vars.items() if not value]
if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Initialize Twilio client
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def outbound_call_app() -> str:
    """
    Generate TwiML response for outbound call.
    
    Returns:
        str: TwiML response as string
    """
    response = VoiceResponse()
    dial = response.dial()
    dial.sip(
        f"sip:{VIDEOSDK_MEETING_ID}@sip.videosdk.live",
        username=VIDEOSDK_SIP_USERNAME,
        password=VIDEOSDK_SIP_PASSWORD,
    )
    return str(response)

def outbound_call(to_phone_number: str) -> Optional[str]:
    """
    Initiate an outbound call using Twilio.
    
    Args:
        to_phone_number (str): The phone number to call in E.164 format
        
    Returns:
        Optional[str]: Call SID if successful, None if failed
        
    Raises:
        ValueError: If phone number is invalid
        TwilioRestException: If Twilio API call fails
    """
    if not to_phone_number.startswith('+'):
        raise ValueError("Phone number must be in E.164 format (e.g., +1234567890)")
        
    try:
        call = twilio_client.calls.create(
            to=to_phone_number,
            from_=TWILIO_PHONE_NUMBER,
            twiml=outbound_call_app()
        )
        logger.debug("Call initiated")
        return call.sid
    except TwilioRestException as e:
        logger.error("Twilio API error")
        raise
    except Exception as e:
        logger.error("Call initiation failed")
        raise

if __name__ == "__main__":
    try:
        call_sid = outbound_call(to_phone_number=TO_PHONE_NUMBER)
        if call_sid:
            logger.info("Call successful")
    except Exception as e:
        logger.error("Call failed")