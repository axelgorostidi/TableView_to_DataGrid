# TableView_to_DataGrid
Change Table View component to a Data Grid in Servoy Framework. 

## Pasos a seguir:

* Pegar el script "cambiarADataGrid.py" en la carpeta donde tengamos los archivos de extensión ".frm" que contengan las tablas a convertir.
* Pegar el archivo "forms.txt" en la misma carpeta que en el paso anterior.
* Escribir los nombres de los formularios, en lineas separadas sin dejar espacios innecesarios. Escribirlos con la extensión ".frm". Ejemplo en "forms.txt".
* Ejecutar script "cambiarADataGrid.py".
* Eliminar los dos archivos del workspace de Servoy.
* Revisar y modificar lo que se requiera mediante la interfaz de Servoy.

## No probado:
* Cambiar varios componentes que se ubiquen en un mismo formulario.

## Requerimientos:
* Python instalado y anclado a las variables del entorno del sistema.

## Alcance actual:
* Formularios que contengan un componente Table View.

______________________________________________________________________________________________________________________________________________

## Steps to follow:

* Paste the script "changeADataGrid.py "in the folder where we have the files with the extension" .frm "that contain the tables to be converted.
* Paste the file "forms.txt" in the same folder as in the previous step.
* Write the names of the forms, on separate lines without leaving unnecessary spaces. Write them with the extension ".frm". Example in "forms.txt"
* Execute "changeADataGrid.py" script.
* Delete the two files from the Servoy workspace.
* Review and modify what is required through the Servoy interface.

## Not tested:
* Change several components that are located in the same form.

## Requirements:
* Python installed and bound to system environment variables.

## Current scope:
* Forms that contain a Table View component.
