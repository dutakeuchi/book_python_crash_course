# %%
from survey import AnnonymousSurvey
# %%
# def test_single_response():
#     question = 'What is your favorite color:'
#     color_survey = AnnonymousSurvey(question)
    
#     color_survey.store_response('blue')
#     assert 'blue' in color_survey.responses

# def test_tree_responses():
#     question = 'What is your favorite color:'
#     color_survey = AnnonymousSurvey(question)
    
#     responses = ['blue','red','yellow']
#     for response in responses:
#         color_survey.store_response(response)
    
#     for response in responses:
#         assert response in color_survey.responses
        
# %%
import pytest
from survey import AnnonymousSurvey

@pytest.fixture

def color_survey():
    question = 'What is your favorite color:'
    color_survey = AnnonymousSurvey(question)
    return color_survey    

def test_single_response(color_survey):
    color_survey.store_response('green')
    assert 'green' in color_survey.responses
    
def test_tree_responses(color_survey):
    responses = ['blue','red','yellow']
    for response in responses:
        color_survey.store_response(response)
    
    for response in responses:
        assert response in color_survey.responses    