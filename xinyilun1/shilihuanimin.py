from  survey import AnoynousSurvey
"实例化对象"
question = "What's your name?"
my_survey = AnoynousSurvey(question)
my_survey.show_question()
print("Enter 'q' exit sys!")
while True:
    reponse = input("名字为：")
    if reponse == 'q':
        break
    else:
        my_survey.score_response(reponse)
# 显示调查结果
print("感谢您参与问卷调查，辛苦啦！")
my_survey.show_result()