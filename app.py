import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

## Function To get response from LLAma 2 model

def getResponse(text_input,words_limit,blog_type):

    ### LLama2 model
    llm=Ollama(model='llama2')
    
    ## Prompt Template

    template="""
        Write a blog for {blog_type} job profile for a topic {text_input}
        within {words_limit} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_typr","text_imput",'words_limit'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm.invoke(prompt.format(blog_type=blog_type,text_input=text_input,words_limit=words_limit))
    print(response)
    return response






st.set_page_config(page_title="Generate the Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

text_input=st.text_input("Write the Blog Topic")


col1,col2=st.columns([5,5])

with col1:
    words_limit=st.text_input('Words Limit')
with col2:
    blog_type=st.selectbox('Writing this blog for',
                            ('Data Scientist','AI Researcher','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getResponse(text_input,words_limit,blog_type))