from priority_list import PriorityList
from norm_list import NormList

'''
test_norm_list = NormList()
test_norm_list.update_list()
test_norm_list.update_list()
test_norm_list.update_list()
print(test_norm_list.call_client(12))
'''

test_priority_list = PriorityList()
test_priority_list.update_list()
test_priority_list.update_list()
test_priority_list.update_list()
print(test_priority_list.call_client(10))
print(test_priority_list.call_client(1))
print(test_priority_list.statistics(day=10, agency=1234, flag='detail'))
