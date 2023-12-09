import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from models import *


def list_to_str(my_list):
    ret = [str(element) for element in my_list]
    return ret


def extract_program_name(text):
    # Find the index of the first opening parenthesis or comma
    index = min([text.find(char) for char in [',', '('] if text.find(char) != -1], default=-1)

    # If there's no opening parenthesis or comma, return the original string
    if index == -1:
        return text

    # Otherwise, return the part of the string before the special character
    return text[:index].strip()

#Works because pandas assigns float nan value to empty cells, even if they're marked as text in Excel
def isEmptyCell(cell):
    return not isinstance(cell, str)

#Removes empty cells from a list of cells
def remove_empty_cells(cells):
    return [cell for cell in cells if not isEmptyCell(cell)]


#Handles the case when "Other" is selected for a question by returning only the answer from the "Please specify" question
def handle_other_selection(primary, other):
    
    '''The selection for specifying an other answer is not uniform over the questions; 
       it's either "Other" or "Other (Please specify)". So we have to use str.startswith()'''
    if primary.strip().startswith("Other") \
       and not isEmptyCell(other):
        return other
    else: 
        return primary

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

    insert_student(entry_dict, session)
    insert_major(entry_dict, session)
    insert_has_major(entry_dict, session)
    insert_program(entry_dict, session)
    insert_term(entry_dict, session)
    insert_participates_in(entry_dict, session)
    insert_personal_reflection(entry_dict, session)
    insert_program_reflection(entry_dict, session)
    insert_is_about_academic_factors(entry_dict, session)
    insert_is_about_financial_factors(entry_dict, session)
    insert_is_about_social_factors(entry_dict, session)
    insert_location(entry_dict, session)
    insert_hosted_in(entry_dict, session)
    session.close()

def insert_student(entry_dict, session):
    foo = Student(
        student_email = entry_dict['student_email'],
        primary_reason = entry_dict['primary_reason']
    )

    session.add(foo)
    session.commit()  



majors = set()
def insert_major(entry_dict, session):
    entry_majors = entry_dict['majors']
    for major in entry_majors.split(val_separator):
        if major not in majors:
            foo = Major(
                major_name = major
            )
            session.add(foo)
            session.commit()


def insert_has_major(entry_dict, session):
    entry_majors = entry_dict['majors']
    for major in entry_majors.split(val_separator):
        foo = Has_Major(
            student_email = entry_dict['student_email'],
            major_name = major
        )
        session.add(foo)
        session.commit()

program_ids = dict() #Dictionary mapping every program name to their program IDs
next_program_id = 0
def insert_program(entry_dict, session):
    
    program = entry_dict['program_name']

    #If we haven't encountered this program yet...
    if program not in program_ids:
        #...assign a program ID to it...
        program_ids[program] = str(next_program_id)
        next_program_id += 1
        #...and add it to the DB.
        foo = Program (
            program_name = program
        )
        session.add(foo)
        session.commit()

terms = set()
def insert_term(entry_dict, session):
    term = entry_dict['term']
    if term not in terms:
        foo = Term(term_id = term)
    session.add(foo)
    session.commit()


def insert_participates_in(entry_dict, session):
    foo = Participates_In(
        student_email = entry_dict['student_email'],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term']
    )

    session.add(foo)
    session.commit()

next_pr_id = 0
def insert_personal_reflection(entry_dict, session):
    foo = Personal_Reflection(
        student_email = entry_dict['student_email'],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term'],
        pr_id = str(next_pr_id),
        goals_reflection = entry['goals_reflection'],
        growth = entry['growth'],
        challenges = entry['challenges'],
        new_perspectives = entry['new_perspectives'],
        language_proficiency_before = entry['language_proficiency_before'],
        language_proficiency_after = entry['language_proficiency_after'],
    )
    next_pr_id += 1
    session.add(foo)
    session.commit()

def insert_program_reflection(entry_dict, session):
    foo = Program_Reflection (
        student_email = entry_dict['student_email'],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term'],
        pgr_id = program_ids[entry_dict['program_name']],
        recommendation_rating = entry['recommendation_rating'],
        recommendation_comments = entry['recommendation_comments']
    )
    session.add(foo)
    session.commit()

def insert_is_about_academic_factors(entry_dict, session):
    foo = Has_Academic_Factors (
        pgr_id = program_ids[entry_dict['program_name']],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term'],
        courses_taken = entry_dict['courses_taken'],
        courses_type = entry_dict['courses_type'],
        academic_exc_avail = entry_dict['academic_excursion_avail'],
        academic_exc_rating = entry_dict['academic_exc_rating'],
        academic_exc_comments = entry_dict['academic_exc_comments'],
        influencing_factors = entry_dict['influencing_factors'],
        orientation_description = entry_dict['orientation_description']
        )
    session.add(foo)
    session.commit()

def insert_is_about_financial_factors(entry_dict, session):
    foo = Has_Financial_Factors (
        pgr_id = program_ids[entry_dict['program_name']],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term'],
        amount_spent = entry_dict['amount_spent'],
        city_affordability = entry_dict['city_affordability'],
        housing_acc = entry_dict['housing_acc'],
        housing_acc_comments = entry_dict['housing_acc_comments']

        )
    session.add(foo)
    session.commit()

def insert_is_about_social_factors(entry_dict, session):
    foo = Has_Social_Factors (
        pgr_id = program_ids[entry_dict['program_name']],
        program_name = entry_dict['program_name'],
        term_id = entry_dict['term'],
        extracurricals = entry_dict['extracurriculars'],
        attitudes_diff = entry_dict['attitudes_diff'],
        attitudes_diff_comments = entry_dict['attitudes_diff_comments'],
        res_staff = entry_dict['res_staff'],
        res_staff_comments = entry_dict['res_staff_comments'],
        leisure_exc_avail = entry_dict['leisure_exc_avail'],
        leisure_exc_rating = entry_dict['leisure_exc_rating'],
        leisure_exc_comments = entry_dict['leisure_exc_comments']
        )
    session.add(foo)
    session.commit()

#A mapping of program names to their locations
location_names = {'IES Abroad Milan': 'Milan',
                  'IES Abroad Rome': 'Rome',
                  'Maastricht University': 'Maastricht',
                  'DIS Copenhagen': 'Copenhagen',
                  'University of Oxford, Lady Margaret Hall': 'Oxford',
                  'Columbia Visiting Students Program': 'New York, NY'}

def insert_location(entry_dict, session):
    foo = Location (
        location_name = location_names[entry_dict['program_name']],
        primary_lang_spoken = entry_dict['primary_lang_spoken'],
        country = entry_dict['country']
        )
    session.add(foo)
    session.commit()

def insert_hosted_in(entry_dict, session):
    foo = Hosted_In (
        program_name = entry_dict['program_name'],
        location_name = location_names[entry_dict['program_name']]
        )
    session.add(foo)
    session.commit()    
  

if __name__ == "__main__":
    val_separator = '; ' #Separator used when creating a single string from an entry with multiple values (e.g. 'courses_taken') 

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
        entry['courses_type'] = obj[10:28]
        entry['primary_reason'] = obj[30]
        entry['primary_lang_spoken'] = handle_other_selection(obj[31], obj[32])
        entry['language_proficiency_before'] = obj[33]
        entry['language_proficiency_after'] = obj[34]
        entry['orientation_description'] = obj[35]
        entry['res_staff'] = obj[36]
        entry['res_staff_comments'] = obj[37]
        entry['housing_acc'] = handle_other_selection(obj[38], obj[39])
        entry['housing_acc_comments'] = obj[40]
        entry['academic_exc_avail'] = obj[41]
        entry['academic_exc_rating'] = obj[43]
        entry['academic_exc_comments'] = obj[44]
        entry['leisure_exc_avail'] = obj[45]
        entry['leisure_exc_rating'] = obj[47]
        entry['leisure_exc_comments'] = obj[48]
        entry['amount_spent'] = obj[50]
        entry['city_affordability'] = obj[51]
        entry['extracurriculars'] = handle_other_selection(obj[52], obj[53])
        entry['goals_reflection'] = obj[55]
        entry['growth'] = obj[75]
        entry['challenges'] = obj[76]
        entry['new_perspectives'] = obj[77]
        entry['influencing_factors'] = [handle_other_selection(obj[89], obj[90]), obj[91]]
        entry['attitudes_diff'] = handle_other_selection(obj[92], obj[93])
        entry['attitudes_diff_comments'] = obj[94]
        entry['recommendation_rating'] = obj[95]
        entry['recommendation_comments'] = obj[96]
        entry['country'] = obj[100]
        entry['majors'] = obj[101:104]
        entry['program_name'] = extract_program_name(obj[104])
        entry['term'] = obj[106]

        #Stringify data & handle empty responses
        for key in entry:
            val = entry[key]
            #Replace single, empty cells with an empty string
            if not isinstance(val, list) and isEmptyCell(val): 
                val = ""
            #If the value represents multiple cells, remove empty cells, and make a single string out of it 
            elif isinstance(val, list):
                val = remove_empty_cells(val)
                val = val_separator.join(val)
            entry[key] = val
    
    for entry in (entries):
        insert_db(entry)
    
