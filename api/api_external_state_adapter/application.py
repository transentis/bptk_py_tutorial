from BPTK_Py import BptkServer
from BPTK_Py import FileAdapter
from model import bptk_factory
import os

adapter = FileAdapter(True, os.path.join(os.getcwd(), "state"))

application = BptkServer(__name__, bptk_factory, external_state_adapter=adapter)

if __name__ == "__main__":
    application.run()
