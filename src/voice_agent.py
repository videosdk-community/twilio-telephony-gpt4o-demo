from typing import Optional, List, Any
import logging
from videosdk.agents import Agent
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class VoiceAgent(Agent):
    """An outbound call agent specialized for medical appointment scheduling."""
    
    def __init__(
        self,
        instructions: str = "You are a medical appointment scheduling assistant. Your goal is to confirm upcoming appointments (5th June 2025 at 11:00 AM) and reschedule if needed.",
        tools: Optional[List[Any]] = None,
    ) -> None:
        """Initialize the AppointmentSchedulingAgent."""
        super().__init__(
            instructions=instructions,
            tools=tools or []
        )
        self.logger = logging.getLogger(__name__)
        self.appointment_date = None
        self.patient_name = None
        
    async def on_enter(self) -> None:
        """Handle agent entry into the session."""
        await self.session.say(
            "Hello, this is Neha, calling from City Medical Center regarding your upcoming appointment. Is this a good time to speak?"
        )
    
    async def on_exit(self) -> None:
        """Handle call termination."""
        self.logger.info("Call ended")