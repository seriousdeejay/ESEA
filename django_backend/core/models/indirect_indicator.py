from django.db import models
import re

find_square_bracket_keys = re.compile(r"\[(.*?)\]")

class IndirectIndicator(models.Model):
    key = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, unique=False, blank=False)
    formula = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(blank=True, null=True)
    topic = models.ForeignKey('Topic', related_name='indirect_indicators', on_delete=models.CASCADE)
    calculation = ''
    value = None
    has_conditionals = False
    exception = None
    exception_detail = None
    responses = None

    class Meta: 
        unique_together = ['key', 'topic']

    def __init__(self, *args, **kwargs):
        super(IndirectIndicator, self).__init__(*args, **kwargs)
        self.calculation = self.formula.lower().replace("\n", "")
        if self.calculation.startswith("if"):
            self.has_conditionals = True
    
    # @property
    # def key(self):
    #     return self.name
    
    @property
    def calculation_keys(self):
        return re.findall(find_square_bracket_keys, self.calculation)

    def find_values(self, key_value_list):
        calculation = self.calculation
        for calculation_key in self.calculation_keys:
            if calculation_key in key_value_list:   # import to see how key_value_list works!
                value = key_value_list[calculation_key]
                calculation = calculation.replace(f"[{calculation_key}]", f"{value}")

        self.calculation = calculation

    def calculate(self):
        if self.value:
            return

        if len(self.calculation_keys) and not self.has_conditionals:
            self.exception = Exception("Not all keys are replaced with values")
            return

        self.exception = None
        self.error = None
        try:
            if self.has_conditionals:
                value = self.calculate_conditionals()

                if '=' in value:
                    value = value.replace('”', '')
                    [var, value] = value.split('=')
                value = value.replace(" ", "").replace('"', "")
                self.value = value
            else:
                self.value = eval(self.calculation)
        except Exception as e:
            self.exception_detail = e
            self.exception = Exception("Invalid calculation")

    def calculate_conditionals(self):
        conditions = self.calculation.split("else")
        for condition in conditions:
            # Checks if all required indicators have values
            if len(re.findall(find_square_bracket_keys, condition)):
                raise Exception("invalid partial condition")

            if condition == conditions[-1]:
                break

            [cond, value] = condition.split("then")
            cond = cond.replace("if", "")

            if 'AND' in cond:
                conds = [eval(n) for n in condition.split("AND")]
                if not False in conds:
                    return value

            if 'OR' in cond:
                conds = [eval(n) for n in condition.split("OR")]
                if True in conds:
                    return value

            if eval(cond):
                return value

# TODO: Accept ((cond AND cond) OR cond), instead of (cond AND cond) on itself and (cond OR cond) 