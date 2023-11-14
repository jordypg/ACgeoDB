import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

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

def insert_student_db():
    url =  'postgresql://postgres:geodb@localhost/project'
    engine = create_engine(url)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class Student(Base):
        __tablename__ = 'student'
        student_email = Column(String(255), primary_key=True, unique=True, nullable=False)
        major = Column(String(100), nullable=False)
        primary_reason = Column(String(255), nullable=False)
        language_proficiency = Column(String(50), nullable=False)
    
    foo = Student(
        student_email = 'foofoo',
        major = 'foo',
        primary_reason = 'foofoofoo',
        language_proficiency = 'foofoofoofoo'
    )
    
    session.add(foo)
    session.commit()

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
        entry['language_proficiency_before_after'] = obj[35]
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
    
    first_entry = extracted_objects[0]

    insert_student_db()

    
    print(entries)
    #first_object = extracted_objects[0] if extracted_objects else None
    #print(first_object['values'][0])
