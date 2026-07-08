from langchain_core.output_parsers import JsonOutputParser
from models import llm
from prompts import  resume_prompt as resume_analysis_prompt
from prompts import  (interview_prompt,feedback_prompt)
from langchain_core.output_parsers import StrOutputParser



parser = JsonOutputParser()
feedback_parser = JsonOutputParser()
string_parser = StrOutputParser()

resume_chain = resume_analysis_prompt | llm | parser
interview_chain = interview_prompt| llm| string_parser
feedback_chain= feedback_prompt | llm | feedback_parser


def analyze_resume(resume, jd):
    result = resume_chain.invoke(
        {
            "resume": resume,
            "jd": jd
        }
    )
    return result


def ask_question(analysis, interview_history, question_number):

    history = ""
    for item in interview_history:
        history += f"""
    Question {item['question_number']}

    {item['question']}

    Answer

    {item['answer']}
    """

    return interview_chain.stream(
        {
            "analysis": analysis,
            "conversation": history,
            "question_number": question_number
        }
    )


def evaluate_interview(analysis,interview_history):
    print(interview_history)
    return feedback_chain.invoke(
        {
            "analysis": analysis,
            "interview_history": interview_history
        }
    )