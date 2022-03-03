import difflib

class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        # Add your code here!
        #
        # The first parameter to this method is a list of diseases, represented as a
        # list of 2-tuples. The first item in each 2-tuple is the name of a disease. The
        # second item in each 2-tuple is a dictionary of symptoms of that disease, where
        # the keys are letters representing vitamin names ("A" through "Z") and the values
        # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
        #
        # The second parameter to this method is a particular patient's symptoms, again
        # represented as a dictionary where the keys are letters and the values are
        # "+", "-", or "0".
        #
        # This method should return a list of names of diseases that together explain the
        # observed symptoms. If multiple lists of diseases can explain the symptoms, you
        # should return the smallest list. If multiple smallest lists are possible, you
        # may return any sufficiently explanatory list.

        # print(str("\n" + str(patient) + "\n"))

        diseases_symptoms = {}
        for disease_id, disease in diseases.items():
            d_symptoms_list = []
            for d_vitamin in disease:
                d_level = disease[d_vitamin]
                d_symptoms_list .append(d_level)
                diseases_symptoms['%s' % disease_id] = d_symptoms_list

        patient_symptoms = {}
        p_symptoms_list = []
        for p_vitamin in patient:
            p_level = patient[p_vitamin]
            p_symptoms_list .append(p_level)
            patient_symptoms["Patient"] = p_symptoms_list

        for d_id, d_symptoms in diseases_symptoms.items():
            # print("\n" + d_id)
            temp = diseases_symptoms[d_id]
            common_normal_ids, common_elevated_ids, common_reduced_ids = [], [], [],
            other_normal_ids, other_elevated_ids, other_reduced_ids = [], [], []
            for temp_id, temp_value in enumerate(temp):
                if temp[temp_id] == p_symptoms_list[temp_id] and temp[temp_id] == "0":
                    common_normal_ids.append(temp_id)
                elif temp[temp_id] == p_symptoms_list[temp_id] and temp[temp_id] == "+":
                    common_elevated_ids.append(temp_id)
                elif temp[temp_id] == p_symptoms_list[temp_id] and temp[temp_id] == "-":
                    common_reduced_ids.append(temp_id)
                else:
                    if temp[temp_id] == "0":
                        other_normal_ids.append(temp_id)
                    elif temp[temp_id] == "+":
                        other_elevated_ids.append(temp_id)
                    elif temp[temp_id] == "-":
                        other_reduced_ids.append(temp_id)
            print("\nCommon normal:", common_normal_ids, "\nCommon elevated:", common_elevated_ids, "\nCommon reduced:",
                  common_reduced_ids, "\nOther normal:", other_normal_ids, "\nOther elevated:", other_elevated_ids,
                  "\nOther reduced:", other_reduced_ids)

        return 0

