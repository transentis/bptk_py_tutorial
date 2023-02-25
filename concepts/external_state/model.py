import BPTK_Py
from BPTK_Py import Model
from BPTK_Py import sd_functions as sd


def bptk_factory():
    model = Model(starttime=1.0,stoptime=60.0, dt=1.0, name="Customer Acquisition SDDSL")

    # stocks
    customers = model.stock("customers")
    potential_customers = model.stock("potential_customers")

    #flows
    customer_acquisition=model.flow("customer_acquisition")

    #converters
    acquisition_through_advertising = model.converter("acquisition_through_advertising")
    acquisition_through_word_of_mouth = model.converter("acquisition_through_word_of_mouth")
    consumers_reached_through_advertising = model.converter("consumers_reached_through_advertising")
    consumers_reached_through_word_of_mouth= model.converter("consumers_reached_through_word_of_mouth")
    market_saturation = model.converter("market_saturation")

    #constants
    initial_customers = model.constant("initial_customers") 
    target_market= model.constant("target_market")
    advertising_success = model.constant("advertising_success")
    consumers_reached_per_euro = model.constant("consumers_reached_per_ruro")
    advertising_budget = model.constant("advertising_budget")
    word_of_mouth_success = model.constant("word_of_mouth_success")
    contact_rate = model.constant("contact_rate")

    #equations
    customers.equation = customer_acquisition
    potential_customers.equation = -customer_acquisition
    customer_acquisition.equation=sd.min(potential_customers,acquisition_through_advertising+acquisition_through_word_of_mouth)
    acquisition_through_advertising.equation = advertising_success*consumers_reached_through_advertising
    consumers_reached_through_advertising.equation = consumers_reached_per_euro*advertising_budget*(1-market_saturation)
    market_saturation.equation = customers/target_market
    acquisition_through_word_of_mouth.equation = word_of_mouth_success*consumers_reached_through_word_of_mouth
    consumers_reached_through_word_of_mouth.equation=contact_rate*customers*(1-market_saturation)

    #initialize model
    customers.initial_value=initial_customers
    potential_customers.initial_value=target_market
    initial_customers.equation = 0.0
    target_market.equation = 60000.0
    advertising_success.equation = 0.1
    consumers_reached_per_euro.equation = 100.0
    advertising_budget.equation = 100.0
    word_of_mouth_success.equation = 0.01
    contact_rate.equation = 10.0

    ### Set up scenarios in bptk

    scenario_manager={
        "sddsl_customer_acquisition":{
            "model":model,
            "base_constants":{
                "initial_customers" : 0.0,
                "target_market" : 60000.0,
                "advertising_success": 0.1,
                "consumers_reached_per_euro" : 100.0,
                "advertising_budget" : 100.0,
                "word_of_mouth_success": 0.01,
                "contact_rate" : 10.0
            }
        }
    }

    bptk = BPTK_Py.bptk()
    bptk.register_scenario_manager(scenario_manager)
    bptk.register_scenarios(
    
        scenario_manager="sddsl_customer_acquisition",
        scenarios=
        {
            "base":{
            
            },
            "low_word_of_mouth":{
                "constants":{
                    "word_of_mouth_success":0.001
                }
            },
            "high_word_of_mouth":{
                "constants":{
                    "word_of_mouth_success":0.1
                }
            },
            "interactive_scenario":{}
        
        }
    

    )
    
    return bptk