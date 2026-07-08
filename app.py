import streamlit as st
from chains import (
    analyze_resume,
    ask_question,
    evaluate_interview,
)
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Interview Coach")

if "warning" not in st.session_state:
    st.session_state.warning=None

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "question_number" not in st.session_state:
    st.session_state.question_number = 1

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "current_question" not in st.session_state:
    st.session_state.current_question = ""
  
if "feedback" not in st.session_state:
   st.session_state.feedback=None



    
resume = st.text_area(
    "Paste Resume",
    height=250
)

jd = st.text_area(
    "Paste Job Description",
    height=250
)



if st.button("Analyze Resume"):
    if not resume or not jd:
        st.warning("Please enter Resume and Job Description.")
    else:
        with st.spinner("Analyzing Resume..."):
            try:
                analysis = analyze_resume(resume, jd)
                st.session_state.analysis = analysis
            except Exception as e:
                st.error(str(e))


if st.session_state.analysis:  
  analysis = st.session_state.analysis

  st.subheader("📊 Match Score")
  st.metric(
      "Score",
      f"{analysis['match_score']}%"
  )


  st.subheader("📄 Resume Summary")
  st.write(
      analysis["resume_summary"]
  )


  st.subheader("📄 Job-Desciption Summary")
  st.write(
      analysis["job_description_summary"]
  )




  st.subheader("✅ Matching Skills")
  for skill in analysis["matching_skills"]:
      st.write(f"• {skill}")




  st.subheader("✅ Missing Skills")
  for skill in analysis["missing_skills"]:
      st.write(f"• {skill}")

  st.subheader("✅ resume_improvements")
  for skill in analysis["resume_improvements"]:
      st.write(f"• {skill}")

  st.subheader("💡 Feedback")
  st.write(
      analysis["overall_feedback"]
  )


# ----------------------------
# Start Interview
# ----------------------------
if st.button("🚀 Start Interview") :
  if not st.session_state.analysis:
    st.warning("first get the analysis")
  else:
    st.session_state.interview_started = True
    st.session_state.question_number = 1
    st.session_state.conversation =[]
    st.session_state.current_question = ""

  # ----------------------------
  # Interview Screen
  # ----------------------------
if st.session_state.interview_started:
  # Generate a question only if there isn't one already
  if st.session_state.current_question == "":
    question_stream = ask_question(
              st.session_state.analysis,
              st.session_state.conversation,
              st.session_state.question_number
          )

    with st.chat_message("assistant"):
      question = st.write_stream(question_stream)

    st.session_state.current_question = question

      # Display the current question
      #st.chat_message("assistant").write(st.session_state.current_question)

      # Wait for user answer
  answer = st.chat_input("Type your answer...")

  if answer:
    st.chat_message("user").write(answer)
    # Save Question + Answer
    st.session_state.conversation.append({"question_number":st.session_state.question_number,                                
    f"question":st.session_state.current_question,
    f"answer":answer})
    

    st.session_state.question_number += 1

            # Clear current question so next rerun generates a new one
    st.session_state.current_question = ""

            # Interview finished?
    if st.session_state.question_number > 5:
      st.session_state.interview_started = False
      st.success("🎉 Interview Completed!")
     
      st.rerun()

        # Immediately rerun to generate next question
    st.rerun()

if st.session_state.question_number>5:
    if st.button("📊 Generate Feedback"):
         with st.spinner("Generating Feedback..."):
            feedback = evaluate_interview(
            st.session_state.analysis,st.session_state.conversation
            )
            st.session_state.feedback = feedback
if st.session_state.feedback:

    feedback = st.session_state.feedback

    st.divider()
    st.header("📊 Interview Performance Report")

    # ===========================
    # Overall Score
    # ===========================

    score = feedback["overall_score"]

    st.metric(
        label="🏆 Overall Score",
        value=f"{score}/100"
    )

    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent performance! You're interview ready. 🚀")
    elif score >= 60:
        st.warning("Good performance. A little more preparation will help.")
    else:
        st.error("Needs improvement. Focus on the recommended topics below.")

    st.divider()

    # ===========================
    # Overall Feedback
    # ===========================

    st.subheader("📝 Overall Evaluation")

    st.info(feedback["overall_feedback"])

    st.divider()

    # ===========================
    # Strengths & Weaknesses
    # ===========================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💪 Strengths")

        for item in feedback["strengths"]:
            st.success(item)

    with col2:

        st.subheader("⚠️ Areas to Improve")

        for item in feedback["weaknesses"]:
            st.warning(item)

    st.divider()

    # ===========================
    # Learning Roadmap
    # ===========================

    st.subheader("📚 Recommended Learning Topics")

    for topic in feedback["topics_to_learn"]:
        st.markdown(f"- {topic}")

    st.divider()

    # ===========================
    # Interview Tips
    # ===========================

    st.subheader("🎯 Interview Tips")

    for tip in feedback["interview_tips"]:
        st.info(tip)

    st.divider()
