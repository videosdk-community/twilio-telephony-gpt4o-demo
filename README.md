# AI Voice Agent Demo with Twilio, VideoSDK and GPT-4o

A Python-based demonstration project that showcases how to build an AI voice agent for phone conversations using Twilio, VideoSDK, and OpenAI's GPT-4o. This demo illustrates how to create natural voice interactions over traditional telephony systems.

## Demo Features

- **Voice Call Handling**: Inbound and outbound call management via Twilio
- **AI Integration**: OpenAI GPT-4o for natural conversation
- **Audio Processing**: Real-time voice transcription and synthesis
- **WebRTC Integration**: Audio streaming with VideoSDK
- **SIP Integration**: Support for SIP-based telephony

## Demo Architecture

![System Architecture](images/call_flow.png)

### Key Components

1. **Twilio Integration** (`make_twilio_call.py`)
   - Outbound call initiation
   - Call status monitoring
   - Voice stream handling

2. **Voice Agent** (`voice_agent.py`)
   - AI conversation management
   - Voice processing pipeline
   - Response generation

3. **Main Application** (`main.py`)
   - Application entry point
   - Configuration management
   - Service orchestration

## Running the Demo

### Prerequisites

- Python 3.11+
- Twilio Account (trial account works)
- OpenAI API key
- VideoSDK account (trial account works)

### Setup

1. Clone the demo:
   ```bash
   git clone https://github.com/videosdk-community/twilio-telephony-gpt4o-demo.git
   cd twilio-telephony-gpt4o-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` with your credentials:
   ```bash
   OPENAI_API_KEY="your-openai-key"
   VIDEOSDK_MEETING_ID="your-meeting-id"
   VIDEOSDK_AUTH_TOKEN="your-auth-token"
   VIDEOSDK_SIP_USERNAME="your-sip-username"
   VIDEOSDK_SIP_PASSWORD="your-sip-password"
   TWILIO_SID="your-twilio-sid"
   TWILIO_AUTH_TOKEN="your-twilio-token"
   TWILIO_PHONE_NUMBER="your-twilio-number"
   TO_PHONE_NUMBER="destination-number"
   ```

5. Start the demo:
   ```bash
   python src/main.py
   ```

6. Make a Call:
     ```bash
     python src/make_twilio_call.py
     ```

### Directory Structure

```
.
├── src/
│   ├── main.py              # Application entry point
│   ├── voice_agent.py       # AI voice agent implementation
│   └── make_twilio_call.py  # Twilio call handling
├── images/                  # Documentation images
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md
```

## Demo Tech Stack

- **Backend**: Python 3.11+
- **Telephony**: Twilio Programmable Voice
- **Real-time**: VideoSDK
- **AI**: OpenAI GPT-4o
- **Dependencies**:
  - videosdk-agents
  - videosdk-plugins-openai
  - asyncio
  - scipy
  - python-dotenv
  - twilio

## License

This demo is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Contributing

Feel free to fork this demo and experiment with it! Some ideas for experimentation:
- Integrate with additional AI models

## Support

For questions about this demo, please open an issue in the [GitHub repository](https://github.com/videosdk-community/twilio-telephony-gpt4o-demo).

---

## Author
[Yash Chudasama](https://github.com/yash-chudasama)
[VideoSDK Community](https://github.com/videosdk-community)