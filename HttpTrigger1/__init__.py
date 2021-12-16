import logging
import os
import azure.functions as func
from ask_sdk_core.skill_builder import SkillBuilder
from HttpTrigger1.DefaultHandler import AllExceptionHandler, CancelAndStopIntentHandler, HelpIntentHandler, LaunchRequestHandler, SessionEndedRequestHandler
from HttpTrigger1.IntentHandler import EchoLanguageHandler
from HttpTrigger1.BioconscienteHandler import BioconcienteNewsHandler
import json
from ask_sdk_webservice_support.webservice_handler import WebserviceSkillHandler
from HttpTrigger1.config import ALEXA_SKILL_ID

def main(req: func.HttpRequest) -> func.HttpResponse:
    print (ALEXA_SKILL_ID)
    skill_builder = SkillBuilder()
    skill_builder.skill_id = ALEXA_SKILL_ID
    skill_builder.add_request_handler(LaunchRequestHandler())
    skill_builder.add_request_handler(EchoLanguageHandler())
    skill_builder.add_request_handler(BioconcienteNewsHandler())
    skill_builder.add_request_handler(HelpIntentHandler())
    skill_builder.add_request_handler(CancelAndStopIntentHandler())
    skill_builder.add_request_handler(SessionEndedRequestHandler())
    skill_builder.add_exception_handler(AllExceptionHandler())

    webservice_handler = WebserviceSkillHandler(skill=skill_builder.create())
    response = webservice_handler.verify_request_and_dispatch(req.headers, req.get_body().decode("utf-8"))
    return func.HttpResponse(json.dumps(response),mimetype="application/json")