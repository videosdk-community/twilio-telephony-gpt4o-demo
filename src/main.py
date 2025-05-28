from voice_agent import VoiceAgent
from videosdk.agents import AgentSession
from videosdk.agents import RealTimePipeline
from videosdk.plugins.openai import OpenAIRealtime
import asyncio
import dotenv
import os
import logging
import signal
from typing import Dict, Any

# Configure minimal logging
logging.basicConfig(
    level=logging.WARNING,  # Only show warnings and errors
    format='%(levelname)s: %(message)s'  # Simplified format
)
logger = logging.getLogger(__name__)

# Load environment variables
dotenv.load_dotenv()

# Environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VIDEOSDK_MEETING_ID = os.getenv("VIDEOSDK_MEETING_ID")
VIDEOSDK_AUTH_TOKEN = os.getenv("VIDEOSDK_AUTH_TOKEN")

# Required environment variables
REQUIRED_ENV_VARS = {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "VIDEOSDK_MEETING_ID": VIDEOSDK_MEETING_ID,
    "VIDEOSDK_AUTH_TOKEN": VIDEOSDK_AUTH_TOKEN
}

def secure_log_error(error_msg: str, error: Exception) -> None:
    """Log error messages without exposing sensitive information."""
    safe_msg = error_msg.replace(str(OPENAI_API_KEY), "[REDACTED]")
    safe_msg = safe_msg.replace(str(VIDEOSDK_AUTH_TOKEN), "[REDACTED]")
    logger.error(f"{safe_msg}: {type(error).__name__}")

def validate_environment() -> None:
    """Validate that all required environment variables are set."""
    missing_vars = [var for var, value in REQUIRED_ENV_VARS.items() if not value]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

def make_context() -> Dict[str, Any]:
    """Create the context dictionary for the agent session."""
    return {
        "name": "VoiceAgent",
        "meetingId": VIDEOSDK_MEETING_ID,
        "videosdk_auth": VIDEOSDK_AUTH_TOKEN
    }

async def main() -> None:
    """Main function to run the voice agent."""
    try:
        validate_environment()
        
        openai_model = OpenAIRealtime(
            model="gpt-4o-realtime-preview",
            api_key=OPENAI_API_KEY
        )
        
        pipeline = RealTimePipeline(model=openai_model)
        
        session = AgentSession(
            agent=VoiceAgent(),
            pipeline=pipeline,
            context=make_context()
        )
        
        await session.start()
        await asyncio.Event().wait()
        
    except Exception as e:
        secure_log_error("Error", e)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())