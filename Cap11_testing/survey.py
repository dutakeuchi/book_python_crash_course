# %%
class AnnonymousSurvey:
    """colect annonymous responses from a survey"""
    
    def __init__(self, question):
        '''store the question'''
        self.question = question
        self.responses = []
        
    def show_question(self):
        '''shows question'''
        print(self.question)
        
    def store_response(self, new_response):
        '''store the response'''
        self.responses.append(new_response)
        
    def show_results(self):
        '''shows all responses'''
        print('Survey responses')
        
        for response in self.responses:
            print(response)
# %%
# question = 'What is your favorite color?'
# color_survey = AnnonymousSurvey(question)

# color_survey.show_question()
# print("Press 'q' to exit")
# while True:
#     color = input()
#     if color == 'q':
#         break
#     else:
#         color_survey.store_response(color)

# color_survey.show_results()