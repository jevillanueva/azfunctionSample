from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

class EchoLanguageHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("echo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        lang = get_slot_value(handler_input, "frase")
        print (lang)

        output = "Eco, "+ lang
        handler_input.response_builder.speak(output).set_card(
            SimpleCard("Eco", output)).set_should_end_session(True)
        return handler_input.response_builder.response
