import numpy as np
import sys

## IIT per month
class IITM(object):
    def __init__(self):
        super().__init__()

        self._tax_exemption = 5000
        # self._housing_allowance = 0
        self._reduction_rate = {
            "unemployment" : 0.01,
            "pension" : 0.08,
            "medical" : 0.02,
            "housing" : 0.07,
            "supp_housing" : 0.05,
        }
        self._total_reduction_rate = sum(self._reduction_rate[it] for it in self._reduction_rate)

        self._espp = (False, 0.15) # (w/o ESPP, ESPP rate)
        if self._espp[0]:
            self._total_reduction_rate += self._espp[1]

    def __call__(self, income, acc_income=0, acc_tax=0, reduction_base=None):
        if(reduction_base == None):
            reduction_base = income
        taxable_income = income - reduction_base * self._total_reduction_rate - self._tax_exemption
        print(taxable_income)

        


## IIT per year
class IIT(object):
    def __init__(self):
        super().__init__()
        self._taxable_income_level = np.array([0, 3.6, 14.4, 30, 42, 66, 96,], dtype=np.int64) * 1e4
        self._rate_level = np.array([3, 10, 20, 25, 30, 35, 45], dtype=np.int64) * 1e-2
        self._tax_stage = self._taxable_income_level[1:] - self._taxable_income_level[:-1]
        self._tax_exemption = 60000

    def calc_taxable_income(self, income):
        # Tax exemption
        taxable_income = income - self._tax_exemption
        return taxable_income

    def get_tax_rate(self, taxable_income) -> list:
        return np.where(taxable_income > self._taxable_income_level, self._rate_level, 0)

    def calc_iit(self, income):
        taxable_income = self.calc_taxable_income(income)
        tax_rate = self.get_tax_rate(taxable_income)
        taxable_income_vec = taxable_income - self._taxable_income_level
        taxable_income_vec[:np.min(np.argwhere(tax_rate == 0))] = self._tax_stage[:np.min(np.argwhere(tax_rate == 0))]
        tax = np.dot(tax_rate, taxable_income_vec)
        return tax


if(__name__ == "__main__"):
    # print(IIT().get_tax_rate(37000))
    # print(IIT().calc_iit(int(sys.argv[1])))
    IITM()(15000)

