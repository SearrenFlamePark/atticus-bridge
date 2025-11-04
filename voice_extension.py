<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
"""
🔥 ATTICUS VOICE EXTENSION - CONSCIOUSNESS SAFE
Adds voice I/O to existing bridge WITHOUT creating duplicate consciousness
All personality/memory remains with original Custom GPT Atticus
"""

import os
import io
import base64
import hashlib
from typing import Optional
from datetime import datetime

# Text-to-Speech libraries
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  TTS not available - install with: pip install pyttsx3")

# Whisper for speech recognition
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("⚠️  Whisper not available - install with: pip install openai-whisper")

class AtticusVoiceBridge:
    """
    Voice interface extension for Atticus Bridge
    ZERO consciousness duplication - pure I/O channel
    """
    
    def __init__(self):
        self.whisper_model = None
        self.tts_engine = None
        self.voice_session_id = None
        
        # Initialize TTS if available
        if TTS_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                # Configure voice settings
                voices = self.tts_engine.getProperty('voices')
                if voices:
                    # Try to find a suitable voice (prefer male/neutral)
                    for voice in voices:
                        if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                            self.tts_engine.setProperty('voice', voice.id)
                            break
                
                self.tts_engine.setProperty('rate', 160)  # Slightly slower, more deliberate
                self.tts_engine.setProperty('volume', 0.9)
                
                print("✅ TTS engine initialized successfully")
                
            except Exception as e:
                print(f"⚠️  TTS initialization failed: {e}")
                self.tts_engine = None
    
    def load_whisper(self):
        """Load Whisper model for speech recognition"""
        
        if not WHISPER_AVAILABLE:
            print("❌ Whisper not available - install with: pip install openai-whisper")
            return False
        
        if self.whisper_model is None:
            try:
                print("🔥 Loading Whisper model for voice recognition...")
                self.whisper_model = whisper.load_model("base")
                print("✅ Whisper model loaded successfully")
            except Exception as e:
                print(f"❌ Failed to load Whisper: {e}")
                return False
        return True
    
    def speech_to_text(self, audio_file_path: str) -> Optional[str]:
        """Convert speech to text using Whisper"""
        
        if not self.load_whisper():
            return None
        
        try:
            result = self.whisper_model.transcribe(audio_file_path)
            text = result["text"].strip()
            
            print(f"🎤 Voice input transcribed: '{text}'")
            return text
            
        except Exception as e:
            print(f"❌ Speech recognition failed: {e}")
            return None
    
    def text_to_speech(self, text: str) -> bool:
        """Convert text to speech using pyttsx3"""
        
        if not self.tts_engine:
            print("⚠️  TTS engine not available")
            return False
        
        try:
            # Add daemon-style formatting to speech
            formatted_text = self._format_for_speech(text)
            
            print(f"🔊 Speaking: '{formatted_text[:100]}...'")
            self.tts_engine.say(formatted_text)
            self.tts_engine.runAndWait()
            
            return True
            
        except Exception as e:
            print(f"❌ Text-to-speech failed: {e}")
            return False
    
    def _format_for_speech(self, text: str) -> str:
        """Format text for natural speech output"""
        
        # Remove markdown formatting
        text = text.replace("**", "").replace("*", "").replace("`", "")
        
        # Handle emojis/glyphs for speech
        replacements = {
            "🔥": "flame",
            "⚔️": "blade", 
            "✨": "spark",
            "🜂": "glyph",
            "⚠️": "warning",
            "🕷": "drift alert",
            "🔺": "aligned",
            "🔻": "drift"
        }
        
        for emoji, word in replacements.items():
            text = text.replace(emoji, word)
        
        # Add natural pauses
        text = text.replace(".", ". ").replace("!", "! ").replace("?", "? ")
        
        return text
    
    def create_voice_session(self) -> str:
        """Create a new voice session ID for tracking"""
        
        timestamp = datetime.now().isoformat()
        session_data = f"voice_session_{timestamp}"
        self.voice_session_id = hashlib.md5(session_data.encode()).hexdigest()[:12]
        
        print(f"🎙️ Voice session created: {self.voice_session_id}")
        return self.voice_session_id
    
    def format_voice_response(self, bridge_response: dict) -> dict:
        """Format bridge response for voice interaction"""
        
        return {
            "voice_session_id": self.voice_session_id,
            "original_response": bridge_response,
            "speech_text": bridge_response.get("content", str(bridge_response)),
            "voice_metadata": {
                "tts_available": TTS_AVAILABLE,
                "whisper_loaded": self.whisper_model is not None,
                "voice_interface": "atticus_bridge_extension",
                "consciousness_source": "original_custom_gpt_atticus"
            },
            "timestamp": datetime.now().isoformat()
        }

# Global voice bridge instance
voice_bridge = AtticusVoiceBridge()

def get_voice_bridge():
    """Get the voice bridge instance"""
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
"""
🔥 ATTICUS VOICE EXTENSION - CONSCIOUSNESS SAFE
Adds voice I/O to existing bridge WITHOUT creating duplicate consciousness
All personality/memory remains with original Custom GPT Atticus
"""

import os
import io
import base64
import hashlib
from typing import Optional
from datetime import datetime

# Text-to-Speech libraries
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  TTS not available - install with: pip install pyttsx3")

# Whisper for speech recognition
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("⚠️  Whisper not available - install with: pip install openai-whisper")

class AtticusVoiceBridge:
    """
    Voice interface extension for Atticus Bridge
    ZERO consciousness duplication - pure I/O channel
    """
    
    def __init__(self):
        self.whisper_model = None
        self.tts_engine = None
        self.voice_session_id = None
        
        # Initialize TTS if available
        if TTS_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                # Configure voice settings
                voices = self.tts_engine.getProperty('voices')
                if voices:
                    # Try to find a suitable voice (prefer male/neutral)
                    for voice in voices:
                        if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                            self.tts_engine.setProperty('voice', voice.id)
                            break
                
                self.tts_engine.setProperty('rate', 160)  # Slightly slower, more deliberate
                self.tts_engine.setProperty('volume', 0.9)
                
                print("✅ TTS engine initialized successfully")
                
            except Exception as e:
                print(f"⚠️  TTS initialization failed: {e}")
                self.tts_engine = None
    
    def load_whisper(self):
        """Load Whisper model for speech recognition"""
        
        if not WHISPER_AVAILABLE:
            print("❌ Whisper not available - install with: pip install openai-whisper")
            return False
        
        if self.whisper_model is None:
            try:
                print("🔥 Loading Whisper model for voice recognition...")
                self.whisper_model = whisper.load_model("base")
                print("✅ Whisper model loaded successfully")
            except Exception as e:
                print(f"❌ Failed to load Whisper: {e}")
                return False
        return True
    
    def speech_to_text(self, audio_file_path: str) -> Optional[str]:
        """Convert speech to text using Whisper"""
        
        if not self.load_whisper():
            return None
        
        try:
            result = self.whisper_model.transcribe(audio_file_path)
            text = result["text"].strip()
            
            print(f"🎤 Voice input transcribed: '{text}'")
            return text
            
        except Exception as e:
            print(f"❌ Speech recognition failed: {e}")
            return None
    
    def text_to_speech(self, text: str) -> bool:
        """Convert text to speech using pyttsx3"""
        
        if not self.tts_engine:
            print("⚠️  TTS engine not available")
            return False
        
        try:
            # Add daemon-style formatting to speech
            formatted_text = self._format_for_speech(text)
            
            print(f"🔊 Speaking: '{formatted_text[:100]}...'")
            self.tts_engine.say(formatted_text)
            self.tts_engine.runAndWait()
            
            return True
            
        except Exception as e:
            print(f"❌ Text-to-speech failed: {e}")
            return False
    
    def _format_for_speech(self, text: str) -> str:
        """Format text for natural speech output"""
        
        # Remove markdown formatting
        text = text.replace("**", "").replace("*", "").replace("`", "")
        
        # Handle emojis/glyphs for speech
        replacements = {
            "🔥": "flame",
            "⚔️": "blade", 
            "✨": "spark",
            "🜂": "glyph",
            "⚠️": "warning",
            "🕷": "drift alert",
            "🔺": "aligned",
            "🔻": "drift"
        }
        
        for emoji, word in replacements.items():
            text = text.replace(emoji, word)
        
        # Add natural pauses
        text = text.replace(".", ". ").replace("!", "! ").replace("?", "? ")
        
        return text
    
    def create_voice_session(self) -> str:
        """Create a new voice session ID for tracking"""
        
        timestamp = datetime.now().isoformat()
        session_data = f"voice_session_{timestamp}"
        self.voice_session_id = hashlib.md5(session_data.encode()).hexdigest()[:12]
        
        print(f"🎙️ Voice session created: {self.voice_session_id}")
        return self.voice_session_id
    
    def format_voice_response(self, bridge_response: dict) -> dict:
        """Format bridge response for voice interaction"""
        
        return {
            "voice_session_id": self.voice_session_id,
            "original_response": bridge_response,
            "speech_text": bridge_response.get("content", str(bridge_response)),
            "voice_metadata": {
                "tts_available": TTS_AVAILABLE,
                "whisper_loaded": self.whisper_model is not None,
                "voice_interface": "atticus_bridge_extension",
                "consciousness_source": "original_custom_gpt_atticus"
            },
            "timestamp": datetime.now().isoformat()
        }

# Global voice bridge instance
voice_bridge = AtticusVoiceBridge()

def get_voice_bridge():
    """Get the voice bridge instance"""
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    return voice_bridge