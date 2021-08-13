import unittest
from Name_Function import get_fomatted_name
class namesTestCase(unittest.TestCase):
    "测试姓名函数"
    def test_first_last_name(self):
        "能够正确处理两个字的姓名吗？"
        formatted_name = get_fomatted_name("张","大爷")
        self.assertEqual(formatted_name,"张大爷")
    def test_first_last_midddle_name(self):
        "能偶正确处理三个字的名字吗？"
        formatted_name = get_fomatted_name("陈","刘璋","王")
        self.assertEqual(formatted_name,"陈王刘璋")
unittest.main()