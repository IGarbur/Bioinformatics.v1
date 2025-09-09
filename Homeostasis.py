
class Hypothalamus:
    def __init__(self,body_temperature,temperature_regulation,temperature_range):
        self.body_temperature = body_temperature
        self.temperature_regulation = temperature_regulation
        self.temperature_range = temperature_range
        while self.body_temperature > temperature_range[1] or self.body_temperature < temperature_range[0]:
            self.body_temperature = self.temperature_regulation(self.body_temperature)
            print(self.body_temperature)


def vasodialation(body_temperature):
    print(f"->Vasodialation")
    return body_temperature - 0.1

def vasoconstriction(body_temperature):
    print(f"->Vasoconstriction")
    return body_temperature + 0.1

def diaphoresis(body_temperature):
    print(f"->Diaphoresis")
    return body_temperature - 0.2

def shivering(body_temperature):
    print(f"->Shivering")
    return body_temperature + 0.2

def create_negative_feedback(fn_high,fn_low,normal_range): #fn_high (contains fns that lower) and fn_low (contains function that raise) is a list of functions, normal range is a list of two values
    def negative_feedback(variable):
        if variable < normal_range[0]:
            print(f"{variable} is below normal range {normal_range}")
            new_variable = variable
            for fn in fn_low:
                new_variable = fn(new_variable)
            return new_variable
        elif variable > normal_range[1]:
            print(f"{variable} is above normal range {normal_range}")
            new_variable = variable
            for fn in fn_high:
                new_variable = fn(new_variable)
            return new_variable
        else:
            print(f"{variable} is in normal range {normal_range}")
            return variable
    return negative_feedback

temperature_range = [36,37]
body_temperature = 40
temperature_regulation = create_negative_feedback([vasodialation,diaphoresis],[vasoconstriction,shivering],temperature_range)
hypothalamus = Hypothalamus(body_temperature,temperature_regulation,temperature_range)