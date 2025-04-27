def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)



info_person(name="kamal",age=30,dept="cs")
info_person(name="sunil",dept="eng")