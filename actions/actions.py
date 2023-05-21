from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class Action_Temp(Action):
    def name(self) -> Text:
         return "action_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        temp = int(next(tracker.get_latest_entity_values("temperature"), None))
        if temp >= 25:
            dispatcher.utter_message(text="You should wear a T-shirt. Is it raining today?")
        else:
            dispatcher.utter_message(text="You should wear a jacket/coat. Is it raining today?")

        return []
