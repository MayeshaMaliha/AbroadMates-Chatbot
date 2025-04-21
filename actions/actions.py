from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionDynamicLlama(Action):
    def name(self) -> Text:
        return "action_dynamic_llama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get("text")

        try:
            # Send user message to locally running LLaMA (via Ollama)
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "mistral",  # or "llama2" if that's what you're using
                "prompt": user_message,
                "stream": False
            })

            if response.status_code == 200:
                reply = response.json().get("response", "").strip()
                dispatcher.utter_message(text=reply)
            else:
                dispatcher.utter_message(text="Hmm, I couldn't get a response from the AI. Try again in a bit!")

        except Exception as e:
            print("Error communicating with LLaMA:", e)
            dispatcher.utter_message(text="Sorry, something went wrong while connecting to the AI.")

        return []