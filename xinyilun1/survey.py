class AnoynousSurvey():
    "搜集匿名问卷调查的结果"
    def __init__(self,question):
        "储存问卷"
        self.question = question
        self.response = []
    def show_question(self):
        "显示问卷调查"
        print(self.question)
    def score_response(self,new_reponse):
        "存储调查问卷答案"
        self.new_response = new_reponse
        self.response.append(new_reponse)
    def show_result(self):
        "显示所有的答卷"
        print("Survey result:")
        for i in self.response:
            print(i)



