from typing import Union

from norm_list import NormList
from priority_list import PriorityList
from constants import TYPE_LIST_NORM, TYPE_LIST_PRIORITY

class FactoryList:
    @staticmethod
    def get_list(list_type) -> Union[NormList, PriorityList]:
        if list_type == TYPE_LIST_NORM:
            return NormList()
        elif list_type == TYPE_LIST_PRIORITY:
            return PriorityList()
        else:
            raise NotImplementedError('Type not implemented')