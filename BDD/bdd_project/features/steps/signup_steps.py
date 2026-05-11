from behave import given, when, then
from utils.logger import LogGen

logger= LogGen.loggen()
@given (u'User Launches Demoblaze application')
def step_impl(context):
    logger.info('Demoblize URL loader')

