import os
import google.generativeai as genai
from PyPDF2 import PdfReader
import requests


#os.environ['GOOGLE_API_KEY'] = "AIzaSyDX8nOYdw3WL_TteBysZpKWPtosyAnDpCM"
os.environ['GOOGLE_API_KEY'] = "AIzaSyC5sFACVH4CCKbtiCqF16KXzK3fs4kJe3k"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
COPYLEAKS_API_KEY = "013356d5-2c34-4415-bd97-8732051e42a2"

model = genai.GenerativeModel('gemini-pro')

try:
    with open("./Course Content.pdf", "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        course_content = ""
        for page in pdf_reader.pages:
            course_content += page.extract_text()
except:
    pass



try:
    with open("./Student Answer MCQ.pdf", "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        stud_MCQ= ""
        for page in pdf_reader.pages:
            stud_MCQ += page.extract_text()
except:
    pass

try:
    with open("./Student Answer Subjective.pdf", "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        stud_Subj= ""
        for page in pdf_reader.pages:
            stud_Subj += page.extract_text()
except:
    pass

try:
    with open("./Solution to Quizzes.pdf", "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        prof_ans= ""
        for page in pdf_reader.pages:
            prof_ans += page.extract_text()
except:
    pass

#def answer_question(question, prof_ans, course_content): 
#    response = model.generate_content(f"This is my class content {course_content} \n This is quiz i conducted  {prof_ans} \n  Answer the question: {question}")
#    return response.text


reinforcement = []
#index 0 goes content_complexity
def content_complexity(prof_ans, course_content):
    response = model.generate_content(f"I am a professor. This is my class content {course_content} \n I have give the following quiz to my students {prof_ans} \n Tell my if the quiz which i have given, explains all the concepts clearly to a beginner in the field. Tell if it could be potentially too complex for them to understand. Give your answer in short concise points.")
    reinforcement.append(response.text)
    return response.text

    
def find_possible_misinterpretations(prof_ans, stud_Subj, course_content):
    respose = model.generate_content(f"I am a professor. This is my class content {course_content}") 
    response = model.generate_content(f"I have give the following quiz to my students {prof_ans} \n These are the answers which the students have responded: {stud_Subj} \n  Analyze these answers and find if the students, who are beginner in the field could have possibly misinterpreted the question which I have presented them in the context of the class content. Give your answer in short concise points")
    return response.text

#Christopher
def analyze_excel(qusetion,prof_ans,excel_file_path, additional_data):
   """here the code for excel analysis will go pandas . it will generate some parameteres like average , maximun etc"""
   respose = model.generate_content(f"") #based on variables form prompt


def find_similarity(text):
    headers = {"Authorization": f"Bearer {COPYLEAKS_API_KEY}"}
    payload = {"text": text}

    try:
        response = requests.post("https://api.copyleaks.com", headers=headers, json=payload)
        response.raise_for_status()
        
        if response.content:  # Check if response is not empty
            data = response.json()
            return data.get("is_ai_generated", False)
        else:
            print("Empty response from the API.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error in API request: {e}")
        return False



#index 1 goes conten_fault
def content_fault(stud_Subj,prof_ans,course_content,stud_MCQ):

    response1 = model.generate_content(f"I am a professor. This is my class content {course_content}")
    response = model.generate_content(f"\n I have give the following quiz to my students {prof_ans} \n These are the answers of the students for the quiz: {stud_MCQ} \n These are the subjective questions which I have given to them as well as their answers. {stud_Subj} \n In context to the answers given, find the fault in the class content and give the possible ways it could have been improved so that the students would have scored better in the quiz.")
    return response.text


def rein_force(prof_ans, stud_Subj, course_content):
    if (stud_Subj==None or prof_ans== None or course_content == None):
        raise ZeroDivisionError("Division by zero is not allowed")
    reinforcement = []
    reinforcement.append(content_complexity(prof_ans, course_content))
    reinforcement.append(find_possible_misinterpretations(prof_ans, stud_Subj, course_content))
    response = model.generate_content(f"I am a professor. This is the feedback given to me regarding my course complexity: {reinforcement[0]} \n This is the feedback given to me regarding the potential faults in my course content which might by causing the students difficulty in the quizzes. {reinforcement[1]} \n Analyze both the feedbacks and give me a concise overall feedback which takes into account both the point of views. Your response should be helpful for me as a professor so that I can provide better lectures to my students. It should briefly highlight the subtle good things I am doing well as well as constructively critique whichever concepts and/or content delivery methods I am lacking and how can I improve them. It should be specific to the class content only and avoid general generic feedback.")
    return (response.text).replace("*",'')

    

def main():
    pass
    # a = content_complexity(prof_ans, course_content)
    # print(a,"\n\n\n")
    # b = find_possible_misinterpretations(prof_ans, stud_Subj, course_content)
    # print(b, "\n\n\n")
    # c = content_fault(stud_Subj,prof_ans,course_content,stud_MCQ)
    # print(c, "\n\n\n")
    # d = rein_force()
    # print(d, "\n\n\n")

if __name__ == "__main__":
    main()