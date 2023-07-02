"""
This module analyzes EHR records.

It analyzes both patient and lab information.
"""
from datetime import datetime


PATIENT_TYPE = dict[str, dict[str, str]]


def parse_patient_file(patient_filename: str) -> PATIENT_TYPE:
    """Parse through just the patient file."""
    patient_records = dict()  # O(1)
    patient_file = open(patient_filename)  # O(1)
    headers = (
        patient_file.readline().strip().split("\t")
    )  # O(n) #chars in line1
    data = patient_file.readlines()  # O(n) - n is num of chars in file
    patient_file.close()  # O(1)

    # Parse rows and get records for each patient
    for patient in data:  # O(n) n is number of patients
        patient_data = patient.split("\t")  # O(m) m is #chars in the line
        patid = patient_data[0]  # O(1)
        patient_records[patid] = dict(
            zip(headers[1:], patient_data[1:])
        )  # O(1)

    return patient_records  # O(1)


LAB_TYPE = dict[str, list[dict[str, str]]]


def parse_lab_file(lab_filename: str) -> LAB_TYPE:
    """Parse through the patient file."""
    lab_records: dict[str, list[dict[str, str]]] = dict()  # O(1)
    lab_file = open(lab_filename)  # O(1)
    headers = lab_file.readline().strip().split("\t")  # O(n) n chars in line1
    data = lab_file.readlines()  # O(n) - n is # of chars in the file
    lab_file.close()  # O(1)

    # Parse lab file and get individual lab records
    for lab in data:  # O(n) n is number of labs
        lab_data = lab.split("\t")  # O(n) n is number of characters in line
        patid = lab_data[0]  # O(1)
        lab_records.setdefault(patid, []).append(
            dict(zip(headers[1:], lab_data[1:]))  # O(1)
        )

    return lab_records  # O(1)


def parse_data(
    patient_filename: str, lab_filename: str
) -> tuple[dict[str, dict[str, str]], dict[str, list[dict[str, str]]]]:
    """Take in files and return dictionaries of data."""
    patient_records = parse_patient_file(patient_filename)  # O(mn) m labs,
    # n characters in line
    lab_records = parse_lab_file(lab_filename)  # O(pq) p patients, q chars

    return patient_records, lab_records  # O(1)


def patient_age(records, patient_id: str) -> int:
    """Calculate the age in years."""
    patient_birthday_str = records[patient_id]["PatientDateOfBirth"]  # O(1)
    format = "%Y-%m-%d %H:%M:%S.%f"  # O(1)
    patient_birthday = datetime.strptime(patient_birthday_str, format)  # O(1)
    current_time = datetime.now()  # O(1)
    delta = current_time - patient_birthday  # O(1)
    age = int(delta.days / 365.2425)  # O(1)
    return age  # O(1)


def patient_is_sick(
    records: dict[str, list[dict[str, str]]],
    patient_id: str,
    lab_name: str,
    operator: str,
    value: float,
) -> bool:
    """
    Take in patient records and determine relationship to threshold.

    Return boolean.
    """
    lab_records = records[patient_id]

    # Parsing that patient's labs of that type
    for lab in lab_records:  # O(n) n is # of labs for that patient
        if lab["LabName"] == lab_name:  # O(1)
            lab_value = lab["LabValue"]  # O(1)
            # seeing if the lab value matches the sickness criterion
            if operator == "<":  # O(1)
                if float(lab_value) < value:  # O(1)
                    return True  # O(1)
            if operator == ">":  # O(1)
                if float(lab_value) > value:  # O(1)
                    return True  # O(1)
    return False  # O(1)



def patient_initial_age(patient_records, lab_records, patient_id: str) -> datetime:
    """Calculate patient age for initial lab record."""
    # Getting Lab records for the patient
    patient_lab_records = lab_records[patiend_id]

    # Finding the birthday for the patient
    format = "%Y-%m-%d %H:%M:%S.%f"  # O(1)
    patient_birthday_str = records[patient_id]["PatientDateOfBirth"]  
    patient_birthday = datetime.strptime(patient_birthday_str, format)

    #Initializing
    min_date = datetime.now()
    age = 0

    # Parsing the lab records to find the lab record with the min date
    for lab in lab_records:
        lab_date_str = lab["LabDateTime"]
        lab_date = datetime.strptime(lab_date_str, format)

        # Updating if this lab is the initial lab
        if lab_date < min_date:
            min_date = lab_date
            delta = min_date - patient_birthday
            age = int(delta.days / 365.2425)
    
    return age



class Patient:
    def __init__(self):
        self.id
        self.gender = 
        self.dob = 
        self.race = 
        self.marriage_status = 
        self.lang = 
        self.poverty = 


class Lab:
    def __init__(self):
        self.admitID = 
        self.lab_name = 
        self.lab_value = 
        self.lab_units = 
        self.lab_datetime = 


def main() -> None:
    """Run the ehr-module."""
    patient_filename = "PatientCorePopulatedTable.txt"
    lab_filename = "LabsCorePopulatedTable.txt"

    patient_records, lab_records = parse_data(patient_filename, lab_filename)


if __name__ == "__main__":
    main()





"""Testing the EHR module."""
from ehr_module import parse_data
from ehr_module import patient_is_sick
from ehr_module import patient_age
from fake_files import fake_files


def test_parse_data() -> None:
    """Test the parse data function."""
    fake_patient = [
        [
            "PatientID",
            "PatientGender",
            "PatientDateOfBirth",
            "PatientRace",
            "PatientMaritalStatus",
            "PatientLanguage",
            "PatientPopulationPercentageBelowPoverty",
        ],
        [
            "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
            "Male",
            "1947-12-28 02:45:40.547",
            "Unknown",
            "Married",
            "Icelandic",
            "18.08",
        ],
    ]

    fake_patient_result = {
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F": {
            "PatientGender": "Male",
            "PatientDateOfBirth": "1947-12-28 02:45:40.547",
            "PatientRace": "Unknown",
            "PatientMaritalStatus": "Married",
            "PatientLanguage": "Icelandic",
            "PatientPopulationPercentageBelowPoverty": "18.08",
        }
    }

    fake_lab = [
        [
            "PatientID",
            "AdmissionID",
            "LabName",
            "LabValue",
            "LabUnits",
            "LabDateTime",
        ],
        [
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "1",
            "URINALYSIS: RED BLOOD CELLS",
            "1.8",
            "rbc/hpf",
            "1992-07-01 01:36:17.910",
        ],
    ]

    fake_lab_result = {
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C": [
            {
                "AdmissionID": "1",
                "LabName": "URINALYSIS: RED BLOOD CELLS",
                "LabValue": "1.8",
                "LabUnits": "rbc/hpf",
                "LabDateTime": "1992-07-01 01:36:17.910",
            }
        ]
    }

    with fake_files(fake_patient, fake_lab) as filenames:
        patient_records, lab_records = parse_data(filenames[0], filenames[1])
        assert patient_records == fake_patient_result
        assert lab_records == fake_lab_result


def test_patient_age() -> None:
    """Test patient age."""
    patient_records = {
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F": {
            "PatientGender": "Male",
            "PatientDateOfBirth": "1947-12-28 02:45:40.547",
            "PatientRace": "Unknown",
            "PatientMaritalStatus": "Married",
            "PatientLanguage": "Icelandic",
            "PatientPopulationPercentageBelowPoverty": "18.08",
        }
    }
    assert (
        patient_age(patient_records, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
        == 75
    )


def test_patient_is_sick() -> None:
    """Test patient_is_sick."""
    fake_lab_records = {
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C": [
            {
                "AdmissionID": "1",
                "LabName": "URINALYSIS: RED BLOOD CELLS",
                "LabValue": "1.8",
                "LabUnits": "rbc/hpf",
                "LabDateTime": "1992-07-01 01:36:17.910",
            }
        ]
    }
    assert (
        patient_is_sick(
            fake_lab_records,
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "URINALYSIS: RED BLOOD CELLS",
            "<",
            4.0,
        )
        == True
    )


def main() -> None:
    """Run the ehr-module."""


if __name__ == "__main__":
    main()
