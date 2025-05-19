import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Marketing
    **The Chinese University of Hongkong | *August 2024 - June 2025*
    
    - GPA: 3.9/4.0
    - Relevant Coursework: Machine Learning, Social Media Analysis, Customer Analysis, Big Data, Integrated Marketing Communication
    
    ### Bachelor of Marketing
    **The Renmin University of China** | *September 2020 - June 2024*
    
    - GPA: 3.7/4.0
    - Graduated with Honors
    - Relevant Coursework: Marketing Principles, Consumer Behavior, Marketing Research, Digital Marketing, Big Data Stragety, Integrated
Marketing Communication, Brand Management, Retail Management, Marketing Decision Model, Statistics, Econometrics,
Advertising Creative Communication, Logistic Management, Statistics, Accounting, Financial Management
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### The Planning of An Integrated Marketing Program for Terun Carbonated Probiotic Milk Drink
    -  Designed and implemented a consumer survey, analyzed the results of 183 questionnaires using SPSS, pinpointed that the
brand’s issue was a lack of product recognition, and developed an integrated marketing campaign
    - Developed a pop-up shop proposal for Shanghai, Chengdu, and Xinjiang based on product and city features, and designed IP
to bring the brand closer to its potential customers through the creation of a cartoon character and limited edition packaging
    
    ### Streets in China - Field Research on the City of Chengdu
    - Researched city data like commodities pricing, rental rates, and digital government, and conducted face-to-face interviews
with grass-roots government staff to know the keys and challenges of street development
    - Visited street markets, day-care centers, etc. to gain first-hand data and produced a research paper
    """)
    
    st.markdown("---") 