import streamlit as st

from agentpro.tools.course_tool import CourseRecommendationTool
from agentpro.tools.blog_tool import BlogRecommendationTool
from agentpro.tools.roadmap_tool import RoadmapTool

st.set_page_config(page_title="AI MOOC Recommender", layout="centered")

st.markdown(
    "<h1 style='text-align: center;'>🌟 AI MOOC Recommender System</h1>",
    unsafe_allow_html=True
)
st.write("Get personalized course, blog, and learning roadmap recommendations.")

topic = st.text_input("Enter the topic you want to learn (e.g., Python, Data Science):")

if st.button("Get Recommendations") and topic:
    st.info("Gathering recommendations...")

    # Instantiate tools
    courses_tool = CourseRecommendationTool()
    blogs_tool = BlogRecommendationTool()
    roadmap_tool = RoadmapTool()

    # Run tools (results should be markdown/text)
    courses_md = courses_tool.run(topic)
    blogs_md = blogs_tool.run(topic)
    roadmap_md = roadmap_tool.run(topic)

    tab1, tab2, tab3 = st.tabs(["📚 Courses", "📝 Blogs", "🛣️ Roadmap"])

    with tab1:
        st.subheader("Courses (with URLs)")
        if courses_md:
            # This expects markdown with [title](url) or similar
            st.markdown(courses_md, unsafe_allow_html=True)
        else:
            st.write("No course recommendations found.")

    with tab2:
        st.subheader("Tech Blogs")
        if blogs_md:
            st.markdown(blogs_md, unsafe_allow_html=True)
        else:
            st.write("No blog recommendations found.")

    with tab3:
        st.subheader("Learning Roadmap")
        if roadmap_md:
            st.markdown(f"```markdown\n{roadmap_md}\n```")
        else:
            st.write("No roadmap could be generated.")

    st.success("Done! Happy Learning 🚀")

else:
    st.write("Enter a topic and click the button above.")

