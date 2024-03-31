import creopyson
import subprocess
import time
import pprint

pathStart="C:\Program Files\PTC\Creo 9.0.3.0\Parametric\\bin\parametric.bat"


c = creopyson.Client()

c.connect()


c.creo_set_creo_version(9)

if not c.is_creo_running():
    subprocess.Popen(pathStart)
    while not c.is_creo_running():
        time.sleep(5)
        print("Jeszcze nie gotowe")

    
    



print("Gotowe")

enter=input("Naciśnij Enter aby kontynuować")
    


c.creo_cd("C:\\Users\\CAD\Desktop\\Krzysztof Malinowski\\Lab3")

c.file_open("model3.prt")

print("z3")
print("")
print("katalog roboczy: "+c.creo_pwd())
print("jednostki masy: "+c.file_get_mass_units())
print("jednostki długości: "+c.file_get_length_units())
print("parametry modelu: ")
for x in range(len(c.parameter_list())):
    print(c.parameter_list()[x])


print("parametry operacji CUT: ")
for x in range(len(c.feature_list_params(name="CUT"))):
    print(c.feature_list_params(name="CUT")[x])

print("materiały: ")
for x in range(len(c.file_list_materials())):
    print(c.file_list_materials()[x])

print("dokładność: ")
pprint.pprint(c.file_get_accuracy())


pathUser=input("podaj ścieżkę do folderu roboczygo: ")

c.creo_cd(pathUser)

print("katalog roboczy: "+c.creo_pwd())

c.file_rename("model_KM.prt",onlysession="true")

c.file_load_material_file("CAST_IRON_GRAY","C:\\Program Files\\PTC\Creo 9.0.3.0\\Common Files\\text\materials-library\\Standard-Materials_Granta-Design\\Ferrous_metals")

c.file_set_cur_material("CAST_IRON_GRAY")

c.file_save()

c.interface_export_file("STEP")

c.file_close_window()

c.file_erase()
