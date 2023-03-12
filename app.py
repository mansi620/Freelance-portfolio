import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="PORTFOLIO", page_icon=":blush:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# bottom_image = st.image('images\jay j.png')
# if bottom_image is not None:
#     image = 'images\jay j.png'
#     new_image = image.resize((300, 100))
#     st.image(new_image)

local_css("style/style.css")

lottie_coding_1 = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_coding_2 = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_fWd36IjnsR.json")
#img_contact_form = Image.open("images/IMG_20200426_201831_225.jpg")
img_lottie_animation = Image.open('images\JJ final (2).jpg')


with st.container():
    st.write("---")
    st.header("")
    st.write("##")

    image_column, text_column = st.columns((1, 5))
    with image_column:
        st.image(img_lottie_animation)
        # image
    with text_column:

        st.subheader("Hi, I am Jay :wave:")
        st.title("PASSION || STRENGTH || FIRE")
        st.write("##")
    st.write(
        """
            Welcome to my website! I am a passionate and experienced industrial engineer with a strong educational background in mechanical trade and pursuing Master of Science in Industrial Engineering from PFH Private Hochschule Göttingen in Germany.

    My technical skills include product costing and development, designing and manufacturing tooling, commercial negotiation, supply chain management, and proficiency in various conventional and CNC machining processes. I am also familiar with computer-aided design software, such as AutoCAD and Siemens UG NX7, and have experience using SAP for materials management, procurement, and production planning.

    During my time at Volvo, I also developed a strong understanding of the automotive industry and the importance of meeting strict quality and environmental standards. I am proud to have contributed to the production of high-quality engines that meet Euro6 emissions standards.

    Outside of my professional work, I am currently learning programming languages such as Python, R, and C++, as well as web development languages such as HTML/CSS and JavaScript.

    In addition to my technical and professional skills, I am fluent in English, Hindi, and have a basic understanding of German. I believe that my diverse skill set and multicultural background make me an attractive candidate for any organization seeking an innovative, solution-driven industrial engineer.

    So, whether you're a potential employer, colleague, or just curious to learn more about me and my work, I invite you to explore my website and get in touch to discuss how we can work together to achieve great things! 
        """
    )
    st.write(
        """
        """)
    #st.write("[Learn More >](link)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:

        st.header("WORK EXPERIENCE")
        st.subheader("Purchase Department (1year) VE Commercial Vehicle (Volvo and Eicher Joint Venture)")
        st.write(
            """
            
            :white_circle: Experience in procurement activities, such as sourcing, supplier selection, and negotiation of
            prices, terms, and contracts.
            
            :white_circle: Expertise in managing supplier relationships and vendor de-risking strategies.
            
            :white_circle: Strong analytical and problem-solving skills, including the ability to identify and resolve
            purchasing-related issues.
            
            :white_circle: Knowledge of product costing and development, including the ability to accurately estimate the
            costs of goods and services.
            
            :white_circle: Familiarity with procurement systems, such as SAP and other ERP platforms.
            
            :white_circle: Experience with commercial negotiation skills.
            
            :white_circle: Knowledge of supply crisis management and the ability to mitigate risks to avoid line stoppage.
            
            :white_circle: Experience in breakthrough cost reduction ideas generation and implementation.
            """)
        st.subheader("Logistics and Supply Chain (2year) VE Commercial Vehicle (Volvo and Eicher Joint Venture)")    
        st.write(
            """    
            :white_circle: Strong knowledge of all sourcing activities, including new supplier selection modules and supplier
            capacity management.
           
            :white_circle: Expertise in international freight forwarding, lead time analysis, mode of shipment, freight cost
            negotiation, contracting with LSP’s, monitoring DSR for shipment status, ensuring pre-alert
            document correctness with LSP, ensuring checklist approvals before arrival of shipments,
            ensuring on-time custom duty payments, domestic transportation, and setting up new line
            transport as per company requirements.
           
            :white_circle: Knowledge of end-to-end coordination with finance for settling the advance and timely payments
            of service providers.
           
            :white_circle: Experience in containers delivery planning from ports and custom duty payment and clearance on
            time as per legal and statutory requirements.
           
            :white_circle: Strong analytical and problem-solving skills, including the ability to identify and resolve supply
            chain-related issues.
           
            :white_circle: Expertise in supply chain planning and management, including forecasting, inventory
            management, and production planning.
           
            :white_circle: Familiarity with logistics and transportation software, such as TMS, WMS, and ERP systems.
           
            :white_circle: Knowledge of supply chain risk management and the ability to mitigate risks and implement
            effective contingency plans. 
        
        """
        )
        st.write("")
        with right_column:
          st_lottie(lottie_coding_1, height=600, key="coding")
        
with st.container():
             st.write("---")
           #  column = st.columns(2)
          #   with column:
             st.write("##")
             st.header("EDUCATION AND QUALIFICATION")
             st.write("""
                   :white_circle: <b>Pursuing MASTER OF SCIENCE in INDUSTRIAL ENGINEERING</b>
                   
                    PFH Private Hochschule Göttingen (Germany)
                    
                   :white_circle: BACHELORS OF TECHNOLOGY IN MECHANICAL TRADE
                   
                    Dr. A.P.J – ABDUL KALAM UNIVERSITY (India)
                    
                   :white_circle: ADVANCE DIPLOMA IN TOOL AND DIE MAKING
                   
                    Indo German Tool Room, Indore (India)
                """)

             st.write("##")
             st.header("TECHNICAL SKILLS")
             st.write("""
                   
            :white_circle: Product Costing and Development: Skilled in developing cost estimates for manufacturing
            products, including materials, labor, and overhead costs.
            
            :white_circle: Designing of Moulds, Forging Dies, Die Casting Die, Press Tools: Experienced in designing
            and developing various types of tooling, including moulds, forging dies, die casting dies, and
            press tools.
            
            :white_circle: Commercial Negotiation Skill: Proficient in negotiating with vendors and suppliers to achieve
            favorable terms and conditions for the company.
            
            :white_circle: Supply Crisis Management &amp; Vendor De-risking: Skilled in managing supply chain disruptions
            and mitigating risks associated with vendors.
           
            :white_circle: Manufacturing of Forging Dies, Die Casting Die, Press Tools: Experienced in manufacturing
            tooling using a variety of techniques and processes, including forging, casting, and machining.
           
            :white_circle: All Conventional Machine Processing (Lathe, Milling, Drilling, grinding, etc.): Proficient in
            using various conventional machining processes to produce precision parts and tooling.
           
            :white_circle: CNC Milling &amp; Turning Programming (with NX7): Skilled in programming and operating CNC
            milling and turning machines using Siemens NX7 software.
           
            :white_circle: AutoCAD (2D &amp; 3D) UG NX7 (Sketcher, Drafting, Part modeling, Assembly): Experienced in using computer-aided design software to create 2D and 3D models, including AutoCAD and Siemens UG NX7.
           
            :white_circle: Costing of Tooling, Die, Press Tools: Proficient in developing cost estimates for tooling, die, and press tool manufacturing processes.
           
            :white_circle: SAP: Familiarity with using SAP software for materials management, procurement, and production planning.
            """)

             st.write("##")
             st.subheader("Programming Languages")
             st.write("""
                        :white_circle: Python: Mid-level proficiency; currently learning through online courses and building small projects
           
                        :white_circle: R : Mid-level proficiency; currently learning in my masters courses and analyzing data sets
                    
                        :white_circle: C++: Mid-level proficiency; currently learning through online courses and building algorithms
                        """)
             st.write("##")
             st.subheader(" Web Development")
             st.write("""   
                        :white_circle: HTML/CSS: Mid-level proficiency; currently learning through online courses and building static web pages
                    
                        :white_circle: JavaScript: Mid-level proficiency; currently learning through online courses and building interactive web pages
                            """)

                

        # projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    image_column, text_column = st.columns((2, 4))
    with image_column:
        st_lottie(lottie_coding_2, height=300, key="graph")

        # image
    with text_column:
        st.subheader("FIRST SEMESTER PROJECTS")
        st.write("PORTFOLIO ON ETHICAL ISSUE RAISED DURING BS6 IMPLEMENTATION - [Link](https://drive.google.com/file/d/1eU8FmM8bTL_XLfEIB4QKoXP5lRbnFBMr/view?usp=share_link)")
        # url = 'https://drive.google.com/file/d/1pn4UiJNwYumBwWlHcR4H6G87nwNdrf-M/view'

        # st.markdown(f'''
        # <a href={url}><button style="background-color:#04AA6D;color:white;
        #     padding: 12px 20px;
        #     border: none;
        #     border-radius: 4px;
        #     cursor: pointer;">EI-PROJECT</button></a>
        # ''',
        # unsafe_allow_html=True)
        st.write("##")
        st.write("PORTFOLIO ON INTELLECTUAL PROPERTY RIGTHS - [Link](https://drive.google.com/file/d/1FhKgcDds3r4sDuihil4EuV3tL5Hz89zG/view?usp=share_link)")
        # url = 'https://drive.google.com/file/d/1FhKgcDds3r4sDuihil4EuV3tL5Hz89zG/view?usp=share_link'

        # st.markdown(f'''
        # <a href={url}><button style="background-color:#04AA6D;color:white;
        #     padding: 12px 20px;
        #     border: none;
        #     border-radius: 4px;
        #     cursor: pointer;">EI-PROJECT</button></a>
        # ''',
        # unsafe_allow_html=True)
        st.write("##")
        st.write("Employee Invention IPR Project - [Link](https://drive.google.com/file/d/1xZI73Og2Vf0Ht3nrWMG7UpPrc8UOyKoJ/view?usp=share_link)")
        st.write("##")
        st.write("Wine Quality Prediction through R language - [Link](https://drive.google.com/file/d/1uZ_XrTuA84uE-qGwkISRjVrX8gc7jHLW/view?usp=share_link)")
        st.write("##")
        st.write("Ultrasonic sensor Project - Water Level Management - [Link](https://drive.google.com/file/d/16DYHnKCKIPBaNrnpIcjMcvdrWIhKV7_l/view?usp=share_link)")

       

   # contact

with st.container():
    st.write("---")
    st.header("CONTACT ")
    st.write("##")

    contact_form = """
   <form action ="https://formsubmit.co/jadonjsj595@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">SEND</button>
    </form>    
   """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

with st.container():
    st.write("---")
    st.header("")
    st.write("##")
    twitter, linkedin, insta, fb = st.columns((1, 1, 1, 1))
    # with twitter:

    #     url = 'LINK'

    #     st.markdown(f'''
    #     <a href={url}><button style="background-color:#04AA6D;color:white;
    #         padding: 12px 20px;
    #         border: none;
    #         border-radius: 4px;
    #         cursor: pointer;">TWITTER</button></a>
    #     ''',
    #                 unsafe_allow_html=True)
    with insta:
        url = 'https://www.instagram.com/people_its_jsj/'

        st.markdown(f'''
        <a href={url}><button style="background-color:#04AA6D;color:white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;">INSTAGRAM</button></a>
        ''',
                    unsafe_allow_html=True)
    # with fb:
    #     url = 'LINK'

    #     st.markdown(f'''
    #     <a href={url}><button style="background-color:#04AA6D;color:white;
    #         padding: 12px 20px;
    #         border: none;
    #         border-radius: 4px;
    #         cursor: pointer;">FACEBOOK</button></a>
    #     ''',
    #                 unsafe_allow_html=True)
    with linkedin:
        url = 'https://www.linkedin.com/in/jay-singh-jadon-a740a0190'

        st.markdown(f'''
        <a href={url}><button style="background-color:#04AA6D;color:white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;">LINKEDIN</button></a>
        ''',
                    unsafe_allow_html=True)
# if __name__ == "__main__":
#     app.run( debug = True)
