forms_names = []
#guardamos los forms a cambiar
with open("forms.txt", mode="r") as txt:
    forms = txt.readlines()
    for line in forms:
        forms_names.append(line.replace("\n",""))
txt.close()

for form in forms_names:
    #leemos linea a linea cada form
    lbl_table = 0 #bandera que indica si estamos leyendo las lineas que corresponden a una tabla
    lbl_autoresize = 0 #para saber si la columna tiene autoresize
    tmp_form_lines = []
    i = 0 #no usamos enumerate porque se van eliminando y agregando lineas (cuenta las líneas)
    try:
        with open(form, mode="r") as actualFormRead:
            lines = actualFormRead.readlines()
            for line in lines:
                tmp_line = line
                if(line.find("columns:[")>-1):
                    lbl_table = 1
                
                if(line.find("autoResize")>-1):
                    lbl_autoresize = 1
                
                if(line.find("}")>-1 and lbl_table == 1):
                    lbl_autoresize = 0
                    if(tmp_form_lines[i-1][-2] == ","): #nos fijamos si la linea anterior quedo con una coma (rompería el form)
                        tmp_form_lines[i-1] = tmp_form_lines[i-1][:-2]+"\n"
                
                if(line.find("headerStyleClass")>-1 and lbl_table == 1):
                    if(lbl_autoresize == 0):
                        tmp_line = "autoResize:false,\n"
                        tmp_form_lines.append(tmp_line) #necesario agregar esta acá
                        i += 1
                    tmp_line = "enableRowGroup:false,\n"

                if(line.find("headerText")>-1 and lbl_table == 1):
                    tmp_line = tmp_line.replace("headerText","headerTitle")

                if(line.find("typeName")>-1 and lbl_table == 1):
                    tmp_line = tmp_line.replace("servoyextra-table", "aggrid-groupingtable")
                    
                if(line.find("uuid")>-1 and lbl_table == 1):
                    lbl_table = 0
                    continue
                 
                if(line.find("width")>-1):
                    tmp_line = tmp_line.replace('"','')
                
                if(line.find('styleClass:"table id-tabla-striped tbody tr"')>-1): 
                    tmp_line = tmp_line.replace("table id-tabla-striped tbody tr","ag-theme-bootstrap")

                if(line.find("svyUUID")==-1): #acá agregamos las lineas          
                    tmp_form_lines.append(tmp_line)
                    i += 1 
                    
            actualFormRead.close()      

            with open(form,'w') as actualFormWrite:
                actualFormWrite.writelines(tmp_form_lines)
            actualFormWrite.close()
    except:
        print("No existe el archivo ",form)