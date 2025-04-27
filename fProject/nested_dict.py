student_data={
    "nimal":{"roll no":10,"age":20,"lan":"python"},
    "amal":{"roll no":20,"age":20,"lan":"java"}
}

print(student_data)
print(student_data["nimal"]["roll no"])
student_data["amal"]["phone_number"]=7565554
print(student_data["amal"])
#del student_data["amal"]["phone_number"]
print(student_data["amal"].pop("phone_number"))
print(student_data["amal"])