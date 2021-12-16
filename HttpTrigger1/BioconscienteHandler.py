from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from .discordRequest import getTopNMessages
from typing import List
class BioconcienteNewsHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BioconcienteNews")(handler_input)


    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        cantidad = get_slot_value(handler_input, "cantidad")
        print (cantidad)
        if cantidad is not None:
            messages = getTopNMessages(size=cantidad)
        else:
            messages = getTopNMessages()
        if messages is None or len(messages) == 0:
            output = "No se encontraron mensajes"
        else:
            output = generate_response(messages)
            output += " Esos son todos los mensajes!."
        handler_input.response_builder.speak(output).set_card(
            SimpleCard("Eco", output)).set_should_end_session(True)
        return handler_input.response_builder.response


def generate_response(messages):
    # type: (List) -> str
    speak_out = ""
    itemCount = 1
    for message in messages:
        speak_out += 'Mensaje {0}: <break time="0.5s"/> {1}. <break time="1s"/>\n'.format(itemCount,message.get("content", ""))
        itemCount +=1
    return speak_out