import numpy as np
import sys

## IIT base class
class IIT_Base(object):
    def __init__(self) -> None:
        super().__init__()
        _contributions = {
            "unemployment" : 0.005,
            "pension" : 0.08,
            "medical" : 0.02,
            "housing" : 0.07,
            "supp_housing" : 0.05,
        }
        self._cont_rate = sum(_contributions.values())
        self._deduction = 0
        self._allowance = 0
        self._m_std_tax_deduction = 60000 / 12
        self._tax_level = {
            "taxable_income" : np.array([0, 3.6, 14.4, 30, 42, 66, 96]) * 1e4,
            "tax_rate" : np.array([0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45]),
            "quick_deduction" : np.array([0, 2520, 16920, 31920, 52920, 85920, 181920]),
        }

    def update_para(self, para_dict:dict):
        self._deduction = sum(para_dict["deduction"].values())
        self._allowance = sum(para_dict["allowance"].values())



## IIT per month
class IIT_Month(IIT_Base):
    def __init__(self, init_para:dict) -> None:
        super(IIT_Month, self).__init__()
        self.update_para(init_para)
        self.continuous_mode = True if init_para["previous_earning"] is None else False

        self._total_allowance = 0
        self._taxable_income = 0
        self._previous_tax = 0
        self._total_earning = 0
        self._tax = 0
        self._pay = 0

    def set_other_deduction(self, deduction_dict:dict):
        self._other_deduction.update(deduction_dict)

    def calc_tax(self):
        if len(self._other_deduction) > 0:
            self._deduction_rate += sum(self._other_deduction.values())
        self._taxable_income = (self._base + sum(self._allowance.values())) * (1-self._deduction_rate)
        return self._tax

    def calc_pay(self):

        return self._pay

    def __call__(self, para_dict:dict):
        self.base = 0



# ## IIT per month
# class IITM(object):
#     def __init__(self):
#         super().__init__()

#         self._tax_exemption = 5000
#         # self._housing_allowance = 0
#         self._reduction_rate = {
#             "unemployment" : 0.01,
#             "pension" : 0.08,
#             "medical" : 0.02,
#             "housing" : 0.07,
#             "supp_housing" : 0.05,
#         }
#         self._total_reduction_rate = sum(self._reduction_rate[it] for it in self._reduction_rate)

#         self._espp = (False, 0.15) # (w/o ESPP, ESPP rate)
#         if self._espp[0]:
#             self._total_reduction_rate += self._espp[1]

#     def __call__(self, income, acc_income=0, acc_tax=0, reduction_base=None):
#         if(reduction_base == None):
#             reduction_base = income
#         taxable_income = income - reduction_base * self._total_reduction_rate - self._tax_exemption
#         print(taxable_income)

        


# ## IIT per year
# class IIT(object):
#     def __init__(self):
#         super().__init__()
#         self._taxable_income_level = np.array([0, 3.6, 14.4, 30, 42, 66, 96,], dtype=np.int64) * 1e4
#         self._rate_level = np.array([3, 10, 20, 25, 30, 35, 45], dtype=np.int64) * 1e-2
#         self._tax_stage = self._taxable_income_level[1:] - self._taxable_income_level[:-1]
#         self._tax_exemption = 60000

#     def calc_taxable_income(self, income):
#         # Tax exemption
#         taxable_income = income - self._tax_exemption
#         return taxable_income

#     def get_tax_rate(self, taxable_income) -> list:
#         return np.where(taxable_income > self._taxable_income_level, self._rate_level, 0)

#     def calc_iit(self, income):
#         taxable_income = self.calc_taxable_income(income)
#         tax_rate = self.get_tax_rate(taxable_income)
#         taxable_income_vec = taxable_income - self._taxable_income_level
#         taxable_income_vec[:np.min(np.argwhere(tax_rate == 0))] = self._tax_stage[:np.min(np.argwhere(tax_rate == 0))]
#         tax = np.dot(tax_rate, taxable_income_vec)
#         return tax


if(__name__ == "__main__"):
    # print(IIT().get_tax_rate(37000))
    # print(IIT().calc_iit(int(sys.argv[1])))

    para = {
        "base" : 23500,
        "previous_earning" : 23500 *6,
        "allowance" : {
            "transport" : 275,
            "housing" : -393.51,
        },
        "deduction" : {
            "espp" : 0.15 * 23500,
            "add_dediction" : 1500,
        },
    }

    # IITM()(15000)

