class Doctor:
    def treat(self):
        pass


class Surgeon(Doctor):
    def treat(self):
        print("Проводит операцию")


class Dentist(Doctor):
    def treat(self):
        print("Лечит зубы")


class Therapist(Doctor):

    def treat(self):
        print("Проводит осмотр")

    def assigning(self, patient):
        if patient.treatment_plan == 1:
            print("Назначен хирург")
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            print("Назначен дантист")
            patient.doctor = Dentist()
        else:
            print("Назначен терапевт")
            patient.doctor = Therapist()
        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


therapist = Therapist()
patient1 = Patient(treatment_plan=1)
therapist.assigning(patient1)

therapist = Therapist()
patient1 = Patient(treatment_plan=2)
therapist.assigning(patient1)

therapist = Therapist()
patient1 = Patient(treatment_plan=3)
therapist.assigning(patient1)