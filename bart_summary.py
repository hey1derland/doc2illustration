from transformers import pipeline

import os

class summary_api:
    def __init__(self, bart_model):

        summarizer = pipeline("summarization", model=bart_model)
        self.summarizer = summarizer
        
    def summarization(self, input_text, max_length=20, min_length=2, do_sample=True):
        
        summary =  self.summarizer(input_text, 
                                   max_length=max_length, min_length=min_length, do_sample=do_sample)
        
        return summary
    
def paragraph_parser(text_path:str)->list:
    with open(text_path, 'r') as t:
        new_txt_list=[txt.strip() for txt in t.read().split('\n\n')]
    
    return new_txt_list

def do_summary_and_save_results(api, text_path:str)->list:
    l = paragraph_parser(text_path)
    
    summary_list = []
    for text in l:
        summary = api.summarization(text)[0]['summary_text']
        # del_part = summary.split('.')[-1]
        # summary = summary.replace(del_part, '')
        summary = summary.split('.')[0]
        summary_list.append(summary)
    return summary_list

if __name__ == "__main__":
    bart_model = "facebook/bart-large-xsum"
    tale_names = ['pinocchio', 'the_frog_prince', 'the_little_match_girl']
    for tale_name in tale_names:
        text_path = f'./{tale_name}.txt'
        api = summary_api(bart_model)
        do_summary_and_save_results(api=api, text_path=text_path)

        
