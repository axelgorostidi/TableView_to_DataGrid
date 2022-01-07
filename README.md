# TableView_to_DataGrid
Change Table View component to a Data Grid in Servoy Framework. 

## Pasos a seguir:

* Pegar el script "cambiarADataGrid.py" en la carpeta donde tengamos los archivos de extensión ".frm" que contengan las tablas a convertir.
* Pegar el archivo "forms.txt" en la misma carpeta que en el paso anterior.
* Escribir los nombres de los formularios, en lineas separadas sin dejar espacios innecesarios. Escribirlos con la extensión ".frm". Ejemplo:
  form1.frm
  form2.frm
  form3.frm
* Ejecutar script "cambiarADataGrid.py".
* Eliminar los dos archivos del workspace de Servoy.
* Revisar y modificar lo que se requiera mediante la interfaz de Servoy.

## No probado:
* Cambiar varios componentes que se ubiquen en un mismo formulario.

## Requerimientos:
* Python instalado y anclado a las variables del entorno del sistema.

## Alcance actual:
* Formularios que contengan un componente Table View.

