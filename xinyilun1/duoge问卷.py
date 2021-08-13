import unittest
from survey import AnoynousSurvey
class TestAnonynousSurvey(unittest.TestCase):
    "对于类的测试"
    def test_single_store_response(self):
        "测试单个问卷数据储存情况"
        question = "What's your name?"
        my_suvey = AnoynousSurvey(question)
        my_suvey.score_response("张三")
        self.assertIn("张三", my_suvey.response)
    def test_mul_store_reponse(self):
        "测试多个问卷的储存情况"
        question = "What's your name?"
        my_survey = AnoynousSurvey(question)
        reponse = ["张三","李四","王五"]
        for n in reponse:
            my_survey.score_response(n)
        for m in reponse:
            self.assertIn(m,my_survey.response)
unittest.main()
