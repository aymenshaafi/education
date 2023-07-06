import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
import base64
def main():
   
    page = st.sidebar.selectbox('Select a page', ['Home','Client', 'HR', 'Proposal', 'Analysis','Table'])
    

    if page == 'Home':
        
        # Client Part
        image = Image.open('C:/Users/Ahmed/Desktop/th (2).jpg')

        st.image(image, use_column_width=150)
        st.title('***Welcome To Egec CRM***') 
        st.info('Easy Way to Drive Buisess Using Smart Tools')

    if page == 'Client':
        st.title('**Client Page**') 

        client_name = st.text_input('Client Name')
        client_location = st.selectbox('Client Location', [" ",'International Client', 'Local Client'])
        client_segment = st.selectbox('**Client Segment**',[" ",'Government','Semi-government','Real Estate Developer','Consultant','Contractor','Development Aid','Private Investor','Other'])

        # Mandatory Data But With Condition

        collaboration = st.selectbox('Collaboration',[' ','Yes','No'])
        clfield = ''
        clcountry = ''
        clphone = ''
        clemail = ''
        clwebsite = ''
        clcontactname = ''
        clcopo = ''
        clegperson = ''
        if collaboration == 'Yes':
            clfield = st.text_input('**Field**')
            clcountry = st.text_input('**Country**')
            clphone = st.text_input('**Phone**')
            clemail = st.text_input('**Email**')
            clwebsite = st.text_input('**Website**')
            clcontactname = st.text_input('**Client Contact Name**')
            clcopo = st.text_input('**Client Contact Position**')
            clegperson = st.text_input('**EGEC Contact Person**')
        cl_save = st.button('Save')
        if cl_save :
            old_df = pd.read_csv('C:/Users/Ahmed/Clients11111.csv') 
            # إضافة البيانات الجديدة
            new_data = [client_name, client_location, client_segment, collaboration, clfield, clcountry, clphone, clemail, clwebsite, clcontactname, clcopo, clegperson]
            new_df = pd.DataFrame([new_data], columns=['Client Name','Client Location','Client Segment','Collaboration','clfield', 'clcountry', 'clphone', 'clemail', 'clwebsite', 'clcontactname', 'Client Contact Position', 'EGEC Contact Person']) 

            # دمج البيانات القديمة والجديدة
            df1 = pd.concat([old_df, new_df], ignore_index=True)

            # حفظ القائمة الجديدة في ملف الإكسل
            df1.to_csv('C:/Users/Ahmed/Clients11111.csv', index=False)

            # عرض رسالة تأكيد عند الحفظ
            st.success('Data saved successfully!')
# _________________________________________________________________________________________________________________________                 
# __________________________________________________________________________________________________________________________         
                        
        # HR Part

    elif page == 'HR':    
    #elif HR_Data:   
        st.header('**HR Details**') 
        Professional_Resources=st.selectbox('**Professional Resources:**',[" ",'EGEC','Sister Company','Affiliated','Ex-Employee'])
        hr_code = st.text_input('1-Employees Code:')
        hr_english_name = st.text_input('2-English Name:')
        hr_arabic_name = st.text_input('Arabic Name:')
        hr_department = st.selectbox('3-A. Department:', [" ",'Architectural', 'Building Information Modeling "BIM"', 'Construction Supervision', 'Design Management Unit "DMU"', 'Electromechanical', 'Geotechnical "Heavy Civil & Marine"', 'MEP CS', 'Project Management', 'Quantity Survey "QS"', 'Structural', 'Technical Quality Unit "TQU"', 'Technical Support for Sister Companies', 'Transportation "Highways & Traffic"', 'Urban Planning', 'W&E CS', 'Water & Environment', 'Others'])
        hr_detail = st.selectbox('More Detail if available:', ['Acoustics', 'Agricultural', 'Arbitration/Claims Disputes', 'Architectural', 'BIM', 'Chemical', 'Coastal', 'Construction Management', 'Corrosion', 'CS - Buildings', 'CS - MEP', 'CS - W&E', 'Design - Civil', 'Design - MEP', 'Design - Treatment Works', 'DMU', 'Economics', 'Electrical', 'Environmental', 'Gas and Oil' 'Geology', 'Geophysics', 'Geotechnical', 'GIS', 'High Voltage and Energy', 'HSE (Safety)', 'Interior Design', 'Irrigation and Hydraulics', 'Lab', 'Landscape Design', 'Light Current', 'Manufacturing', 'Mechanical - FF & Plumbing', 'Mechanical - HVAC', 'Pavement Design & Maintenance', 'Planning', 'PM', 'QA/QC', 'QS', 'Railway', 'Restoration & Conservation', 'Roads & Bridges', 'SCADA', 'Sister Companies Technical Support', 'Socio-economics', 'Sociology', 'Solid Waste Management', 'Storm', 'Structural', 'Structural & QS', 'Topographical Surveying & Geodesy', 'TQ', 'Transportation & Traffic', 'Urban Planning & Landscape', 'Wastewater', 'Water', 'Others'])

        hr_service = st.selectbox('4-Service:', [" ",'Design', 'Construction', 'Supervision', 'Project Management', 'Studies'])
        hr_position = st.selectbox('5-Position:', [" ",'Chemist', 'Construction Manager', 'Dept. Deputy Manager', 'Design Manager', 'Director', 'Document Controller', 'Draftsman', 'Engineer', 'Expert', 'Follow up Engineer', 'Freelancer', 'Geologist', 'Group Leader', 'Inspector', 'Junior Draftsman', 'Junior Engineer', 'Junior Geologist', 'Junior Officer', 'Junior Specialist', 'Manager', 'Monitor', 'Project Engineer', 'Project Geologist', 'Project Manager', 'Project Manager Assistant', 'Senior Document Controller', 'Senior Draftsman', 'Senior Engineer', 'Senior Geologist', 'Senior Project Manager', 'Senior Technician', 'Supervisor', 'Surveyor', 'Technical Consultant', 'Technical Manager', 'Technician', 'Unit / Dept. Manager', 'Other'])
        hr_qualification = st.selectbox('6-Qualification:', [" ",'Ph.D', 'M.Sc', 'B.Sc', 'B.A', 'Diploma', 'Diplome', 'Institute', 'others'])
        hr_grad_specialization = st.date_input('Graduation Specialization:')
        hr_years_exp = st.text_input('Years of Experience:')
        hr_joined_egec = st.date_input('Join Date at EGEC:')

        st.subheader('***Personal Data:***')
        hr_Mobile=st.text_input('Mobile: ')
        hr_Email=st.text_input('Email:') 
        hr_Year_of_Birth=st.date_input('Year of Birth:')
        Last_update_CV=st.date_input('Last update CV (Date):')
        Available_certificate=st.text_input('Available certificate:')
        Comment=st.text_input('Comment (Notes):')
        Attachment=st.file_uploader('Attachment CV (original):')
        hr_save=st.button('Save')
        if hr_save :

            old_df2 = pd.read_csv('C:/Users/Ahmed/HR11111.csv') if os.path.isfile('C:/Users/Ahmed/HR11111.csv') else pd.DataFrame()
            new_data2={'Professional_Resources': Professional_Resources, 'hr_code': hr_code, 'hr_english_name': hr_english_name, 'hr_arabic_name': hr_arabic_name, 'hr_department': hr_department, 'hr_detail': hr_detail, 'hr_service': hr_service, 'hr_position': hr_position, 'hr_qualification': hr_qualification, 'hr_grad_specialization': hr_grad_specialization, 'hr_years_exp': hr_years_exp, 'hr_joined_egec': hr_joined_egec, 'hr_Mobile': hr_Mobile, 'hr_Email': hr_Email, 'hr_Year_of_Birth': hr_Year_of_Birth, 'Last_update_CV': Last_update_CV, 'Available_certificate': Available_certificate, 'Comment': Comment, 'Attachment': Attachment}
            new_df2=pd.DataFrame([new_data2])
            dtf=pd.concat([old_df2, new_df2], ignore_index=True)

            # حفظ القائمة الجديدة في ملف الإكسل
            dtf.to_csv('C:/Users/Ahmed/HR11111.csv', index=False)

            # عرض رسالة تأكيد عند الحفظ
            st.success('Data saved successfully!')
#_________________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________________         
                    
    # Proposal Page          

    elif page == 'Proposal':
    #elif Proposal_Data:
        
        st.text_input('1- EGEC Proposal No')
        Proposal_Type= st.selectbox('**2- Proposal Type:**',[" ",'Proposal','Prequalification','EOI'])
        Service_Type= st.selectbox('**3- Service Type:**',[" ",'Design', 'Construction','Supervision','Project','Management','Studies'])
        Business_Line=st.selectbox('**4- Business Line:**',[" ",'Building & Facilities', 'EnergySpecialized', 'Studies', 'Transportation','Urban', 'Development', 'Water & Environment'])
        Specialized_Studies=st.selectbox('**Specialized Studies:**',[" ",'Geotechnical', 'Heavy Civil & Marine', 'TIAS', 'EIA', 'Energy' ,'Audit'])
        pro_Country=st.text_input('5- Country:')
        Project_Location=st.text_input('6- Project Location')
        Project_Type=st.selectbox('**7- Project Type:**',[" ",'Airports','Bridges & Tunnels','Coastal & Marine','Commercial & Administrative','Buildings','Cultural, Sports & Worship',
    'Facilities','Dams & Hydraulic Structures','Data Centers & Telecom','Buildings','Desalination Plant','Educational Facilities','Energy','Environmental','Ground Water Lowering',
    'Healthcare Facilities','Hotels','Industrial Facilities','Integrated Wastewater','Master Plan','Military Facilities','Multipurpose Highrise Buildings','Museums',
    'Parking','Parks','Pharmaceutical Facilities','Police Facilities','Primary Infrastructure (Dr. ER)','Railways','Residential Buildings','Restoration of Historical',
    'Buildings','Roads','Secondary Infrastructure (MEPTeam)','Shopping Malls','TIAS Traffic Impact Assessment','Studies','Wastewater Treatment Plant'
    'Water Supply''Water Treatment Plant''Others'])
        Internal_Disciplines=st.selectbox("**8- Internal Disciplines related to the Proposal:**",[" ",'Architecture', 'Interior' ,'Design' ,'Urban' ,'Planning',
    'Landscape', 'Structure' ,'Geotechnical','W&E' ,'Treatment' ,'Plants' ,'Transportation','Traffic' ,'Railway', 'QS',
    'PM' ,'Mech – FF & Plumb', 'Mech – HVAC','Electrical' ,'High Voltage' ,'Low Current (LC)',
    'Solar Energy' ,'Wind Energy', 'Green / Sustainability','CS Bldg' ,'CS Water' ,'CS Energy','BIM', 'Other'])
        EGEC_Branch=st.selectbox('**9- EGEC Branch: (Proposal prepared by)**:',[" ",'KSA', 'Egypt'])
        #_______________________________________________________________________________________________________________________

        Proposal_Deadline=st.date_input('13- Proposal Deadline Date',None)
        Date_Submitted=st.date_input('14- Date Submitted Date',None)
        Date_Closed=st.date_input('15- Date Closed: Date',None)

    # Convert Currancy

        #st.subheadertitle('***Currancy Converter App***')
        #def load_data():
        #   src=requests.get('https://www.xe.com/ar/currencyconverter/')
        #  soup=BeautifulSoup(src,'html.parser')
        # data=soup.find('section',{'class':'large-container-sc-1j708v7-0 fsQASC'})
            #data """

        Proposal_Manager=st.text_input('17- Proposal Manager')
        Proposal_Director=st.text_input('18- Proposal Director')    
        Account_Manager=st.text_input('19- Account Manager')
        Proposal_Status=st.selectbox('**20- Proposal Status**',[" ",'Ongoing','Pending','Lost financial','Lost technical','Awarded','Cancelled by EGEC','Cancelled by Client'])      
        Project_Number=st.text_input('21- Project Number')
        Project_Name=st.text_input( '22- Project Name')  
        Contract_title=st.text_input('23- Contract title')
        Overview=st.text_input( '24- Overview')       
        Scope=st.text_input('25- Scope')
        Contract=st.subheader("**26- Contract Total Duration**")
        Start_Date=st.date_input('Start Date')
        DS_Duration=st.date_input('a. DS Duration')
        CS_Duration=st.date_input('b. CS Duration')
        Contract_Value=st.text_input('27- Contract Value')
        Project_Manager=st.text_input('28- Project Manager')
        Owner=st.text_input('29- Owner')    
        Estimated_Construction_Cost=st.text_input('30- Estimated Construction Cost')
        Need_Project_sheet=st.selectbox('**31- Need Project Sheet**',[" ",'Yes','No'])
        Photo_available=st.selectbox('**32- Photo available**',[" ",'Yes','No'])
        st.file_uploader('33- Attachement Contract')
        save_data = st.button('Save')
        if save_data:
            old_df3 = pd.read_csv('C:/Users/Ahmed/Proposal111111.csv') 
            new_data3={'Proposal_Type': Proposal_Type, 'Service_Type': Service_Type, 'Business_Line': Business_Line, 'Specialized_Studies': Specialized_Studies, 'pro_Country': pro_Country, 
                        'Project_Location': Project_Location, 'Project_Type': Project_Type, 'Internal_Disciplines': Internal_Disciplines, 'EGEC_Branch': EGEC_Branch, 'Proposal_Deadline': Proposal_Deadline, 
                        'Date_Submitted': Date_Submitted, 'Date_Closed': Date_Closed, 'Proposal_Manager': Proposal_Manager, 'Proposal_Director': Proposal_Director, 'Account_Manager': Account_Manager, 
                        'Proposal_Status': Proposal_Status, 'Project_Number': Project_Number, 'Project_Name': Project_Name, 'Contract_title': Contract_title, 'Overview': Overview, 'Scope': Scope, 
                        'Start_Date': Start_Date, 'DS_Duration': DS_Duration, 'CS_Duration': CS_Duration, 'Contract_Value': Contract_Value, 'Project_Manager': Project_Manager, 'Owner': Owner, 
                        'Estimated_Construction_Cost': Estimated_Construction_Cost, 'Need_Project_sheet': Need_Project_sheet, 'Photo_available': Photo_available}
            new_df3=pd.DataFrame([new_data3])
            df3=pd.concat([old_df3, new_df3], axis=0, ignore_index=True)

            # حفظ القائمة الجديدة في ملف الإكسل
            df3.to_csv('C:/Users/Ahmed/Proposal111111.csv', index=False, header=True)

            # عرض رسالة تأكيد عند الحفظ
            st.success('Data saved successfully!')
#_____________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________ 
    
# Data Table Part
    # Data Table Part
    if page == 'Table':
        data1 = pd.read_csv('C:/Users/Ahmed/Clients11111.csv')    
        data2 = pd.read_csv('C:/Users/Ahmed/HR11111.csv') 
        data3 = pd.read_csv('C:/Users/Ahmed/Proposal111111.csv')

        # إنشاء DataFrame للتجربة مع تحديد فهرس
        dataf = pd.DataFrame({'Proposal_Type': ' ', 'Service_Type': ' ', 'Business_Line': ' ', 'Specialized_Studies': ' ', 'pro_Country': ' ', 
                        'Project_Location': ' ', 'Project_Type': ' ', 'Internal_Disciplines': ' ', 'EGEC_Branch': ' ', 'Proposal_Deadline': ' ', 
                        'Date_Submitted': ' ', 'Date_Closed': ' ', 'Proposal_Manager': ' ', 'Proposal_Director': ' ', 'Account_Manager': ' ', 
                        'Proposal_Status': ' ', 'Project_Number': ' ', 'Project_Name': ' ', 'Contract_title': ' ', 'Overview': ' ', 'Scope': ' ', 
                        'Start_Date': ' ', 'DS_Duration': ' ', 'CS_Duration': ' ', 'Contract_Value': ' ', 'Project_Manager': ' ', 'Owner': ' ', 
                        'Estimated_Construction_Cost': ' ', 'Need_Project_sheet': ' ', 'Photo_available': ' '}, index=[0])

        # إنشاء زر تنزيل
        def download_button(dataf, filename, button_text):
            csv = dataf.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f"data:file/csv;base64,{b64}"
            st.markdown(f'<a href="{href}" download="{filename}">{button_text}</a>', unsafe_allow_html=True)

        # استخدام الزر تنزيل
        download_button(dataf, 'my_data.csv', 'Download csv file')

        # إذا تم تحميل ملف Excel، قراءته ودمجه مع DataFrame الحالي
        uploaded_file = st.file_uploader("Upload Excel file", type=["csv","xlsx",'xml'])
        merged_df = None  # تعيين القيمة الافتراضية
        if uploaded_file is not None:
            # قراءة ملف Excel وتحويله إلى DataFrame باستخدام المحرك 'openpyxl'
            if uploaded_file.type == 'application/vnd.ms-excel' or uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                try:
                    excel_df = pd.read_excel(uploaded_file, engine='openpyxl')
                    # دمج DataFrame الحالي مع Excel DataFrame
                    merged_df = pd.concat([data1, data2, data3, excel_df], axis=1, ignore_index=False)
                except Exception as e:
                    st.write("Error reading file:", e)
            else:
                st.write("Invalid file format. Only CSV and Excel files are allowed.")
        else:
            merged_df = pd.concat([data1, data2, data3], axis=1, ignore_index=False)

        # التحقق من تعيين قيمة merged_df وعرض DataFrame كجدول
        if merged_df is not None:
            st.dataframe(merged_df)
        else:
            st.write("No data to display.")


if __name__ == '__main__':
   main()
#_______________________________________________________________________________________________________
# ___________________________________________________________________________________________________________

#Create Table Data Page
