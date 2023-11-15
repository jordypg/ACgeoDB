import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from models import Student, Program, Student_Program
# 

def extract_values(input_file):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Create an empty list to store objects
    objects_list = []

    # Iterate through each row in the DataFrame
    for index in range(1, len(df)):
        row = df.iloc[index]
        # Extract values from columns 3 to 109
        values = row.iloc[2:109].tolist()

        # Create an object (you can use a dictionary or a custom class)
        obj = {'row_number': index + 1, 'values': values}

        # Append the object to the list
        objects_list.append(obj)

    return objects_list

def insert_db(entry_dict):
    url =  'postgresql://postgres:geodb@localhost/project'
    engine = create_engine(url)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    # insert_students_db(entry_dict, session)
    insert_student_program_db(entry_dict, session)
    session.close()

def insert_program_db(entry_dict):
    url =  'postgresql://postgres:geodb@localhost/project'
    engine = create_engine(url)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    ### DEAL WTIH DIFFERENT PROGRAMS WITHIN A PROGRAM
    '''
    my_string = "example(text, more)"
    substring = my_string.split(('(', ','))[0]
    '''

    ### WORK ON FIXING THIS
    program_list = ['DIS Copenhagen', 'Maastricht University', 'IES Abroad Milan', 'IES Abroad Rome', 'University of Oxford', 'Columbia Visting Students Program ']
    country_list = ['Denmark', 'Netherlands', 'Italy', 'Italy', 'United Kingdom', 'United States']
    for i,program in enumerate(program_list):
        foo = Program(
            program_name = program,
            country = country_list[i]
        )
        session.add(foo)
        session.commit()
    session.close()

def list_to_str(my_list):
    ret = [str(element) for element in my_list]
    return ret


def extract_before_special_chars(text):
    # Find the index of the first opening parenthesis or comma
    index = min([text.find(char) for char in [',', '('] if text.find(char) != -1], default=-1)

    # If there's no opening parenthesis or comma, return the original string
    if index == -1:
        return text

    # Otherwise, return the part of the string before the special character
    return text[:index].strip()

def insert_student_program_db(entry_dict, session):
    tmp = extract_before_special_chars(entry_dict['program_name'])

    foo = Student_Program(
        student_email = entry_dict['student_email'],
        program_name = tmp,
        term = entry_dict['term']
    )

    session.add(foo)
    session.commit()

def insert_student_db(entry_dict, session):
    # print(entry)
    # print(type(entry))
    # print(entry_dict)
    # print(entry)
    # print(entry['majors'])
    tmp = list_to_str(entry_dict['majors'])
    print(tmp)
    foo = Student(
        student_email = entry_dict['student_email'],
        major = tmp, ## INCLUDE ALL MAJORS LATER
        primary_reason = entry_dict['primary_reason_for_abroad'],
        language_proficiency = entry_dict['language_proficiency_before_after']
    )

    session.add(foo)
    session.commit()    

def insert_students_db(entry_dict, session):
    # for entry in entry_list:
    #     foo = Student (
    #         student_email = entry['student_email'],
    #         major = entry['majors'], ## INCLUDE ALL MAJORS LATER
    #         primary_reason = entry['primary_reason_for_abroad'],
    #         language_proficiency = entry['language_proficiency_before_after'] 
    #     )
    #     session.add(foo)
    #     session.commit()
    insert_student_db(entry_dict, session)

'''
# def insert_students_db():
#     url =  'postgresql://postgres:geodb@localhost/project'
#     engine = create_engine(url)
#     connection = engine.connect()
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     Base = declarative_base()
    

#     class Student(Base):
#         __tablename__ = 'student'
#         student_email = Column(String(255), primary_key=True, unique=True, nullable=False)
#         major = Column(String(100), nullable=False)
#         primary_reason = Column(String(255), nullable=False)
#         language_proficiency = Column(String(50), nullable=False)
    
#     foo = Student(
#         student_email = 'foofoo',
#         major = 'foo',
#         primary_reason = 'foofoofoo',
#         language_proficiency = 'foofoofoofoo'
#     )
    
#     session.add(foo)
#     session.commit()
'''

if __name__ == "__main__":
    # Use the relative path for the Excel file
    excel_file_path = 'Study Away Eval S23 AY2223 for CS class.xlsx'

    # Call the function and get the list of objects
    extracted_objects = extract_values(excel_file_path)

    entries = []
    # Print the extracted objects
    for obj in extracted_objects:
        obj = obj['values']
        entry = {}
        entry['student_email'] = obj[0]
        entry['courses_taken'] = obj[1:10]
        entry['course_types'] = obj[10:28]
        entry['primary_reason_for_abroad'] = obj[30]
        entry['primary_language_spoken'] = obj[31:33]
        entry['language_proficiency_before_after'] = obj[33]
        entry['res_staff_availability'] = obj[36:38]
        entry['housing_accomodation'] = obj[38:41]
        entry['academic_excursion_availability'] = obj[41:45]
        entry['leisure_excursion_availability'] = obj[45:49]
        entry['amount_of_money_spent'] = obj[50]
        entry['affordability'] = obj[51]
        entry['extracurricular_participated'] = obj[52]
        entry['reflection_on_goals'] = obj[55]
        entry['personal_and_academic_growth'] = obj[75]
        entry['challenges_of_experience'] = obj[76]
        entry['new_persoectives_post_program'] = obj[77]
        entry['factor_influencing_experience'] = obj[89:93]
        entry['attitudes_different_from_us'] = obj[92:95]
        entry['recommendation_rating'] = obj[95:97]
        entry['country'] = obj[100]
        entry['majors'] = obj[101:104]
        entry['program_name'] = obj[104]
        entry['term'] = obj[106]
        entries.append(entry)
    
    # first_entry = extracted_objects[0]
    # print((first_entry))
    # insert_db(first_entry)
    for entry in (entries):
        insert_db(entry)
        # print('sex')
        # print(entry)
    # insert_program_db()
    # insert_db(extracted_objects)
    # for i, entry in enumerate(entries):
    #first_object = extracted_objects[0] if extracted_objects else None
    #print(first_object['values'][0])
